# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список можно считать заданным.
# Введенное число не обязательно содержится в списке.
my_list = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
figure = 8
diff = abs(my_list[0] - figure)
my_fig = my_list[0]

for i in range(len(my_list)):
    if abs(my_list[i] - figure) < diff:
        my_fig = my_list[i]
        diff = abs(my_list[i] - figure)
print(my_fig)