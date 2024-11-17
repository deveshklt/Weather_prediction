from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'hi'
@app.route('/predict_weather',methods=['POST'])
def predict_weather():
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    wind_speed = float(request.form['wind_speed'])
    cloud_cover = float(request.form['cloud_cover'])
    pressure = float(request.form['pressure'])
    response = jsonify({
        'predicted_weather': float(util.get_weather_prediction(temperature,humidity,wind_speed,cloud_cover,pressure))
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
if __name__ == '__main__':
    print('Starting python flask server for weather prediction')
    util.load_saved_artifacts()  # Load saved artifacts before starting the server
    app.run()