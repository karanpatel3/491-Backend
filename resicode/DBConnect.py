import psycopg2, json
from GitHubScraper import GetRepo as gr

try:
    connection = psycopg2.connect(host="localhost",database="test", user="karanpatel", password="")
    cur = connection.cursor()
    connection.autocommit = True
except:
    print("Unable to Connect to Database")


gi = gr('944a69adfc88a90271f1c5c3b47dc1d577db4c58')
gi.repo_getter() # Update empty Dictionary
gi.get_keyval() # Sum up all the respective dictionary key values
print(gi.emp_dict) # Print final dictionary
test = gi.emp_dict
test = json.dumps(test)
test = json.loads(test)
print(test)
cur.execute("INSERT INTO user_skills (languages) VALUES ('"+str(test)+"')")