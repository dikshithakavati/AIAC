import requests
import json

def display_weather(city_name):
    api_key = '46f59f4da7a889af7f91036007720574'  # Replace with your actual OpenWeatherMap API key
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Task 1: Display full JSON response
        print("\n--- Full JSON Response ---")
        print(json.dumps(data, indent=4))

        # Task 3: Extract and display specific fields
        print("\n--- Extracted Weather Details ---")
        city = data.get('name')
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")

    except requests.exceptions.HTTPError:
        print("Error: Could not connect to API. Check your API key or city name.")
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please check your network connection.")
    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")

# Example usage:
city = input("Enter city name: ")
display_weather(city)
