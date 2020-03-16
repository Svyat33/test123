# Напишите сюда домашку.
"""
Task 6.4 with star.

"""

import random

lower_bound = int(input('Нижний предел промежутка: '))
upper_bound = int(input('Верхний предел промежутка: '))
number_to_guess = int(input('Введите число, которое должно быть угадано компьютером: '))
values_list = list(range(lower_bound, upper_bound+1))

number_of_attempts = int(input('Введите количество попыток: '))

i = 1
while i <= number_of_attempts:
    i += 1
    random.shuffle(values_list)
    computer_guess = values_list.pop()
    print("Computer guess is: ", computer_guess)

    if computer_guess == number_to_guess:
        print('Computer won!')
else:
    print('Computer lost!')
#еще строка
