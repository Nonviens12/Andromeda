login = input("Введите логин: ")
password = input("Введите пароль: ")

with open('DataBase.txt', 'a') as file:
    file.write(login+' : '+password+'\n')