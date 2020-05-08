from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_mail import Mail, Message
# from models import app
app = Flask(__name__)
with app.app_context():
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = 'resicode@gmail.com'
    app.config['MAIL_PASSWORD'] = 'Resicode96!'

    mail = Mail(app)

    def sendemail(name, email):

        msg = Message("OMG GUESS WHAT??!?!?!??!?!?!"+name+"",
                    sender="resicode@gmail.com",
                    recipients=[email])

        msg.body = "IT'S WORKING \n -K "
        mail.send(msg)


    if __name__ =="__main__":
        name = "Dayanna"
        email = 'dym17@rutgers.edu'
        sendemail(name, email)