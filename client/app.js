function predictWeather() {
    // Collect form data
    const data = {
        temperature: $("#temperature").val(),
        humidity: $("#humidity").val(),
        wind_speed: $("#wind_speed").val(),
        cloud_cover: $("#cloud_cover").val(),
        pressure: $("#pressure").val()
    };

    // Make an AJAX POST request
    $.ajax({
        url: "http://127.0.0.1:5000/predict_weather",
        type: "POST",
        data: data,
        success: function(response) {
            // Display the predicted weather
            $("#result").text("Predicted Weather: " + response.predicted_weather);
        },
        error: function(error) {
            console.error("Error:", error);
            $("#result").text("An error occurred while predicting the weather.");
        }
    });
}
