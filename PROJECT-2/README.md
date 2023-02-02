# Проект 1. Анализ резюме из HeadHunter 
<table>
  <tr style="vertical-align:middle">
    <th><img src = 'https://i.hh.ru/logos/svg/hh.ru__min_.svg?v=11032019'></th>
    <th><img style="vertical-align:middle" img src = https://lms.skillfactory.ru/static/rg-theme/images/logo-header.svg></th>
  </tr>
</table>

## Оглавление
[1. Описание проекта](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-2#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-2#Какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-2#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-2#Этапы-работы-над-проектом)

[5. Результаты](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-2#Результаты)

  > Перейти прямо к [запросам SQL](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-2/SQL)

  > Перейти прямо к [презентации решения кейса](https://github.com/yaroslav-vorobyov/SF_DST/blob/main/PROJECT-2/Project-2.ipynb)

[6. Выводы](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-2#Выводы)  

[7. Фидбэк от ментора](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-2#Фидбэк-от-ментора)

<br>

## Описание проекта
Представьте, что вы устроились на работу в кадровое агентство, которое подбирает вакансии для IT-специалистов. 
Необходимо понять, что из себя представляют данные и насколько они соответствуют целям проекта. В литературе эта часть работы над *ML-проектом* называется *Data Understanding*, или анализ данных.

<br>

### Какой кейс решаем?
Проект — используя навыки написания запросов SQL и Postgers, создание модели машинного обучения, которая будет рекомендовать вакансии клиентам агентства, претендующим на позицию *Data Scientist*. 

<br>

**Условия:**
- Решение оформляется только в *Jupyter Notebook*.
- Решение оформляется в соответствии с *ноутбуком-шаблоном*.
- Каждое задание выполняется в отдельной ячейке, выделенной под задание (в шаблоне они помечены как **ваш код здесь**). Не следует создавать много ячеек для решения задачи — это провоцирует неудобства при проверке.
- Текст *SQL*-запросов и код на *Python* должны быть читаемыми. Не забывать про отступы в SQL-коде.
- Выводы по каждому этапу оформляются в формате *Markdown* в отдельной ячейке (в шаблоне они помечены как **ваши выводы здесь**).
- Выводы можно дополнительно проиллюстрировать с помощью графиков. Они оформляются в соответствии с теми правилами, которые мы приведены в модуле по визуализации данных.
- Не забыть удалить ячейку с данными соединения перед фиксацией работы в *GitHub*.

<br>

**Метрика качества:**
* Результаты оцениваются согласно требованиям, указанным к проекту: 
  - 2 балла, правильность решения задач, логичность построения запросов;
  - 2 балла, читабельность и верное форматирование запросов и кода на Python, наличие комментариев в запросах; аккуратность оформления решения;
  - 2 балла, логичность и полнота выводов;
  - 2 балла, дополнительные исследования данных.
* Необходимо: ответить на контрольные вопросы (максимум 6 баллов), провести дополнительные исследования данных (максимум 2 балла), сдать проект на проверку, загрузив ноутбук-шаблон со своим решением на GitHub.

**Максимальное количество баллов** за задание — 8.

<br>

**Что на практике:**
-   Учусь писать отличный код на SQL & Python;
-   Взаимодействие с внешней БД Postgres;
-   Учусь эффективно работать с IDE VSCode;
-   Учусь эффективно работать с DBeaver;
-   Учусь эффективно работать с Metabase
-   Повышаю квалификацию по методам преобразования и очистки данных; 
-   Повышаю квалификацию с GitHub.

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-2#Оглавление)

<br>

### Краткая информация о данных
В данном проекте первоначальные данные представлены в схеме ***public***, она объединяет 5 таблиц для анализа вакансий: ***vacancies*** (вакансии), ***employers*** (работодатели), ***areas*** (регионы), ***industries*** (сферы деятельности предприятий), и промежуточная дополнительная таблица ***employers_industries*** (имеет связи по ключам "многие-ко-многим" между таблицами *employers* и *industries*)., в отдельных столбцах присутствуют пропуски и дубликаты. В связи с этим необходимо более детально проанализировать структуру первоначальных данных, сделать выводы о дальнейших преобразованиях. 

<br>

#### Схема **PUBLIC**
---

Хранится в базе данных ***project_sql***:

<p align="center"><img src='./images/scheme_public.png' width='50%'></p>

---

* #### Таблица-справочник **VACANCIES**
  Хранит в себе данные по вакансиям и содержит следующие столбцы:

  <p align="center"><img src='./images/table_vacancies.png' width='50%'></p>

  > Зарплатная вилка — это верхняя и нижняя граница оплаты труда в рублях (зарплаты в других валютах уже переведены в рубли).
  >
  > Соискателям она показывает, в каком диапазоне компания готова платить сотруднику на этой должности.

---

* #### Таблица-справочник **AREAS**
  Хранит код города и его название:

  <p align="center"><img src='./images/table_areas.png' width='50%'></p>

---

* #### Таблица-справочник **EMPLOYERS**
  Хранит списк работодателей:

  <p align="center"><img src='./images/table_employers.png' width='50%'></p>

---

* #### Таблица-справочник **INDUSTRIES**
  Хранит варианты сфер деятельности работодателей:

  <p align="center"><img src='./images/table_industries.png' width='50%'></p>

---

* #### Дополнительная таблица **EMPLOYERS_INDUSTRIES**
  Cуществует для организации связи между работодателями и сферами их деятельности.

  <p align="center"><img src='./images/table_employers_industries.png' width='50%'></p>
  
  > Эта таблица нужна нам, поскольку у одного работодателя может быть несколько сфер деятельности (или работодатели могут вовсе не указать их).
  >
  > Для удобства анализа необходимо хранить запись по каждой сфере каждого работодателя в отдельной строке таблицы.

<br>

### Требования для работы
*   Основой интерпретатор - Python 3.10 (у меня взят из Windows App Store для максимальной бесшовной интеграции с VSCode);
*   Дополнительные требования перечислены в requirements.txt (получены командой pip freeze > requirements.txt);
*   Установка всех недостающих дополнительных компонент:

            pip install -r requirements.txt

*   В проекте используется модуль <font color='LightSeaGreen'>**Plotly.io**</font> для сохранения диаграмм и графиков в файл, для сохранения доступны 2 "движка", предварительно нужно установить любой, на ваш выбор, чтобы механизм экспорта на диск работал:
    * "kaleido",

          pip install kaleido

    или, как в моём проекте, я использовал

    * "orca"

          pip install orca

    Документация по использованию [Orca](https://github.com/plotly/orca) на GitHub.

    Документация по использованию [Plotly.io](https://plotly.github.io/plotly.py-docs/generated/plotly.io.write_image.html)

*   В проекте используется модуль <font color='LightSeaGreen'>**PostgreSQL Database Client**</font> для построения запросов из IDE VSCode:

            https://marketplace.visualstudio.com/items?itemName=cweijan.vscode-postgresql-client2

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-2#Оглавление)

<br>

### Этапы работы над проектом
- Ознакомление с описанием задачи;
- Знакомство с данными;
- Предварительный анализ данных;
- Детальный анализ вакансий;
- Анализ работодателей;
- Предметный анализ;
- Проверка соответствия результата выполнения кода условию, приведенному в метрике качества;
- Проверка соответствия написанного кода стандарту PEP8;
- Оформление проекта;
- Загрузка проекта на GitHub.

<br>

### Результаты:

  > [Запросы SQL](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-2/SQL)

Проект c корректным выполнением кейса ["Анализ резюме из HeadHunter (SQL)"](https://github.com/yaroslav-vorobyov/SF_DST/blob/main/PROJECT-2/Project-2.ipynb).

<br>

### Выводы
В процессе выполнения кейса первоначальные данные по методологии <font color='LightSeaGreen'>**CRISP в части Data Understanding**</font> были:
* Внимательно изучены данные вакансий HeadHunter и проанализированы;
* Проведен детальный анализ вакансий и работодателей;
* Проведен подробный предметный анализ вакансий из области Data Science;
* Проведены дополнительные исследования для лучшего понимания представленных данных; 
* Реализована визуализация дополнительных результатов для выявления взаимосвязей между признаками. 

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-2#Оглавление)

<br>

### Фидбэк от ментора
* Фидбэк PROJECT-2.url - содержит ссылку на отзыв, файл находится на Google Drive ментора
* Фидбэк PROJECT-2.pdf - версия отзыва с полным оформлением, если по ссылке файл будет удалён
* Фидбэк PROJECT-2.txt - текстовая версия отзыва, если по ссылке файл будет удалён

Перейти к [отзыву](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-2/docs)

<br>

Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами.