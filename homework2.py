#____________________1________________________
#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# n = input('Введи число: ').split('.')
# if len(n)>1:
#     n_list = n[0]+n[1]
# else:
#     n_list = n[0]
# sum_list = []
# for x in range(len(n_list)):
#     sum_list.append(n_list[x])
# for i in range(len(sum_list)):
#     sum_list[i]=int(sum_list[i])
# result = 0
# for j in range(len(sum_list)):
#     result = result + sum_list[j]
# print(result)

#______________________2__________________________
#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите число: '))
# res_list = []
# for i in range(n):
#     res_list.append(i+1)
# print(res_list)
# count = 0
# for x in range(n):
#     result = 1
#     count = count + 1
#     for i in range(count):
#         result = result*(i+1)
#         res_list[x] = result
# print(res_list)

#________________________3_______________________
#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# n = int(input('Введите число: '))
# res_list = []
# sum = 0
# for i in range(n):
#     res_list.append(round((1 + float(1/(i+1)))**(i+1), 2))
#     sum = sum + (1 + float(1/(i+1)))**(i+1)
# print(res_list)
# print(round(sum,2))

#__________________4___________________________
#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input('Введите число: '))
num_list = []
for j in range(-n,n+1):
        num_list.append(j)
print(num_list)
sum = 0
data = open('1.txt' , 'r')
for line in data:
    sum = sum + num_list[int(line)]
data.close()
print(sum)