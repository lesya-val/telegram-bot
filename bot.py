import telebot
from telebot import types

token = '6306041543:AAFHxK1lULkkc54M2ddZwodaJHvXfqN5eO0'
bot = telebot.TeleBot(token)


# Start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton('Начать')
    markup.row(item)

    bot.send_message(message.chat.id, "Привет! Нажми 'Начать' для продолжения.", reply_markup=markup)


bot.infinity_polling()
