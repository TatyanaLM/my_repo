
class User():
    def __init__(self, login, password, mode="user"):
        self.login = login
        self.password = password
        self.mode = mode
    def __str__(self):
        return f"Логин: {self.login}, пароль: {self.password}, роль: {self.mode}"





