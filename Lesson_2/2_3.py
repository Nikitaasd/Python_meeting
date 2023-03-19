# 2.3[14]: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

chislo = int(input('Введите число: '))

vivod = ''
if chislo == 1:
    print(chislo,' >>>> 1',)
else:
    for i in range(chislo):
        c=2**i
        if c>chislo:
            break
        a = str(c)
        vivod+=a+','
    print(chislo,' >>>> ', vivod) 
          

