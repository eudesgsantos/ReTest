from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, jsonify
from pingsite import app, db, bcrypt
from pingsite.models import models
from pingsite.Forms import Lugarform
from pingsite.Forms import Loginform
from pingsite import Forms
from pingsite.models.models import Report
import telebot
import logging
import smtplib
import ssl
import _thread
from pingsite import app
from telebot import types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json

canudo = []
lista_suprema = [
'at',
'avca',
'akw',
'ayms',
'arc3',
'bsm',
'bbbgc',
'cvjso',
'cba',
'csef',
'crsm',
'drnb',
'dsa',
'dnio',
'damo',
'eemb',
'esv',
'earo',
'emfd',
'eljs',
'eess',
'fwsp',
'gsmf',
'gnp2',
'gm',
'gtb',
'hsag',
'hbf',
'hrs',
'hss',
'jcsc',
'jfcd',
'jmsda',
'jp',
'jvdc',
'jvmc',
'jvmls',
'jvca',
'jsaa',
'jcrm',
'kbcv',
'kms',
'lvco',
'lms',
'lcf',
'lfv',
'lfps',
'lml',
'lns',
'lns2',
'lra2',
'lat',
'ltf',
'ladccc',
'lfmm',
'lmbc',
'mcs',
'mlaj',
'mjsv',
'miam',
'mlml',
'mabr',
'mda',
'mcfv',
'mcla',
'msn',
'mvn',
'nbvs',
'ofn',
'phmt',
'phbbp',
'phsv',
'pqla',
'pbv',
'rdr',
'tmo',
'vrss',
'vrgf',
'wfl',
'fsf'
]

@app.route("/", methods=['GET','POST'])
def home():
    form = Lugarform()
    if request.method =="POST" and form.validate():
        place = form.lugarF.data
        problem = form.problemas.data
        extr = form.extra.data
        realprob = problem+extr
        confi02 = 1
        return redirect(url_for('login',place=place,realprob=realprob))
    return render_template('tela1.html',form=form)

@app.route("/VerifiqueSeuEmail")
def final():
    return render_template('tela3.html')

@app.route("/login", methods=['GET','POST'])
def login():
    form = Loginform()
    place = request.args['place']
    realprob = request.args['realprob']
    if request.method =="POST" and form.validate():
        nom = form.nomeF.data
        escol = form.hole.data
        ema = nom + escol
        confi01 = 1
        xez = 0
        DEBUG = False
        """if(not DEBUG):
            import serial
            Arduinoserial = serial.Serial('COM14')
        """
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
                sup = name[1].replace("'","")
                chama = kin[-2].split(': ')
                nenem = chama[1].replace("'","")
                nenem = nenem.replace(' quem vai resolver?}', '')
                nenem = nenem.replace('"', '')
                nenem = nenem.replace('}', '')
                cheia = sup
                lun = nenem.replace(indv,'')
                lun = lun.replace(' pediu ','')
                if mens[1] == "'Eu vou'}}" and nenem in formA:
                    formA.remove(nenem)
                    pedsup = sup + " vai resolver o chamado do(a) "+ lun
                    formB.append(pedsup)
                    number = 2
                    enviarEmail()
                    bot.send_message(-1001225815995, pedsup)
                if mens[1] == "'Feito'}}" and nenem in formB:
                    lun = lun.replace(sup,'')
                    lun = lun.replace(' vai resolver o chamado do(a) ','')
                    formB.remove(nenem)
                    relsup ="{} resolveu {}!".format(sup,lun)
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

        strokes = []
        formA = []
        formB = []
        _thread.start_new_thread(fazPoll, ())

        while xez == 0:
            if confi01 == 1 :
                strokes.append(ema)
                strokes.append(realprob)
                strokes.append(place)
                print('entrou')
            """else:
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
        """
            if len(strokes) >= 3:
                timestamp = datetime.now()
                tempo = timestamp.strftime('%Y-%m-%d %H:%M:%S')
                crac = strokes[0]
                lala = str(strokes[1])
                lulu = str(strokes[2])
                problema = ' '+lala
                identity = crac
                serial = problema
                data = {}
                subindice = serial + ', ' + tempo
                with open('./pingsite/controllers/data_file.json', 'r') as read_file:
                    print(read_file)
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
                if '29 0 ' not in crac:
                    d = {}
                    with open('Nomes.json', 'r+') as f:
                        data = json.load(f)

                    if crac in data:
                        print(data[crac])

                    else:
                        print('Este e-mail não está registrado')

                    username = data[crac]
                if crac in dicA:
                    email = dicA[crac]
                    indv = dicB[crac]
                else:
                    email = strokes[0]
                lugar = lulu
                respo = problema + ' no(a) ' + lugar
                if '@cesar' not in email:
                    emailT = email+'@cesar.school'
                else:
                    emailT = email
                cheia = ''
                ticket = indv + ' pediu ' + problema + ' no(a) '+ lugar
                formA.append(ticket)
                pedido = ticket + ' quem vai resolver?'
                bot.send_message(-1001225815995, pedido)
                del strokes[0]
                del strokes[0]
                del strokes[0]
                xez = 1
        bot.set_update_listener(handle_messages)
        if nom in lista_suprema:
            return redirect(url_for('final'))
        
    return render_template('login.html',form=form)
