'''
Задача A
++++++++

В массиве ровно два элемента равны. Найдите эти элементы.

Программа получает на вход число N, в следующей строке заданы N элементов списка через пробел.

Выведите значение совпадающих элементов.

+-------------+-------+
| Ввод        | Вывод |
+=============+=======+
| 6           | 5     |
+-------------+-------+
| 8 3 5 4 5 1 |       |
+-------------+-------+
'''

f = open('input.txt')
N = int(f.readline())
A = f.readline().split()
for i in range(len(A)):
    A[i] = int(A[i])

for i in range(len(A) - 1):
    for j in range(i +1, len(A)):
        if A[i] == A[j]:
            x = A[i]

f = open('output.txt', 'w')
print(x, file = f)
f.close()
