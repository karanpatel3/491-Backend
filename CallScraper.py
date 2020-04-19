from flask import Flask, jsonify, request, json
import psycopg2

from GitHubScraper import GetRepo as gr

# import GitHubScraper
import os 
# os.system('GitHubScraper.py')

def GetLang(self):
	# b203a017f509cd3693a466e398b2ffcb193ea0ed - jorge acc_tok
    #POST GET THE USERNAME OF USER
    access_token = "b203a017f509cd3693a466e398b2ffcb193ea0ed"
    # diction = gr.__init__(access_token)
    # diction2 = gr.repo_getter(access_token)
    # diction3 = gr.get_keyval(access_token)
    # print('This is diction: ' + diction)
    # print('This is diction2: ' + diction2)
    # print('This is diction3: ' + diction3)
    languages=""
    byte_num=""
    
    #send access token to github scraper and get output, dictionary variable equal to output
    dictionary = obj.emp_dict
    print(dictionary)
    #dictionary = result from scraper
    #tablename = USERNAME OF USER
    #CREATE TABLE (WITH THE USERNAME OF THE USER) (languages, bytes)
    tablename = ""
   
    sql = ""
    sql += "CREATE TABLE "
    sql += "'" + tablename + "'"
    sql += " ("
    sql += "languages"
    sql += ", bytes"
    sql += " )"

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
    
    for mydict in diction3:
        placeholders = ', '.join(['%s'] * len(mydict))
        columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in mydict.keys())
        values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('mytable', columns, values)
        cur.execute(sql)   


	#for i in n.length:
		#”INSERT INTO [NEW TABLE] (languages, bytes) 

#After the dictionary is inserted, return the languages and bytes to the front as a json

    return jsonify(dictionary)

if __name__ =="__main__":
    self.GetLang()
    #GetLang()
