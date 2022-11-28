# Task 04
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

#  Make random list
n = int(input("Задайте длину списка N, N>2 "))
if n<3:
    print("Задайте другое число")
    exit()
list1 = []
for i in range(n):
    list1.append(random.randint(-n,n))
print(f"Случайная последовательность {list1}")

#  Create file with random number (<n) of random indexes(<n)
data = open('file.txt','w')
numberOfIndexes = random.randint(1,n)
for i in range(numberOfIndexes):
    index = random.randint(0,numberOfIndexes)
    data.write(f"{index}\n")
data.close

#  Open file with random indexes for getting prod
prod = 1
data = open('file.txt','r')
list_index = []
for line in data:
    index = int(line)
    prod *= list1[int(index)]
    list_index.append(index)
data.close   
print(f"Произведение случайных элементов массива с индексами {list_index} из файла file.txt = {prod}")