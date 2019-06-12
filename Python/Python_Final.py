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

DEBUG = True

if(not DEBUG):
    Arduinoserial = serial.Serial('COM14')
bot = telebot.TeleBot('830353241:AAE3P5ciHJf_VmGflxJw7kCWiJ3r8EAxGxY', threaded=True)

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
        chama = kin[-2].split(': ')
        nenem = chama[1].replace("'","")
        nenem = nenem.replace(' quem vai resolver?}', '')
        print(nenem)
        cheia = sup
        if mens[1] == "'Eu vou'}}" and nenem in form:
            lun = nenem.replace(indv,'')
            lun = lun.replace(' pediu ','')
            pedsup = sup + " vai resolver o chamado do(a) "+ lun
            number = 2
            enviarEmail()
            bot.send_message(-1001225815995, pedsup)
            form.remove(nenem)
        if mens[1] == "'Feito'}}":
            relsup = sup + " resolveu o problema!"
            number = 1
            bot.send_message(-1001225815995, relsup)
            enviarEmail()


def fazPoll():
    bot.polling()


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
form = []
_thread.start_new_thread(fazPoll, ())

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
    if len(strokes) >= 3:
        timestamp = datetime.now()
        tempo = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        crac = strokes[0]
        problema = strokes[1]+' '+strokes[2]
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
        indv = 'Usuario'
        if crac in dicA:
            email = dicA[crac]
            indv = dicB[crac]
        else:
            email = 'kkk'
        lugar = 'Auditório'
        respo = problema + ' no(a) ' + lugar
        emailT = email+'@cesar.school'
        cheia = ''
        ticket = indv + ' pediu ' + problema + ' no(a) '+ lugar
        print(ticket)
        form.append(ticket)
        print(form)
        pedido = ticket + ' quem vai resolver?'
        bot.send_message(-1001225815995, pedido)
        del strokes[0]
        del strokes[0]
        del strokes[0]
        bot.set_update_listener(handle_messages)
