'''
Напишите программу, которая получает на вход три целых числа, по одному числу в строке,
и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
'''
a = int(input())
b = int(input())
c = int(input())
max = (abs(2*c-abs(b-a)-b-a)+2*c+abs(b-a)+b+a)/4
min = (((max - abs(a-b))+(max - abs(b-c))+(max - abs(a-c))) - max)/2
mid = (a+b+c)-(max+min)
print(max)
print(min)
print(mid)
