import os, sys, re
import pandas as pd
import numpy as np

# библиотека для расчетов метрик
from sklearn import metrics

# тесты (тест Дики-Фуллера)
from statsmodels.tsa import stattools

# импортируем константы
from src.constants import *


def mase(
        y_true_:pd.DataFrame, y_pred_:pd.DataFrame, 
        y_train_:pd.DataFrame, season_period_:int=1
    ) -> float:
    """ Функция, реализующая вычисление метрики MASE - средняя абсолютная масштабированная ошибка 
        (mean absolute scaled error).
        Если значение MASE меньше 1, то новая модель работает лучше, 
        если значение MASE равно 1, то модели работают одинаково, 
        если значение MASE больше 1, то исходная модель работает лучше, чем новая модель.

    Args:
        y_true_ (pd.DataFrame): вектор тестовых значений
        
        y_pred_ (pd.DataFrame): вектор предсказанных значений
        
        y_train_ (pd.DataFrame): вектор тренировочных значений
        
        season_period_ (int, optional): количество периодов в полном сезонном цикле. Defaults to 1.

    Returns:
        float: значение метрики MASE
    """

    # формируем значения наивного прогноза
    y_pred_naive = y_train_[:-season_period_]

    # вычисляем метрику MAE наивного прогноза
    mae_naive = metrics.mean_absolute_error(y_train_[season_period_:], y_pred_naive)

    # вычисляем метрику MAE
    mae_pred = metrics.mean_absolute_error(y_true_, y_pred_)

    # метрика MASE
    return np.round(mae_pred / mae_naive, 3)


def get_metrics(
        y_true_:pd.DataFrame, y_pred_:pd.DataFrame, 
        y_train_:pd.DataFrame, season_period_:int=1
    ) -> None:
    """ Функция, реализующая вычисление метрик MAPE, MSE, RMSE, R2, MASE.

    Args:
        y_true_ (pd.DataFrame): вектор тестовых значений
        
        y_pred_ (pd.DataFrame): вектор предсказанных значений
        
        y_train_ (pd.DataFrame): вектор тренировочных значений
        
        season_period_ (int, optional): количество периодов в полном сезонном цикле. Defaults to 1.
    """
    
    # вычисляем метрики
    mape_score = metrics.mean_absolute_percentage_error(y_true_, y_pred_) * 100
    mse_score = metrics.mean_squared_error(y_true_, y_pred_) * 100
    rmse_score = metrics.mean_squared_error(y_true_, y_pred_, squared=False)
    r2_score = metrics.r2_score(y_true_, y_pred_)
    mase_score = mase(y_true_, y_pred_, y_train_, season_period_)

    # выводим метрики
    print(f'MAPE: {mape_score:.{int(TOL/2)}f} %')
    print(f'MSE: {mse_score:.{TOL}e} $^2')
    print(f'RMSE: {rmse_score:.{TOL}e} $')
    print(f'R2: {r2_score:.{int(TOL/2)}f}')
    print(f'MASE: {mase_score:.{int(TOL/2)}f}')


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


