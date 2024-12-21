import requests
import pandas as pd
import logging

# 로그 설정
logging.basicConfig(filename="logs/app.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def fetch_subway_data(api_key, output_file):
    BASE_URL = "https://data.seoul.go.kr/api/subway/congestion"
    params = {
        "key": api_key,
        "type": "json",
        "startIndex": 1,
        "endIndex": 1000
    }
    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()["RESULT"]["row"]
            df = pd.DataFrame(data)
            df.to_csv(output_file, index=False)
            logging.info("데이터를 성공적으로 저장했습니다.")
            print(f"데이터 저장 완료: {output_file}")
        else:
            logging.error(f"API 요청 실패: {response.status_code}")
            print(f"API 요청 실패: {response.status_code}")
    except Exception as e:
        logging.error(f"API 호출 중 오류 발생: {e}")
        print(f"API 호출 중 오류 발생: {e}")
