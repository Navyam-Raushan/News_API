import smtplib
import ssl
import os


def send_gmail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "bsarthak935@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "bsarthak935@gmail.com"
    # receiver = "jullykumari112@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)




