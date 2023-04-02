# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X. 

input_list = []
list_len = int(input("Введите количество элементов в массиве: "))
for _ in range (list_len):
    input_list.append(int(input("Введите элемент массива - целое число: ")))
print(input_list)
search_el = int(input("Введите элемент, количество которого в массиве необходимо вычислить: "))
el_count = input_list.count(search_el)
print(f"Элемент {search_el} в списке появляется {el_count} раз")



input_list2 = []
list_lentgh = int(input("Введите количество элементов в массиве: "))
for _ in range (list_lentgh):
    input_list2.append(int(input("Введите элемент массива - целое число: ")))
print(input_list2)
search_elem = int(input("Введите элемент, количество которого в массиве необходимо вычислить: "))
elem_count = 0
for element in input_list2:
    if element == search_elem:
        elem_count += 1
print(f"Элемент {search_elem} в списке появляется {elem_count} раз")

import time


start = time.perf_counter()
print(5 in input_list)
end = time.perf_counter()
first_time = end - start

start = time.perf_counter()
print(5 in input_list2)
end = time.perf_counter()
second_time = end - start
print(first_time / second_time)


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

some_list = []
list_len = int(input("Введите количество элементов в массиве: "))
for _ in range (list_len):
    some_list.append(int(input("Введите элемент массива: ")))
print(some_list)
search_number = int(input("Введите число, близкий элемент к которому необходимо найти: "))
ind = 0
min_difference = abs(search_number - some_list[0])
for i in range (list_len):    
    difference = abs(search_number - some_list[i])
    if difference < min_difference:
        min_difference = difference
        ind = i
print(f"Самый близкий по величине элемент к заданному числу - {some_list[ind]}")


# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

points_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
points_2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
points_3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
points_4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
points_5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
points_8 = ['J', 'X', 'Ш', 'Э', 'Ю']
points_10 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']
word = input("Введите слово либо на английском, либо на русском языке: ")
sum = 0
for i in word:
    if i in points_1:
        sum += 1
    if i in points_2:
        sum += 2
    if i in points_3:
        sum += 3
    if i in points_4:
        sum += 4
    if i in points_5:
        sum += 5
    if i in points_8:
        sum += 8
    if i in points_10:
        sum += 10
print(sum, 'очков')
