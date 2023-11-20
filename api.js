// Team: N.A.D.A
// Weather Station Web Application

let weather = {
  apiKey: "ce941f39aab90056289106d7803ab71a",
  fetchWeather: (city, display) => {
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
      .then((data) => display(data));
  },
};



