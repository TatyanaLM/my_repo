elif comand == "/all_users":
username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")
if is_user_admin(mode):

    while True:
        comand = input("Введите команду...")
        if comand == "/login":
            login = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            if is_user_exist(login, list_of_users) and is_password_correct(password, list_of_users):
                print("ok")
            elif not is_user_exist(login, list_of_users):
                print("Пользователь не найден")
            else:
                print("Пароль некорректный")
        elif comand == "/register":
            login = input("Введите имя пользователя: ")
            password = input("Введите пароль: ")
            if is_user_exist(login, list_of_users):
                print("Неправильный логин")
            else:
                new_user = User(login, password)
                list_of_users.append(new_user)
                print("ok")
        else:
            print("Неверная команда")