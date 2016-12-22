#task1------------------------------------------------------
"""
Дан список чисел. Определите, сколько в нем встречается различных чисел.
Примечание. Эту задачу на Питоне можно решить в одну строчку.
"""

i=set(input())
print(len(i)-1)

#-----------------------------------------------------------


#task2------------------------------------------------------
"""
Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
Примечание. Эту задачу на Питоне можно решить в одну строчку.
"""

A = input()
B = input()
A1 = A.split()
B1 = B.split()
A2 = set(A1)
B2 = set(B1)
C = A2.intersection(B2)
print(len(C))

#-----------------------------------------------------------


#task3------------------------------------------------------
"""
Даны два списка чисел. Найдите все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.
Примечание. И даже эту задачу на Питоне можно решить в одну строчку.
"""

a = set([int(i) for i in input().split()])&set([int(i) for i in input().split()])
for i in list(a):
  print(i, end=' ')
#-----------------------------------------------------------


#task4------------------------------------------------------
"""
Во входной строке записана последовательность чисел через пробел. 
Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, 
если не встречалось.
"""

a = [int(ch) for ch in input().split()]
A = set()
for elem in a:
    if elem in A:
        print("YES")
    else:
        A.add(elem)
        print("NO")
        
#-----------------------------------------------------------


#task5------------------------------------------------------
"""
Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор и в каждом наборе все кубики различны по цвету. 
Однажды дети заинтересовались, сколько существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах. 
Для этого они занумеровали все цвета случайными числами от 0 до 108. На этом их энтузиазм иссяк, 
поэтому вам предлагается помочь им в оставшейся части.
В первой строке входных данных записаны числа N и M — число кубиков у Ани и Бори. 
В следующих N строках заданы номера цветов кубиков Ани. В последних M строках номера цветов Бори.
Найдите три множества: номера цветов кубиков, которые есть в обоих наборах; 
номера цветов кубиков, которые есть только у Ани и номера цветов кубиков, которые есть только у Бори. 
Для каждого из множеств выведите сначала количество элементов в нем, а затем сами элементы, отсортированные по возрастанию.
"""

n,m=[int(i) for i in input().split()]
a=set()
b=set()
for i in range(n):
    a.add(int(input()))
for i in range(m):
    b.add(int(input()))
a_b=list(a&b)
a_b.sort()
only_a=list(a-b)
only_a.sort()
only_b=list(b-a)
only_b.sort()
print(len(a&b))
print(' '.join([str(i) for i in (a_b)]))
print(len(a-b))
print(' '.join([str(i) for i in (only_a)]))
print(len(b-a))
print(' '.join([str(i) for i in (only_b)]))

#-----------------------------------------------------------


#task6------------------------------------------------------
"""
Дан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько различных слов содержится в этом тексте.
Словом считается последовательность непробельных символов идущих подряд, 
слова разделены одним или большим числом пробелов или символами конца строки.
"""

N = int(input())
s = set()
for i in range(N):
    a = [str(i) for i in input().split()]
    for j in a:
        s.add(j)
print (len(s))

#-----------------------------------------------------------

#task7------------------------------------------------------
"""
Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n. 
Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел. 
Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное или NO в противном случае. 
После нескольких заданныъх вопросов Беатриса запуталась в том, какие вопросы она задавала и какие ответы получила 
и просит вас помочь ей определить, какие числа мог задумать Август.
В первой строке задано n - максимальное число, которое мог загадать Август. 
Далее каждая строка содержит вопрос Беатрисы (множество чисел, разделенных пробелом) и ответ Августа на этот вопрос.
Вы должны вывести через пробел, в порядке возрастания, все числа, которые мог задумать Август.
"""


#-----------------------------------------------------------


#task8------------------------------------------------------
"""
Август и Беатриса продолжают играть в игру, но Август начал жульничать.
На каждый из вопросов Беатрисы он выбирает такой вариант ответа YES или NO, 
чтобы множество возможных задуманных чисел оставалось как можно больше. 
Например, если Август задумал число от 1 до 5, а Беатриса спросила про числа 1 и 2, то Август ответит NO, 
а если Беатриса спросит про 1, 2, 3, то Август ответит YES.
Если же Бетриса в своем вопросе перечисляет ровно половину из задуманных чисел, 
то Август из вредности всегда отвечает NO. Наконец, Август при ответе учитывает все предыдущие вопросы Беатрисы и свои ответы на них,
то есть множество возможных задуманных чисел уменьшается.
Первая строка содержит наибольшее число, которое мог загадать Август. 
Каждая следующая строка содержит очередной вопрос Беатрисы: набор чисел, разделенных пробелами. 
Последняя строка входных данных содержит одно слово HELP.
Для каждого вопроса Беатрисы выведите ответ Августа на этот вопрос. 
После этого выведите через пробел, в порядке возрастания, все числа, которые мог загадать Август после ответа на все вопросы Беатрисы.
"""

n=int(input())
arr = set([I for I in range(1, n+1)])
tmp=input()
while True:
    if tmp=="HELP":
        break
    else:
        tmp=set([int(i) for i in tmp.split()])
        if len(arr-tmp) >= len(arr&tmp):
            print("NO")
            arr-=tmp
        else:
            print("YES")
            arr&=tmp
    tmp=input()    
print(" ".join(str(i) for i in sorted(arr)))

#-----------------------------------------------------------


#task9------------------------------------------------------
"""
Каждый из некоторого множества школьников некоторой школы знает некоторое количество языков. 
Нужно определить сколько языков знают все школьники, и сколько языков знает хотя бы один из школьников.
В первой строке задано количество школьников. 
Для каждого из школьников сперва записано количество языков, которое он знает, а затем - названия языков, по одному в строке.
В первой строке выведите количество языков, которые знаю все школьники. Начиная со второй строки - список таких языков. 
Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков. 
Языки нужно выводить в лексикографическом порядке, по одному на строке.
"""


#-----------------------------------------------------------


#task10------------------------------------------------------
"""
Политическая жизнь одной страны очень оживленная. 
В стране действует K политических партий, каждая из которых регулярно объявляет национальную забастовку. 
Дни, когда хотя бы одна из партий объявляет забастовку, при условии, что это не суббота или воскресенье (когда и так никто не работает),
наносят большой ущерб экономике страны.
i-я партия объявляет забастовки строго каждые b_i дней, начиная с дня с номером a_i. 
То есть i-я партия объявляет забастовки в дни a_i, a_i + b_i, a_i + 2 * b_i и т.д. 
Если в какой-то день несколько партий объявляет забастовку, то это считается одной общенациональной забастовкой.
В календаре страны N дней, пронумерованных, начиная с единицы. 
Первый день года является понедельником, шестой и седьмой дни года — выходные, неделя состоит из семи дней.
В первой строке даны числа N и K. Далее идет K строк, описывающие графики проведения забастовок. 
i-я строка содержит числа a_i и b_i. Вам нужно определить число забастовок, произошедших в этой стране в течении года.
"""


#-----------------------------------------------------------
