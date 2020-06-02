'''
На прошлой неделе мы сжимали строки, используя кодирование повторов.
Теперь нашей задачей будет восстановление исходной строки обратно.
Напишите программу, которая считывает из файла строку, соответствующую тексту,
сжатому с помощью кодирования повторов, и производит обратную операцию,
получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
Примечание. Это первое задание типа Dataset Quiz.
В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка "download your dataset".
Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер.
Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл,
который при этом у вас получится,
надо отправить в качестве ответа на эту задачу.

Sample Input:
a3b4c2e10b1

Sample Output:
aaabbbbcceeeeeeeeeeb
'''
coded_string = str(input().split())
list_for_decoding = []
result = []
for i in range (len(coded_string)-1):
    if coded_string[i].isalpha():
        list_for_decoding.append(coded_string[i])
        if coded_string[i+1].isdigit():
            if coded_string[i+2].isdigit():
                list_for_decoding.append(coded_string[i+1]+coded_string[i+2])
            else:
                list_for_decoding.append(coded_string[i+1])

for i in range (len(list_for_decoding)):
    if list_for_decoding[i].isalpha():
        for j in range(int(list_for_decoding[i+1])):
            result.append(list_for_decoding[i])
result_string = ''.join(result)
print(result_string)
