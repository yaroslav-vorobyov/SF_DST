import pandas as pd
import numpy as np

# библиотека модели кластеризации
from sklearn import cluster

# импортируем константы
from src.constants import *


def add_datetime_features(
        df_:pd.DataFrame, 
        col_:str='pickup_datetime'
    ) -> pd.DataFrame:
    """ Функция, реализующая выделения дополнительных временных признаков из основного признака. 

    Args:
        df_ (pd.DataFrame, optional): датафрейм для обработки. Defaults to df.

        col (str, optional): временнОй признак для обработки из df_. Defaults to 'pickup_datetime'.

    Returns:
        df_ (pd.DataFrame): датафрейм с добавлением новых признаков
    """

    # с аксессором dt выделяем дату, час и день недели, 
    df_['pickup_date'] = pd.to_datetime(df_[col_]).dt.date
    df_['pickup_hour'] = pd.to_datetime(df_[col_]).dt.hour

    # преобразуем полученный аксессором dt признак в формат datetime (понадобится далее)
    df_['pickup_date'] = pd.to_datetime(df_['pickup_date'])

    # для всех дней недели применяем смещение нумерации: 1 - Пн, 7 - Вс
    df_['pickup_day_of_week'] = pd.to_datetime(df_[col_]).dt.weekday + 1
    
    # понижаем размерность признаков по типу занимаемых данных
    df_[['pickup_hour', 'pickup_day_of_week']] = df_[['pickup_hour', 'pickup_day_of_week']].astype('int8')
    
    return df_


def add_holiday_features(
        df_1:pd.DataFrame, 
        df_2:pd.DataFrame
    ) -> pd.DataFrame:
    """ Функция, реализующая новый признак с помощью дополнительного датафрейма с данными о праздничных днях.

    Args:
        df_1 (pd.DataFrame, optional): основной датафрейм для слияния. Defaults to df.

        df_2 (pd.DataFrame, optional): датафрейм с данными о праздничных днях. Defaults to holiday_data.

    Returns:
        df_1 (pd.DataFrame): основной датафрейм с добавлением нового признака
    """

    # выполняем слияние данных
    df_1 = pd.merge(df_1, df_2, left_on='pickup_date', right_on='date', how='left')

    # из основного датафрейма убираем ненужные признаки
    df_1.drop(columns=['date', 'day'], inplace=True)

    # заполняем nan-значения 0-ми и понижаем тип до int8 вместо float64
    df_1['pickup_holiday'].fillna(0, downcast='int8', inplace=True)
    
    return df_1


def add_osrm_features(
        df_1:pd.DataFrame, 
        df_2:pd.DataFrame
    ) -> pd.DataFrame:
    """ Функция, реализующая новые признаки с помощью дополнительного датафрейма с данными из OSRM.

    Args:
        df_1 (pd.DataFrame, optional): основной датафрейм для слияния. Defaults to df.
        
        df_2 (pd.DataFrame, optional): датафрейм с данными о праздничных днях. Defaults to osrm_data.

    Returns:
        df_1 (pd.DataFrame): основной датафрейм с добавлением новых признаков
    """
    
    # понижаем размерность признаков по типу занимаемых данных
    # т.к. есть nan / NA, тип int8 никак не применить, только float (float16)
    df_2['number_of_steps'] = df_2['number_of_steps'].astype('float16')

    # понижаем размерность признаков по типу занимаемых данных
    df_2['total_distance'] = df_2['total_distance'].astype('float32')
    df_2['total_travel_time'] = df_2['total_travel_time'].astype('float16')

    # оставляем необходимые признаки
    df_2 = df_2[['id', 'number_of_steps', 'total_distance', 'total_travel_time']]
    
    # выполняем слияние данных
    df_1 = pd.merge(df_1, df_2, left_on='id', right_on='id', how='left')
    
    return df_1


def get_haversine_distance(
        lat1:float, lng1:float, 
        lat2:float, lng2:float
    ) -> float:
    """ Функция, реализующая вычисление расстояния Хаверсина в километрах (км)

    Args:
        lat1 (float): широта точки 1
        
        lng1 (float): долгота точки 1
        
        lat2 (float): широта точки 2
        
        lng2 (float): долгота точки 2

    Returns:
        h (float): расстояние Хаверсина в километрах (км)
    """

    # переводим углы в радианы
    lat1, lng1, lat2, lng2 = map(np.radians, (lat1, lng1, lat2, lng2))

    # считаем кратчайшее расстояние h по формуле Хаверсина
    lat_delta = lat2 - lat1
    lng_delta = lng2 - lng1
    d = np.sin(lat_delta * 0.5) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(lng_delta * 0.5) ** 2
    h = 2 * EARTH_RADIUS * np.arcsin(np.sqrt(d))

    return h


