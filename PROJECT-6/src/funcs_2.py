import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import seaborn as sns
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

# библиотека для расчетов метрик
from sklearn import metrics

# библиотека для нормализации, стандартизации
from sklearn import preprocessing

# импортируем константы
from src.constants import *

# импортируем собственные функции
from src.funcs_3 import *


def get_day_names_sorted(
        ser_:pd.Series
    ) -> pd.Series:
    """ Функция, реализующая сортировку поименных дней недели в хронологическом порядке.

    Args:
        ser_ (pd.Series): исходный объект Series для обработки

    Returns:
        pd.Series: обработанный объект Series
    """

    # задаём список-словарь дней недели
    cats = {'Monday':0, 'Tuesday':1, 'Wednesday':2, 'Thursday':3, 'Friday':4, 'Saturday':5, 'Sunday':6}

    # конвертируем Series в DataFrame, сбрасываем индекс
    df_ = ser_.to_frame().reset_index()

    # первую колонку (с днями недели) преобразуем в "упорядоченную категориальную"
    df_[df_.columns[0]] = pd.Categorical(df_[df_.columns[0]], categories=[*cats.keys()], ordered=True)

    # сортируем по категориальной колонке
    df_ = df_.sort_values(df_.columns[0]).reset_index(drop=True).drop(columns=df_.columns[0])
    
    # возвращаем от DataFrame первую колонку (Series)
    return df_.iloc[:, 0]


def get_barplot(
        df_:pd.DataFrame, 
        col_1:str, col_2:str, operation_:str, 
        title_:str, x_axis_label_:str, y_axis_label_:str, 
        num_feat_:int=10, rotate_:bool=False, 
        xtick_angle_:int=0, xticks_labels_:list=None, 
        figsize_:tuple=(5, 8), 
        grid_:bool=False
    ) -> None:
    """ Функция, реализующая построение столбчатого графика, 
        бары откладываются горизонтально (по умолчанию) или вертикально.

    Args:
        df_ (pd.DataFrame): датасет для построения графика

        col_1 (str): столбец, по которым группируются данные
        
        col_2 (str): столбец, по которому вычисляются агрегированные значения
        
        operation_ (str): агрегирующая операция
        
        title_ (str): заголовок графика
        
        x_axis_label_ (str): подпись горизонтальной оси
        
        y_axis_label_ (str): подпись вертикальной оси
        
        num_feat_ (int, optional): число баров на графике. Defaults to 10.
        
        rotate_ (bool, optional): триггер поворота столбчатого графика. Defaults to False.
        
        xtick_angle_ (int, optional): угол поворота меток на оси абсцисс. Defaults to 0.
        
        xticks_labels_ (list, optional): список меток оси абсцисс. Defaults to None.
        
        figsize_ (tuple, optional): размер полотна графика. Defaults to (5, 8).
        
        grid_ (bool, optional): триггер отображения решетки. Defaults to False.
    """

    # формируем датафрейм для столбчатого графика в зависимости от агрегирующей операции
    match operation_:
        case 'nunique':
            temp=df_.groupby(col_1)[col_2].nunique(
                ).sort_values(ascending=True).nlargest(num_feat_)
        
        case 'sum_asc':
            temp=df_.groupby(col_1)[col_2].sum(
                ).sort_values(ascending=True).nlargest(num_feat_)

        case 'sum':
            temp=df_.groupby(col_1)[col_2].sum()

        case 'count':
            temp=get_day_names_sorted(
                df_.groupby(col_1, sort=False)[col_2].count()
            )

        case 'pivot':
            temp=df_

    # если rotate == True: бары столбчатого графика - вертикально (график горизонтальный)
    if rotate_:
        # задаём полотно
        _, ax_bar = plt.subplots(figsize=(figsize_[1], figsize_[0]))

        # строим график
        ax_bar = sns.barplot(
            x=temp.index, 
            y=temp.values
        )

        # задаём заголовок, подписи осей
        ax_bar.set(
            title=title_, 
            xlabel=y_axis_label_, 
            ylabel=x_axis_label_
        )

        # задаём угол поворота меток на оси абсцисс 
        plt.xticks(rotation=xtick_angle_)

    # если rotate == False: бары столбчатого графика - горизонтально (график вертикальный)
    else:
        # задаём полотно
        _, ax_bar = plt.subplots(figsize=figsize_)

        # строим график
        ax_bar = sns.barplot(
            x=temp.values, 
            y=temp.index
        )

        # задаём заголовок, подписи осей
        ax_bar.set(
            title=title_, 
            xlabel=x_axis_label_, 
            ylabel=y_axis_label_
        )
    
    # если хотим видеть сетку на графике
    if grid_:
        ax_bar.grid()

    # для временнЫх графиков задаём разные метки по оси абсцисс
    if (col_1 == 'Month'):
        ax_bar.set_xticks(list(range(0, len(temp))), xticks_labels_)
        
    elif (col_1 == 'DayOfWeek'):
        ax_bar.set_xticks(list(range(0, len(temp))), xticks_labels_)


