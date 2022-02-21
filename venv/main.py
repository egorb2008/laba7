import telebot
import datetime

token = "2019045554:AAGATJlMbr47wr_2LdaWlAwG7ALtf2Vzu1M"
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ["start"]) # команда старт
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я пока ничего не умею, но скоро что-то смогу.')

@bot.message_handler(commands = ['help'])
def start_message(message):
    bot.send_message(message.chat.id, "Я пока ничего не умею")

@bot.message_handler(commands = ['mtuci'])
def start_message(message):
    bot.send_message(message.chat.id, 'https://mtuci.ru/')

@bot.message_handler(content_types = ['text'])
def manipulator(message):
    week = int(datetime.date.today().isocalendar()[1]) % 2  # чётная ли неделя
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет!')
    elif message.text == "Какая сейчас неделя?":
        if week == 0:
          bot.send_message(message.chat.id, 'Чётная')
        if week != 0:
            bot.send_message(message.chat.id, 'Нечётная')
    else:
        bot.send_message(message.chat.id, "Я не понимаю что ты от меня хочешь.")

bot.infinity_polling() # бесконечная работа бота