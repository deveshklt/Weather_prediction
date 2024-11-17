import json
import pickle
import numpy as np

__data_columns = None
__model = None


def get_weather_prediction(temperature,humidity,wind_speed,cloud_cover,pressure):
    x = np.zeros(len(__data_columns))
    x[0] = temperature
    x[1] = humidity
    x[2] = wind_speed
    x[3] = cloud_cover
    x[4] = pressure
    return __model.predict([x])[0]
def load_saved_artifacts():
    print('Load saved artifacts start...')

    global __data_columns
    global __model

    with open('./artifacts/columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
    
    with open('./artifacts/weather_forecast_model.pickle','rb') as f:
        __model = pickle.load(f)

    print('load_saved_artifacts ends successfully')

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_weather_prediction(23.720338,89.592641,7.335604,50.501694,1032.378759))
