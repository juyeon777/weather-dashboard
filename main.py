from scripts.fetch_weather_data import fetch_weather_data
from scripts.visualize_weather import visualize_weather
import time

API_KEY = "c80714957aff9be02fbe9ac56ac34d13"  # OpenWeatherMap API 키
CITIES = ["Seoul", "Jeonju"]
OUTPUT_FILES = {
    "Seoul": "data/weather_seoul.csv",
    "Jeonju": "data/weather_jeonju.csv",
}

def main():
    print("날씨 대시보드 실행 중...")
    while True:
        for city in CITIES:
            fetch_weather_data(API_KEY, city, OUTPUT_FILES[city])
        
        # Visualize both cities in a single graph
        visualize_weather(OUTPUT_FILES["Seoul"], OUTPUT_FILES["Jeonju"])
        
        time.sleep(300)  # 5분 간격으로 데이터 수집 및 갱신

if __name__ == "__main__":
    main()
