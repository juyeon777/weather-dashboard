# 🌤️ 실시간 날씨 대시보드
이 프로젝트는 OpenWeatherMap API를 사용하여 특정 도시의 실시간 날씨 데이터를 수집하고, 이를 시각화하여 대시보드 형태로 보여주는 Python 애플리케이션입니다.

---

## 📋 주요 기능
실시간 데이터 수집

OpenWeatherMap API를 사용하여 특정 도시의 실시간 날씨 데이터를 주기적으로 수집합니다.
수집 데이터는 CSV 파일에 저장됩니다.
데이터 시각화

온도(°C), 습도(%), 풍속(m/s)을 실시간으로 그래프에 표시합니다.
그래프는 기존 창에서 업데이트되며, 새 창을 띄우지 않습니다.
사용자 정의 설정

API 키와 도시 이름을 설정하여 원하는 지역의 데이터를 수집할 수 있습니다.

--

## 📂 프로젝트 구조
weather-dashboard/
│
├── data/
│   └── weather_data.csv       # 날씨 데이터를 저장하는 CSV 파일
│
├── logs/
│   └── app.log                # 실행 중 발생하는 로그 기록
│
├── scripts/
│   ├── fetch_weather_data.py  # 날씨 데이터를 수집하는 스크립트
│   └── visualize_weather.py   # 날씨 데이터를 시각화하는 스크립트
│
├── main.py                    # 애플리케이션 메인 실행 파일
├── README.md                  # 프로젝트 설명 파일
└── requirements.txt           # 의존성 패키지 목록
