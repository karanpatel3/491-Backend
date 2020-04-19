from github import Github
import json
# import matplotlib.pyplot as plt
"""
This is the test file of the BackendTest
"""
class GetRepo:
    def __init__(self, acc_tok):
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

# plt.title('Bytes of Code in all Github Repositiries')
# plt.xlabel('Bytes ------->')
# plt.ylabel('Languages --------->')
# plt.tick_params(axis='x', colors='Blue')
# plt.tick_params(axis='y', colors='Red')
# plt.bar(range(len(obj.emp_dict)), list(obj.emp_dict.values()), align='center', color = ['Red', 'Yellow'])
# plt.xticks(range(len(obj.emp_dict)), list(obj.emp_dict.keys()))
# plt.show()
