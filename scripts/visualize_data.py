import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(input_file):
    try:
        # CSV 파일 읽기
        df = pd.read_csv(input_file)
        
        # 데이터 정제
        df['boarding'] = df['boarding'].astype(int)
        df['alighting'] = df['alighting'].astype(int)
        time_slots = df['time_slot'].unique()
        boarding_counts = df.groupby('time_slot')['boarding'].sum()
        alighting_counts = df.groupby('time_slot')['alighting'].sum()

        # 그래프 그리기
        plt.clf()  # 이전 그래프 지우기
        plt.plot(time_slots, boarding_counts, label="승차 인원", color="blue")
        plt.plot(time_slots, alighting_counts, label="하차 인원", color="red")
        plt.title("시간대별 승차/하차 인원")
        plt.xlabel("시간대")
        plt.ylabel("인원 수")
        plt.legend()
        plt.pause(0.1)  # 실시간 갱신 대기
        print("그래프 업데이트 완료.")
    except Exception as e:
        print(f"그래프 생성 중 오류 발생: {e}")
