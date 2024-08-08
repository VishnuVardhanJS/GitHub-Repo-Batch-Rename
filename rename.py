import requests
import os
from dotenv import load_dotenv
from art import *
from os import system, name

load_dotenv()

usr_name = os.getenv('GH_USERNAME')

auth_token = os.getenv("GH_TOKEN")

repo_list_url = f"https://api.github.com/users/{usr_name}/repos"

repo_list = requests.get(repo_list_url).json()

common_files = {"index.html", "style.css", "styles.html", ".gitignore", "script.js", "package.json", "package-lock.json", "README.md"}

headers = {
    'Authorization': f'token {auth_token}',
    'Content-Type': 'application/json'
}

def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def get_files(current_repo):
    file_list = []
    repo_list_url = f"https://api.github.com/repos/{usr_name}/{current_repo}/git/trees/main"
    repo_list = requests.get(repo_list_url).json()
    for i in repo_list['tree']:
        if "." in i['path'] and i["path"] not in common_files:
            file_list.append(i["path"])
    
    return file_list


try:
    for repo in repo_list:
        clear()
        tprint('\nGITHUB RENAME\n')
        print("By Vishnu Vardhan JS\n\n")

        print("(press Enter to Skip or Ctrl + c to Quit)\n")

        current_repo = repo["name"]

        print("Current Repository Name : ", current_repo, "\n")
        print("File Peek : ", end="")
        cur_files = get_files(current_repo)

        if cur_files:
            print(cur_files,"\n")
        else:
            print("No Useful Files Found!...\n")
        
        rename_name = input("Enter New Name : ")
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
except:
    print("Unable To Fetch Repositories Please Try Again Later!\n")





