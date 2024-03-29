# Проект 6. Задача кластеризации
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
[1. Описание проекта](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-6#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-6#Какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-6#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-6#Этапы-работы-над-проектом)

[5. Результаты](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-6#Результаты)

  > Перейти прямо к [презентации решения кейса](https://github.com/yaroslav-vorobyov/SF_DST/blob/main/PROJECT-6/project/Project-6.ipynb)

[6. Выводы](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-6#Выводы)  

[7. Фидбэк от ментора](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-6#Фидбэк-от-ментора)

<br>

<center> <img src=https://salesupnow.ru/storage/app/media/pipeople.png align="right" width="300"/> </center>

## Описание проекта

Маркетинг — неотъемлемая часть любого бизнеса. Для повышения прибыли компании важно понимать своего клиента, его пожелания и предпочтения. С появлением **[электронной коммерции](https://trends.rbc.ru/trends/industry/607fe4549a7947027eaffbe6)**, или онлайн-продаж, стало намного проще собирать данные о клиентах, анализировать их, находить закономерности и реализовывать маркетинговые кампании.

Большинство интернет-магазинов используют инструменты веб-аналитики, чтобы отслеживать просмотры страниц, количество и поведение посетителей и коэффициент отказов. Но отчёта из *Google Analytics* или аналогичной системы может быть недостаточно для полного понимания того, как клиенты взаимодействуют с сайтом. Компаниям важно иметь возможность быстро и точно реагировать на перемены в поведении клиентов, создавая инструменты, которые обнаруживают эти изменения практически в режиме реального времени.

Машинное обучение помогает поисковой системе анализировать огромное количество данных о посетителях платформы, узнавать **[модели поведения профессиональных покупателей](http://b2bmotion.ru/b2b-pokupatel)**, определять категорию клиентов (например, лояльные/перспективные/новички/«спящие»/ушедшие) и выбирать правильную стратегию взаимодействия с ними.

Стоит также отметить, что компании, использующие машинное обучение на своих платформах электронной коммерции, могут постоянно повышать эффективность бизнес-процессов: настраивать товарную выборку персонально для каждого покупателя и предлагать выгодную цену в соответствии с бюджетом клиента и т. д. Эта задача относится к категории построения рекомендательных систем.

> Как правило, наборы данных для электронной коммерции являются частной собственностью и, следовательно, их трудно найти среди общедоступных данных.
> 
> В **[The UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/index.php)** создали набор данных, содержащий фактические транзакции за 2010 и 2011 годы. С ним как раз и предстоит поработать в этом проекте.

Датасет содержит все транзакции, произошедшие за период с 01/12/2010 по 09/12/2011, для базирующейся в Великобритании компании, занимающейся розничной онлайн-торговлей. Компания в основном продаёт уникальные подарки на все случаи жизни. Многие клиенты являются оптовиками.

<br>

### Какой кейс решаем?

**Бизнес-задача:** произвести сегментацию существующих клиентов, проинтерпретировать эти сегменты и определить стратегию взаимодействия с ними.

**Техническая задача как для специалиста в Data Science:** построить модель кластеризации клиентов на основе их покупательской способности, частоты заказов и срока давности последней покупки, определить профиль каждого из кластеров.

<br>

### Задачи проекта:

1. Произвести предобработку набора данных.

2. Провести разведывательный анализ данных и выявить основные закономерности.

3. Сформировать категории товаров и клиентов.

4. Построить несколько моделей машинного обучения, решающих задачу кластеризации клиентов, определить количество кластеров и проинтерпретировать их.

5. Спроектировать процесс предсказания категории интересов клиента и протестировать вашу модель на новых клиентах.

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-6#Оглавление)

<br>

**Условия:**
- Решение оформляется только в *Jupyter Notebook*.
- Решение оформляется в соответствии с *ноутбуком-шаблоном*.
- Не следует создавать много ячеек для решения задачи — это проявляет неудобства при проверке.
- Код на *Python* должен быть читаемым и понятным: имена переменных и функций отражают их сущность. Не забывать про отступы, разметку и комментарии в коде.
- Вывод оформляется в формате *Markdown* в отдельной ячейке.

<br>

За каждое задание можно получить **от 1 до 7 баллов**.
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

**Максимальное количество баллов** за проект — 67.

<br>

**Что на практике:**
-   Учусь писать отличный код на Python;
-   Учусь строить оптимальные модели "декомпозиция методом главных компонент" PCA, "мягкой" EM-кластеризации GaussianMixture, "жёсткой" Kmeans-кластеризации Kmeans, агломеративной кластеризации AgglomerativeClustering, поиск оптимальных гиперпараметров для "дерева решений" GridSearchCV, ансамблирование - "случайный лес" RandomForestClassifier, градиентный бустинг над деревьями решений GradientBoostingClassifier, а также конвейерная обработка Pipeline;
-   Учусь сравнивать модели с точки зрения метрик, параметров;
-   Учусь следить за оптимизацией метрик модели;
-   Учусь следить за оптимизацией модели;
-   Учусь эффективно работать с IDE VSCode;
-   Повышаю квалификацию по методам преобразования и очистки данных; 
-   Повышаю квалификацию с GitHub.

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-6#Оглавление)

<br>

### Краткая информация о данных

В данном проекте первоначальные данные представлены в виде совокупного датасета размером: свыше 540 тыс. строк, 8 столбцов, типа object, float64 и int64, в отдельных столбцах присутствуют пропуски и дубликаты. По итогам обработки будут отобраны 3 признака с помощью методов уменьшения размерности, наилучшим образом подходящих для предсказания целевой переменной. В связи с этим необходимо более детально проанализировать структуру первоначальных данных, сделать выводы о дальнейших преобразованиях. Построить обучающие модели, которые должны произвести сегментацию существующих клиентов, выбрать лучшую из них.

**Датасеты**:

* ***customer_segmentation_project.csv*** содержит датасет тренировочных + валидационных данных со следующей информацией:



  * *InvoiceNo* — номер счёта-фактуры (уникальный номинальный шестизначный номер, присваиваемый каждой транзакции; буква "*C*" в начале кода указывает на отмену транзакции);
  * *Stock Code* — код товара (уникальное пятизначное целое число, присваиваемое каждому отдельному товару);
  * *Description* — название товара;
  * *Quantity* — количество каждого товара за транзакцию; 
  * *InvoiceDate* — дата и время выставления счёта/проведения транзакции;
  * *UnitPrice* — цена за единицу товара в фунтах стерлингов;
  * *CustomerID* — идентификатор клиента (уникальный пятизначный номер, однозначно присваиваемый каждому клиенту);
  * *Country* — название страны, в которой проживает клиент.

<br>

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-6#Оглавление)

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

    *   gdown:

            pip install -U gdown

    Документация по использованию - [gdown](https://github.com/wkentaro/gdown)

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-6#Оглавление)

<br>

### Этапы работы над проектом
- Ознакомление с описанием задачи;
- Знакомство с данными;
- Импортирование необходимых библиотек;
- Изучение датасета на предмет наличия пропусков и типов данных;
- Обработка данных: извлечение данных из выборки, создание новых признаков;
- Очистка и отбор признаков: преобразование и удаление признаков, на которых модель обучаться не будет, отбор признаков;
- Разделение данных для модели: выделение тестовой части, разделение тренингового датасета: 80% всех данных - на обучение, 20% данных - на валидацию, проверка размерности разделённых датасетов;
- Построение и обучение моделей;
- Сравнение и оценка целевых метрик на тестовом датасете;
- Проверка соответствия написанного кода стандарту PEP8;
- Оформление проекта.

<br>

### Результаты:

Проект c корректным выполнением кейса ["Задача кластеризации"](https://github.com/yaroslav-vorobyov/SF_DST/blob/main/PROJECT-6/project/Project-6.ipynb).

<br>

### Выводы
В процессе выполнения кейса первоначальные данные были:
* Внимательно изучены исходные данные и проанализированы;
* Проведена подготовка данных к использованию: очистка, преобразование, исключение, создание признаков;
* Данные были исследованы на длительности поездок, выявлены зависимости, построены графики отражающие зависимости, сформированы выводы по данным;
* Построены обучающие модели, основанные на алгоритмах машинного обучения, выбраны несколько из них по максимальной целевой метрике *Accuracy*;

Для решения задачи кластеризации в данном кейсе **отлично себя показали модели**:

* <font color=LightSeaGreen>**&check;**</font> **случайный леc RandomForestClassifier**
* <font color=LightSeaGreen>**&check;**</font> **Градиентный бустинг над деревьями решений GradientBoostingClassifier**

<br>

| Обученная модель | Accuracy<br> на тестовой выборке |
| :---: | :---: |
| **RandomForestClassifier** | <font color=LightSeaGreen>**0.985**</font> |
| **GradientBoostingClassifier** | <font color=LightSeaGreen>**0.990**</font> |

<br>

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-6#Оглавление)

<br>

### Фидбэк от ментора
<!-- * Фидбэк PROJECT-6.url - содержит ссылку на отзыв, файл находится на Google Drive ментора -->
* Фидбэк PROJECT-6.pdf - версия отзыва с полным оформлением, если по ссылке файл будет удалён
* Фидбэк PROJECT-6.txt - текстовая версия отзыва, если по ссылке файл будет удалён

Перейти к [отзыву](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-6/docs)

<br>

Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами.