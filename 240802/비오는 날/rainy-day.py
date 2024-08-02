class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self. day = day
        self.weather = weather

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
arr.sort()
forecast = [Weather(date, day, weather) for date, day, weather in arr]


index = 0

for i, f in enumerate(forecast):
    if f.weather == 'Rain':
        index = i
        break

print(f'{forecast[index].date} {forecast[index].day} {forecast[index].weather}')