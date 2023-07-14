import telebot
from telebot import types
import schedule
import time

TOKEN = '6306041543:AAFHxK1lULkkc54M2ddZwodaJHvXfqN5eO0'
CHAT_ID = None
bot = telebot.TeleBot(TOKEN)
start_time = time.time()


def check_message(message):
  if message.text == 'Начать':
    start_message(message)
  else:
    return True


markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_button = types.KeyboardButton('Начать')
markup.add(start_button)


@bot.message_handler(func=lambda message: True)
def start_message(message):
  global CHAT_ID
  CHAT_ID = message.chat.id
  bot.send_message(CHAT_ID, 'Введите ваше имя:', reply_markup=markup)
  bot.register_next_step_handler(message, ask_question)


def ask_question(message):
  if check_message(message):
    name = message.text
    bot.send_message(CHAT_ID, 'Введите ваш вопрос:')
    bot.register_next_step_handler(message, handle_question, name)


def handle_question(message, name):
  if check_message(message):
    question = message.text
    bot.send_message(CHAT_ID, f'Спасибо, {name}! Вы задали вопрос: {question}')


def send_days():
  global CHAT_ID
  days_count = int((time.time() - start_time) // (24 * 60 * 60))
  bot.send_message(CHAT_ID, f'Прошло {days_count} дней со старта')


schedule.every().day.at("12:00").do(send_days)

while True:
  schedule.run_pending()
  time.sleep(1)
  bot.polling(none_stop=True)
