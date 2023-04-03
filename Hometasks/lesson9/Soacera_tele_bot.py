import telebot
from telebot import types

#@soacera_bot

bot = telebot.TeleBot("5995529298:AAEMZ0YuW5042X4A2oaH4sH4lgRSiNs6tjY")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.from_user.id, "Привет, я бот-калькулятор 2.0", reply_markup=markup)
    bot.send_message(message.from_user.id, "Я умею считать /calculate")

@bot.message_handler(commands=['calculate'])
def register(message):
    bot.send_message(message.chat.id, "Введите число А")
    bot.register_next_step_handler(message, read_a)

def read_a(message):
    a = message.text
    bot.send_message(message.chat.id, "Введите число Б")
    bot.register_next_step_handler(message, read_b, a)

def read_b(message, a):
    b = message.text
    bot.send_message(message.chat.id, f"Что сделать с числами {a} и {b}?")
    bot.register_next_step_handler(message, calc, a, b)

def calc(message, a, b):
    if message.text == '+':
        result = float(a) + float(b)
        bot.send_message(message.chat.id, f"{a} + {b} = {result}")
    elif message.text == "-":
        result = float(a) - float(b)
        bot.send_message(message.chat.id, f"{a} - {b} = {result}")
    elif message.text == "*":
        result = float(a) * float(b)
        bot.send_message(message.chat.id, f"{a} * {b} = {result}")
    elif message.text == "/":
        result = float(a) / float(b)
        bot.send_message(message.chat.id, f"{a} / {b} = {result}")
    else:
        return "Некорректный ввод"


bot.infinity_polling()