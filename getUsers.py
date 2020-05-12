from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from models import db, Acct

def ListUsers():

    try:
        rows = db.session.query(Acct.github_name).all()
        
        # di = {}
        c = jsonify(rows)
        # c['name'] = c.pop('github_name')
        # b = json.dumps([{"name": ip[0]} for ip in rows])
        print(rows)
        # a = dict(rows)
        # a = json.dumps(a)
        # print(a)
        return jsonify(rows)

    except Exception as error:
        print(error.orig.args)
        return error.orig.args
    


    

if __name__ =="__main__":
    ListUsers()