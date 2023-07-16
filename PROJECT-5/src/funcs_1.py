import os, sys, re
import pandas as pd
import numpy as np

# загрузка и обработка файлов
import wget, gdown, fast_unzip, rm

# импортируем константы
from src.constants import *


def get_dataset(
        filename_:str, url_:str, hoster_:str, sep_:str, new_filename:str=''
    ) -> pd.DataFrame:
    """ Функция, реализующая загрузку датасетов с Google Drive или Skillfactory по ссылке

    Args:
        filename_ (str): имя файла, включающее подкаталог хранения ('./data/*.csv)
        
        url_ (str): ссылка на хостинг:
                    - Google Drive: 'https://drive.google.com/file/d/FILE_ID/view?usp=sharing'
                    - Skillfactory: 'https://lms-cdn.skillfactory.ru/ ... /filename_.*'
        
        hoster_ (str):  мнемоническое обозначение хостинга:
                        - Google Drive: 'g'
                        - Skillfactory: 's'
        
        sep_ (str): символ-сепаратор для корректного считывания данных датасета

        new_filename (str, optional):   новое имя файла для переименования, если имя загружаемого 
                                        файла не устраивает. Default to None. 

    Returns:
        df_ (pd.DataFrame): возвращает считанный из файла датасет
    """
    
    # если файл есть (со старым | новым именем) - просто читаем его
    if os.path.exists(filename_):
        df_ = pd.read_csv(filename_, sep=sep_)
        return df_
    elif os.path.exists(new_filename):
        df_ = pd.read_csv(new_filename, sep=sep_)
        return df_ 
    
    # если файла нет - выгружаем, сохраняем, переименовываем, читаем с диска
    else:
        # создаём подкаталог для записи датасета
        if os.path.exists(DATA_SUBFOLDER +'data') == False:
            os.mkdir(DATA_SUBFOLDER + 'data')

        match hoster_:
            case 'g':
                # загружаем файл, выводим сообщения только при ошибке, перезаписываем при наличии в ./
                gdown.download(url=url_, output='data.zip', quiet=True, fuzzy=True)

                # извлекаем загруженный архив в подкаталог для данных
                os.system('fast_unzip data.zip -d' + DATA_SUBFOLDER + 'data/')

                # удаляем загруженный архив
                os.system('rm data.zip')

                # если new_filename != None, переименовываем и читаем файл с новым именем
                if new_filename is not None:
                    try:
                        os.replace(filename_, new_filename)
                        df_ = pd.read_csv(new_filename, sep=sep_)
                    except FileNotFoundError:
                        df_ = pd.read_csv(filename_, sep=sep_)
                
                # если не переименовываем файл (new_filename == None), то просто читаем файл
                else:
                    df_ = pd.read_csv(filename_, sep=sep_)

                return df_

            case 's':
                # wget.download(url_, filename_.split('/')[1])
                # фиксируем расширение файла
                extesion_ = url_.split('/')[-1].split('.')[1]
                
                # если по ссылке 'csv'
                if extesion_ == 'csv':
                    gdown.download(url=url_, output=filename_, quiet=True, fuzzy=True)

                # если по ссылке 'zip'
                elif extesion_ == 'zip':
                    # загружаем файл, выводим сообщения только при ошибке, перезаписываем при наличии в ./
                    gdown.download(url=url_, output='data.zip', quiet=True, fuzzy=True)
                
                    # извлекаем загруженный архив в подкаталог для данных
                    os.system('fast_unzip data.zip -d' + DATA_SUBFOLDER + 'data/')

                    # удаляем загруженный архив
                    os.system('rm data.zip')
                
                # если new_filename != None, переименовываем и читаем файл с новым именем
                if new_filename is not None:
                    try:
                        os.replace(filename_, new_filename)
                        df_ = pd.read_csv(new_filename, sep=sep_)
                    except FileNotFoundError:
                        df_ = pd.read_csv(filename_, sep=sep_)
                
                # если не переименовываем файл (new_filename == None), то просто читаем файл
                else:
                    df_ = pd.read_csv(filename_, sep=sep_)
                
                return df_


def modify_data_types(
        df_:pd.DataFrame
    ) -> pd.DataFrame:
    """ Функция, реализующая "облегчение" типов данных в целях сокращения занимаемого места в памяти. 

    Args:
        df_ (pd.DataFrame, optional): датафрейм для обработки. Defaults to df.

    Returns:
        df_ (pd.DataFrame): датафрейм с обработанными признаками
    """
    
    # преобразуем признаки в формат datetime
    df_['pickup_datetime'] = pd.to_datetime(df_['pickup_datetime'], format='%Y-%m-%d %H:%M:%S')

    # преобразуем признак в бинарный
    df_['store_and_fwd_flag'] = df_['store_and_fwd_flag'].swifter.apply(lambda x: 1 if x == 'Y' else 0)

    # понижаем размерность признаков по типу занимаемых данных
    df_[['vendor_id', 'passenger_count', 'store_and_fwd_flag']] = \
        df_[['vendor_id', 'passenger_count', 'store_and_fwd_flag']].astype('int8')

    df_[['pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude']] = \
        df_[['pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude']].astype('float32')

    return df_


def fill_null_weather_data(
        df_:pd.DataFrame
    ) -> pd.DataFrame:
    """ Функция, реализующая заполнение пропущенных значений в столбцах основного датафрейма
    
    Args:
        df_ (pd.DataFrame): датафрейм для обработки. Defaults to df.

    Returns:
        df_ (pd.DataFrame): датафрейм с обработанными признаками
    """
    
    # заполнение пропусков в признаках с погодными условиями
    df_[['temperature', 'visibility', 'wind speed', 'precip']] = \
        df_[['temperature', 'visibility', 'wind speed', 'precip']].fillna(
            df_.groupby('pickup_date')[['temperature', 'visibility', 'wind speed', 'precip']].transform('median')
        )
    
    # заполнение пропусков со словарём 'имя_столбца': число (признак)
    values = {
        'total_distance': df_['total_distance'].median(),
        'total_travel_time': df_['total_travel_time'].median(),
        'number_of_steps': df_['number_of_steps'].median(),
        'events': 'None'
    }
    
    # заполняем пропуски в соответствии с заявленным словарем
    df_ = df_.fillna(values)
    
    # # понижаем размерность признаков по типу занимаемых данных
    # df['number_of_steps'] = df['number_of_steps'].astype('int8')

    return df_


