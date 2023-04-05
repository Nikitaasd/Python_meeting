
def function_name(str_):
    wolwes = 'аяоёуюыиеэ'
    my_list = list(str_.split(' '))
    counter_set = set()
    for idx, el in enumerate(my_list):
        count = 0
        for letter in el:
            if letter in wolwes:
                count+=1
        counter_set.add(count)
    if len(counter_set)>1:
        return False
    else:
        return True

print(function_name('Пам-парам-пурум Пум-пурум-карам'))