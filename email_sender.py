import smtplib
from socket import gaierror
from dotenv import load_dotenv
import os
load_dotenv()
port = os.getenv("port")
smtp_server = os.getenv("host")
login = os.getenv("username")
password = os.getenv("password")
sender = os.getenv("sender")
receiver = os.getenv("reciever")


def send(val):
    message = f"""\
    Subject: Hi USer
    To: {receiver}
    From: {sender}

    The BTC value has crossed the threshold value.
    Value: {val}

    """
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.login(login, password)
            server.sendmail(sender, receiver, message)
    except (gaierror, ConnectionRefusedError) as e:
        print('Failed to connect to the server. Bad connection settings?', e)
    except smtplib.SMTPServerDisconnected as e:
        print('Failed to connect to the server. Wrong user/password?', e)
    except smtplib.SMTPException as e:
        print('SMTP error occurred: ' + str(e))
