let displayWeather = ((data) => {
    console.log(data);
    const { name: city } = data;
    const { icon, description } = data.weather[0];
    const { temp, humidity } = data.main;
    const { speed } = data.wind;
    document.querySelector("#city").innerText = city;
    document.querySelector(".icon").src =
      "https://openweathermap.org/img/wn/" + icon + ".png";
    document.querySelector("#description").innerText = description;
    document.querySelector("#temp").innerText = temp;
    document.querySelector("#humidity").innerText = humidity;
    document.querySelector("#wind").innerText = speed;
    document.querySelector(".weather").classList.remove("loading");
    document.body.style.backgroundImage =
      "url('https://source.unsplash.com/1600x900/?" + city + "')";
 });

let search = (() => {
    weather.fetchWeather(document.querySelector(".search-bar").value, displayWeather);
});


document.querySelector(".search button").addEventListener("click", function () {
  search();
});

document
  .querySelector(".search-bar")
  .addEventListener("keyup", function (event) {
    if (event.key === "Enter") {
      search();
    }
  });


weather.fetchWeather("San Jose", displayWeather);
