import telebot

token = '6306041543:AAFHxK1lULkkc54M2ddZwodaJHvXfqN5eO0'
bot = telebot.TeleBot(token)


# Start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет!")


bot.infinity_polling()
