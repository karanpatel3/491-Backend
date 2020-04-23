from flask import Flask, request, json
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from GitHubScraper import GetRepo as gr

def GetLang(access_token):
    
    #POST GET THE ACCESS TOKEN OF USER
    
    access_token = "XXXX" #REPLACE WITH ACCESS TOKEN WHEN TESTING LOCALLY
    gi = gr(access_token)
    gi.repo_getter() # Update empty Dictionary
    gi.get_keyval() # Sum up all the respective dictionary key values
    print(gi.emp_dict) # Print final dictionary
    test = gi.emp_dict
    print(test['Swift'])
    languages=""
    byte_num=""
    
    #send access token to github scraper and get output, dictionary variable equal to output

    #tablename = USERNAME OF USER
    #CREATE TABLE (WITH THE USERNAME OF THE USER) (languages, bytes)
    tablename = input()
   
    sql = ""
    sql += "CREATE TABLE "
    sql += "" + tablename + ""
    sql += " ("
    sql += "languages varchar(255)"
    sql += ", bytes int"
    sql += ")"

    try:
        connection = psycopg2.connect(host="localhost",database="test", user="karanpatel", password="")
        cur = connection.cursor()
        connection.autocommit = True
    except:
        print("Unable to Connect to Database")
   
    try:
        cur.execute(sql)   
    except psycopg2.Error as e:
        message = "Database error: " + e + "/n SQL: " + sql
        result = 'false'
        cur.close()
        return result
    
    sql = "INSERT INTO "
    sql += " '" + tablename + "'"
    sql += "("
    sql += "  languages"
    sql += ") VALUES ("
    sql += " '" + languages + "'"
    sql += ",'" + byte_num + "'"
    sql += ")"
    

    for key in test.keys():
        val = test[key]
        sql = "INSERT INTO "+tablename+" (languages, bytes ) VALUES ('"+key+"', "+str(val)+");"
        cur.execute(sql)



    return 'IT WORKED'
    

if __name__ =="__main__":
    access_token = "b203a017f509cd3693a466e398b2ffcb193ea0ed"
    print(GetLang(access_token))
