# 6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии
#
# Ввод: 7 2 5
# Вывод: [7 9 11 13 15]
# Ввод: 2 3 12
# Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]

def elements (input_char):
    new_list = list()
    for num, el in enumerate(input_char):
        print(el)
        new_list.append(int(input()))
    return [i for i in range(new_list[0], new_list[0]+new_list[1]*new_list[2], new_list[1])]

print(elements(['Значение первого элемента a1 ', 'Шаг n ', 'Кол-во элементов: ']))


