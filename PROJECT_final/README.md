# Финальный проект
<table>
  <tr style="vertical-align:middle">
  <tr style="vertical-align:middle">
    <!-- <th><img src = 'https://i.hh.ru/logos/svg/hh.ru__min_.svg?v=11032019'></th> -->
    <!-- <th><img style="vertical-align:middle" img src = https://lms.skillfactory.ru/static/rg-theme/images/logo-header.svg></th> -->
    <!-- <th><img style="vertical-align:middle" img src = https://static.tildacdn.com/tild3862-3932-4061-b763-363135393134/logo.svg></th> -->
    <th height=30><img style="vertical-align:middle" img src = https://static.tildacdn.com/tild3736-6663-4331-b065-623334663336/SkillFactory.svg height=20></th>
  </tr>
</table>

## Оглавление
[1. Описание проекта](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT_final#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT_final#Какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT_final#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT_final#Этапы-работы-над-проектом)

[5. Результаты](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT_final#Результаты)

  > Перейти прямо к [презентации решения кейса](https://github.com/yaroslav-vorobyov/SF_DST/blob/main/PROJECT_final/project/PROJECT.ipynb)

[6. Выводы](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT_final#Выводы)  

[7. Фидбэк от ментора](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT_final#Фидбэк-от-ментора)

<br>

<center> <img src=https://previews.123rf.com/images/popovia/popovia1602/popovia160200275/51955530-stock-market-graph-and-bar-chart.jpg align="right" width="300"/> </center>

## Описание проекта

Представляет исследование временных рядов основных котировок крупных корпораций - Apple, Microsoft, Google, nVidia. Построение прогнозных моделей по всем котировкам в проекте, поиск наилучшего сочетания модель-котировка. Запуск лучшей модели в Docker. 

<br>

### Какой кейс решаем?

**Бизнес-задача:** произвести анализ, исследование временных рядов, выявить взаимосвязи, построить прогнозную модель.

**Техническая задача как для специалиста в Data Science:** построить оптимальную модель прогнозирования с возможностью использования в продакшене - в контейнере Docker.

<br>

### Задачи проекта:

1. Произвести предобработку набора данных.

2. Провести разведывательный анализ данных и выявить основные закономерности.

3. Построить несколько моделей машинного обучения, решающих задачу прогнозирования, определить оптимальную модель и подготовить к работе в контейнере.

5. Сформировать конфигурацию для успешного запуска в контейнере Docker и получения прогноза на заданную дату.

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT_final#Оглавление)

<br>

**Условия:**
- Решение оформляется только в *Jupyter Notebook*.
- Код на *Python* должен быть читаемым и понятным: имена переменных и функций отражают их сущность. Не забывать про отступы, разметку и комментарии в коде.
- Вывод оформляется в формате *Markdown* в отдельной ячейке.

<br>

За каждое задание можно получить **от 1 до 5 баллов**.
<!-- <table>
  <tbody>
    <tr style="vertical-align:middle">
      <td style="background-color: #2e765e; color: white; font-weight: bold">2 балла</td>
      <td style="align:left">Правильность решения задач, логичность построения запросов</td>
    </tr>
    <tr>
      <td style="background-color: #2e765e; color: white; font-weight: bold">2 балла</td>
      <td style="align:left">Читабельность и верное форматирование запросов и кода на Python, наличие комментариев в запросах;<br>Аккуратность оформления решения</td>
    </tr>
    <tr>
      <td style="background-color: #2e765e; color: white; font-weight: bold">2 балла</td>
      <td style="align:left">Логичность и полнота выводов</td>
    </tr>
    <tr>
      <td style="background-color: #2e765e; color: white; font-weight: bold">2 балла</td>
      <td style="align:left">Дополнительные исследования данных</td>
    </tr>
  </tbody>
</table> -->

* Необходимо: ответить на контрольные вопросы, загрузить ноутбук-шаблон со своим решением на GitHub.

**Максимальное количество баллов** за проект — 25.

<br>

**Что на практике:**
-   Учусь писать отличный код на Python;
-   Учусь строить оптимальные модели "скользящего среднего" SMA, "сезонная модель" SARIMAX, модель от FACEBOOK - Prophet, ансамблевая голосующая модель VotingRegressor, кросс-валидатор TimeSeriesSplit, поиск оптимальных гиперпараметров GridSearchCV, ансамблирование - "случайный лес" RandomForestClassifier, адаптивный бустинг AdaBoostRegressor, градиентный бустинг над деревьями решений GradientBoostingRegressor, а также самое продвинутое ML-решение - CatBoost;
-   Учусь сравнивать модели с точки зрения метрик, параметров;
-   Учусь следить за оптимизацией метрик модели;
-   Учусь следить за оптимизацией модели;
-   Учусь эффективно работать с IDE VSCode;
-   Повышаю квалификация по работе и обработке временных рядов;
-   Повышаю квалификацию по методам преобразования и очистки данных; 
-   Повышаю квалификацию с GitHub.

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT_final#Оглавление)

<br>

### Краткая информация о данных

В данном проекте первоначальные данные представлены в виде совокупного датасета размером: свыше 1500 тыс. строк, 5 лет ретроспективных данных, присутствуют пропуски и дубликаты. По итогам обработки будут выполнен upsamling для предсказания целевой переменной. Построить обучающие модели, которые должны произвести построение прогноза на выбранную дату, выбрать лучшую из них.

**Датасеты**:

* данные динамически подгружаются с Yahoo Finance, глубина котировок - за предыдущие 5 лет.

<br>

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT_final#Оглавление)

<br>

### Требования для работы
*   Основой интерпретатор - Python 3.10 (у меня взят из Windows App Store для максимальной бесшовной интеграции с VSCode);
*   Дополнительные требования перечислены в requirements.txt (получены командой pip freeze > requirements.txt);
*   Установка всех недостающих дополнительных компонент:

            pip install -r requirements.txt

*   В проекте используется:
    
    *   scikit-learn:
            
            pip install -U scikit-learn
    
    Документация по использованию - [Guide scikit-learn](https://scikit-learn.org/stable/user_guide.html)

    *   Prophet:

            python -m pip install prophet

    Документация по использованию - [Prophet](https://facebook.github.io/prophet/docs/quick_start.html)

    *   auto_arima:

            python -m pip install pmdarima

    Документация по использованию - [auto_arima](https://alkaline-ml.com/pmdarima/modules/generated/pmdarima.arima.auto_arima.html)

    *   statsmodels:

            python -m pip install statsmodels

    Документация по использованию - [statsmodels](https://www.statsmodels.org/stable/user-guide.html)

    *   CatBoost:

            pip install catboost

    Документация по использованию - [CatBoost](https://catboost.ai/en/docs/)

    
    *   Docker:

            https://docs.docker.com/get-docker/

    Документация по использованию - [Docker](https://docs.docker.com/)

*   Для контейнеризации:
    
    *   собрать контейнер:
            
            docker build -t server_image .
        
    *   запустить контейнер:
            
            docker run -it -d --rm -p 5000:5000 --name server_container server_image

*   Для получения предсказания:
        
    *   в браузере (на текущую дату):
            
            http://127.0.0.1:5000/predict
        
    *   в браузере (на произвольную дату):
            
            http://127.0.0.1:5000/predict?date=YYYY-MM-DD
            
            где date в формате год-месяц-день
            


:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT_final#Оглавление)

<br>

### Этапы работы над проектом
- Знакомство с данными;
- Импортирование необходимых библиотек;
- Изучение датасета на предмет наличия пропусков и типов данных;
- Обработка данных;
- Разделение данных для модели: выделение тестовой части, разделение тренингового датасета: 95% всех данных - на обучение, 5% данных - на валидацию, проверка размерности разделённых датасетов;
- Построение и обучение моделей;
- Сравнение и оценка целевых метрик на тестовом датасете;
- Проверка соответствия написанного кода стандарту PEP8;
- Оформление проекта.

<br>

### Результаты:

Проект c корректным выполнением кейса ["Финальный проект"](https://github.com/yaroslav-vorobyov/SF_DST/blob/main/PROJECT_final/project/PROJECT.ipynb).

<br>

### Выводы
В процессе выполнения кейса первоначальные данные были:
* Внимательно изучены исходные данные и проанализированы;
* Проведена подготовка данных к использованию;
* Данные были исследованы, выявлены зависимости, построены графики отражающие зависимости, сформированы выводы по данным;
* Построены обучающие модели, основанные на алгоритмах машинного обучения, выбраны несколько из них по минимальным целевым метрикам MAPE, MSE, RMSE;

Для решения задачи прогнозирования в данном кейсе **отлично себя показали модели**:

* <font color=LightSeaGreen>**&check;**</font> **SARIMA(1, 1, 1)x(1, 1, 1, 5)**
* <font color=LightSeaGreen>**&check;**</font> **Ансамбль<br>VotingRegressor + TimeSeriesSplit**
* <font color=LightSeaGreen>**&check;**</font> **GridSearchCV<br>CatBoostRegressor + TimeSeriesSplit**

По итогам моделирования построена модель **SARIMA(1, 1, 1)x(1, 1, 1, 5) для котировок Google**.

<br>

<center>

| Модель \ Котировка | <font color='LightSeaGreen'>**AAPL**</font> | <font color='LightSeaGreen'>**MSFT**</font> | <font color='LightSeaGreen'>**GOOG**</font> | NVDA |
| :-: | :-: | :-: | :-: | :-: |
| <font color='LightSeaGreen'>**SARIMA(1, 1, 1)x(1, 1, 1, 5)**</font> | AIC - 7238.361<br>MAPE: 4.53 %<br>MSE: 98.261 <br>RMSE: 9.913 | AIC - 9251.928<br>MAPE: 2.89 %<br>MSE: 164.325 <br>RMSE: 12.819 | <font color='LightSeaGreen'>**AIC - 6474.312<br>MAPE: 2.67 %<br>MSE: 16.393 <br>RMSE: 4.049**</font> | AIC - 10233.636<br>MAPE - 7.90 %<br>MSE - 1645.49 <br>RMSE - 40.565 |
| **Ансамбль<br>VotingRegressor + TimeSeriesSplit** | MAPE: 7.49 %<br>MSE: 243.376 <br>RMSE: 15.601 | MAPE: 3.38 %<br>MSE: 188.141 <br>RMSE: 13.716 | MAPE: 2.83 %<br>MSE: 16.958 <br>RMSE: 4.118 | MAPE - 17.47 %<br>MSE - 6480.24 <br>RMSE - 80.500 |
| **GridSearchCV<br>CatBoostRegressor + TimeSeriesSplit** | MAPE: 6.43 %<br>MSE: 1.90320e+02 <br>RMSE: 1.37956e+01 | MAPE: 3.85 %<br>MSE: 243.680 <br>RMSE: 15.610 | MAPE: 2.97 %<br>MSE: 21.789 <br>RMSE: 4.668 | MAPE - 22.12 %<br>MSE - 9984.72 <br>RMSE - 99.924 |

</center>

<br>

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT_final#Оглавление)

<br>

### Фидбэк от ментора
* Фидбэк PROJECT_final.url - содержит ссылку на отзыв, файл находится на Google Drive ментора
* Фидбэк PROJECT_final.pdf - версия отзыва с полным оформлением, если по ссылке файл будет удалён
* Фидбэк PROJECT_final.txt - текстовая версия отзыва, если по ссылке файл будет удалён

Перейти к [отзыву](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT_final/docs)

<br>

Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами.