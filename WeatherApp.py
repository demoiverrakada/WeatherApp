# Import necessary libraries
import requests

# Function to fetch weather data
def get_weather(api_key, city):
    # API endpoint for OpenWeatherMap's current weather data
    endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    # Make the API request
    response = requests.get(endpoint)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        weather_data = response.json()

        # Extract relevant information
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        # Display the weather information
        print(f"Weather in {city}: {description.capitalize()}, Temperature: {temperature} K")
    else:
        # Display an error message for unsuccessful requests
        print(f"Error: Unable to fetch weather data for {city}")

# API Key from OpenWeatherMap (sign up on their website to get your key)
api_key = "3c1ad02ebb838886bc2041d8dcb1b691"

# Get user input for the city
city = input("Enter the city name: ")

# Call the function to get and display weather information
get_weather(api_key, city)
