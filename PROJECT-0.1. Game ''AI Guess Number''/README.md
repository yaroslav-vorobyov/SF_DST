# Проект 0. Угадай число
<img style="vertical-align:middle" img src = https://lms.skillfactory.ru/static/rg-theme/images/logo-header.svg>

## Оглавление
[1. Описание проекта](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.1.%20Game%20''AI%20Guess%20Number''#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.1.%20Game%20''AI%20Guess%20Number''#Какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.1.%20Game%20''AI%20Guess%20Number''#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.1.%20Game%20''AI%20Guess%20Number''#Этапы-работы-над-проектом)

[5. Результаты](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.1.%20Game%20''AI%20Guess%20Number''#Результаты)

  >Перейти прямо к [презентации решения кейса](https://github.com/yaroslav-vorobyov/SF_DST/blob/main/PROJECT-0.1.%20Game%20''AI%20Guess%20Number''/game_ai_guess_number.ipynb)

[6. Выводы](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.1.%20Game%20''AI%20Guess%20Number''#Выводы)  

[7. Фидбэк от ментора](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.1.%20Game%20''AI%20Guess%20Number''#Фидбэк-от-ментора)

<br>

## Описание проекта
Найти и реализовать алгоритм самого быстрого перебора чисел и угадать загаданное компьютером число за минимальное количество попыток.

<br>

### Какой кейс решаем?
Нужно написать программу, которая угадывает число, загаданное ей же самой, за минимальное число попыток.

<br>

**Алгоритм работы:**
- Компьютер загадывает число от 0 до 100. Есть 2 варианта кода:
    - где предполагается нам его угадать у компьютера (game guess number.py);
    - где компьютер отгадывает сам у себя загаданное им же число (game_ai_guess_number.py);
- Под "отгадывает", подразумевается написать "программу, которая реализует алгоритм угадывания числа".
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

<br>

**Метрика качества:**
Результаты оцениваются по среднему количеству попыток при 1000 повторений.

<br>

**Что на практике:**
- Учусь писать отличный код на Python;
- Учусь эффективно работать с IDE VSCode;
- Повышаю квалификацию с GitHub.

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.1.%20Game%20''AI%20Guess%20Number''#Оглавление)

<br>

### Краткая информация о данных
-   game guess number.py - файл проекта с угадыванием числа человеком, компьютер загадывает число;
-   game_ai_guess_number.py - файл проекта с угадыванием числа компьютером самим собой, загадывает число и пытается его подобрать методом половинного деления, включает модуль расчета среднего числа удачных попыток отгадывания;
-   game_ai_guess_number.ipynb - файл-презентация Jupyter Notebook, взаимодействует с файлом game_ai_guess_number.py.

<br>

### Требования для работы
*   Основой интерпретатор - Python 3.10 (у меня взят из Windows App Store для максимальной бесшовной интеграции с VSCode);
*   Дополнительные требования перечислены в requirements.txt (получены командой pip freeze > requirements.txt);
*   Установка недостающих дополнительных компонент:

        pip install -r requirements.txt

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.1.%20Game%20''AI%20Guess%20Number''#Оглавление)

<br>

### Этапы работы над проектом
*   Провел тесты нескольких запусков, код задокументирован, всё, по возможности, соответствует PEP8;
*   np.random.seed(1) сид для воспроизводимости закомментирован для получения динамических результатов угадывания самим компьютером.

<br>

### Результаты:
На моем железе (i7-3820QM/16Gb SO-DIMM DDR3/mSATA SSD 256Gb) комфортно отрабатывает до 10000 запусков, для более быстрого завершения расчета можно установить предел в 250 запусков.

Проект c корректным выполнением кейса [представлен в репозитории на GitHub](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.1.%20Game%20''AI%20Guess%20Number''/game_ai_guess_number.ipynb)

<br>

### Выводы
Код полностью рабочий, достигнуто минимальное число попыток угадывания числа компьютером.

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.1.%20Game%20''AI%20Guess%20Number''#Оглавление)

<br>

### Фидбэк от ментора
* Фидбэк Python-8, юнит 8.pdf - версия отзыва с полным оформлением
* Фидбэк Python-8, юнит 8.txt - текстовая версия отзыва

Перейти к [отзыву](https://github.com/yaroslav-vorobyov/SF_DST/tree/main/PROJECT-0.1.%20Game%20''AI%20Guess%20Number''/docs)

Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами.