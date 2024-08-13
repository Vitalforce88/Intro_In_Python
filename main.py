import random as rnd



def create_rnd_list(sizeOf):
    '''
    функция возврващает список нужной величины
    со случайными значениями от 1 до 150

    '''
    lst = []
    for _ in range(sizeOf):
        lst.append(rnd.randint(1,150))
    return lst

print(create_rnd_list(10))

print(create_rnd_list.__doc__) # вывести документацию по функции (всё что между тройными кавычками """здесь любая инфа внутри функции""")

text = input("Input text:\n")

text = text.lower().replace('.',' ').split() # привести к нижнему регистру, поменять точки на пробелы, разделить по словам

result = len(set(text)) # сохранить длину множества в переменную result

print(result)