#  игра на угадывание числа

from random import random
import numpy as np


# number = round(random() * 100)
number = np.random.randint(1, 101)
count = 0       # счетчик попыток

while True:
    count += 1
    predict_num = int(input('Guess number from 1 to 100. You enter '))

    if predict_num > number:
        print('Number is lower')
    
    elif predict_num < number:
        print('Number is bugger')
    
    else:
        print(f'You won. This is {number}. You guess for {count} attempts')
    
