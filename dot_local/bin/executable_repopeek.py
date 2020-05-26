from colorama import Fore, Back, Style
from colorama import init
import requests
import git
import re
import os

init(autoreset=True)

print(Fore.CYAN +  r'''


__________                    __________               __    
\______   \ ____ ______   ____\______   \ ____   ____ |  | __
 |       _// __ \\____ \ /  _ \|     ___// __ \_/ __ \|  |/ /
 |    |   \  ___/|  |_> >  <_> )    |   \  ___/\  ___/|    < 
 |____|_  /\___  >   __/ \____/|____|    \___  >\___  >__|_ \
        \/     \/|__|                        \/     \/     \/
                                        [by Sameera Madushan]

''')

try:
    get_repo = input("Enter the repository URL: ")

    x = re.match(r'^(https:|)[/][/]([^/]+[.])*github.com', get_repo)

    if x:
        # got this from https://serverfault.com/a/917253
        extract  = re.match(r'^(https|git)(:\/\/|@)([^\/:]+)[\/:]([^\/:]+)\/(.+)(.git)?$', get_repo)
        organization = extract.group(4)
        repo = extract.group(5).strip(".git")

        url = 'https://api.github.com/repos/{0}/{1}'.format(organization, repo)
        check_exist = requests.get(url).json()
        
        for i,v in check_exist.items():
            if v == 'Not Found':
                print(Fore.RED + "Oops!! Repository not found. ")
                print(Style.RESET_ALL)
                quit()
            else:
                pass

        repo_name = check_exist['name']
        description = check_exist['description']
        forks = check_exist['forks']
        open_issues = check_exist['open_issues']
        watchers = check_exist['watchers']
        default_branch = check_exist['default_branch']
        git_url = check_exist['git_url']
        ssh_url = check_exist['ssh_url']
        clone_url = check_exist['clone_url']
        svn_url = check_exist['svn_url']
        repo_size = check_exist['size']
        stargazers_count = check_exist['stargazers_count']
        language = check_exist['languages_url']

        def license():
            for k, v in check_exist['license'].items():
                if k == 'name':
                    return v

        def languages():
            list = []
            req = requests.get(language).json()
            for i in req:
                list.append(i)
            return list

        def convert(size):
            while True:
                megabytes = size / 1000
                if size < 1000:
                    return str(size) + " KB"
                if megabytes > 1000:
                    gigabyte = megabytes / 1000
                    return str(gigabyte) + " GB"
                else:
                    return str(megabytes) + " MB"
                    
        
        print(Fore.YELLOW + "\n[x] Basic information about the repository [x]")
        print(Fore.YELLOW + "-----------------------------------------------")
        print("Repository Name: " + repo_name)
        print("Default Branch: " + default_branch)
        print("Repository Size: " + convert(size=repo_size))
        print("Repository License: " + license())
        print("Repository Description: " + description)

        print(Fore.YELLOW + "\n[x] Languages used in the repository [x]")
        print(Fore.YELLOW + "-----------------------------------------------")
        print(*languages(), sep=', ')

        print(Fore.YELLOW + "\n[x] Repository Statistics [x]")
        print(Fore.YELLOW + "-----------------------------------------------")
        print("Forks: " + str(forks))
        print("Watchers: " + str(watchers))
        print("Open Issues: " + str(open_issues))
        print("Total Stars: " + str(stargazers_count))

        print(Fore.YELLOW + "\n[x] URls of the repository [x]")
        print(Fore.YELLOW + "-----------------------------------------------")
        print("GIT URl: " + Fore.BLUE + git_url)
        print("SSH URL: " + Fore.BLUE + ssh_url)
        print("SVN URL: " + Fore.BLUE + svn_url)
        print("Clone URL: " + Fore.BLUE + clone_url)

        user_input = input("\nWould you like to clone this repository (y/n): ").lower()
        if user_input == 'y':
            print("Cloning...")
            git.Git(os.getcwd()).clone(get_repo)
            print("Done.")
        else:
            quit()
    else:
        print("Error")
except KeyboardInterrupt:
    print("\nKeyboard Interrupted")
