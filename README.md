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
