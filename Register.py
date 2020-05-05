from flask import Flask, jsonify, request, json, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2, hashlib, json, os
from models import Acct
from CallScraper import GetLang

app = Flask(__name__)
@app.route('/')
#Variables below to put into query, convert these to be POSTED later
@app.route('/register', methods=['POST'])
def Register(c):
    content = c
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    db = SQLAlchemy(app)
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
   

if __name__ =="__main__":
    # app.debug = True
    # app.run(host = '0.0.0.0', port = 5000)

    #hardcoded data to test if script works
    f = 'Ashish'
    l = 'Gare'
    a = '944a69adfc88a90271f1c5c3b47dc1d577db4c58'
    g = 'ashish'
    e = 'avg53@rutgers.edu'
    p = 'yes'
    c = 'newark'
    o =  'software'
    b = 'father'
    
    new_json = {
        'firstName' : f,
        'lastName' : l,
        'token' : a,
        'github_userName' : g,
        'email' : e,
        'password': p,
        'city' : c,
        'occupation' : o,
        'bio' : b
    }
    print(Register(new_json))