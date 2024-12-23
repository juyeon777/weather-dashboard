from scripts.fetch_weather_data import fetch_weather_data
from scripts.visualize_weather import visualize_weather
import time

API_KEY = "c80714957aff9be02fbe9ac56ac34d13"
cities = ["Seoul", "Jeonju"]
input_files = [f"data/weather_{city.lower()}.csv" for city in cities]
bucket_name = "user-weather-data-bucket"
log_group = "weather-data-logs"
log_streams = {
    "Seoul": "weather-stream-seoul",
    "Jeonju": "weather-stream-jeonju",
}

def main():
    while True:
        for city, input_file in zip(cities, input_files):
            # 데이터 수집 및 CSV 파일 저장
            fetch_weather_data(API_KEY, city, input_file)
            
        # 실시간 시각화
        visualize_weather(input_files, cities)

        time.sleep(300)  # 5분 간격

if __name__ == "__main__":
    main()
