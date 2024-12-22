import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib import rc

rc('font', family='DejaVu Sans')  # CloudShell에서 사용 가능한 기본 폰트
# 인터랙티브 모드 활성화
plt.ion()

# 그래프 그리기 함수
def visualize_weather(input_files, cities):
    """
    여러 도시의 실시간 날씨 변화를 그래프로 표시
    """
    try:
        # 그래프 초기화
        plt.figure(figsize=(12, 6))

        # 각 도시 데이터 플롯
        for input_file, city in zip(input_files, cities):
            df = pd.read_csv(input_file)

            # 데이터가 비어 있는지 확인
            if df.empty:
                print(f"{city}의 CSV 파일이 비어 있습니다. 데이터를 확인하세요.")
                continue

            # 타임스탬프 변환
            df["timestamp"] = pd.to_datetime(df["timestamp"])

            # 온도, 습도, 풍속 데이터 추가
            plt.plot(df["timestamp"], df["temperature"], marker="o", label=f"{city} 온도 (°C)")
            plt.plot(df["timestamp"], df["humidity"], marker="o", label=f"{city} 습도 (%)")
            plt.plot(df["timestamp"], df["wind_speed"], marker="o", label=f"{city} 풍속 (m/s)")

        # 그래프 제목 및 레이블
        plt.title("도시별 실시간 날씨 변화")
        plt.xlabel("시간")
        plt.ylabel("값")
        plt.legend()
        plt.grid()

        # X축 시간 포맷 설정
        plt.gca().xaxis.set_major_formatter(DateFormatter("%Y-%m-%d %H:%M"))
        plt.xticks(rotation=45)

        # 그래프 업데이트
        plt.draw()
        plt.pause(0.1)
        print("그래프 업데이트 완료.")

    except Exception as e:
        print(f"그래프 생성 중 오류 발생: {e}")
