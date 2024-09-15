# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

phonebook = open("phoneBook.txt","r",encoding="utf-8")
spisok = [str(i).split() for i in phonebook]
print(spisok)
q = True
while q:
    command = input("Введите команду: ")
    if command == "поиск":
        x = input("Введите имя абонента: ")
        for i in range(len(spisok)):
            if spisok[i][1] == x:
                print(spisok[i][0],spisok[i][1],spisok[i][2],spisok[i][3])

    elif command == "добавить":
        x = input("введите имя обонента и его номера через пробел: ")
        abonent = x.split()
        spisok.append(abonent)
        with open("phoneBook.txt","a", encoding="utf-8") as book:
            book.write("\n"+ x)            
            book.close()
    elif command == "вывод":
        for i in spisok:
            print(*i)
    elif command == "выход":
        q = False

    else:
        print("неверная команда")