import os, sys, re

import pandas as pd
import numpy as np

# библиотека для нормализации, стандартизации
from sklearn import preprocessing

# библиотека для формирования пайплайнов
from sklearn import pipeline

# библиотека модели ансамблей
from sklearn import ensemble

# библиотека модели кластеризации
from sklearn import cluster

# библиотека модели эллиптической кластеризации
from sklearn import mixture

# библиотека модели метода главных компонент PCA
from sklearn import decomposition

# библиотека модели TSNE
from sklearn import manifold

# импортируем константы
from src.constants import *


# создаём объект класса как estimator
def get_estimator(
        model_type:pipeline.Pipeline | decomposition.PCA | \
            manifold.TSNE | cluster.KMeans | \
            mixture.GaussianMixture | cluster.AgglomerativeClustering |\
            ensemble.RandomForestClassifier | ensemble.GradientBoostingClassifier,
        
        **params:dict | None
    ) -> pipeline.Pipeline | decomposition.PCA | \
            manifold.TSNE | cluster.KMeans | \
            mixture.GaussianMixture | cluster.AgglomerativeClustering |\
            ensemble.RandomForestClassifier | ensemble.GradientBoostingClassifier:
    """ Функция генерации объекта класса: 

            - объект класса "конвейер" (Pipeline), 
            - объект класса "декомпозиция методом главных компонент" (PCA), 
            - объект класса нелинейного уменьшения размерности (T-SNE), 
            - объект класса "жёсткой" Kmeans-кластеризации (Kmeans), 
            - объект класса "мягкой" EM-кластеризации (GaussianMixture), 
            - объект класса агломеративной кластеризации (AgglomerativeClustering), 
            - объект класса "случайный лес" (RandomForestClassifier), 
            - объект класса "градиентный бустинг над деревьями решений" (GradientBoostingClassifier).

    Args:
        model_type (str): 
            текстовое сокращённое наименование модели:

                - 'pipe_pca' : конвейер StandardScaler + PCA, 
                - 'pipe_tsne': конвейер StandardScaler + TSNE, 
                - 'pca'      : модель декомпозиция методом главных компонент, 
                - 't_sne'    : модель нелинейного уменьшения размерности, 
                - 'kmeans'   : модель "жёсткой" Kmeans-кластеризации, 
                - 'em'       : модель "мягкой" EM-кластеризации, 
                - 'aggl'     : модель агломеративной кластеризации, 
                - 'rfc'      : модель"случайный лес", 
                - 'gbc'      : модель "градиентный бустинг над деревьями решений".

        params (dict | None): 
            внешний словарь параметров модели | значение None (пустой словарь). 
            При значении None генерируется стандартный объект класса + заданные параметры в params_estimator_

    Returns:
        estimator_ (
            pipeline.Pipeline | decomposition.PCA | 
            manifold.TSNE | cluster.KMeans | 
            mixture.GaussianMixture | cluster.AgglomerativeClustering) | 
            ensemble.RandomForestClassifier | ensemble.GradientBoostingClassifier: 
            
                - объект класса "конвейер" (Pipeline), 
                - объект класса "декомпозиция методом главных компонент" (PCA), 
                - объект класса нелинейного уменьшения размерности (T-SNE), 
                - объект класса "жёсткой" Kmeans-кластеризации (Kmeans), 
                - объект класса "мягкой" EM-кластеризации (GaussianMixture), 
                - объект класса агломеративной кластеризации (AgglomerativeClustering), 
                - объект класса "случайный лес" (RandomForestClassifier), 
                - объект класса "градиентный бустинг над деревьями решений" (GradientBoostingClassifier).
    """
    
    # словарь парараметров модели
    params_estimator_ = {
        'random_state':RANDOM_SEED_42, 
        **params    # внешние параметры
    }

    match model_type:
        case 'pipe_pca':
            # рекурсивный вызов
            estimator_ = pipeline.Pipeline([
                    ('scaler', preprocessing.StandardScaler()), 
                    ('pca', get_estimator('pca', **params_estimator_))
                ]
            )

        case 'pipe_tsne':
            # рекурсивный вызов
            estimator_ = pipeline.Pipeline([
                    ('scaler', preprocessing.StandardScaler()), 
                    ('tsne', get_estimator('t_sne', **params_estimator_))
                ]
            )

        case 'pca':
            estimator_ = decomposition.PCA(**params_estimator_)

        case 't_sne':
            estimator_ = manifold.TSNE(**params_estimator_)

        case 'kmeans':
            estimator_ = cluster.KMeans(**params_estimator_)

        case 'em':
            estimator_ = mixture.GaussianMixture(**params_estimator_)

        case 'aggl':
            params_estimator_.pop('random_state')
            estimator_ = cluster.AgglomerativeClustering(**params_estimator_)
        
        case 'rfc':
            estimator_ = ensemble.RandomForestClassifier(**params_estimator_)

        case 'gbc':
            estimator_ = ensemble.GradientBoostingClassifier(**params_estimator_)
        
    return estimator_


