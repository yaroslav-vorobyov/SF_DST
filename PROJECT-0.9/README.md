# Проект 0.9. Домашнее задание. Модуль: ML-7. Оптимизация гиперпараметров модели
<table>
  <tr style="vertical-align:middle">
    <!-- <th><img src = 'https://i.hh.ru/logos/svg/hh.ru__min_.svg?v=11032019'></th> -->
    <!-- <th><img style="vertical-align:middle" img src = https://lms.skillfactory.ru/static/rg-theme/images/logo-header.svg></th> -->
    <!-- <th><img style="vertical-align:middle" img src = https://static.tildacdn.com/tild3862-3932-4061-b763-363135393134/logo.svg></th> -->
    <th height=30><img style="vertical-align:middle" img src = https://static.tildacdn.com/tild3736-6663-4331-b065-623334663336/SkillFactory.svg height=20></th>
  </tr>
</table>

## Оглавление
[1. Описание проекта](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.9#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.9#Какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.9#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.9#Этапы-работы-над-проектом)

[5. Результаты](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.9#Результаты)

  > Перейти прямо к [презентации решения кейса](https://github.com/yaroslav-vorobyov/SF_DST/blob/main/PROJECT-0.9/HW-09.ipynb)

[6. Выводы](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.9#Выводы)  

[7. Фидбэк от ментора](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.9#Фидбэк-от-ментора)

<br>

## Описание проекта
Необходимо предсказать биологический ответ молекул (столбец 'Activity') по их химическому составу (столбцы D1-D1776).

<br>

### Какой кейс решаем?
Необходимо обучить две модели: **логистическую регрессию** и **"случайный лес"**. Далее нужно сделать подбор гиперпараметров с помощью базовых и продвинутых методов оптимизации. Важно использовать все четыре метода (GridSeachCV, RandomizedSearchCV, Hyperopt, Optuna), хотя бы по разу, максимальное количество итераций не должно превышать 50.

<br>

**Условия:**
- Решение оформляется только в *Jupyter Notebook*.
- Решение оформляется в соответствии с *ноутбуком-шаблоном*.
- Не следует создавать много ячеек для решения задачи — это проявляет неудобства при проверке.
- Код на *Python* должен быть читаемым и понятным: имена переменных и функций отражают их сущность. Не забывать про отступы, разметку и комментарии в коде.
- Вывод оформляется в формате *Markdown* в отдельной ячейке.

<br>

**Метрика качества:**
* В ноутбуке должны быть ответы на следующие вопросы:

<!-- <table>
  <thead style="vertical-align:middle">
    <tr>
      <td style="text-align: center; color: black; font-weight: bold">Балл</td>
      <td style="text-align: center; color: black; font-weight: bold">Критерий</td>
    </tr>
    <tr>
      <td style="text-align: center; background-color: #eb6b56; color: black; font-weight: bold">0</td>
      <td style="text-align:left">Задание не выполнено</td>
    </tr>
  </thead>
  <tbody style="vertical-align:middle">
    <tr>
      <td style="text-align: center; background-color: #f7da64; color: black; font-weight: bold">1</td>
      <td style="text-align:left">Обучено две модели; гипепараметры подобраны при помощи одного метода</td>
    </tr>
    <tr>
      <td style="text-align: center; background-color: #f7da64; color: black; font-weight: bold">2</td>
      <td style="text-align:left">Обучено две модели; гипепараметры подобраны при помощи двух методов</td>
    </tr>
    <tr>
      <td style="text-align: center; text-align: center; background-color: #61bd6d; color: black; font-weight: bold">3</td>
      <td style="text-align:left">Обучено две модели; гипепараметры подобраны при помощи трёх методов</td>
    </tr>
    <tr>
      <td style="text-align: center; background-color: #61bd6d; color: black; font-weight: bold">4</td>
      <td style="text-align:left">Обучено две модели; гипепараметры подобраны при помощи четырёх методов</td>
    </tr>
    <tr>
      <td style="text-align: center; background-color: #61bd6d; color: black; font-weight: bold">5</td>
      <td style="text-align:left">Обучено две модели; гипепараметры подобраны при помощи четырёх методов;<br> использована кросс-валидация</td>
    </tr>
  </tbody>
</table> -->

| **Балл** | <center>**Критерий** |
| :---: | --- |
| <font color='eb6b56'>**0**</font> | <font color='eb6b56'>Задание не выполнено</font> |
| <font color='f7da64'>**1**</font> | <font color='f7da64'>Обучено две модели; гипепараметры подобраны при помощи одного метода</font> |
| <font color='f7da64'>**2**</font> | <font color='f7da64'>Обучено две модели; гипепараметры подобраны при помощи двух методов</font> |
| <font color='61bd6d'>**3**</font> | <font color='61bd6d'>Обучено две модели; гипепараметры подобраны при помощи трёх методов</font> |
| <font color='61bd6d'>**4**</font> | <font color='61bd6d'>Обучено две модели; гипепараметры подобраны при помощи четырёх методов</font> |
| <font color='61bd6d'>**5**</font> | <font color='61bd6d'>Обучено две модели; гипепараметры подобраны при помощи четырёх методов;<br> использована кросс-валидация</font> |

* Необходимо: ответить на контрольные вопросы, сдать проект на проверку, загрузив ноутбук-шаблон со своим решением на GitHub.

**Максимальное количество баллов** за выполнение задания — 5.

<br>

**Что на практике:**
-   Учусь писать отличный код на Python;
-   Учусь строить оптимальные модели логистической регрессии и "случайного леса";
-   Учусь сравнивать модели с точки зрения метрик, параметров;
-   Учусь следить за оптимизацией метрик модели;
-   Учусь следить за оптимизацией модели;
-   Учусь эффективно работать с IDE VSCode;
-   Повышаю квалификацию по методам преобразования и очистки данных; 
-   Повышаю квалификацию с GitHub.

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.9#Оглавление)

<br>

### Краткая информация о данных

В данном проекте первоначальные данные представлены в виде датасета размером: свыше 3750 строк, 1776 столбцов, типа float64 и int64, в столбцах пропуски и дубликаты отсутствуют. Предварительная обработка не требуется, данные уже закодированы и нормализованы. В связи с этим необходимо построить обучающие модели: логистической регрессии и модель случайного леса с оптимизацией на кросс-валидации.

* train_sem09.csv - первоначальные данные.

  Данные представлены в формате CSV.  Каждая строка представляет молекулу. 

  Первый столбец 'Activity' содержит экспериментальные данные, описывающие фактический биологический ответ [0, 1];
  
  Остальные столбцы D1-D1776 представляют собой молекулярные дескрипторы — это вычисляемые свойства, которые могут фиксировать некоторые характеристики молекулы, например размер, форму или состав элементов.

<br>

### Требования для работы
*   Основой интерпретатор - Python 3.10 (у меня взят из Windows App Store для максимальной бесшовной интеграции с VSCode);
*   Дополнительные требования перечислены в requirements.txt (получены командой pip freeze > requirements.txt);
*   Установка всех недостающих дополнительных компонент:

            pip install -r requirements.txt

*   В проекте используется:

    *   scikit-learn:
            
            pip install -U scikit-learn
    
    Документация по использованию scikit-learn - [Guide scikit-learn](https://scikit-learn.org/stable/user_guide.html)
    
    <br>

    *   Hyperopt:
            
            pip install -U hyperopt
    
    Документация по использованию [Hyperopt](https://hyperopt.github.io/hyperopt/)
    
    <br>

    *   Optuna:

            pip install -U optuna

    Документация по использованию [Optuna](https://optuna.readthedocs.io/en/stable/reference/index.html)

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.9#Оглавление)

<br>

### Этапы работы над проектом
- Ознакомление с описанием задачи;
- Знакомство с данными;
- Импортирование необходимых библиотек;
- Сравнительный анализ выборок;
- Построение обучающих моделей, поиск оптимальных параметров и их оптимизация;
- Выбор оптимальной модели на основании полученных метрик и алгоритма выбора лучших признаков;
- Проверка соответствия написанного кода стандарту PEP8;
- Оформление проекта;
- Загрузка проекта на GitHub.

<br>

### Результаты:

Проект c корректным выполнением кейса ["Практическая работа"](https://github.com/yaroslav-vorobyov/SF_DST/blob/main/PROJECT-0.9/HW-09.ipynb).

<br>

### Выводы
В процессе выполнения кейса первоначальные данные были:
* Внимательно изучены исходные данные и проанализированы;
* Проведено обучение 2 машинных моделей с оптимизацией на кросс-валидации;

**Самые лучшие метрики - сочетание модели **RandomForest** и с помощью *Optuna***

<br>

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.9#Оглавление)

<br>

### Фидбэк от ментора
<!-- * Фидбэк PROJECT-0.9.url - содержит ссылку на отзыв, файл находится на Google Drive ментора -->
* Фидбэк PROJECT-0.9.pdf - версия отзыва с полным оформлением, если по ссылке файл будет удалён
* Фидбэк PROJECT-0.9.txt - текстовая версия отзыва, если по ссылке файл будет удалён

Перейти к [отзыву](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.9/docs)

<br>

Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами.