import os
from flask import app, json
import datetime
import pickle
import numpy as np

# объект Flask-приложения
application = app.Flask(__name__)

# # обработчик запросов на endpoint '/welcome'
# @application.route('/welcome')
# def hello_func():
#     name = app.request.args.get('name', default='world')
#     return f'Hello, {name}!'

# обработчик запросов на endpoint '/'
@application.route('/')
def index():
    return 'Test message. The server is running'

# обработчик запросов на endpoint '/time'
@application.route('/time')
def current_time():
    now = datetime.datetime.now()
    return {'time':now}


# производим десериализацию и извлекаем модель из файла формата pkl
with open('./model/arima.pkl', 'rb') as pkl_file:
    model_from_file = pickle.load(pkl_file)

# обработчик запросов на endpoint '/predict'
@application.route('/predict')#, methods=['POST'])
def predict():
    while True:
        try:
            # для скрипта
            features = app.request.args.get('date', default=(datetime.datetime.today() + datetime.timedelta(days=+1)).strftime("%Y-%m-%d"))
            
            # забираем единственное предсказание
            prediction_model_from_file = model_from_file.forecast(features)[-1]

            return f'Предсказание на {features}: {prediction_model_from_file:.5f}'
        except:
            print('\033[33mЕсли требуется предсказание на конкретную дату, то в адресной строке "http://localhost:5000/predict?date=YYYY-MM-DD", '\
                f'где date в формате год-месяц-день\033[0m')
            return


# запуск приложения
if __name__ == '__main__':

    application.run(host='0.0.0.0', port=5000)