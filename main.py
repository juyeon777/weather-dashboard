from scripts.fetch_exchange_rate import fetch_exchange_rate
from scripts.visualize_exchange_rate import visualize_exchange_rate
import time

API_KEY = "9d1b3aacc91a240332f92357"
BASE_CURRENCY = "USD"
TARGET_CURRENCY = "KRW"
OUTPUT_FILE = "data/exchange_rate.csv"

def main():
    print("실시간 환율 대시보드 실행 중...")
    while True:
        fetch_exchange_rate(API_KEY, BASE_CURRENCY, TARGET_CURRENCY, OUTPUT_FILE)
        visualize_exchange_rate(OUTPUT_FILE)
        time.sleep(300)  # 5분 간격으로 갱신

if __name__ == "__main__":
    main()
