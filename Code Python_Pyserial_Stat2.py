import serial
import time
import smtplib, ssl
ArduinoSerial = serial.Serial('COM3')
time.sleep(2)

def enviarEmail():
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    port = 465
    password = 'arduinopython'
    sender_email = 'retestping@gmail.com'
    receiver_email = 'drnb@cesar.school'

    message = MIMEMultipart("alternative")
    message["Subject"] = "FeedBack Ping"
    message ["From"] = sender_email
    message ["To"] = receiver_email
    text = """\
    Seu Mario esta indo resolver seu problema,acompanhe seu email para saber mais informações do andamento do problema

    """
    html = """\
    <html>
        <body>
            <p>Seu Mario esta indo resolver seu problema, acompanhe seu email para saber mais informações do andamento do problema


            </p>
        
        </body>
    </html>

    """
    part1 = MIMEText(text,"plain")
    part2 = MIMEText(html,"html")
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
        server.login('retestping@gmail.com', password)
        server.sendmail(sender_email, receiver_email, message.as_string())

while True:
    res = ArduinoSerial.readline().decode('ascii')
    print(res)
    if 'YES' in res:
        enviarEmail()
        break
