import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib import rc

# Set font for Korean text
rc('font', family='Malgun Gothic')  # Windows 환경용 (맑은 고딕)

# Initialize the figure globally to reuse it
plt.ion()  # Enable interactive mode
figure, ax = plt.subplots(figsize=(12, 6))  # Create a reusable figure

def visualize_weather(seoul_file, jeonju_file):
    try:
        # Read data for Seoul
        df_seoul = pd.read_csv(seoul_file)
        if df_seoul.empty:
            print("서울 CSV 파일이 비어 있습니다. 데이터를 확인하세요.")
            return

        # Read data for Jeonju
        df_jeonju = pd.read_csv(jeonju_file)
        if df_jeonju.empty:
            print("전주 CSV 파일이 비어 있습니다. 데이터를 확인하세요.")
            return

        # Convert timestamp column to datetime
        df_seoul["timestamp"] = pd.to_datetime(df_seoul["timestamp"])
        df_jeonju["timestamp"] = pd.to_datetime(df_jeonju["timestamp"])

        # Clear the previous plot
        ax.clear()

        # Plot graph for Seoul
        ax.plot(df_seoul["timestamp"], df_seoul["temperature"], marker="o", label="서울 온도 (°C)", color="red")
        ax.plot(df_seoul["timestamp"], df_seoul["humidity"], marker="o", label="서울 습도 (%)", color="blue")
        ax.plot(df_seoul["timestamp"], df_seoul["wind_speed"], marker="o", label="서울 풍속 (m/s)", color="green")

        # Plot graph for Jeonju
        ax.plot(df_jeonju["timestamp"], df_jeonju["temperature"], marker="^", label="전주 온도 (°C)", color="orange")
        ax.plot(df_jeonju["timestamp"], df_jeonju["humidity"], marker="^", label="전주 습도 (%)", color="cyan")
        ax.plot(df_jeonju["timestamp"], df_jeonju["wind_speed"], marker="^", label="전주 풍속 (m/s)", color="lime")

        ax.set_title("서울 & 전주 실시간 날씨 변화")
        ax.set_xlabel("시간")
        ax.set_ylabel("값")
        ax.legend()
        ax.grid()

        # Format X-axis labels
        ax.xaxis.set_major_formatter(DateFormatter("%Y-%m-%d %H:%M"))
        plt.xticks(rotation=45)

        # Redraw the updated figure
        figure.canvas.draw()
        figure.canvas.flush_events()
        print("그래프 업데이트 완료.")

    except Exception as e:
        print(f"그래프 생성 중 오류 발생: {e}")
