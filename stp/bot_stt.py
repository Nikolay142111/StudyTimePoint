import datetime

import telebot
from telebot import types
import stt

def read_config_file():
    with open('config', 'r') as file:
        for line in file:
            if line.strip().startswith('TOKEN'):
                token = line.strip().split('TOKEN')[1].strip()
                return token

# Присвоим значение переменной
token_value = read_config_file()
#x='6592942350:AAE8GOMZ7USDZV73gbc-1eD7GQfW7XquLrc'

bot = telebot.TeleBot(token_value)


@bot.message_handler(commands=['start'])
def start(message):

    last_point = stt.check_last_points()
    # Создание объекта клавиатуры
    keyboard = types.ReplyKeyboardMarkup()

    # Создание кнопок и добавление их на клавиатуру
    button_start = types.KeyboardButton("Start")

    keyboard.row(button_start)
    bot.send_message(message.chat.id, f'{last_point} points', reply_markup=keyboard)


# @bot.message_handler(func=lambda message: message.text == 'Начать запись')
# def function_start(message):
#     keyboard = types.ReplyKeyboardMarkup()
#
#     button_practice = types.KeyboardButton("Практика")
#     button_theory = types.KeyboardButton("Теория")
#
#     keyboard.row(button_practice, button_theory)
#     bot.send_message(message.chat.id, 'Категория занятия:', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Start')
def stop_recording(message):
    keyboard = types.ReplyKeyboardMarkup()

    button_stop = types.KeyboardButton("Stop")
    keyboard.row(button_stop)
    bot.send_message(message.chat.id, 'Запись идёт', reply_markup=keyboard)

    stt.create_nev_log_part_1()


@bot.message_handler(func=lambda message: message.text == 'Stop')
def stop_recording_2(message):
    last_point = stt.check_last_points()
    bot.send_message(message.chat.id, 'Запись закончена')
    stt.write_datalog_part_2()

        # Создание объекта клавиатуры
    keyboard = types.ReplyKeyboardMarkup()

    # Создание кнопок и добавление их на клавиатуру
    button_start = types.KeyboardButton("Start")

    keyboard.row(button_start)
    bot.send_message(message.chat.id, f'{last_point} points', reply_markup=keyboard)




bot.polling(none_stop=True)
