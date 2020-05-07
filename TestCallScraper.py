from flask import Flask, request, json, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2, random, os
from github import Github, BadCredentialsException
from GitHubScraper import GetRepo as gr
from models import Acct, Skills, db


def IfExists(username):
    
    userexists = db.session.query(Acct).filter(Acct.github_name==username).scalar() is not None
    if userexists is True:

        id = db.session.query(Acct.userid).filter_by(github_name=username).one()    
        idexists = db.session.query(Acct, Skills).filter(Skills.userid==id).first() is not None
        if idexists is True: 
            results = db.session.query(Skills.skill_name, Skills.byte_num).filter(Acct.userid==Skills.userid).all()
            results = dict(results)
            return results

        else:
            return GetTok(username, id)
    else:
        return 'Invalid Username'
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


#WORK ON FUNCTION FOR VERIFYING IF GITHUB TOKEN IS VALID
def VerifyTok(access_token):
    
    if len(access_token)==40:
        
        print("Valid Length of a personal access token.")
        
        try:
            g = Github(access_token)
            user = g.get_user().get_repos()
            print(user)
            return user.name
        except BadCredentialsException as e:
            
            return e

    elif len(access_token)<40:
        return "Invalid Token. Character Count is less than minimum Token length."
    
    elif len(access_token)>40:
        return "Invalid Token. Character Count is more than minimum Token length."

if __name__ =="__main__":
    user = '51b72b49f73dcd4f1d99d93212e486ea87f8be26'
    print(VerifyTok(user))