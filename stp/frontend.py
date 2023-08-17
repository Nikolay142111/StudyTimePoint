import telebot
from telebot import types
import stt

bot = telebot.TeleBot('6176765790:AAEhdEUDkzQkNyGk11YKeQYUl1SJ5XkRX3I')




@bot.message_handler(commands=['start'])
def start(message):
    # Создание объекта клавиатуры
    keyboard = types.ReplyKeyboardMarkup()

    # Создание кнопок и добавление их на клавиатуру
    button1 = types.KeyboardButton("Начать запись")
    button2 = types.KeyboardButton("Закончить запись")
    keyboard.row(button1, button2)
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=keyboard)


@bot.message_handler()
def start(message):

    if message.text == 'Начать запись':
        bot.send_message(message.chat.id, 'Начало записи')
        bot.send_message(message.chat.id, stt.create_nev_log_part_1())

    if message.text == 'Закончить запись':
        bot.send_message(message.chat.id, 'Конец записи')
        bot.send_message(message.chat.id, stt.write_datalog_part_2())



bot.polling(none_stop=True)
