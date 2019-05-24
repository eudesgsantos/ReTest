import telebot
import smtplib, ssl
from telebot import types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
bot = telebot.TeleBot('830353241:AAE3P5ciHJf_VmGflxJw7kCWiJ3r8EAxGxY')

channelID = "-1001225815995"

bot_id = 830353241

carlos = 871256317
will =  628657757

user = bot.get_me()
print(user)

problema = input('Qual o seu problema? ')
lugar = input('Aonde esta o problema? ')
email = input('Digite as iniciais do seu nome ')
pedido = problema+' no(a)'+lugar+' quem vai resolver?'
emailT = email+'@cesar.school'
print(emailT)
cheia = ''
pedCar = "Carlos vai resolver o chamado do(a) "+problema+" no(a) "+lugar
pedWill = "Will vai resolver o chamado do(a) "+problema+" no(a) "+lugar


markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
itembta = types.KeyboardButton('Eu vou')
markup.add(itembta)
bot.send_message(-1001225815995,pedido,reply_markup=markup)

def enviarEmail():
    port = 465
    password = 'arduinopython'
    sender_email = 'retestping@gmail.com'
    receiver_email = emailT

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message ["From"] = sender_email
    message ["To"] = receiver_email
    print("cheia é", cheia)
    text = """\
    {} esta indo resolver seu problema,acompanhe seu email para mais informes do andamento do problema
    """.format(cheia)
    html = """\
    <html>
        <body>
            <p>{} esta indo resolver seu problema, acompanhe seu email para mais informes do andamento do problema


            </p>
        
        </body>
    </html>

    """.format(cheia)
    part1 = MIMEText(text,"plain")
    part2 = MIMEText(html,"html")
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login('retestping@gmail.com', password)
        server.sendmail(sender_email, receiver_email, message.as_string())


def handle_messages(messages):
    global cheia
    for message in messages:
        if "Carlos" in str(message):
            cheia = 'Carlos'
            markup = types.ReplyKeyboardRemove(selective=True)
            bot.send_message(-1001225815995,pedCar,reply_markup=markup)
            print(cheia)
            enviarEmail()
        if "Will" in str(message):
            cheia = 'Will'
            markup = types.ReplyKeyboardRemove(selective=True)
            bot.send_message(-1001225815995,pedWill,reply_markup=markup)
            print(cheia)
            enviarEmail()

bot.set_update_listener(handle_messages)
bot.polling()

updates = bot.get_updates(1234,100,20)
bot.polling(none_stop=False, interval=0, timeout=20)
