import requests
import json
import os

def get_weather_details(city_name):
    api_key = '46f59f4da7a889af7f91036007720574'  # Replace with your actual OpenWeatherMap API key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code == 200 and data.get("cod") == 200:
            city = data.get('name')
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description'].capitalize()

            # ✅ Display formatted output
            print(f"\nCity: {city}")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {description}")

            # ✅ Prepare data to store
            entry = {
                "city": city,
                "temp": temp,
                "humidity": humidity,
                "weather": description
            }

            # ✅ Append to results.json
            filename = "results.json"
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    try:
                        existing_data = json.load(file)
                    except json.JSONDecodeError:
                        existing_data = []
            else:
                existing_data = []

            existing_data.append(entry)

            with open(filename, "w") as file:
                json.dump(existing_data, file, indent=4)

        else:
            print("\nError: City not found. Please enter a valid city.")

    except requests.exceptions.RequestException:
        print("\nError: Could not connect to API. Check your API key or network connection.")

# 🔄 Prompt user for input
city_input = input("Enter city name: ")
get_weather_details(city_input)
