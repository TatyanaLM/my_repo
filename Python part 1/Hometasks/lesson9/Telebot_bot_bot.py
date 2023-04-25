#5995529298:AAEMZ0YuW5042X4A2oaH4sH4lgRSiNs6tjY

import telebot
from telebot import types

bot = telebot.TeleBot("5995529298:AAEMZ0YuW5042X4A2oaH4sH4lgRSiNs6tjY")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.from_user.id, "Привет, я бот-калькулятор", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'h':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('+')
        btn2 = types.KeyboardButton('-')
        btn3 = types.KeyboardButton('=')
        btn4 = types.KeyboardButton('*')
        btn5 = types.KeyboardButton('/')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота

    elif message.text == "":
        bot.send_message(message.from_user.id, "Да нормально все, остальные новости по " + "[ссылке](https://levelp.ru/news/)", parse_mode="Markdown")
    elif message.text == "Какое расписание?":
        bot.send_message(message.from_user.id, "Расписание доступно по [ссылке](https://levelp.ru/courses/schedule/)", parse_mode="Markdown")
    elif message.text == "Какие есть курсы?":
        bot.send_message(message.from_user.id, "Список курсов находится по [ссылке](https://levelp.ru/courses/)", parse_mode="Markdown")

bot.polling(none_stop=True, interval=0)

'''
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, я умею /register")

@bot.message_handler(commands=['register'])
def register(message):
    bot.send_message(message.chat.id, "Введите пожалуйста свое имя")
    bot.register_next_step_handler(message, read_name)

def read_name(message):
    name = message.text
    bot.send_message(message.chat.id, "Введите пожалуйста свою фамилию")
    bot.register_next_step_handler(message, read_sname, name)

def read_sname(message, name):
    sname = message.text
    bot.send_message(message.chat.id, f"Спасибо за регистрацию {name} {sname}")

bot.infinity_polling()