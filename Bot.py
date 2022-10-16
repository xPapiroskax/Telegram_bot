import telebot
from telebot import types

bot = telebot.TeleBot('5627226187:AAGXTG6uIg5xYvlrMD42wycpfl8OQB72HUk') # привязка бота по токену

import covid_people

@bot.message_handler(commands=['start'])    # Отслеживание команд, вводимых в телеграме
def start(message):    # Создаем функцию(лучше называть как и команда)
    mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'Hello':
#         #bot.send_message(message.chat.id, message, parse_mode='html')
#         bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')
#     elif message.text == 'id':
#         bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
#     elif message.text == 'photo':
#         photo = open('star-wars-darth-vader-x-wing-wife-mw.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, f"Я тебя не понимаю", parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, крутое фото')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://docs.gitlab.com/"))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3) #Будут подстраиваться под нужный размер и ширина ряда
    website = types.KeyboardButton('Веб сайт')
    start = types.KeyboardButton('Start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

bot.polling(none_stop=True)