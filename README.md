# 🌤️ 실시간 날씨 대시보드
이 프로젝트는 OpenWeatherMap API를 사용하여 특정 도시의 실시간 날씨 데이터를 수집하고, 이를 시각화하여 대시보드 형태로 보여주는 Python 애플리케이션입니다.

---

## 📋 주요 기능

OpenWeatherMap API를 사용하여 특정 도시의 실시간 날씨 데이터를 주기적으로 수집합니다.

    * 수집 데이터는 CSV 파일에 저장

온도(°C), 습도(%), 풍속(m/s)을 실시간으로 그래프에 표시합니다.

    * 그래프는 기존 창에서 업데이트

API 키와 도시 이름을 설정하여 원하는 지역의 데이터를 수집할 수 있습니다.

    * 해당 코드는 지역을 서울, 전주로 설정

---

## 실행 방법

**1. 환경 설정**

+ Python 3.8 이상 설치 확인.
+ 필수 라이브러리 설치:
`
    pip install -r requirements.txt
`

**2. AWS 설정**

+ S3 버킷 생성:
    수집된 데이터를 저장할 버킷 이름을 설정합니다.
+ CloudWatch 로그 그룹 및 스트림 생성:
    * 로그 그룹 이름 예시: weather-data-logs
    * 로그 스트림 이름 예시: weather-stream-seoul, weather-stream-jeonju.

**3. API 키 설정**

+ OpenWeatherMap API 키를 발급받아 스크립트에 추가합니다.
+ main.py에서 API 키 및 도시 이름 설정:

    API_KEY = "your_api_key"

    CITIES = ["Seoul", "Jeonju"]

**4. 프로젝트 실행**

다음 명령어로 스크립트를 실행합니다:

    python main.py


**5. 결과 확인**

+ S3 버킷: 업로드된 날씨 데이터를 확인합니다.
+ CloudWatch 대시보드: 서울과 전주의 온도, 습도, 풍속 데이터를 실시간으로 확인할 수 있습니다.

---
## 📁 프로젝트 구조

```plaintext
weather-dashboard/
├── data/                                # 날씨 데이터를 저장하는 디렉토리
│   ├── weather_seoul.csv                # 서울 날씨 데이터 파일
│   ├── weather_jeonju.csv               # 전주 날씨 데이터 파일
│
├── scripts/                             # 프로젝트에 사용되는 스크립트 모음
│   ├── aws_utils.py                     # AWS S3 업로드 및 CloudWatch 로그 작성 함수
│   ├── fetch_weather_data.py            # 날씨 데이터 수집 스크립트
│   ├── visualize_weather.py             # 데이터를 시각화하는 스크립트
│
├── .gitignore                           # Git에 포함하지 않을 파일/폴더 설정
├── main.py                              # 프로젝트의 메인 실행 파일
├── README.md                            # 프로젝트 설명 및 실행 방법 안내
├── requirements.txt                     # Python 패키지 의존성 정보

