# Задача 4. 4.	Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов
# (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0
#  просто пропускаем данную итерацию степени.

import random
def createDict():
    equation={}
    degree=int(input('Введите максимальную степень многочлена: '))
    for i in range (degree, -1, -1):
        equation[i]=random.randint(-10, 10)
    return equation
def createEquation(equation: dict):
    strEquation=''
    first=True
    for k,v in equation.items():
        if first:
            first=False
            if v>0:
                strEquation+=f'{v}*x^'
            elif v<0:
                strEquation+=f'-{abs(v)}*x^{k}'
        else:
            if v>0:
                strEquation+=f'+{v}*x^{k}'
            elif v<0:
                strEquation+=f'-{abs(v)}*x^{k}'
        return strEquation
def printEquation(equation: str):
    print(equation.replace('*x^1', 'x').replace('*x^0', '') + ' = 0 ')
print(createEquation(createDict()))
