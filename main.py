import time
from scripts.fetch_data import fetch_subway_data
from scripts.visualize_data import visualize_data

API_KEY = "6c4a466f4b6f6b6b37395a4b767856"

def main():
    print("서울시 지하철 혼잡도 실시간 대시보드 실행 중...")
    while True:
        try:
            # 데이터를 API에서 가져오기
            fetch_subway_data(API_KEY, "data/subway_data.csv")
            # 데이터로 그래프 갱신
            visualize_data("data/subway_data.csv")
            # 주기적 실행 (10초)
            time.sleep(10)
        except KeyboardInterrupt:
            print("\n프로그램 종료.")
            break
        except Exception as e:
            print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()
