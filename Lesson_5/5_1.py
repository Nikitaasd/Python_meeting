# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16
def exponentiation(a, b):
    if (b == 0 and a == 0) or b == 0:
        return 1
    if a == 0:
        return 0
    if b == 1:
        return a
    return a*exponentiation(a,b-1)

print(f'exponentiation(2, 9) -> {exponentiation(2, 9)}')