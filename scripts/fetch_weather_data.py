import requests
import pandas as pd
from datetime import datetime
import os

def fetch_weather_data(api_key, city, output_file):
    # Ensure the data folder and CSV file exist
    if not os.path.exists("data"):
        os.mkdir("data")
    if not os.path.exists(output_file):
        with open(output_file, "w") as f:
            f.write("timestamp,temperature,humidity,wind_speed\n")  # Ensure consistent structure

    BASE_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    print(f"API 요청 URL: {BASE_URL}")

    try:
        response = requests.get(BASE_URL)
        print(f"API 응답 상태 코드: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print(f"API 응답 데이터: {data}")

            # Extract weather data
            timestamp = datetime.now()
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            # Append the new data to the CSV file
            weather_data = {
                "timestamp": [timestamp],
                "temperature": [temperature],
                "humidity": [humidity],
                "wind_speed": [wind_speed],
            }
            df = pd.DataFrame(weather_data)
            df.to_csv(output_file, mode="a", index=False, header=False)
            print(f"{city} 날씨 데이터 저장 완료.")
        else:
            print(f"API 요청 실패. 상태 코드: {response.status_code}")

    except Exception as e:
        print(f"오류 발생: {e}")
