#! /usr/bin/python3
import sys, os, time, subprocess
from github import Github

token = os.environ['GitHubAuthKey']
def CIFolder(project):
    platform = sys.platform
    if 'lin' in platform:
        print("Linux")
        subprocess.call(['mkdir', project])
        os.chdir(project)
        subprocess.run([f'echo "# {project}" >> README.md'],shell=True)
        subprocess.run(['git init'],shell=True)
        subprocess.run(['git add .'],shell=True)
        subprocess.run(['git commit -m "Initial Commit"'],shell=True)
        subprocess.run(['git branch -M master'],shell=True)
        
    elif 'win' in platform:
        print('Windows')
        subprocess.call(['mkdir', project])
        os.chdir(project)
        subprocess.run([f'echo "# {project}" >> README.md'],shell=True)
        subprocess.run(['git init'],shell=True)
        subprocess.run(['git add .'],shell=True)
        subprocess.run(['git commit -m "Initial Commit"'],shell=True)
        subprocess.run(['git branch -M master'],shell=True)


def InitGit(project):
    g = Github(token)
    repo = g.get_user().create_repo(project)
    print(repo.ssh_url)
    subprocess.run([f'git remote add origin {repo.ssh_url}'], shell=True)
    subprocess.run([f'git push -u origin master'], shell=True)


project_name = sys.argv[1]
CIFolder(project_name)
InitGit(project_name)


print("\n---------------\nDoneeeee")
