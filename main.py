import time
from scripts.fetch_weather_data import fetch_weather_data
from scripts.visualize_weather import visualize_weather

# Provided API key and city
API_KEY = "c80714957aff9be02fbe9ac56ac34d13"  # OpenWeatherMap API 키
CITY = "Seoul"  # 도시 이름
OUTPUT_FILE = "data/weather_data.csv"

def main():
    print("날씨 대시보드 실행 중...")
    while True:
        fetch_weather_data(API_KEY, CITY, OUTPUT_FILE)
        visualize_weather(OUTPUT_FILE)
        time.sleep(300)  # 5분 간격으로 데이터 수집 및 갱신

if __name__ == "__main__":
    main()
