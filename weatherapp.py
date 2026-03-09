import urllib.request
import urllib.parse
import json

city = input("Enter city name: ").strip()  # remove extra spaces
api_key = "147ee5d6d7b12b24910a05a192745d41"

# Encode city name to handle spaces or special characters
city_encoded = urllib.parse.quote(city)

url = f"http://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appid={api_key}&units=metric"

try:
    with urllib.request.urlopen(url, timeout=5) as response:
        data = json.load(response)

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        print(f"City: {city}")
        print(f"Temperature: {temp} °C")
        print(f"Weather: {weather}")
    else:
        print("City not found or API key invalid")

except Exception as e:
    print("Error fetching data:", e)

