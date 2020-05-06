from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from models import Acct, Users, Skills, db, app
import os, hashlib, json
from GitHubScraper import GetRepo as gr

@app.route('/db')
def login():

    test = 'yes'
    useremail='foofoo'
    password = hashlib.sha256(test.encode())
    hashedpass= password.hexdigest()
    result = Acct.query.filter_by(github_name=useremail, passw=hashedpass).scalar() is not None
    print(result)

    return result

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

#FOR CALLSCRAPER
@app.route('/scrape', methods= ['GET', 'POST'])
def scrape():

    username='josue'

#If languages exist
#ADD PART WHERE YOU NEED TO INTEGRATE THE USERNAME FOR CHECKING IF IT EXISTS
    id = db.session.query(Acct.userid).filter_by(github_name=username).one()    
    exists = db.session.query(Acct, Skills).filter(Skills.userid==id).first() is not None
    if exists is True:
        results = db.session.query(Skills.skill_name, Skills.byte_num).filter(Acct.userid==Skills.userid).all()
        results = [r._asdict() for r in results]
        return str(results)

#   FOR GETTING TOKEN
#****************************************************************    
    else:
        result = Acct.query.filter_by(github_name=username).one()
        token = result.access_token
        print(token)
    # return token
#   FOR GETTING LANGUAGES AND PUTTING THEM INSIDE USER_SKILLS TABLE
#********************************************************************
    gi = gr(token)
    gi.repo_getter() # Update empty Dictionary
    gi.get_keyval() # Sum up all the respective dictionary key values
    print(gi.emp_dict) # Print final dictionary
    res = gi.emp_dict

    id = result.userid

    for key, value in res.items():
        np = Skills(skill_name = key, byte_num = value, userid = id)
        db.session.add(np)
    db.session.commit()

    
    return "<h1>IT WORKED</h1>"

if __name__ =="__main__":
    app.run(host = '0.0.0.0', port = 5000, debug=True, threaded=True)