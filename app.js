// Team: N.A.D.A
// Weather Station Web Application

let weather = {
  apiKey: "ce941f39aab90056289106d7803ab71a",
  fetchWeather: (city) => {
    fetch(
      "https://api.openweathermap.org/data/2.5/weather?q=" +
        city +
        "&units=imperial&appid=" +
        weather.apiKey
    )
      .then((response) => {
        if (!response.ok) {
          alert("No weather found.");
          throw new Error("No weather found.");
        }
        return response.json();
      })
      .then((data) => weather.displayWeather(data));
  },
  displayWeather: (data) => {
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
  },
  search: function () {
    this.fetchWeather(document.querySelector(".search-bar").value);
  },
};

document.querySelector(".search button").addEventListener("click", function () {
  weather.search();
});

document
  .querySelector(".search-bar")
  .addEventListener("keyup", function (event) {
    if (event.key === "Enter") {
      weather.search();
    }
  });

weather.fetchWeather("San Jose");
