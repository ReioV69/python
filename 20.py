# Reio Viikmaa 14.01.25
# 20

import requests

# API võtme ja linna nime määramine
city = input("Mis linn: ")
api_key = "df5bbd3e5f5a44aa17b7d96495c1fc9b"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
print(url)
# API päringu tegemine
response = requests.get(url)

# Vastuse kontrollimine
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Ilma kirjeldus: {weather}")
    print(f"Temperatuur: {temperature} °C")
else:
    print("Viga andmete allalaadimisel:", response.status_code)