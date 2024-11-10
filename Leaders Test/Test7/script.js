const form = document.getElementById('myForm')
const result = document.getElementById('weatherResult');
const btn = document.getElementById('btn')


btn.addEventListener('click', () => {
    const city = form.elements.city.value;
    if (city) {
        getWeather(city);
    }
})

async function getWeather(city) {
    const apiKey = "3bd9b53a9b9d4d36894133733241011"
    // const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;
    const url = `http://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${city}&aqi=no`

    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error('City not found');

        const data = await response.json();
        displayWeather(data);
        console.log(data)
    } catch (error) {                  
        result.innerHTML = `<p style="color: red;">${error.message}</p>`;
    }
}


function displayWeather(data) {
    console.log(data)
    result.innerHTML = `
        <h2>${data.location.name}</h2>
        <p>Temperature: ${data.current.temp_c} °C</p>
        <p>Weather: ${data.current.condition.text}</p>
        <p>Humidity: ${data.current.humidity} %</p>
        <img src="${data.current.condition.icon}" width='50'>
    `;
}