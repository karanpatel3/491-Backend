from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from models import Acct
import os, hashlib, json

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

# customer = db.Table('customer', db.metadata, autoload=True, autoload_with=db.engine)

# Base = automap_base()
# Base.prepare(db.engine, reflect=True)
# User = Base.classes.acct_logins

class User(db.Model):
    __tablename__ = 'acct_logins'
    userid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    github_name = db.Column(db.String)
    passw = db.Column(db.String)
    email = db.Column(db.String)
    bio = db.Column(db.String)
    city = db.Column(db.String)
    occupation = db.Column(db.String)
    access_token = db.Column(db.String)


@app.route('/db')
def index():

    test = 'yes'
    useremail='foofoo'
    password = hashlib.sha256(test.encode())
    hashedpass= password.hexdigest()
    result = Acct.query.filter_by(github_name=useremail, passw=hashedpass).scalar() is not None
    print(result)

    return ''

@app.route('/reg', methods= ['POST'])
def reg():
    content = request.get_json()
    
    new_entry = Acct(github_name=content['github_userName']
                     ,email=content['email']
                     ,first_name=content['firstName']
                     ,last_name=content['lastName']
                     ,passw=(hashlib.sha256(content['password'].encode())).hexdigest()
                     ,occupation=content['occupation']
                     ,bio=content['bio']
                     ,access_token=content['token']
                     ,city=content['city'])
    db.session.add(new_entry)
    db.session.commit()
    obj = db.session.query(Acct).order_by(Acct.email.desc()).first()
    print(obj)
    return ''
if __name__ =="__main__":
    app.run(host = '0.0.0.0', port = 5000, debug=True, threaded=True)