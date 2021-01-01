from threading import Thread
from flask_mail import Message, Mail


def send_async_email(app, msg):
    with app.app_context():
        try:
            mail = Mail(app)
            mail.send(msg)
            return {"message": "sent", "status": 204}
        except ConnectionRefusedError:
            return {"message": "[MAIL SERVER] not working", "status": 403}


def send_email(subject, sender, recipients, text_body, html_body):
    from api import app
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.body = html_body
    Thread(target=send_async_email, args=(app, msg)).start()
