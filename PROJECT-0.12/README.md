# Проект 0.12. Домашнее задание. Модуль: MATH_ML-7. Наивный байесовский классификатор
<table>
  <tr style="vertical-align:middle">
    <!-- <th><img src = 'https://i.hh.ru/logos/svg/hh.ru__min_.svg?v=11032019'></th> -->
    <!-- <th><img style="vertical-align:middle" img src = https://lms.skillfactory.ru/static/rg-theme/images/logo-header.svg></th> -->
    <!-- <th><img style="vertical-align:middle" img src = https://static.tildacdn.com/tild3862-3932-4061-b763-363135393134/logo.svg></th> -->
    <th height=30><img style="vertical-align:middle" img src = https://static.tildacdn.com/tild3736-6663-4331-b065-623334663336/SkillFactory.svg height=20></th>
  </tr>
</table>

## Оглавление
[1. Описание проекта](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.12#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.12#Какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.12#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.12#Этапы-работы-над-проектом)

[5. Результаты](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.12#Результаты)

  > Перейти прямо к [презентации решения кейса](https://github.com/yaroslav-vorobyov/SF_DST/blob/main/PROJECT-0.12/HW-12.ipynb)

[6. Выводы](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.12#Выводы)  

[7. Фидбэк от ментора](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.12#Фидбэк-от-ментора)

<br>

## Описание проекта
Можно полностью самостоятельно, «с нуля» реализовать байесовский классификатор с довольно высокой точностью. Разумеется, при решении реальных задач не будем каждый раз самостоятельно прописывать алгоритм  — можно использовать готовые методы. В библиотеке ***sklearn*** есть несколько байесовских классификаторов:

* **[GaussianNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html)** — самый простой вариант, работает с непрерывными признаками;

* **[MultinomialNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html)**  — работает с категориальными признаками, текстами и несбалансированными выборками;

* **[ComplementNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html)** — улучшенная версия MultinomialNB, стабильно показывает более высокое качество в задачах классификации текстов;

* **[BernoulliNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html)** — версия для работы с бинарными признаками;

* **[CategoricalNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.CategoricalNB.html#sklearn.naive_bayes.CategoricalNB)** — работает с категориальными признаками, предполагает кодировку данных через **OrdinalEncoder**.

Набор данных - ***spam_or_not_spam.csv***, набор данных с *e-mail*-сообщениями.

<br>

### Какой кейс решаем?
Задача - реализовать классификацию спам-сообщений уже с использованием готовых функций.

<br>

**Условия:**
- Решение оформляется только в *Jupyter Notebook*.
- Решение оформляется в соответствии с *ноутбуком-шаблоном*.
- Не следует создавать много ячеек для решения задачи — это проявляет неудобства при проверке.
- Код на *Python* должен быть читаемым и понятным: имена переменных и функций отражают их сущность. Не забывать про отступы, разметку и комментарии в коде.
- Выводы по каждому этапу оформляются в формате *Markdown* в отдельной ячейке.

<br>

**Метрика качества:**
* В ноутбуке должны быть ответы на следующие вопросы:
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

| **Количество баллов** | **Задание** |
| --- | --- |
| **1 балл** | Задание 1 |
| **2 балла** | Задание 2 |
| **2 балла** | Задание 3 |
| **3 балла** | Задание 4 |
| **3 балла** | Задание 5 |

* Необходимо: ответить на контрольные вопросы, сдать проект на проверку, загрузив ноутбук-шаблон со своим решением на GitHub.

**Максимальное количество баллов** - 11.

<br>

**Что на практике:**
-   Учусь писать отличный код на Python;
-   Учусь сравнивать модели с точки зрения метрик, параметров;
-   Учусь следить за оптимизацией метрик модели;
-   Учусь следить за оптимизацией модели;
-   Учусь эффективно работать с IDE VSCode;
-   Повышаю квалификацию по методам преобразования и очистки данных; 
-   Повышаю квалификацию с GitHub.

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.12#Оглавление)

<br>

### Краткая информация о данных

В данном проекте первоначальные данные представлены в виде датасета размером: 3000 строк, 2 столбца, типа int64 и object, в столбцах присутствуют пропуски и дубликаты. В связи с этим необходимо более детально проанализировать структуру первоначальных данных, сделать выводы о дальнейших преобразованиях.

* ***spam_or_not_spam.csv*** - первоначальные данные.

Необходимо: 

* Загрузить данные и определить целевую переменную и предикторы;

* Удалить пропуски в данных;

* Реализовать обучение модели наивного байесовского классификатора;

* Оценить качество модели с помощтю кривой ROC-AUC;

* Оценить качество обеих полученной модели с помощью метрики F1.

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


:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.12#Оглавление)

<br>

### Этапы работы над проектом
- Ознакомление с описанием задачи;
- Знакомство с данными;
- Импортирование необходимых библиотек;
- Обработка данных;
- Написание обработчиков и функций в соответствии с ТЗ;
- Проверка соответствия написанного кода стандарту PEP8;
- Оформление проекта;
- Загрузка проекта на GitHub.

<br>

### Результаты:

Проект c корректным выполнением кейса ["Практическая работа"](https://github.com/yaroslav-vorobyov/SF_DST/blob/main/PROJECT-0.12/HW-12.ipynb).

<br>

### Выводы
В процессе выполнения кейса первоначальные данные были:
* Внимательно изучены исходные данные и проанализированы;
* Проведена подготовка данных к использованию: удаление пропусков;
* Выполнена визуализация обученной модели наивного байесовского классификатора с помощью кривой ROC;
* Реализована функция поиска оптимального гиперпараметра для наивного байесовского классификатора;

Подобранное лучшее значение параметра $\alpha = 0.35$ может ещё немного улучшить метрику $F_1$ после 2 знака и, соответственно - качество модели.

<br>

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.12#Оглавление)

<br>

### Фидбэк от ментора
<!-- * Фидбэк PROJECT-0.12.url - содержит ссылку на отзыв, файл находится на Google Drive ментора -->
* Фидбэк PROJECT-0.12.pdf - версия отзыва с полным оформлением, если по ссылке файл будет удалён
* Фидбэк PROJECT-0.12.txt - текстовая версия отзыва, если по ссылке файл будет удалён

Перейти к [отзыву](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.12/docs)

<br>

Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами.