'''
Выведите таблицу размером n×n, заполненную числами от 1 до n*n по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):

Sample Input:
5                                   3
Sample Output:
1 2 3 4 5                           1 2 3
16 17 18 19 6                       8 9 4
15 24 25 20 7                       7 6 5
14 23 22 21 8
13 12 11 10 9
'''
sizeTable = int(input())
table = [[0]*sizeTable for i in range(sizeTable)]
count = 1
x = 0

table[sizeTable//2][sizeTable//2] = sizeTable*sizeTable

for i in range(sizeTable//2):
    for j in range(sizeTable-x):
        table[i][j+i] = count
        count+=1

    for j in range(i+1, sizeTable-i):
        table[j][-i-1] = count
        count+=1

    for j in range(i+1, sizeTable-i):
        table[-i-1][-j-1] = count
        count+=1

    for j in range(i+1, sizeTable-(i+1)):
        table[-j-1][i] = count
        count+=1

    x += 2

for i in table:
    print(*i)
