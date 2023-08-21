import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('6337593852:AAGKYzP1BNyRLUeWF4fUtaEGESEvg1NC4DU')


@bot.message_handler(commands=['start'])
def start(message):
    global message_chat_id
    message_chat_id = message.chat.id

    button_January = InlineKeyboardButton('Январь', callback_data='January')
    button_February = InlineKeyboardButton('Февраль', callback_data='February')
    button_March = InlineKeyboardButton('Март', callback_data='March')
    button_April = InlineKeyboardButton('Апрель', callback_data='April')
    button_May = InlineKeyboardButton('Май', callback_data='May')
    button_June = InlineKeyboardButton('Июнь', callback_data='June')
    button_July = InlineKeyboardButton('Июль', callback_data='July')
    button_August = InlineKeyboardButton('Август', callback_data='August')
    button_September = InlineKeyboardButton('Сентябрь', callback_data='September')
    button_October = InlineKeyboardButton('Октябрь', callback_data='October')
    button_November = InlineKeyboardButton('Ноябрь', callback_data='November')
    button_December = InlineKeyboardButton('Декабрь', callback_data='December')

    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.row(button_January, button_February, button_March, button_April, button_May, button_June, button_July,
                 button_August, button_September, button_October, button_November, button_December)
    bot.send_message(message_chat_id, 'Выберете месяц из списка:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    mount = call.data

    if call.data == 'January':
        mount_number = '01'
        bot.send_message(message_chat_id, f'Вы выбрали {mount}')

    elif call.data == 'February':
        mount_number = '02'
        bot.send_message(message_chat_id, f'Вы выбрали {mount}')

    elif call.data == 'March':
        mount_number = '03'
        bot.send_message(message_chat_id, f'Вы выбрали {mount}')

    elif call.data == 'April':
        mount_number = '04'
        bot.send_message(message_chat_id, f'Вы выбрали {mount}')

    elif call.data == 'May':
        mount_number = '05'
        bot.send_message(message_chat_id, f'Вы выбрали {mount}')

    elif call.data == 'June':
        mount_number = '06'
        bot.send_message(message_chat_id, f'Вы выбрали {mount}')

    elif call.data == 'July':
        mount_number = '07'
        bot.send_message(message_chat_id, f'Вы выбрали {mount}')

    elif call.data == 'August':
        mount_number = '08'
        bot.send_message(message_chat_id, f'Вы выбрали {mount}')

    elif call.data == 'September':
        mount_number = '09'
        bot.send_message(message_chat_id, f'Вы выбрали {mount}')

    elif call.data == 'October':
        mount_number = '10'
        bot.send_message(message_chat_id, f'Вы выбрали {mount}')

    elif call.data == 'November':
        mount_number = '11'
        bot.send_message(message_chat_id, f'Вы выбрали {mount}')

    elif call.data == 'December':
        mount_number = '12'
        bot.send_message(message_chat_id, f'Вы выбрали {mount}')


bot.polling(none_stop=True)
