from datetime import datetime
from pprint import pprint
import requests
API_weather = 'c93753322e2352f0812982b8008cf32a'
# дополнительный api key 504ae7a2597100bebb0b96ec3e727072


def get_weather(city):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F32B",
        "Mist": "Туман \U0001F32B"
    }

    req = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_weather}&units=metric')
    date = req.json()
    pprint(date)
    city = date['name']
    current_temp = date['main']['temp']

    weather_description = date["weather"][0]['main']
    if weather_description in code_to_smile:
        wd = code_to_smile[weather_description]
    else:
        wd = "Посмотри лучше на улицу!"
    feels_like = date['main']['feels_like']
    humidity = date['main']['humidity']
    pressure = date['main']['pressure']
    speed_of_wind = date['wind']['speed']
    sunrise_time = datetime.fromtimestamp(date['sys']['sunrise'])
    sunset_time = datetime.fromtimestamp(date['sys']['sunset'])

    return f'Погода в городе {city} 🏙.\n' \
           f'Температура: 🌡 {current_temp}°С . {wd}\n' \
           f'Ощущается как: 🌡 {feels_like}°С . \n' \
           f'Влажность: {humidity}% .\n' \
           f'Давление: {pressure} мм.рт.ст .\n' \
           f'Скорость ветра: {speed_of_wind} м/c.\n' \
           f'Время восхода солнца: 🌅 {sunrise_time}.\n' \
           f'Время заката: 🌇 {sunset_time}.\n' \
           f'Хорошего дня!'
