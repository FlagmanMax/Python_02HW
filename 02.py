# Task 02
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Введите число N "))
list_prod = []
list_str = []

list_prod.insert(0,1)
list_str.insert(0,'1')
for i in range(1,n):
    list_prod.insert(i,(i+1)*list_prod[i-1])
    list_str.insert(i,f'{list_str[i-1]}*{i+1}')
        
print(list_prod)
print(list_str)