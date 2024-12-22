import requests
import boto3
import time
import os

# CloudWatch 로그 전송 함수
def log_to_cloudwatch(log_group, log_stream, message):
    client = boto3.client('logs', region_name='us-east-1')  # 리전 설정 필요
    try:
        # 로그 그룹 및 스트림 확인
        try:
            client.create_log_group(logGroupName=log_group)
        except client.exceptions.ResourceAlreadyExistsException:
            pass

        response = client.describe_log_streams(
            logGroupName=log_group,
            logStreamNamePrefix=log_stream
        )
        if not response['logStreams']:
            client.create_log_stream(logGroupName=log_group, logStreamName=log_stream)
            sequence_token = None
        else:
            stream = response['logStreams'][0]
            sequence_token = stream.get('uploadSequenceToken', None)

        # 로그 이벤트 생성
        log_event = {
            'logGroupName': log_group,
            'logStreamName': log_stream,
            'logEvents': [
                {
                    'timestamp': int(round(time.time() * 1000)),
                    'message': message,
                }
            ]
        }
        if sequence_token:
            log_event['sequenceToken'] = sequence_token

        client.put_log_events(**log_event)
        print(f"Logged to {log_group}/{log_stream}: {message}")
    except Exception as e:
        print(f"Failed to log to CloudWatch: {e}")

# OpenWeatherMap API 데이터 수집 함수
def fetch_weather_data(api_key, city, output_file):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            weather_desc = data["weather"][0]["description"]
            log_message = (
                f"Time: {timestamp}, City: {city}, "
                f"Temp: {temperature}°C, Humidity: {humidity}%, Wind: {wind_speed} m/s, Desc: {weather_desc}"
            )

            # CloudWatch로 로그 전송
            log_stream = f"weather-stream-{city.lower()}"
            log_to_cloudwatch("weather-data-logs", log_stream, log_message)

            # CSV 파일 저장
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            file_exists = os.path.isfile(output_file)
            with open(output_file, "a") as f:
                if not file_exists:
                    f.write("timestamp,temperature,humidity,wind_speed\n")
                f.write(f"{timestamp},{temperature},{humidity},{wind_speed}\n")

            print(f"{city} 데이터 저장 완료: {log_message}")
        else:
            print(f"API 요청 실패: 상태 코드 {response.status_code}")
    except Exception as e:
        print(f"API 요청 중 오류 발생: {e}")
