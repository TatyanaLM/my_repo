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
    return False

def is_user_admin(login, password, list_of_users):
    for current_user in list_of_users:
        if current_user.login == login and current_user.password == password and current_user.mode == "admin":
            return True
    return False

def save_user(login, password):
    with open("users.txt", "a") as f:
        f.write(login + " " + password + "\n")

def read_users():
    with open("users.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            splitted_line = line.split()
            login, password = splitted_line[0], splitted_line[1]
            return login, password


print(hash("password") == hash("password"))


