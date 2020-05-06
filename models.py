from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from app import app
import os, hashlib

with current_app.app_context():
    db = SQLAlchemy(app)

class Acct(db.Model):
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

class Users(db.Model):
    __tablename__ = 'users'
    userid = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

class Skills(db.Model):
    __tablename__ = 'user_skills'
    skillid = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String)
    byte_num = db.Column(db.Integer)
    userid = db.Column(db.Integer, db.ForeignKey('users.userid'))
