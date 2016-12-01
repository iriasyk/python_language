#task1--------------------------------------------------------------------
'''
Даны четыре действительных числа: x1, y1, x2, y2. 
Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). 
Считайте четыре действительных числа и выведите результат работы этой функции. 
'''

from math import sqrt
def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
print(distance(x1,y1,x2,y2))

#--------------------------------------------------------------------------


#task2---------------------------------------------------------------------
'''
Дано действительное положительное число a и целоe число n.
Вычислите a^n. Решение оформите в виде функции power(a, n). 
'''

def power(a, n):
    res=1
    if n>0:
        for i in range(n):
            res*=a
    elif n<0:
        for i in range(-1*n):
            res/=a
    return res
print(power(float(input()), int(input())))

#--------------------------------------------------------------------------


#task3---------------------------------------------------------------------
'''
Дано действительное положительное число a и целое неотрицательное число n.
Вычислите an не используя циклы, возведение в степень через ** и функцию math.pow(), а используя рекуррентное соотношение a^n=a*a^(n-1).
Решение оформите в виде функции power(a, n). 
'''

def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

print(power(float(input()), int(input())))

#--------------------------------------------------------------------------


#task4----------------------------------------------------------------------
'''
Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи. 
В этой задаче нельзя использовать циклы — используйте рекурсию. 
'''

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
n = int(input())
print(fib(n))

#--------------------------------------------------------------------------