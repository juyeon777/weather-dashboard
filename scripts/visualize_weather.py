import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib import rc

# Set font for Korean text
rc('font', family='Malgun Gothic')  # Windows 환경용 (맑은 고딕)

# Initialize the figure globally to reuse it
plt.ion()  # Enable interactive mode
figure, ax = plt.subplots(figsize=(12, 6))  # Create a reusable figure

def visualize_weather(input_file):
    try:
        # Read data
        df = pd.read_csv(input_file)
        if df.empty:
            print("CSV 파일이 비어 있습니다. 데이터를 확인하세요.")
            return

        # Convert timestamp column to datetime
        df["timestamp"] = pd.to_datetime(df["timestamp"])

        # Clear the previous plot
        ax.clear()

        # Plot graph
        ax.plot(df["timestamp"], df["temperature"], marker="o", label="온도 (°C)", color="red")
        ax.plot(df["timestamp"], df["humidity"], marker="o", label="습도 (%)", color="blue")
        ax.plot(df["timestamp"], df["wind_speed"], marker="o", label="풍속 (m/s)", color="green")

        ax.set_title("실시간 날씨 변화")
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
