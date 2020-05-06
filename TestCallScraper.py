from flask import Flask, request, json, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2, random, os
from GitHubScraper import GetRepo as gr
from models import Acct, Skills, db


def IfExists(username):
    
    id = db.session.query(Acct.userid).filter_by(github_name=username).first()    
    exists = db.session.query(Acct, Skills).filter(Skills.userid==id).first() is not None
    if exists is True: 
        results = db.session.query(Skills.skill_name, Skills.byte_num).filter(Acct.userid==Skills.userid).all()
        results = dict(results)
        return results

    else:
        return GetTok(username, id)

def GetTok(username, id):
    result = Acct.query.filter_by(github_name=username).one()
    token = result.access_token
    return GetLang(id, token)
    
def GetLang(id, access_token):
    gi = gr(access_token)
    gi.repo_getter() # Update empty Dictionary
    gi.get_keyval() # Sum up all the respective dictionary key values
    print(gi.emp_dict) # Print final dictionary
    res = gi.emp_dict
    
    for key, value in res.items():
        np = Skills(skill_name = key, byte_num = value, userid = id)
        db.session.add(np)
    db.session.commit()

    res = json.dumps(res)
    res = json.loads(res)
    return res

if __name__ =="__main__":
    user = 'ashish'
    print(IfExists(user))