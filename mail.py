from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime


def send_email(to,cc,bcc,subject,message):
    msg = MIMEMultipart()
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    # Login Credentials for sending the mail
    me = "user@domain.com"
    password = "<your-pass>"#Use an App Password
    server.login(me, password)
    # setup the parameters of the message
    list_recepts = [to]
    if cc != "":
        list_recepts = list_recepts + cc.split(",")

    if bcc != "":
        list_recepts = list_recepts + bcc.split(",")

    msg['From'] = me
    msg['To'] = to
    if cc != "":
        msg['Cc'] = cc
    msg['Subject'] = subject
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    # send the message via the server.
    server.sendmail(me, list_recepts, msg.as_string())
    server.quit()
        
    return print(f"successfully sent email to: {list_recepts}")


def run():
    #Vamos a enviar un mail
    to = "principalUser@gmail.com"
    cc = "user1@gmail.com,user2@gmail.com"
    bcc = "user3@gmail.com,user4@gmail.com"
    subject = "Mail para decir Hola"
    message = """Este es un mensaje de prueba.

Aqui vamos a escribir el mail que queremos enviar.

Saludos.

--
Angel Estrada
CDMX, México

Fecha de envío: {0}
Hora: {1}
"""
    dia = datetime.datetime.today().strftime("%Y-%m-%d")
    hora = datetime.datetime.today().strftime("%H:%M:%S")

    send_email(to, cc, bcc, subject, message.format(dia, hora))

if __name__ == "__main__":
    run()
