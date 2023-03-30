import telebot
from telebot import types

bot = telebot.TeleBot("токен из телеги")

@bot.message_handler(command=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("😀 Привяy")
    markup.add(btn1)
    bot.send_message(message.chat.id, "Привет, я бот-помощник", reply_markup=markup)

@bot.message_handler(command=["text"])
def get_text_message(message):
    if message.text = "😀 Привяy":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Новости")
        btn2 = types.KeyboardButton("Расписание")
        btn3 = types.KeyboardButton("Курсы")
        markup.add(btn1,btn2, btn3)
        bot.send_message(message.chat.id, "Задайте мне вопрос", reply_markup=markup)
    elif message.text = "Какие новости?":
        bot.send_message(message.chat.id, "Все ок, остальные новости по [ссылке](https://levelup/news/", parse_mode="Markdown")
    elif message.text = "Какие расписание?":
        bot.send_message(message.chat.id, "Расписание доступно по [ссылке](https://levelup/courses/schedule/",parse_mode="Markdown")
    elif message.text = "Какие курсы есть?":
        bot.send_message(message.chat.id, "Курсы доступны по [ссылке](https://levelup/courses/",parse_mode="Markdown")



bot.infinity_polling()  # чтобы бот не завершал работу