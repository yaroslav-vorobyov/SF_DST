import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


def plot_hist_box(
        df_1_:pd.DataFrame, 
        df_2_:pd.DataFrame, 
        legend_str_1:str='', 
        legend_str_2:str='', 
        hide_x_ax_vals:bool=True, 
        rotate:bool=True, 
        kde_:bool=False, 
        figsize_:tuple=(20, 7), 
        bins_:int=100
    ) -> None:
    """ Функция, реализующая построение 4 графиков (полотно 2 x 2 субплоскости), гистограмма и коробчатый график, 
        для 2 выборок (признаков).

    Args:
        df_1_ (pd.DataFrame): датафрейм с 1-ым признаком

        df_2_ (pd.DataFrame): датафрейм со 2-ым признаком
        
        legend_str_1 (str, optional): легенда к заголовку графика 1. Defaults to ''.
        
        legend_str_2 (str, optional): легенда к заголовку графика 1. Defaults to ''.

        hide_x_ax_vals (bool, optional): триггер скрытия числовых значений на оси абсцисс. Defaults to True.
        
        rotate (bool, optional):    триггер разворота отрисовки графиков, графики одного типа строятся либо горизонтали, 
                                    либо по вертикали. Defaults to True.

        kde_ (bool, optional):  триггер рисования сглаживающего графика. Если True - время выполнения увеличится, 
                                примерно, в 2 раза. Defaults to False.
        
        figsize_ (tuple, optional): общие размеры полотна для всех графиков. Defaults to (20, 7).
        
        bins_ (int, optional): число столбцов гистограммы. Defaults to 100.
    """

    # если rotate == True: гистограммы - слева по вертикали, а коробчатые диаграммы - справа по вертикали
    if rotate:
        # задаём полотно, соотношение пропорций графиков
        fig, axes = plt.subplots(
            nrows=2, ncols=2, 
            figsize=(figsize_[0], figsize_[1]*1.3), 
            gridspec_kw={'height_ratios': (0.5, 0.5)}
        )

        # строим графики
        histplot_1 = sns.histplot(data=df_1_, x=df_1_, ax=axes[0][0], kde=kde_, bins=bins_)
        boxplot_1 = sns.boxplot(data=df_1_, x=df_1_, ax=axes[0][1], orient='h')
        histplot_2 = sns.histplot(data=df_2_, x=df_2_, ax=axes[1][0], kde=kde_, bins=bins_)
        boxplot_2 = sns.boxplot(data=df_2_, x=df_2_, ax=axes[1][1], orient='h')

        # задаём названия графиков и подписи осей
        axes[0][0].set(
            title='Распределение признака ' + "'" + df_1_.name + "'" + ' ' + legend_str_1, 
            xlabel='', 
            ylabel='Количество',
            )
        
        axes[0][1].set(
            title='Распределение признака ' + "'" + df_1_.name + "'" + ' ' + legend_str_1
            )
        
        axes[1][0].set(
            title='Распределение признака ' + "'" + df_2_.name + "'" + ' ' + legend_str_2, 
            xlabel='', 
            ylabel='Количество',
            )
        
        axes[1][1].set(
            title='Распределение признака ' + "'" + df_2_.name + "'" + ' ' + legend_str_2
            )

    # если rotate == False: гистограмма и под ней коробка, в 2 колонки
    else:
        # задаём полотно, соотношение пропорций графиков
        fig, axes = plt.subplots(
            nrows=2, ncols=2, 
            figsize=figsize_, 
            gridspec_kw={'height_ratios': (0.8, 0.2)}
        )
    
        # строим графики
        histplot_1 = sns.histplot(data=df_1_, x=df_1_, ax=axes[0][0], kde=kde_, bins=bins_)
        histplot_2 = sns.histplot(data=df_2_, x=df_2_, ax=axes[0][1], kde=kde_, bins=bins_)
        boxplot_1 = sns.boxplot(data=df_1_, x=df_1_, ax=axes[1][0], orient='h')
        boxplot_2 = sns.boxplot(data=df_2_, x=df_2_, ax=axes[1][1], orient='h')

        # задаём названия графиков и подписи осей
        axes[0][0].set(
            title='Распределение признака ' + "'" + df_1_.name + "'" + ' ' + legend_str_1, 
            xlabel='', 
            ylabel='Количество',
            )
        
        axes[1][0].set_xlabel('Признак ' + "'" + df_1_.name + "'" + ' ' + legend_str_1)

        axes[0][1].set(
            title='Распределение признака ' + "'" + df_2_.name + "'" + ' ' + legend_str_2, 
            xlabel='', 
            ylabel='Количество',
            )
        
        axes[1][1].set_xlabel('Признак ' + "'" + df_2_.name + "'" + ' ' + legend_str_2)
    
    # если триггер hide_x_ax_vals == True
    if hide_x_ax_vals:
        # скрываем числовые значения на осях абсцисс
        histplot_1.xaxis.set_major_formatter(plt.NullFormatter())
        histplot_2.xaxis.set_major_formatter(plt.NullFormatter())
        boxplot_1.xaxis.set_major_formatter(plt.NullFormatter())
        boxplot_2.xaxis.set_major_formatter(plt.NullFormatter())

    # выравниваем графики
    plt.tight_layout()


