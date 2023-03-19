def doLogin():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    with open('DataBase.txt', 'r') as file:
        loggedIn = False
        for line in file.readlines():
            DB_login, DB_pass = line.strip().split(' : ')
            # print(DB_login, DB_pass)
            if login == DB_login and password == DB_pass:
                print('Вошли')
                loggedIn = True
                break
        if not loggedIn:
            print('Не вошли')

        

    # print(f"Это - мой логин {login}\n А это - пароль{password}")