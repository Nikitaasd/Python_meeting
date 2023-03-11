# 1.1[2]. Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод
# Например для числа 145 сумма цифр будет 10: 1 + 4 + 5
vvod = input('Введите число: ')
chislo = int(vvod)
summa = 0

while chislo >= 1:
    ostatock = chislo%10
    summa += ostatock
    chislo //= 10
vivod = ''
j=0
for i in vvod:
    j+=1
    if j == len(vvod):
        vivod +=i
        break 
    vivod +=i+'+'



print(f'Сумма чисел числа {vvod} равна {summa} ({vivod})')