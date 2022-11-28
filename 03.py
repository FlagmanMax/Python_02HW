# Task 03
# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("Введите число N "))
list1 = []
sum = 0
for i in range(n):
    num = i+1
    val = round((1+1/num)**num,4)
    sum += val
    print("{0:2d}: {1:4.2f}".format(num,val), end="\t")
    list1.insert(i, val)
print("\nСумма = {:4.2f}".format(sum))
print(list1)