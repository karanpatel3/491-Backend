#USE FOR TESTING PURPOSES WITH DATABASE
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

import psycopg2

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://karanpatel:@localhost/test'

db = SQLAlchemy(app)

def my_function():
    with app.app_context():
        user = db.User(...)
        db.session.add(user)
        db.session.commit()

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    email = db.Column(db.String())
    userid = db.Column(db.Integer, primary_key = True)
    def __repr__(self):
        return '<User %r>' % self.username

class Skills(db.Model):
    __tablename__ = 'user_skills'

    skillid = db.Column(db.Integer, primary_key = True)
    skill_name = db.Column(db.String())
    byte_num = db.Column(db.String())
    userid = db.Column(db.Integer, db.ForeignKey('Users.userid'), nullable=False)

# try:
#     connection = psycopg2.connect(host="localhost",database="test", user="karanpatel", password="")
#     cur = connection.cursor()
#     connection.autocommit = True
# except:
#     print("Unable to Connect to Database")


# cur.execute("SELECT * FROM users")

# url = "qr.com/user"+str(cur.rowcount+1)

# cur.execute("UPDATE users SET url = "+url+" WHERE condition = "+(cur.rowcount+1)+"")

if __name__ =="__main__":
    forever = Users()
    print(forever)