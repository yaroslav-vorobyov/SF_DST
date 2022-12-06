# Проект 1. Анализ резюме из HeadHunter 
<table>
  <tr style="vertical-align:middle">
    <th><img src = 'https://i.hh.ru/logos/svg/hh.ru__min_.svg?v=11032019'></th>
    <th><img style="vertical-align:middle" img src = https://lms.skillfactory.ru/static/rg-theme/images/logo-header.svg></th>
  </tr>
</table>



## Оглавление
[1. Описание проекта](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-1.%20Resume%20analysis%20from%20HeadHunter/README.md#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-1.%20Resume%20analysis%20from%20HeadHunter/README.md#Какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-1.%20Resume%20analysis%20from%20HeadHunter/README.md#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-1.%20Resume%20analysis%20from%20HeadHunter#Этапы-работы-над-проектом)

[5. Результат](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-1.%20Resume%20analysis%20from%20HeadHunter/README.md#Результат)

  >Перейти прямо к [презентации решения кейса](https://github.com/yaroslav-vorobyov/SF_DST/blob/main/PROJECT-1.%20Resume%20analysis%20from%20HeadHunter/Project-1.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D0%91%D0%94%20%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5%20c%20HH.ipynb)

[6. Выводы](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-1.%20Resume%20analysis%20from%20HeadHunter/README.md#Выводы)  

  <br/>

## Описание проекта
На основе базы резюме, выгруженной с сайта поиска вакансий HH.ru, необходимо подготовить первичные данные для построения модели, которая бы автоматически определяла примерный уровень заработной платы, подходящей пользователю, исходя из информации, которую он указал о себе. 

  <br/>

### Какой кейс решаем?
Нужно предварительно подготовить имеющиеся данные путем их изучения, преобразования с возможностью дальнейшего исследования и проведения очистки, что позволит в дальнейшем построить математическую прогнозную модель.

  <br/>

**Условия:**
- Каждая часть проекта представляет собой блок практических заданий, которые небходимо выполнить в шаблоне jupyter-ноутбука от SkillFactory;
- При выполнении проекта также необходимо ответить на контрольные вопросы на платформе;
- Каждое задание выполняется в отдельной ячейке, выделенной под задание, код для каждого задания оформляется в одной-двух jupyter-ячейках;
- Код должен быть читаемым и понятным: имена переменных и функций должны отражать их сущность, важно избегать многострочных конструкций и условий;
- Графики оформляются в соответствии с теми правилами, которые изучались в модуле по визуализации данных. Обязательное требование: графики должны содержать название, отражающее их суть, и подписи осей;
- Выводы к графикам оформляются в формате Markdown под самим графиком в отдельной ячейке.

  <br/>

**Метрика качества:**
* Результаты оцениваются согласно требованиям, указанным к проекту. 
* Необходимо: ответить на контрольные вопросы (максимум 30 баллов), сдать проект на проверку, загрузив ноутбук-шаблон со своим решением на GitHub (максимум 10 баллов).

  <br/>

**Что на практике:**
-   Учусь писать отличный код на Python;
-   Учусь эффективно работать с IDE VSCode;
-   Повышаю квалификацию по методам преобразования и очистки данных; 
-   Повышаю квалификацию с GitHub.

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-1.%20Resume%20analysis%20from%20HeadHunter/README.md#Оглавление)

  <br/>

### Краткая информация о данных
В данном проекте первоначальные данные представлены в виде датасета размером: 44744 строки, 12 столбцов, типа object, в отдельных столбцах присутствуют пропуски и дубликаты. В связи с этим необходимо более детально проанализировать структуру первоначальных данных, сделать выводы о дальнейших преобразованиях. 

-  dst-3.0_16_1_hh_database.csv - база резюме, выгруженная с сайта поиска вакансий hh.ru, предварительно подготовленная SkillFactory;
-  ExchangeRates.csv - курсы валют, предосталенные SkillFactory.

  <br/>

### Требования для работы
*   Основой интерпретатор - Python 3.10 (у меня взят из Windows App Store для максимальной бесшовной интеграции с VSCode);
*   Дополнительные требования перечислены в requirements.txt (получены командой pip freeze > requirements.txt);
*   Установка всех недостающих дополнительных компонент:

            pip install -r requirements.txt

*   В проекте используется модуль Plotly.io для сохранения диаграмм и графиков в файл, для сохранения доступны 2 "движка", их предварительно нужно установить:
    * "kaleido",

          pip install kaleido

    или, как в моём проекте

    * "orca"

          pip install orca

    Решение возникающих проблем описаны на GitHub проекта ["Orca"](https://github.com/plotly/orca)

    Документация по использованию [Plotly.io](https://plotly.github.io/plotly.py-docs/generated/plotly.io.write_image.html)

*   Для выгрузки исходного датасета, применил надстройку GitHub - [Git LFS](https://git-lfs.github.com/). 

    Документация по использованию Git LFS - [Docs Git LFS](https://github.com/git-lfs/git-lfs/tree/main/docs)

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-1.%20Resume%20analysis%20from%20HeadHunter/README.md#Оглавление)

  <br/>

### Этапы работы над проектом
* Ознакомление с описанием задачи
* Базовый анализ исходных данных
* Преобразование данных
* Разведывательный анализ
* Очистка данных
* Проверка соответствия результата выполнения кода условию, приведенному в метрике качества
* Проверка соответствия написанного кода стандарту PEP8
* Оформление проекта
* Загрузка проекта на GitHub 

  <br/>


### Результаты:
Проект c корректным выполнением кейса "Анализ резюме из HeadHunter" [представлен в репозитории на GitHub](https://github.com/yaroslav-vorobyov/SF_DST/blob/main/PROJECT-1.%20Resume%20analysis%20from%20HeadHunter/Project-1.%20%D0%90%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%20%D0%91%D0%94%20%D1%80%D0%B5%D0%B7%D1%8E%D0%BC%D0%B5%20c%20HH.ipynb)

  <br/>

### Выводы
В процессе выполнения кейса первоначальные данные были:
* Проанализированы, 
* Преобразованы в соответствии с поставленным ТЗ, 
* Проведен разведывательный анализ данных с последующей визуализацией результатов с целью выявления взаимосвязей между признаками, 
* Данные были очищены от пропусков и дубликатов. 

Таким образом, первоначальный датасет подготовлен для дальнейшего использования при построении требуемой модели.
Также, после преобразования исходного датасета получен выигрыш занимаемого места новыми данными - новые данные занимают места в 32 раза меньше&#10071; &#129351;&#127942;

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-1.%20Resume%20analysis%20from%20HeadHunter/README.md#Оглавление)

  <br/>


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами.