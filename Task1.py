# Задача 1. 1.	Вычислить число ПИ c заданной точностью *d*

import math
d=float(input('Введите шаблон для округления: '))
def digit_after_dot_counter(num: float):
    count=0
    div=1
    while True:
        if not(num*div==int(num*div)):
            count+=1
            div*=10
        else: break
    return count
print(round(math.pi, digit_after_dot_counter(d)))