def plot_bar_line(
        df_1_:pd.DataFrame, df_2_:pd.DataFrame, 
        title_:str, xlabel_:str, 
        week_labels_:list=None,
        figsize_:tuple=(12, 6)
    ) -> None:
    """ Функция, реализующая построение 2 графиков в одном полотне, для 2 выборок (признаков).

    Args:
        df_1_ (pd.DataFrame): датафрейм с 1-ым признаком

        df_2_ (pd.DataFrame): датафрейм со 2-ым признаком

        title_ (str): заголовок графика

        xlabel_ (str): подпись к общей оси абсцисс

        week_labels_ (list): список меток оси графика (абсцисс / ординат). Defaults to None.

        figsize_ (tuple, optional): размеры полотна. Defaults to (12, 6).
    """
    
    # задаём число баров
    x = np.arange(len(df_1_))

    # лимит и шаг по верхней границе оси ординат
    limit_y = int(round(max(df_1_), -3)) + int(round(max(df_1_), -3) * 0.1)
    step_y = int(round((limit_y / 10), -4))

    # задаём размеры полотна
    fig, ax_1 = plt.subplots(figsize=figsize_)

    # строим график 1
    ax_1.bar(x, df_1_)
    
    # задаём подписи и размерность осей
    ax_1.set(title=title_, 
        xlabel=xlabel_, 
        ylabel='Количество поездок', 
        yticks=range(0, limit_y, step_y)
    )

    # для разных графиков задаём разные метки по оси абсцисс
    if (len(x) == 6) or (len(x) == 7):
        ax_1.set_xticks([0, 1, 2, 3, 4, 5, 6], week_labels_)
    else:
        ax_1.set_xticks(range(0, len(x)))

    # задаём 2-ую ось ординат, которая делит общую ось абсцисс с 1-ой осью ординат
    ax_2 = ax_1.twinx()

    # строим график 2
    ax_2.plot(df_2_, 'red')
    ax_2.grid()
    ax_2.set(ylabel='Медианная продолжительность поездки')


def plot_scatter_cluster(
        x_col_:str, y_col_:str, 
        ax_:plt.Axes, 
        title_:str, xlabel_:str, ylabel_:str, 
        df_:pd.DataFrame, 
        x_coords_lim:tuple, 
        y_coords_lim:tuple, 
        pnt_size:int=5, alpha_:float=0.8, 
    ) -> None:
    """ Функция, реализующая построение графика точек рассеяния кластеров.

    Args:
        x_col_ (str): признак оси абсцисс

        y_col_ (str): признак оси ординат

        ax_ (plt.Axes): оси координатной субплоскости построения графика

        title_ (str): заголовок графика

        xlabel_ (str): подпись оси абсцисс

        ylabel_ (str): подпись оси ординат

        df_ (pd.DataFrame, optional): датафрейм для построения графика

        x_coords_lim (tuple, optional): нижняя и верхняя границы координатных долгот. 
                                        Defaults to city_long_border.

        y_coords_lim (tuple, optional): нижняя и верхняя границы координатных широт. 
                                        Defaults to city_lat_border.

        pnt_size (int, optional): размер точки на графике. Defaults to 5.

        alpha_ (float, optional): степень прозрачности. Defaults to 0.8.
    """
    
    # строим график рассеяния
    scatter_ = sns.scatterplot(
        data=df_, 
        x=x_col_, 
        y=y_col_, 
        hue='geo_cluster', 
        legend=True, 
        palette='bright', 
        sizes=pnt_size, 
        alpha=alpha_, 
        ax=ax_
    )

    # задаём заголовок, подписи и крайние границы осей
    scatter_.set(
        title=title_, 
        xlabel=xlabel_, 
        ylabel=ylabel_, 
        xlim=x_coords_lim, 
        ylim=y_coords_lim
    )

    # задаём заголовок легенды и расположение на графике
    scatter_.legend(
        title='Номер географического кластера', 
        loc='upper right'
    )


