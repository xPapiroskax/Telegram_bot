import COVID19Py

import telebot
from telebot import types
bot = telebot.TeleBot('5627226187:AAGXTG6uIg5xYvlrMD42wycpfl8OQB72HUk') # привязка бота по токену

# Отслеживание данных о ковиде
covid19 = COVID19Py.COVID19()
#latest = covid19.getLatest()
#location = covid19.getLocationByCountryCode("RU")
#print(latest) - в консоле
#print(location) - в консоле
@bot.message_handler(commands=['covid'])
def covid(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Во всем мире')
    btn2 = types.KeyboardButton('США')
    btn3 = types.KeyboardButton('Россия')
    btn4 = types.KeyboardButton('Украина')
    btn5 = types.KeyboardButton('Франция')
    btn6 = types.KeyboardButton('Италия')
    btn7 = types.KeyboardButton('Германия')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

    send_message = f"<b>Привет {message.from_user.first_name}!</b>\nЧтобы узнать данные про коронавируса напишите " \
                   f"название страны, например: США, Украина, Россия и так далее\n\n"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

    #mess = f"Привет, <b>{message.from_user.first_name}</b>\nВведите страну"
    #bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

# Функция, что сработает при отправке какого-либо текста боту
# Здесь мы создаем отслеживания данных и вывод статистики по определенной стране
@bot.message_handler(content_types=['text'])
def mess(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "казахстан":
        location = covid19.getLocationByCountryCode("KZ")
    elif get_message_bot == "италия":
        location = covid19.getLocationByCountryCode("IT")
    elif get_message_bot == "франция":
        location = covid19.getLocationByCountryCode("FR")
    elif get_message_bot == "германия":
        location = covid19.getLocationByCountryCode("DE")
    else:
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n \
        <b>Сметрей: </b>{location['deaths']:,}"

    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
				f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
				f"{location[0]['latest']['deaths']:,}"

    bot.send_message(message.chat.id, final_message, parse_mode='html')

bot.polling(none_stop=True)