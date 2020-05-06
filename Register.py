from flask import Flask, jsonify, request, json, jsonify
import psycopg2, hashlib, json, os
from CallScraper import GetLang
from models import Acct, Skills, db


app = Flask(__name__)
@app.route('/')
#Variables below to put into query, convert these to be POSTED later
@app.route('/register')
def Register(c):
    content = c
    content = request.get_json()
    try:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
        
    except:
        print ("I am unable to connect to the database.")
    
    try:
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
        return 'User added'

    except:
        print ("I am unable to connect to the database.")
        return 'Registration failed, please speak to admin'
   

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