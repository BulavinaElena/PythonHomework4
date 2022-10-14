# Задача 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def factor(n):
    ans=[]
    d=2
    while d*d<=n:
        if n%d==0:
            ans.append(d)
            n//=d
        else:
            d+=1
    if n>1:
        ans.append(n)
        print('Множители заданного числа: ')
    return ans
print(factor(int(input('Введите число: '))))

