import requests
import datetime

def get_weather(api_key, lat, lon):
    # API URL
    url = f"https://api.openweathermap.org/data/3.0/onecall"
    
    # Parameters for the API request
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric"  # Temperature in Celsius
    }
    
    # Make the API call
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

def display_weather(data):
    # Display current weather
    current = data["current"]
    print("\n--- Current Weather ---")
    print(f"Temperature: {current['temp']}°C")
    print(f"Feels Like: {current['feels_like']}°C")
    print(f"Description: {current['weather'][0]['description'].capitalize()}")
    print(f"Humidity: {current['humidity']}%")
    print(f"Wind Speed: {current['wind_speed']} m/s")
    
    # Display daily weather
    print("\n--- Daily Forecast ---")
    for day in data["daily"][:3]:  # Limit to next 3 days
        date = datetime.datetime.utcfromtimestamp(day["dt"]).strftime('%Y-%m-%d')
        temp_day = day["temp"]["day"]
        temp_night = day["temp"]["night"]
        description = day["weather"][0]["description"].capitalize()
        print(f"{date}: Day {temp_day}°C, Night {temp_night}°C, {description}")
    
    # Display weather alerts if any
    if "alerts" in data:
        print("\n--- Alerts ---")
        for alert in data["alerts"]:
            print(f"Event: {alert['event']}")
            print(f"Description: {alert['description']}")
    else:
        print("\nNo weather alerts.")

def main():
    # API Key (replace with your own key)
    api_key = ""
    
    # Location coordinates
    lat = 33.44
    lon = -94.04

    # Fetch and display weather
    weather_data = get_weather(api_key, lat, lon)
    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
