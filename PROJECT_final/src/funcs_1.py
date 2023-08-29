import os, sys, re
import pandas as pd
import numpy as np

# библиотека для расчетов метрик
from sklearn import metrics

# тесты (тест Дики-Фуллера)
from statsmodels.tsa import stattools

# импортируем константы
from src.constants import *


def get_metrics(
        y_true_:pd.DataFrame, y_pred_:pd.DataFrame, 
    ) -> None:
    """ Функция, реализующая вычисление метрик MAPE, MSE, RMSE.

    Args:
        y_true_ (pd.DataFrame): вектор тестовых значений
        
        y_pred_ (pd.DataFrame): вектор предсказанных значений
    """
    
    # вычисляем метрики
    mape_score = metrics.mean_absolute_percentage_error(y_true_, y_pred_) * 100
    mse_score = metrics.mean_squared_error(y_true_, y_pred_)
    rmse_score = metrics.mean_squared_error(y_true_, y_pred_, squared=False)

    # выводим метрики
    print(f'MAPE: {mape_score:.{int(TOL/2)}f} %')
    print(f'MSE: {mse_score:.{TOL}e} $^2')
    print(f'RMSE: {rmse_score:.{TOL}e} $')


def get_adfuller_test(
        df_:pd.DataFrame, 
        crit_val_:int=1
    ) -> None:
    """ Функция, реализующая тест Дики-Фуллера.

    Args:
        df_ (pd.DataFrame): 
            датафрейм для оценки

        crit_val_ (int, optional): 
            пороговое значения из словаря критических значений, значения от 1 до 3. Defaults to 1.
    """

    if  (crit_val_< 1) or (crit_val_ > 3):
        print('Пороговые значения могут быть только от 1 до 3, включительно')
        return None
    
    # выполянем тест
    result = stattools.adfuller(df_)

    # выводим результат
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    print(f'Critical Values: {result[4]}')

    # выводим заключение
    if result[0] > result[4][list(result[4].keys())[crit_val_ - 1]]: 
        print (f"При пороге '{list(result[4].keys())[crit_val_ - 1]}' есть единичные корни, ряд НЕ стационарен")
    else:
        print (f"При пороге '{list(result[4].keys())[crit_val_ - 1]}' единичных корней нет, ряд СТАЦИОНАРЕН")


def split_data(
        df:pd.DataFrame, 
        split_:int=0.75
    ) -> tuple:
    """ Функция, реализующая разбиение датасета.

    Args:
        df (pd.DataFrame): исходный датафрейм для разбиения
        split_ (int, optional): коэффициент разбиения тренировочной выборки. Defaults to 0.75.

    Returns:
        tuple: тренировочная и тестовая выборки
    """

    split_size = round(len(df) * split_)
    train_, test_ = df[:split_size], df[split_size:]
    return train_, test_


