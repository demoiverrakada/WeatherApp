function getWeather() {
    // Get user input for the city
    const city = document.getElementById('cityInput').value;

    // API Key from OpenWeatherMap (sign up on their website to get your key)
    const apiKey = "3c1ad02ebb838886bc2041d8dcb1b691";

    // API endpoint for OpenWeatherMap's current weather data
    const endpoint = `http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;

    // Make the API request
    fetch(endpoint)
        .then(response => response.json())
        .then(data => {
            // Extract relevant information
            const temperature = data.main.temp;
            const description = data.weather[0].description;

            // Display the weather information
            const weatherInfo = document.getElementById('weatherInfo');
            weatherInfo.innerHTML = `Weather in ${city}: ${description}, Temperature: ${temperature} K`;
        })
        .catch(error => {
            // Display an error message for unsuccessful requests
            console.error(`Error: Unable to fetch weather data for ${city}`, error);
        });
}
