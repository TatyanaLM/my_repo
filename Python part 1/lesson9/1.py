from login.user import User
from login.functions import is_user_exist, is_password_correct, is_user_admin, save_user

admin = User('admin', 'admin_pass', 'admin')
save_user('admin', "admin_pass")
list_of_users = [admin]

while True:
    comand = input("Введите команду...")
    if comand == "/login":
        login = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        if is_user_exist(login, list_of_users) and is_password_correct(login, password, list_of_users):
            print("ok")
        elif not is_user_exist(login, list_of_users):
            print("Пользователь не найден")
        else:
            print("Пароль некорректный")
    elif comand == "/register":
        login = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        if is_user_exist(login, list_of_users):
            print("Пользователь уже существует")
        else:
            new_user = User(login, password)
            list_of_users.append(new_user)
            print("Пользователь зарегистрирован")
    elif comand == "/all_users":
        login = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        if is_user_admin(login, password, list_of_users):
            for user in list_of_users:
                print(user)
        else:
            print("Нет доступа")
    else:
            print("Неверная команда")