#  игра на угадывание числа компьютером

from random import random
import numpy as np




def random_predict(number:int=1) -> int:
    """Компьютер угадывает число методом половинного деления.
    Функция всегда угадывает число в диапазоне от 1 до 100 за число попыток не больше 8 
    (только при загаданном числе 100, и не более 7 попыток в других случаях)
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    
    Returns:
        int: Число попыток
    """
    
    count = 0                           # счетчик попыток угадывания
    max = 100                           # верхняя граница предполагаемого числа
    min = 1                             # нижняя граница предполагаемого числа
    number = np.random.randint(min, max + 1) # компьютер загадывает случайное число от 1 до 100

    # угадываем число в цикле, итерируем пока не будет совпадения загаданного предполагаемому
    while True:                         
        count += 1                      # увеличиваем номер очередной попытки на 1
        
        # mid - предполагаемое число        
        if number == 1:
            # если загаданное число равно 1, то среднee от min и max вычисляем с поправкой
            mid = round((max + min) / 2) - 1
        else:
            # если условие ложно, то среднee от min и max вычисляем как обычно
            mid = round((max + min) / 2)
        
        # вывод промежуточных результатов, можно ниже в каждую ветку if-elif-else добавить, 
        # чтобы видеть какие переменные на каждой итерации ветвления
        # этот 1 print здесь или 3 print в if-elif-else ниже
        print('загаданное число={0} mid={1} min={2} max={3}'.format(number, mid, min, max))
        
        # если угадали загаданное число, то выходим из цикла
        if number == mid:
            break
        # если загаданное число больше предполагаемого, 
        # сдвигаем нижнюю границу на место предполагаемого числа
        elif number > mid:
            min = mid
        # иначе, сдвигаем верхнюю границу на место предполагаемого числа
        else:                           
            max = mid                   
    return count                        # возвращаем число попыток отгадывания

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """

    count_ls = []                                         # список для сохранения количества попыток
    # np.random.seed(1)                                   # фиксируем сид для воспроизводимости
    # задаем список чисел от 1 до 100 размерностью 1000 элементов (попыток)
    random_array = np.random.randint(1, 101, size=(1000))
    # в цикле наполняем список элементами - числом попыток угадывания числа
    for number in random_array:
        count_ls.append(random_predict(number))
    
    # находим среднее количество попыток от всех элементов списка
    score = int(np.mean(count_ls))
    # выводим метрику качества
    print(f'Алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# не запускать вызов функции из jupiter notebook
if __name__ == '__main__':
    print(f'Количество попыток: {random_predict()}')
    score_game(random_predict)