import requests

import os
from dotenv import load_dotenv
from art import *

load_dotenv()

usr_name = os.getenv('GH_USERNAME')

auth_token = os.getenv("GH_TOKEN")

repo_list_url = f"https://api.github.com/users/{usr_name}/repos"

repo_list = requests.get(repo_list_url).json()

headers = {
    'Authorization': f'token {auth_token}',
    'Content-Type': 'application/json'
}

tprint('\nGITHUB RENAME\n')
print("By Vishnu Vardhan JS")
print('\n\n')

for repo in repo_list:
    current_repo = repo["name"]
    print("Current_Repo : ", current_repo)
    rename_name = input("Enter New Name (press Enter to Skip) : ")
    if rename_name == "":
        continue
    else:
        data = {'name': rename_name}
        url = f'https://api.github.com/repos/{usr_name}/{current_repo}'
        rename_patch = requests.patch(url, headers=headers, json=data)
        if rename_patch.status_code==200:
            print(f"{current_repo} Rename to {rename_name} Successful!...")
        else:
            print(f"{current_repo} Rename to {rename_name} Failed!...")