def get_boxplot(
        df_:pd.DataFrame, 
        image_path_:str
    ) -> None:
    """ Функция, реализующая построение 3-ёх коробчатых графиков на одном полотне
    
    Args:
        df_ (pd.DataFrame): датафрейм с данными для графиков
        
        image_path_ (str): путь к файлу в системе для сохранения полотна с графиками
    """

    # формируем данные графиков
    boxes = [px.box(df_, x=column) for column in df_.columns]

    # задаём полотно, заголовки к графикам
    fig = make_subplots(
        rows=1, cols=3, 
        subplot_titles=(
            'Recency', 'Frequency', 'Monetary'
        )
    )

    # строим графики
    for i, _ in enumerate(boxes):
        fig.add_trace(boxes[i]['data'][0], row=1, col=i + 1)

    # обновляем размеры полотна
    fig.update_layout(height=500, width=800)

    # сохраняем в файл
    fig.write_image(DATA_SUBFOLDER + image_path_)

    # отобразить в формате svg
    fig.show('svg')


def get_scatterplot(
        df_:pd.DataFrame, 
        grid_:bool=False, 
        hue_labels_:np.ndarray=None, 
        palette_:str='bright', 
        figsize_:tuple=(12, 6)
    ) -> None:
    """ Функция, реализующая построения графика рассеяния.

    Args:
        df_ (pd.DataFrame): датасет для построения графика

        grid_ (bool, optional): триггер отображения решетки. Defaults to False.

        hue_labels_ (np.ndarray, optional): список меток для окрашивания значений, 
                                            принадлежащих одному кластеру. Defaults to None.
        
        palette_ (str, optional):   палитра окраски, работает при количестве кластеров больше 1. 
                                    Defaults to 'bright'.
        
        figsize_ (tuple, optional): размер полотна графика. Defaults to (12, 6).
    """

    fig = plt.subplots(figsize=figsize_)
    sns.scatterplot(
        data=df_, 
        x='axis-1', 
        y='axis-2', 
        hue=hue_labels_,
        palette=palette_
    )
    
    # если хотим видеть сетку на графике
    if grid_: 
        plt.grid()


def plot_cluster_profile(
        df_:pd.DataFrame, 
        image_path_:str, 
        width_:int=800
    ) -> None:
    """ Функция, реализующая построение полярной диаграммы. 

    Args:
        df_ (pd.DataFrame): датасет для построения графика
        
        image_path_ (str): путь к файлу в системе для сохранения полотна с графиками
        
        width_ (int, optional): ширина = высота графика (т.к. окружность). Defaults to 800.
    """
    # нормализуем сгруппированные данные, приводя их к масштабу 0-1
    scaler = preprocessing.MinMaxScaler()
    grouped_data = pd.DataFrame(
        scaler.fit_transform(df_), 
        columns=df_.columns
    )
    
    # создаём пустую фигуру (полотно)
    fig = go.Figure()

    # в цикле визуализируем полярную диаграмму для каждого кластера
    for i in range(df_.shape[0]):
        # создаём полярную диаграмму и добавляем её на общий график
        fig.add_trace(go.Scatterpolar(
            r=grouped_data.iloc[i].values,  # радиусы
            theta=grouped_data.columns,     # название засечек
            fill='toself',                  # заливка многоугольника цветом
            name=f'Cluster {i}',            # название - номер кластера
        ))
    
    # обновляем параметры фигуры (полотна)
    fig.update_layout(
        showlegend=True,                    # отображение легенды
        autosize=False,                     # устаналиваем свои размеры графика
        width=width_,                       # ширина (в пикселях)
        height=width_,                      # высота (в пикселях)
    )

    # сохраняем в файл
    fig.write_image(DATA_SUBFOLDER + image_path_)

    # отобразить в формате svg
    fig.show('svg')


