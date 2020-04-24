from github import Github
import json


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
