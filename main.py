from scripts.fetch_weather_data import fetch_weather_data
from scripts.visualize_weather import visualize_weather
import time

API_KEY = "c80714957aff9be02fbe9ac56ac34d13"
cities = ["Seoul", "Jeonju"]
input_files = [f"data/weather_{city.lower()}.csv" for city in cities]

def main():
    while True:
        # Fetch weather data for each city
        for city, input_file in zip(cities, input_files):
            fetch_weather_data(API_KEY, city, input_file)
        
        # Visualize weather data for all cities in one graph
        visualize_weather(input_files, cities)
        time.sleep(300)  # 5분 간격

if __name__ == "__main__":
    main()
