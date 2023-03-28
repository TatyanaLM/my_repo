#from user import User

def is_user_exist(login, list_of_users):
    for current_user in list_of_users:
        if current_user.login == login:
            return True
    return False
def is_password_correct(login, password, list_of_users):
    for current_user in list_of_users:
        if current_user.login == login:
            if current_user.password == password:
                return True
            else:
                return False


#def is_user_admin(mode, list_of_users):




    if str == '/login':
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        new_user = User(login, password)
        list_of_users.append(new_user)


