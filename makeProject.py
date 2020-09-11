#!/usr/bin/python
import sys
import os
import time
import subprocess
import shutil
from github import Github

import secret as s

token = s.GITHUB_KEY
WindowsLocation = s.WINDOWS_LOCATION
LinuxLocation = s.LINUX_LOCATION
MacLocation = s.MAC_LOCATION
globalgitignore = s.GITIGNORE


def CIFolder(project):
    platform = sys.platform
    if 'lin' in platform:
        print("Linux")
        subprocess.call(['mkdir', project])
        os.chdir(project)
        subprocess.run([f'echo "# {project}" >> README.md'], shell=True)
        subprocess.run(['git init'], shell=True)
        subprocess.run(['git add .'], shell=True)
        subprocess.run(['git commit -m "Initial Commit"'], shell=True)
        subprocess.run(['git branch -M master'], shell=True)

    elif 'win' in platform:
        if not os.path.exists(f'{WindowsLocation}\\{project}'):
            os.chdir(WindowsLocation)
            subprocess.run(['mkdir', project], shell=True)
            os.chdir(project)
            with open('README.md', 'w') as f:
                f.write(f'# {project}')
            with open(".gitignore", "w") as f1:
                for line in globalgitignore:
                    f1.write(line)
            subprocess.run(['git', 'init'])
            subprocess.run(['git', 'add', '.'])
            subprocess.run(['git', 'commit', '-m', '"Initial Commit"'])
            subprocess.run(['git', 'branch', '-M', 'master'])
            subprocess.run(['code', '.'], shell=True)
        else:
            print("Folder already exists")


def InitGit(project):
    g = Github(token)
    user = g.get_user()
    repo = user.create_repo(project)
    subprocess.run(['git', 'remote', 'add', 'origin', repo.ssh_url], shell=True)

    subprocess.run(['git', 'push', 'origin', 'master'], shell=True)


if len(sys.argv) < 2:
    print("No arguements given, please add a project name after the execution string")
else:
    project_name = sys.argv[1]
    if not os.path.exists(f'{WindowsLocation}\\{project_name}'):
        CIFolder(project_name)
        InitGit(project_name)
        if len(sys.argv) >= 3:
            if sys.argv[2]:
                g = Github(token)
                user = g.get_user()
                repo = user.get_repo(project_name)
                repo.delete()
                projectdir = os.getcwd()
                os.chdir('..')
                subprocess.call(['rmdir', '/Q', '/S', projectdir], shell=True)
            else:
                print("weird selection. I'm doing nothing.")
    else:
        print("Project Might already exist")
