from github import Github
import json
import matplotlib.pyplot as plt
"""
This program uses OOP to get users repositiories and gives the total number of bytes of each languages 
"""
class GetRepo:
    
   
    
    def __init__(self):
        acc_tok = input("Enter Your Access Token: ")
        self.g = Github("{}". format(acc_tok))
        self.emp_dict = {}

    def repo_getter(self):
              
        for rep in self.g.get_user().get_repos():
    
            try:
                dict_data = rep.get_languages()
                self.emp_dict.update(dict_data)
            
            except Exception as e: 
                print(e) 
                
    def get_keyval(self):
        
        for repo in self.g.get_user().get_repos():

            data = repo.get_languages() #placeholder for for dict  
            
            for key in data:     #Iterating through the dict to print individual values

                
                value = data[key] #value being set to get the value of key
                self.emp_dict[key] = self.emp_dict[key] + value  

obj = GetRepo()

obj.repo_getter() # Update empty Dictionary

obj.get_keyval() # Sum up all the respective dictionary key values
print(obj.emp_dict) # Print final dictionary

 #Plotting the graph on matplotlib
plt.xlabel('Bytes')
plt.ylabel('Languages')
plt.bar(range(len(obj.emp_dict)), list(obj.emp_dict.values()), align='center', color = ['Red', 'Blue'])
plt.xticks(range(len(obj.emp_dict)), list(obj.emp_dict.keys()))

# graph_name = input("Enter Graph Name: ")
# plt.savefig('{}.png'.format(graph_name))

plt.show()
               
    





       



 
