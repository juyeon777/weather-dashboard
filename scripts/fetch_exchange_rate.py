import requests
import pandas as pd
from datetime import datetime

def fetch_exchange_rate(api_key, base_currency, target_currency, output_file):
    BASE_URL = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            data = response.json()
            conversion_rate = data["conversion_rates"][target_currency]
            timestamp = datetime.now()

            # 데이터를 저장할 데이터프레임 생성
            exchange_data = {"timestamp": [timestamp], "rate": [conversion_rate]}
            df = pd.DataFrame(exchange_data)
            
            # CSV 파일로 저장 (추가 모드로 저장)
            df.to_csv(output_file, mode="a", index=False, header=False)
            print(f"{base_currency} → {target_currency}: {conversion_rate} 저장 완료")
        else:
            print(f"API 요청 실패: 상태 코드 {response.status_code}")
    except Exception as e:
        print(f"오류 발생: {e}")