def get_angle_direction(
        lat1:float, lng1:float, 
        lat2:float, lng2:float
    ) -> float:
    """ Функция, реализующая вычисление угла направления движения (в градусах)

    Args:
        lat1 (float): широта точки 1
        
        lng1 (float): долгота точки 1
        
        lat2 (float): широта точки 2
        
        lng2 (float): долгота точки 2

    Returns:
        alpha (float): угол направления движения (в градусах)
    """

    # переводим углы в радианы
    lat1, lng1, lat2, lng2 = map(np.radians, (lat1, lng1, lat2, lng2))

    # считаем угол направления движения alpha по формуле угла пеленга
    lng_delta_rad = lng2 - lng1
    y = np.sin(lng_delta_rad) * np.cos(lat2)
    x = np.cos(lat1) * np.sin(lat2) - np.sin(lat1) * np.cos(lat2) * np.cos(lng_delta_rad)
    alpha = np.degrees(np.arctan2(y, x))
    
    return alpha


def add_geographical_features(
        df_:pd.DataFrame
    ) -> pd.DataFrame:
    """ Функция, реализующая новые признаки с помощью внешних функций. 
        На вход функции подаётся 4 признака, для каждой строки вычисляется:
        - расстояние расстояние Хаверсина в километрах (км)
        - угол направления движения (в градусах)

    Args:
        df_ (pd.DataFrame, optional): датафрейм для обработки. Defaults to df.

    Returns:
        df_ (pd.DataFrame): датафрейм с добавлением новых признаков
    """

    df_['haversine_distance'] = df_.swifter.apply(
        lambda row: get_haversine_distance(
            row['pickup_latitude'], row['pickup_longitude'],
            row['dropoff_latitude'], row['dropoff_longitude'],
            ), 
        axis=1
        )

    df_['direction'] = df_.swifter.apply(
        lambda row: get_angle_direction(
            row['pickup_latitude'], row['pickup_longitude'],
            row['dropoff_latitude'], row['dropoff_longitude'],
            ), 
        axis=1
        )

    # понижаем размерность признаков по типу занимаемых данных
    df_[['haversine_distance', 'direction']] = \
        df_[['haversine_distance', 'direction']].astype('float32')
    return df_


def add_cluster_features(
        df_:pd.DataFrame, 
        cluster_model:cluster.KMeans
    ) -> pd.DataFrame:
    """ Функция, реализующая новый признак из коэффициентов предсказания модели KMeans

    Args:
        df_ (pd.DataFrame, optional): датафрейм для обработки. Defaults to df.
        
        cluster_model (cluster.KMeans, optional):   обученная модель кластеризации KMeans. 
                                                    Defaults to KMns.

    Returns:
        df_ (pd.DataFrame): датафрейм с добавлением нового признака
    """

    # создаем обучающую выборку из географических координат всех точек
    coords_= df_[['pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude']].values

    # переносим в новый признак в датафрейм
    df_['geo_cluster'] = cluster_model.predict(coords_)

    # понижаем размерность признаков по типу занимаемых данных
    df_['geo_cluster'] = df_['geo_cluster'].astype('int8')

    return df_


def add_weather_features(
        df_1:pd.DataFrame, 
        df_2:pd.DataFrame
    ) -> pd.DataFrame:
    """ Функция, реализующая новые признаки с помощью дополнительного датафрейма с данными о погоде.

    Args:
        df_1 (pd.DataFrame, optional): основной датафрейм для слияния. Defaults to df.
        
        df_2 (pd.DataFrame, optional): датафрейм с ежечасными данными о погоде. Defaults to weather_data.

    Returns:
        df_1 (pd.DataFrame): основной датафрейм с добавлением новых признаков
    """
    
    # выполняем слияние данных
    df_1 = pd.merge(df_1, df_2, left_on=['pickup_date', 'pickup_hour'], right_on=['date', 'hour'], how='left')

    # из основного датафрейма убираем ненужные признаки
    df_1.drop(columns=['date', 'hour'], inplace=True)

    return df_1