def get_opt_metric_coef(
        model_:str, metric_:str, 
        start:int, stop:int, 
        X_:np.ndarray,
        random_state_:int=RANDOM_SEED_42, 
    ) -> pd.DataFrame:
    """ Функция, реализующая поиск оптимального числа кластеров с визуализацией. 

    Args:
        model_ (str): 
            строковое обозначение модели:
            
                - 'kmeans': cluster.Kmeans()
                - 'em'    : mixture.GaussianMixture(
                - 'aggl'  : cluster.AgglomerativeClustering()

        metric_ (str): 
            строковое обозначение метрики:

                - 'si'  : metrics.silhouette_score()
                - 'chi' : metrics.calinski_harabasz_score()
                - 'dbi' : metrics.davies_bouldin_score()

        start (int): начальное значение числа кластеров

        stop (int): конечное значение числа кластеров

        X_ (np.ndarray): стандаризованный массив наблюдений

        random_state_ (int): сид генерации значений. Defaults to 42.

    Returns:
        pd.DataFrame: датафрейм одной строкой - метрика (макс или мин), оптимальное значение кластеров
    """

    # создаём словарь, ключами будут коэффициент силуэта и количество кластеров
    df_res = {'metric': [], 'cluster': []}

    # задаём список меток для имени признака датафрейма | оси ординат, 
    # ключ - метрика расчёта, значение - наглядное название метрики на графике
    metric_names = {
        'si': ['silhouette_score', 'Коэффициент силуэта'], 
        'chi': ['calinski_harabasz_score', 'Индекс Калински-Харабаса'], 
        'dbi': ['davies_bouldin_score', 'Индекс Дэвиса-Болдина']
    }

    # в цикле перебираем все значения кластеров
    for cluster_num in range(start, stop + 1):
        # обучаем модель и предсказываем метки моделей
        match model_:
            case 'kmeans':
                estimator_ = get_estimator(
                    'kmeans', 
                    **{'n_clusters':cluster_num, 'random_state':random_state_}
                )
                labels_ = estimator_.fit_predict(X_)

            case 'em':
                estimator_ = get_estimator(
                    'em', 
                    **{'n_components':cluster_num, 'random_state':random_state_, 'warm_start':True}
                )
                labels_ = estimator_.fit_predict(X_)

            case 'aggl':
                estimator_ = get_estimator(
                    'aggl', 
                    **{'n_clusters':cluster_num}
                )
                labels_ = estimator_.fit_predict(X_)

        # вычисляем значение метрики, вносим число кластеров и метрику по ключам в словарь
        match metric_:
            case 'si':
                df_res['metric'].append(metrics.silhouette_score(X_, labels_))
            
            case 'chi':
                df_res['metric'].append(metrics.calinski_harabasz_score(X_, labels_))
            
            case 'dbi':
                df_res['metric'].append(metrics.davies_bouldin_score(X_, labels_))

        df_res['cluster'].append(cluster_num)

    # конвертируем словарь в датафрейм 
    df_res = pd.DataFrame(df_res)

    # визуализируем зависимость значения метрики от количества кластеров
    sns.lineplot(data=df_res, x='cluster', y='metric', marker='o', label="'" + metric_names[metric_][0] + "'")
    plt.title(metric_names[metric_][1] + ' ' + estimator_.__class__.__name__)
    plt.ylabel(metric_names[metric_][1])
    plt.xlabel('Число кластеров')

    # ищем строку в массиве с максимальным или мининимальным значением в столбце метрики, 
    # забираем пару, перезаписываем датафрейм
    if metric_ != 'dbi':
        df_res = pd.DataFrame(df_res.iloc[df_res.iloc[:, 0].idxmax()]).T
    else:
        df_res = pd.DataFrame(df_res.iloc[df_res.iloc[:, 0].idxmin()]).T

    # конвертируем кластеры до целых значений, переименовываем колонку с кластерами
    df_res['cluster'] = df_res['cluster'].astype('int8')
    df_res.rename({'cluster': metric_names[metric_][0]}, axis=1, inplace=True)

    # рисуем вертикальную линию - оптимальное значение числа кластеров
    plt.axvline(df_res.iloc[0, 1], lw=2, c='deeppink', linestyle='--', label='Оптим. число кластеров')
    plt.legend()

    return df_res


