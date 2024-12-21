import pandas as pd
import matplotlib.pyplot as plt

def visualize_exchange_rate(input_file):
    try:
        # CSV 파일에서 데이터 읽기
        df = pd.read_csv(input_file, names=["timestamp", "rate"])
        if df.empty:
            print("CSV 파일이 비어 있습니다. 데이터를 확인하세요.")
            return

        # 그래프 그리기
        plt.figure(figsize=(10, 5))
        plt.plot(df["timestamp"], df["rate"], marker="o", label="환율 (USD → KRW)", color="blue")
        plt.title("실시간 환율 변화")
        plt.xlabel("시간")
        plt.ylabel("환율 (KRW)")
        plt.legend()
        plt.grid()
        plt.pause(0.1)  # 그래프 갱신 대기
        print("그래프 업데이트 완료.")
    except Exception as e:
        print(f"그래프 생성 중 오류 발생: {e}")
