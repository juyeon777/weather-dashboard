import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib import rc

# Set font for Korean text
rc('font', family='Malgun Gothic')

# Enable interactive mode for live updates
plt.ion()
figure, ax = plt.subplots(figsize=(12, 6))


def visualize_weather(input_files, cities):
    """
    두 도시의 실시간 날씨 데이터를 한 그래프에 시각화
    """
    try:
        # Clear the previous plot
        ax.clear()

        # Loop through each city and its corresponding file
        for input_file, city in zip(input_files, cities):
            # Read the CSV file
            df = pd.read_csv(input_file)
            if df.empty:
                print(f"{city}의 CSV 파일이 비어 있습니다. 데이터를 확인하세요.")
                continue

            # Convert timestamp column to datetime
            df["timestamp"] = pd.to_datetime(df["timestamp"])

            # Plot weather data for each city
            ax.plot(df["timestamp"], df["temperature"], marker="o", label=f"{city} 온도 (°C)")
            ax.plot(df["timestamp"], df["humidity"], marker="o", label=f"{city} 습도 (%)")
            ax.plot(df["timestamp"], df["wind_speed"], marker="o", label=f"{city} 풍속 (m/s)")

        # Add title and labels
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
