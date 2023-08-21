import datetime

import telebot
from telebot import types
import stt

bot = telebot.TeleBot('6176765790:AAEhdEUDkzQkNyGk11YKeQYUl1SJ5XkRX3I')


@bot.message_handler(commands=['start'])
def start(message):
    # Создание объекта клавиатуры
    keyboard = types.ReplyKeyboardMarkup()

    # Создание кнопок и добавление их на клавиатуру
    button_start = types.KeyboardButton("Начать запись")
    button_holidays = types.KeyboardButton("Указать каникулы")

    keyboard.row(button_start, button_holidays)
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Начать запись')
def function_start(message):
    keyboard = types.ReplyKeyboardMarkup()

    button_practice = types.KeyboardButton("Практика")
    button_theory = types.KeyboardButton("Теория")

    keyboard.row(button_practice, button_theory)
    bot.send_message(message.chat.id, 'Категория занятия:', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Практика' or message.text == 'Теория')
def stop_recording(message):
    keyboard = types.ReplyKeyboardMarkup()

    button_stop = types.KeyboardButton("Остановить запись")
    keyboard.row(button_stop)
    bot.send_message(message.chat.id, 'Запись идёт', reply_markup=keyboard)

    stt.create_nev_log_part_1()


@bot.message_handler(func=lambda message: message.text == 'Остановить запись')
def stop_recording_2(message):
    bot.send_message(message.chat.id, 'Запись закончена')
    stt.write_datalog_part_2()


@bot.message_handler(func=lambda message: message.text == 'Указать каникулы')
def write_holidays(message):
    bot.send_message(message.chat.id, 'Введите диапазон каникул в формате: месяц-день месяц-день')
    global holidays
    holidays = +1


@bot.message_handler()
def write_holidays_2(message):
    date_year = datetime.date.today().strftime("%Y-")
    if holidays >= 1:
        date_from = date_year + message.text[:5]
        date_before = date_year + message.text[6:]

        if date_from < datetime.date.today():
            date_year = + 1
            date_from = date_year + message.text[:5]
        elif date_before < datetime.date.today():
            date_year =+1
            date_before = date_year + message.text[6:]

        stt.write_dates_holidays(date_from, date_before)
        bot.send_message(message.chat.id, 'Готово!')
        bot.send_message(message.chat.id, f' Каникулы от {date_from} до {date_before}')
        # 08-19 08-22


bot.polling(none_stop=True)
