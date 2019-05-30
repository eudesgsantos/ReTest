import time
import telebot
import logging
import smtplib, ssl
import serial
from telebot import types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

Arduinoserial = serial.Serial('COM14')
bot = telebot.TeleBot('830353241:AAE3P5ciHJf_VmGflxJw7kCWiJ3r8EAxGxY')

global respo
number = 0

def handle_messages(messages):
    global cheia
    global number
    global problema
    global lugar
    for message in messages:
        kin = str(message).split(',')
        print(kin)
        mens = kin[-1].split(': ')
        print(mens[1])
        name = kin[4].split(': ')
        print(name[1])
        sup = name[1]
        cheia = sup
        if mens[1] == "'Eu vou'}}":
            pedsup = sup+" vai resolver o chamado do(a) "+problema+" no(a) "+lugar
            number = 2
            enviarEmail()
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            itembta = types.KeyboardButton('Feito')
            markup.add(itembta)
            bot.send_message(-1001225815995,pedsup,reply_markup=markup)
        if mens[1] == "'Feito'}}":
            relsup = sup+" resolveu o problema!"
            number = 1
            bot.send_message(-1001225815995,relsup)
            enviarEmail()


def enviarEmail():
    global strokes
    global number
    if number == 2:
        msg = '{} esta indo resolver "{}", acompanhe seu email para mais informes do andamento do problema'.format(cheia,respo)
    if number == 1:
        msg = '{} resolveu {}, obrigado por usar o PiNG, contamos com voce para os proximos reportes'.format(cheia,respo)
        del strokes[0]
        del strokes[0]
    port = 465
    password = 'arduinopython'
    sender_email = 'retestping@gmail.com'
    receiver_email = emailT

    message = MIMEMultipart("alternative")
    message["Subject"] = "Feedback P!NG"
    message ["From"] = sender_email
    message ["To"] = receiver_email
    text = """\
    {}
    """.format(msg)
    html = """\
    <html>
        <body>
            <p>{}
            </p>

        </body>
    </html>
    """.format(msg)
    part1 = MIMEText(text,"plain")
    part2 = MIMEText(html,"html")
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login('retestping@gmail.com', password)
        server.sendmail(sender_email, receiver_email, message.as_string())


channelID = "-1001225815995"

bot_id = 830353241

carlos = 871256317
will =  628657757

strokes = []

while True:
    res = Arduinoserial.readline().decode('ascii')
    if res not in strokes:
        res = res.replace("'",'')
        res = res.replace("  ",'')
        res = res.replace("\n",'')
        res = res.replace("<",'')
        res = res.replace(">",'')
        res = res.replace("\r",'')
        strokes.append(res)
    print(strokes)
    if len(strokes)>=2:
        problema = strokes[0]+strokes[1]
        lugar = 'Auditório'
        respo = problema +' no(a) '+ lugar
        email = input('Digite as iniciais do seu nome ')
        pedido = problema+' no(a)'+lugar+' quem vai resolver?'
        emailT = email+'@cesar.school'
        print(emailT)
        cheia = ''


        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        itembta = types.KeyboardButton('Eu vou')
        markup.add(itembta)
        bot.send_message(-1001225815995,pedido,reply_markup=markup)

        bot.set_update_listener(handle_messages)
        time.sleep(1)
        bot.infinity_polling(True)
        while True:
            try:
                bot.polling(none_stop=True,interval=0,timeout=123)
            except Exception as e:
                logger.error(e)
                time.sleep(15)
