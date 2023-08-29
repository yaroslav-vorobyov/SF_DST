import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# библиотека построения коррелограмм
from statsmodels.graphics import tsaplots

# импортируем константы
from src.constants import *


def get_correlograms(
        y_train_:pd.DataFrame, lags_:int=15, 
        figsize_:tuple=(10, 10)
    ) -> None:
    """ Функция, реализующая построение коррелограмм:
        - автокорреляция временного ряда;
        - автокорреляция частичных остатков временного ряда.

    Args:
        y_train_ (pd.DataFrame): вектор тренировочныъ значений

        lags_ (int, optional): число лагов (меток) на оси абсцисс. Defaults to 15.

        figsize_ (tuple, optional): размер общего полотна. Defaults to (10, 10).
    """

    # строим коррелограммы: 
    # автокорреляция (верхний), автокорреляция частичных остатков (нижний)
    _, axes = plt.subplots(2, 1, figsize=figsize_)
    tsaplots.plot_acf(y_train_, lags=lags_, ax=axes[0])
    tsaplots.plot_pacf(y_train_, lags=lags_, ax=axes[1])


def get_plot_time_series_predicted(
        y_pred_:pd.DataFrame, y_test_:pd.DataFrame, 
        title_main:str, title_pred:str,
        color_main:str='blue', color_pred:str='orange', 
        color_pred_border:str='red', pred_border_style='--',
        grid_main:bool=True, grid_pred:bool=False, 
        figsize_:tuple=(20, 12)
    ) -> None:
    """ Функция, реализующая построеник графика предсказания на общем графике и с масштабированием

    Args:
        y_pred_ (pd.DataFrame): массив предсказанных значений с границами доверительными значений
        
        y_test_ (pd.DataFrame): вектор тестовых значений
        
        title_main (str): заголовок основного графика
        
        title_pred (str): заголовок масштабированного графика предсказания
        
        color_main (str, optional): цвет основного графика. Defaults to 'blue'.
        
        color_pred (str, optional): цвет графика предсказания. Defaults to 'orange'.
        
        color_pred_border (str, optional): цвет границ доверительных интервалов. Defaults to 'red'.
        
        pred_border_style (str, optional): стиль границ доверительных интервалов. Defaults to '--'.
        
        grid_main (bool, optional): сетка основного графика. Defaults to True.
        
        grid_pred (bool, optional): сетка графика предсказания. Defaults to False.
        
        figsize_ (tuple, optional): общий размер полотна. Defaults to (20, 12).
    """

    def get_plot_pred_only():
        """ Функция, реализующая отрисовку только предсказания 
            с доверительными границами на общем графике и с масштабированием
        """
        plt.plot(
            y_pred_.loc[y_test_.index][y_pred_.columns[0]], 
            color=color_pred, 
            label='Предсказанные значения'
        )
        plt.plot(
            y_pred_.loc[y_test_.index][y_pred_.columns[2]], 
            color=color_pred_border, 
            linestyle=pred_border_style, label='Доверительный интервал 95%'
        )
        plt.plot(
            y_pred_.loc[y_test_.index][y_pred_.columns[3]], 
            color=color_pred_border, 
            linestyle=pred_border_style
        )


    # размер общего полотна
    plt.figure(figsize=figsize_)

    # верхний график
    plt.subplot(2, 1, 1)
    plt.plot(
        y_pred_[y_pred_.columns[1]], 
        color=color_main, label='Истинные значения'
    )
    get_plot_pred_only()
    plt.title(title_main, size = 18)

    # если нужна сетка
    if grid_main: plt.grid()

    plt.legend()

    # нижний график
    plt.subplot(2, 2, 3)
    plt.plot(
        y_pred_.loc[y_test_.index][y_pred_.columns[1]], 
        color=color_main, label='Предсказанные значения'
    )
    get_plot_pred_only()
    plt.title(title_pred, size=14)

    # если нужна сетка
    if grid_pred: plt.grid()

    plt.legend()


