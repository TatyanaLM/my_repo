#@botfather /newbot
#скопировать токен из телеги и никому не показывать

import telebot

bot = telebot.TeleBot("токен из телеги")

@bot.message_handler(command=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, я умею /register")
@bot.message_handler(command=["register"])
def register(message):
    bot.send_message(message.chat.id, "Введите свое имя")
    bot.register_next_step_handler(message, read_name)

def read_name(message):
    name = message.txt
    bot.send_message(message.chat.id, "Введите свою фамилию")
    bot.register_next_step_handler(message, read_name)

def read_sname(message, name):
    sname = message.txt
    bot.send_message(message.chat.id, f"Спасибо за регистрацию {name} {sname}!")



bot.infinity_polling() # чтобы бот не завершал работу

