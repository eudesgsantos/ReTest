import time
from datetime import datetime
import json
import telebot
import logging
import smtplib
import ssl
import _thread
import serial
from telebot import types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

DEBUG = False

if(not DEBUG):
    Arduinoserial = serial.Serial('COM14')
bot = telebot.TeleBot(
    '830353241:AAE3P5ciHJf_VmGflxJw7kCWiJ3r8EAxGxY', threaded=True)

global respo
number = 0


def handle_messages(messages):
    global cheia
    global number
    global problema
    global lugar
    for message in messages:
        kin = str(message).split(',')
        mens = kin[-1].split(': ')
        name = kin[4].split(': ')
        sup = name[1]
        cheia = sup
        if mens[1] == "'Eu vou'}}":
            pedsup = sup + \
                " vai resolver o chamado do(a) "+problema+" no(a) "+lugar
            number = 2
            enviarEmail()
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            itembta = types.KeyboardButton('Feito')
            markup.add(itembta)
            bot.send_message(-1001225815995, pedsup, reply_markup=markup)
        if mens[1] == "'Feito'}}":
            relsup = sup+" resolveu o problema!"
            number = 1
            bot.send_message(-1001225815995, relsup)
            enviarEmail()


def fazPoll(var1, var2):
    bot.polling()
    print(var1, var2)


def enviarEmail():
    global strokes
    global number
    if number == 2:
        msg = '{} esta indo resolver "{}", acompanhe seu email para mais informes do andamento do problema'.format(
            cheia, respo)
    if number == 1:
        msg = '{} resolveu {}, obrigado por usar o PiNG, contamos com voce para os proximos reportes'.format(
            cheia, respo)

    port = 465
    password = 'arduinopython'
    sender_email = 'retestping@gmail.com'
    receiver_email = emailT

    message = MIMEMultipart("alternative")
    message["Subject"] = "Feedback P!NG"
    message["From"] = sender_email
    message["To"] = receiver_email
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
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login('retestping@gmail.com', password)
        server.sendmail(sender_email, receiver_email, message.as_string())


channelID = "-1001225815995"

bot_id = 830353241

carlos = 871256317
will = 628657757

strokes = []

_thread.start_new_thread(fazPoll, ("chamei", "o coisa"))

while True:
    if(DEBUG):
        res = input("digita ai: ")
    else:
        res = Arduinoserial.readline().decode('ascii')
    if res not in strokes:
        res = res.replace("'", '')
        res = res.replace("  ", '')
        res = res.replace("\n", '')
        res = res.replace("<", '')
        res = res.replace(">", '')
        res = res.replace("\r", '')
        strokes.append(res)
        print(strokes)
    if len(strokes) >= 3:
        timestamp = datetime.now()
        tempo = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        crac = strokes[0]
        problema = strokes[1]+' '+strokes[2]
        print(crac)
        identity = crac
        serial = problema
        data = {}
        subindice = serial + ', ' + tempo
        with open('data_file.json', 'r') as read_file:
            data = json.load(read_file)
        if identity in data:
            data[identity].append(subindice)
            with open('data_file.json', 'w') as write_file:
                json.dump(data, write_file, indent=4)
        else:
            data[identity] = []
            data[identity].append(subindice)
            with open('data_file.json', 'w') as write_file:
                json.dump(data, write_file, indent=4)

        dicA = {'29 0 95 E0 C7 ': 'phmt', '29 0 9A 90 97 ': 'egsf', '29 0 95 E0 AE ': 'pqla', '29 0 9A 90 92 ': 'earo',
                '29 0 9A 91 F6 ': 'jmsda', '29 0 9A 91 F0 ': 'jcsc', '29 0 9C 12 3C ': 'avca', '29 0 9A 90 D5 ': 'eemb', '29 0 9C 9C A0 ': 'jcrm',
                '29 0 95 F4 DC ': 'mlml', '29 0 95 F4 FC ': 'mcla', '29 0 9A 91 F4 ': 'gsmf', '29 0 43 C1 EB ': 'lfvf', '29 0 9C 9E 1D ': 'lvco',
                '29 0 9C 9E 5E ': 'jvmls', '29 0 95 F4 F3 ': 'mda', '29 0 95 F5 13 ': 'nvn'}
        dicB = {'29 0 95 E0 C7 ': 'Paulo Teixeira', '29 0 9A 90 97 ': 'Eudes Santos', '29 0 95 E0 AE ': 'Pedro Luis',
                '29 0 9A 90 92 ': 'Enrico Amorim', '29 0 9A 91 F6 ': 'João Marcelo', '29 0 9A 91 F0 ': 'João Carlos', '29 0 9C 12 3C ': 'Ana Vivian',
                '29 0 9A 90 D5 ': 'Eduardo Eile', '29 0 9C 9C A0 ': 'Julio César', '29 0 95 F4 DC ': 'Maria Luísa Leitão', '29 0 95 F4 FC ': 'Milena Costa Leimig',
                '29 0 9A 91 F4 ': 'Gabriel Soriano', '29 0 43 C1 EB ': 'Lucas Felinto', '29 0 9C 9E 1D ': 'Larissa Virginia',
                '29 0 9C 9E 5E ': 'José Victor Macedo', '29 0 95 F4 F3 ': 'Matheus Dias', '29 0 95 F5 13 ': 'Nivaldo Neto'}
        indv = ''
        if crac in dicA:
            email = dicA[crac]
            indv = dicB[crac]
        else:
            email = 'kkk'
        print(crac)
        lugar = 'Auditório'
        respo = problema + ' no(a) ' + lugar
        pedido = indv + ' pediu '+problema + \
            ' no(a) '+lugar+' quem vai resolver?'
        emailT = email+'@cesar.school'
        print(emailT)
        cheia = ''

        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        itembta = types.KeyboardButton('Eu vou')
        markup.add(itembta)
        bot.send_message(-1001225815995, pedido, reply_markup=markup)
        del strokes[0]
        del strokes[0]
        del strokes[0]
        bot.set_update_listener(handle_messages)
        print('sai do bot')
        time.sleep(1)
