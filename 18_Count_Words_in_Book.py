'''
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра)
в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.

Sample Input 1:
a aa abC aa ac abc bcd a

Sample Output 1:
ac 1
a 2
abc 2
bcd 1
aa 2

Sample Input 2:
a A a

Sample Output 2:
a 3
'''
book = input().lower().split()
listOfWords = []
for word in book:
    if word not in listOfWords:
        listOfWords.append(word)
        print(word, book.count(word))
