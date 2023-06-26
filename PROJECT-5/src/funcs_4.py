import os, sys, re

import pandas as pd
import numpy as np

# библиотека для расчетов метрик
from sklearn import metrics

# библиотека модели линейной регрессии
from sklearn import linear_model

# библиотека модели деревьев решения
from sklearn import tree

# библиотека модели ансамблей
from sklearn import ensemble

# импортируем константы
from src.constants import *


# создаём объект класса как estimator
def get_estimator(
        model_type:linear_model.LinearRegression | linear_model.Ridge | \
            tree.DecisionTreeRegressor | ensemble.RandomForestRegressor | \
            ensemble.GradientBoostingRegressor,
        
        **params:dict | None
    ) -> linear_model.LinearRegression | linear_model.Ridge | \
        tree.DecisionTreeRegressor | ensemble.RandomForestRegressor | \
        ensemble.GradientBoostingRegressor:
    """ Функция генерации объекта класса:   объект класса линейная регрессия (LinearRegression), 
                                                                                            
                                            объект класса линейная регрессия с L2-регуляризацией (Ridge), 

                                            объект класса "дерево решений" (DecisionTreeRegressor), 

                                            объект класса "случайный лес", 

                                            объект класса "градиентный бустинг над деревьями решений".

    Args:
        model_type (str):   текстовое сокращённое наименование модели.

                            'linear' - модель линейной регрессии, 

                            'ridge' - модель линейной регрессии с L2-регуляризацией, 

                            'dtr' - модель "дерево решений", 

                            'rfr' - модель "случайный лес", 

                            'gbr' - модель "градиентный бустинг над деревьями решений"

        params (dict | None):   внешний словарь параметров модели | значение None (пустой словарь). 
                                При значении None генерируется стандартный объект класса 
                                + заданные параметры в params_estimator_

    Returns:
        estimator_ (
            linear_model.LinearRegression | linear_model.Ridge | 
            
            tree.DecisionTreeRegressor | ensemble.RandomForestRegressor | 
            
            ensemble.GradientBoostingRegressor):    объект класса линейная регрессия (LinearRegression)
                                                                                            
                                                    объект класса линейная регрессия с L2-регуляризацией (Ridge)

                                                    объект класса "дерево решений" (DecisionTreeRegressor)

                                                    объект класса "случайный лес"

                                                    объект класса "градиентный бустинг над деревьями решений"

    """
    
    # словарь парараметров модели
    params_estimator_ = {
        **params,                           # внешние параметры
        'random_state':RANDOM_SEED_42, 
        'n_jobs':CPU_ALL
    }

    match model_type:
        case 'linear':
            params_estimator_.pop('random_state')
            estimator_ = linear_model.LinearRegression(**params_estimator_)

        case 'ridge':
            params_estimator_.pop('n_jobs')
            estimator_ = linear_model.Ridge(**params_estimator_)

        case 'dtr':
            params_estimator_.pop('n_jobs')
            estimator_ = tree.DecisionTreeRegressor(**params_estimator_)

        case 'rfr':
            estimator_ = ensemble.RandomForestRegressor(**params_estimator_)

        case 'gbr':
            params_estimator_.pop('n_jobs')
            estimator_ = ensemble.GradientBoostingRegressor(**params_estimator_)
        
    return estimator_


def get_model_metrics(
    estimator_:callable, 
    X_train_:pd.DataFrame, y_train_:pd.Series, 
    X_test_:pd.DataFrame, y_test_:pd.Series, 
    print_metrics:bool=True, 
    return_values:bool=False
    ) -> float:
    """ Функция, реализующая вычисление метрики RMSLE на тренировочной и валидационной выборках. 

    Args:
        estimator_ (callable): функция формирования объекта класса - модели обучения. 

        X_train_ (pd.DataFrame, optional):  тренировочный датасет, содержит стандартизованные признаки. 
                                            Defaults to X_train_scaled.

        y_train_ (pd.Series, optional): тренировочный вектор целевых значений, содержит логарифмированный признак. 
                                        Defaults to y_train_log.

        X_test_ (pd.DataFrame, optional):   валидационный датасет, содержит стандартизованные признаки. 
                                            Defaults to X_valid_scaled.

        y_test_ (pd.Series, optional):  валидационный вектор целевых значений, содержит логарифмированный признак. 
                                        Defaults to y_valid_log.

        print_metrics (bool, optional): триггер вывода отчёта. 
                                        Defaults to True.

        return_values (bool, optional): триггер возвращения метрик и обученной модели. 
                                        Defaults to False.

    Returns:
        estimator_ (
            linear_model.LinearRegression | linear_model.Ridge | 
            
            tree.DecisionTreeRegressor | ensemble.RandomForestRegressor | 
            
            ensemble.GradientBoostingRegressor):    объект класса линейная регрессия (LinearRegression)
                                                                                            
                                                    объект класса линейная регрессия с L2-регуляризацией (Ridge)

                                                    объект класса "дерево решений" (DecisionTreeRegressor)

                                                    объект класса "случайный лес"

                                                    объект класса "градиентный бустинг над деревьями решений"
    
        train_rmsle (float): метрика RMSLE на тренировочной выборке
        
        valid_rmsle (float): метрика RMSLE на валидационной выборке
    """

    # обучаем модель и предсказание значений для обеих выборок
    estimator_.fit(X_train_, y_train_)
    y_pred_train_ = estimator_.predict(X_train_)
    y_pred_valid_ = estimator_.predict(X_test_)

    # вычисляем метрики RMSLE на обеих выборках
    train_rmsle = metrics.mean_squared_error(y_train_, y_pred_train_, squared=False)
    valid_rmsle = metrics.mean_squared_error(y_test_, y_pred_valid_, squared=False)

    # выводим только отчёт, без возвращения значений
    if print_metrics:
        print(f'-= {estimator_.__class__.__name__} =-')
        print(f'RMSLE на обучающей выборке: {train_rmsle:.{TOL}f}')
        print(f'RMSLE на валидационной выборке: {valid_rmsle:.{TOL}f}')

    # если return_scores == True, то возвращаем значения
    if return_values:
        return estimator_, y_pred_valid_, (train_rmsle, valid_rmsle)


