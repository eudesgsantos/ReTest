import telebot
from telebot import types

bot = telebot.TeleBot('830353241:AAE3P5ciHJf_VmGflxJw7kCWiJ3r8EAxGxY')

channelID = "-1001225815995"

bot_id = 830353241

carlos = 871256317
will =  628657757

user = bot.get_me()
print(user)
"""
usuario = input("digite algo ")
usuario = usuario.lower()
if usuario ==("marcelo"):
    bot.send_message(-1001225815995,"marcelo esta indo")
"""

markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
itembta = types.KeyboardButton('Eu vou')
markup.add(itembta)
bot.send_message(-1001225815995,"Um Ping foi feito quem vai?",reply_markup=markup)


bot.send_message(reply_to_message,-1001225815995,"Você vai!")



"""
@bot.message_handler(func=lambda message:True)
def echo(message):
    bot.reply_to(message,"Fulano vai resolver o problema")
"""


updates = bot.get_updates(1234,100,20)
bot.polling(none_stop=False, interval=0, timeout=20)
