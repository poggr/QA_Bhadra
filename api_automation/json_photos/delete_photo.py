import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)

print(response.json())
print(response.status_code)

assert response.status_code== 200, "request status code in not 200"
print("request successfully")

#  git config --global user.name "poggr"
#  git config --global user.email "bidushirai002@gmail.com"
# git config --list

'''
…or create a new repository on the command line
echo "# QA_Bhadra" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/poggr/QA_Bhadra.git
git push -u origin main

…or push an existing repository from the command line
git remote add origin https://github.com/poggr/QA_Bhadra.git
git branch -M main
git push -u origin main

git add . (note: for all)

git commit -m "fix: Api automatiom"

git commit -m "feat: new updat"    
'''