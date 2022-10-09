#  игра на угадывание числа человеком у копьютера

from random import random
import numpy as np


number = np.random.randint(1, 101)      # компьютер загадывает число в диапазоне от 1 до 100
count = 0                               # счетчик попыток

# угадываем число в цикле, итерируем пока не угадаем число
while True:
    count += 1                          # увеличиваем номер очередной попытки на 1
    # приглашение для человека, попытка угадать число
    predict_num = int(input('I guess number from 1 to 100, your is '))

    # если загаданное число больше предполагаемого, предлагаем ввести число поменьше
    if predict_num > number:
        print('No, number is lower')
    # если загаданное число меньше предполагаемого, предлагаем ввести число побольше
    elif predict_num < number:
        print('No, number is bigger')
    # если угадали загаданное число, то выходим из цикла и поздравляем с угадыванием
    else:
        print(f'You won. This is {number}. You had guessed my num for {count} attempts')
    
