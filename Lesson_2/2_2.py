# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.

summa, proisved = int(input('Сумма чисел: ')), int(input('Произведение чисел: '))

for i in range(summa+1):
    for j in range(proisved+1):
            if i+j == summa and i*j == proisved:
                print(summa, proisved, ' -> ', i, j)
        