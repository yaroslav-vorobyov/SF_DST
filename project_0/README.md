# Проект 0. Угадай число

## Оглавление
[1. Описание проекта](https://github.com/yaroslav-vorobyov/SF_DST_game_guess_number/tree/main/project_0/README.md#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/yaroslav-vorobyov/SF_DST_game_guess_number/tree/main/project_0/README.md#Какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/yaroslav-vorobyov/SF_DST_game_guess_number/tree/main/project_0/README.md#Краткая-информация-о-данных)

[4. Этапы работы над проектом](https://github.com/yaroslav-vorobyov/SF_DST_game_guess_number/tree/main/project_0/README.md#Этапы-работы-над-проектом)

[5. Результат](https://github.com/yaroslav-vorobyov/SF_DST_game_guess_number/tree/main/project_0/README.md#Результат)

[6. Выводы](https://github.com/yaroslav-vorobyov/SF_DST_game_guess_number/tree/main/project_0/README.md#Выводы)


## Описание проекта
Угадать загаданное компьютером число за минимальное количество попыток.

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST_game_guess_number/tree/main/project_0/README.md#Оглавление)


### Какой кейс решаем?
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**
- Компьютер загадывает число от 0 до 100 и нам его нужно угадать. Под "угадать", подразумевается "написать программу, которая угадывает число".
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества:**
Результаты оцениваются по среднему количеству попыток при 250 повторений

**Что практикуем:**
Учусь писать хороший код на Python и ломать свои паттерны мышления от Си


### Краткая информация о данных
-   game self-guess number.py - файл проекта с угадыванием числа человек-компьютер
-   game_ai_guess_number.py - файл проекта с угадыванием числа компьютер сам с собой, включает расчет среднего числа попыток
-   game_ai_guess_number.ipynb - файл-презентация Jupyter Notebook

### Требования для работы
*   Основой интерпретатор - 
*   

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST_game_guess_number/tree/main/project_0/README.md#Оглавление)


### Этапы работы над проектом
*   Провел тесты нескольких запусков, код задокументирован, всё, по возможности, соответствует PEP8
*   np.random.seed(1) сид для воспроизводимости закомментирован для получения динамических результатов угадывания самим компьютером

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST_game_guess_number/tree/main/project_0/README.md#Оглавление)


### Результаты:
На моем железе (i7-3820QM/16Gb SO-DIMM DDR3/mSATA SSD 256Gb) комфортно отрабатывает до 1000 запусков, для проекта установил предел 250

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST_game_guess_number/tree/main/project_0/README.md#Оглавление)


### Выводы
Проект на данном этапе завершен

:arrow_up:[к оглавлению](https://github.com/yaroslav-vorobyov/SF_DST_game_guess_number/tree/main/project_0/README.md#Оглавление)