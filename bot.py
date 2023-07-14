import telebot

TOKEN = '6306041543:AAFHxK1lULkkc54M2ddZwodaJHvXfqN5eO0'
bot = telebot.TeleBot(TOKEN)


def check_message(message):
  if message.text == '/start':
    start(message)
  else:
    return True


@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, 'Привет! Добро пожаловать в бота.')
  bot.send_message(message.chat.id, 'Введите ваше имя:')
  bot.register_next_step_handler(message, ask_question)


def ask_question(message):
  if check_message(message):
    name = message.text
    bot.send_message(message.chat.id, 'Введите ваш вопрос:')
    bot.register_next_step_handler(message, handle_question, name)


def handle_question(message, name):
  if check_message(message):
    question = message.text
    bot.send_message(message.chat.id, f'Спасибо, {name}! Вы задали вопрос: {question}')


bot.polling(none_stop=True)