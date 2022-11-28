# Реализуйте алгоритм перемешивания списка.

import random

#  Make random list
n = int(input("Задайте длину списка N "))
list1 = []
for i in range(n):
    list1.append(random.randint(-n,n))
print(f"Случайная последовательность {list1}")

# Shufftle random list by exchanging 2 random elements random times
numberOfShufftles = random.randint(1,10)
for i in range(numberOfShufftles):
    index1 = random.randint(0,n-1)
    index2 = random.randint(0,n-1)
    temp1 = list1[index1]
    list1[index1] = list1[index2]
    list1[index2] = temp1
    print(f"Итерация {i+1}: {list1}")
print(f"Перемешанный список {list1}")