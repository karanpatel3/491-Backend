from flask import Flask, jsonify, request, json, jsonify
import json, os
from models import Acct, db

def UpEmail(c):
    content = c
    gituser = content['userName']
    email = content['email']

    try:
        user = Acct.query.filter_by(username=gituser).one()
        user.email = email
        db.session.commit()
        result = 'true'
        message = "Your email has been updated to: "+ email +"."
        return message

    except Exception as error:
        print(error.orig.args)
        return error.orig.args