const result = document.getElementById('weatherResult');

document.getElementById('searchButton').addEventListener('click', () => {
    const city = document.getElementById('cityInput').value;
    if (city) {
        getWeather(city);
    }
});

async function getWeather(city) {
    const apiKey = "038e45e1170c1161db236f50c6162dba"
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error('City not found');

        const data = await response.json();
        displayWeather(data);
    } catch (error) {
        result.innerHTML = `<p style="color: red;">${error.message}</p>`;
    }
}
function displayWeather(data) {
    result.innerHTML = `
        <h2>${data.name}</h2>
        <p>Temperature: ${data.main.temp} °C</p>
        <p>Weather: ${data.weather[0].description}</p>
        <p>Humidity: ${data.main.humidity} %</p>
    `;
}
