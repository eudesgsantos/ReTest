import telebot
import time

bot = telebot.TeleBot("830353241:AAE3P5ciHJf_VmGflxJw7kCWiJ3r8EAxGxY")
meta_charset = "UTF8"
@bot.message_handler(commands=['start'])
def send_message(message):
    bot.reply_to(message, 'Ola')

@bot.message_handler(commands=['ping'])
def send_message(message):
    bot.reply_to(message, 'Tu vais!')
    bot.reply_to(message, 'por obsequio resolva-o')





while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
