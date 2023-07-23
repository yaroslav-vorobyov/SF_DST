import os, sys, re
import pandas as pd
import numpy as np

# импортируем константы
from src.constants import *


def get_hypothesis(
        df_:pd.DataFrame
    ) -> None:
    """ Функция, реализующая проверку гипотезы на наличие пар транзакций 
        код товара-индентификатор клиента в связке покупка-отмена.

    Args:
        df_ (pd.DataFrame): датафрейм для обработки
    """

    # пробегаемся в цикле по отменённым позициям в транзакциях
    for _, row in df_.iterrows():
        # создаём и объединям маски с совпадающим кодом товара, 
        # идентификатором клиента и инверсным значением количества товара
        # если аналогов не найдено - завершаем цикл
        if df_[(df_['CustomerID'] == row['CustomerID']) & \
                (df_['StockCode'] == row['StockCode']) & \
                (df_['Quantity'] == -row['Quantity'])
            ].shape[0] == 0:
            print('Гипотеза не верна')
            break
        else:
            print('Гипотеза верна')


def get_quantity_canceled(
        df_:pd.DataFrame, 
        neg_qty:pd.DataFrame
    ) -> pd.Series:
    """ Функция, реализующая формирование нового признака - количество
        возвращенного товара для каждой транзакции

    Args:
        df_ (pd.DataFrame): датафрейм для обработки

        neg_qty (pd.DataFrame): датафрейм с транзакциями с отрицательным количеством товара

    Returns:
        qty_canceled (pd.Series): признак с количеством возвратов по каждой операции
    """

    # задаём Series той же длины, что и столбцы таблицы, заполняем нулями
    qty_canceled = pd.DataFrame(np.zeros(df_.shape[0]), index=df_.index)
    
    for _, col in neg_qty.iterrows():
        # создаём DataFrame из всех контрагентов
        df_test = df_[(df_['CustomerID'] == col['CustomerID']) &
                        (df_['StockCode']  == col['StockCode']) & 
                        (df_['InvoiceDate'] < col['InvoiceDate']) & 
                        (df_['Quantity'] > 0)].copy()
        # если транзация-возврат не имеет контрагента - ничего не делаем
        if (df_test.shape[0] == 0): 
            continue
        
        # а если транзакция-возврат имеет ровно одного контрагента, то
        # добавляем количество отмененного в столбец QuantityCanceled 
        elif (df_test.shape[0] == 1): 
            index_order = df_test.index[0]
            qty_canceled.loc[index_order] = -col['Quantity']       
        
        # и если транзакция-возврат имеет несколько контрагентов
        # задаём количество отмененного товара в столбец QuantityCanceled для той транзакции на покупку,
        # в которой количество товара < -(количество товаров в транзакции-возврате)
        elif (df_test.shape[0] > 1): 
            df_test.sort_index(axis=0, ascending=False, inplace=True)        
            for ind, val in df_test.iterrows():
                if val['Quantity'] < -col['Quantity']: 
                    continue
                qty_canceled.loc[ind] = -col['Quantity']
                break    
    
    return qty_canceled


