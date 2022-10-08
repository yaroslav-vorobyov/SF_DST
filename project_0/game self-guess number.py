#  игра на угадывание числа

from random import random
import numpy as np


number = np.random.randint(1, 101)      # загадываем число в диапазоне от 1 до 100
count = 0                               # счетчик попыток

# выполняем условие цикла пока не угадаем число
while True:
    count += 1
    predict_num = int(input('I guess number from 1 to 100, your is '))

    if predict_num > number:
        print('No, number is lower')
    
    elif predict_num < number:
        print('No, number is bigger')
    
    else:
        print(f'You won. This is {number}. You had guessed my num for {count} attempts')
    
