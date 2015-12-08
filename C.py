'''
Задача C
++++++++

В прихожей в ряд стоит N тапочек, которые бывают разных размеров, а также левыми и правыми. Гость выбирает два тапочка,
удовлетворяющих следующим условиям:

- выбранные тапочки должны быть одного размера;
- из выбранных тапочков левый тапочек должен стоять левее правого;
- если можно выбрать несколько пар тапочек, удовлетворяющих первым двум условиям, то выбирается два тапочка с наименьшим
  расстоянием между ними.

  В первой строке входны данных записано число тапочков N. Во второй строке записаны размеры тапочков в порядке слева
  направо, при этом левые тапочки условно обозначаются отрицательными числами (то есть -s обозначает левый тапочек, а s
  обозначает правый тапочек размера s).

  Выведите одно число: минимальное расстояние между двумя тапочками одного размера таких, что левый тапочек стоит левее
  правого. Если таких пар тапочек нет, то выведите одно число 0.

  +----------------------+-------+
  | Ввод                 | Вывод |
  +======================+=======+
  | 6                    | 2     |
  +----------------------+-------+
  | -40 41 -42 -41 42 40 |       |
  +----------------------+-------+
'''

f = open('input.txt')
N = int(f.readline())
A = f.readline().split()
for i in range(len(A)):
    A[i] = int(A[i])
min = 999

for i in range(len(A) - 1):
    for j in range(i + 1, len(A)):
        if (A[i] == A[j]*(-1)) and (A[i] < 0):
            x = j - i
            if x < min:
                min = x

f = open('output.txt', 'w')
if min == 999:
    print(0, file = f)
else:
    print(min, file = f)
f.close()