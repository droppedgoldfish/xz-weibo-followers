import requests
import random
import json
from datetime import date
from github import Github

github_access_token = "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"

REPO_NAME = 'xz-weibo-followers'


github = Github(github_access_token)

def get_repos():
    for repo in github.get_user().get_repos():
        print(repo.name)


def get_file(filename):
    repository = github.get_user().get_repo(REPO_NAME)
    file = repository.get_contents(filename)

    print(file.url)

    return file

def put_file(filename, content):

    repository = github.get_user().get_repo(REPO_NAME)

    if check_file_exist(filename):
        print(f'update_file {filename}')
        f = get_file(filename)
        f = repository.update_file(filename, "update_file via PyGithub", content, f.sha)
    else:
        print(f'create_file {filename}')
        f = repository.create_file(filename, "create_file via PyGithub", content)

def check_file_exist(filename):
    try:
        file = get_file(filename)
    except:
        return False

    return True

def get_user(name):
    user = github.get_user(name)
    return user


actual_url = "https://m.weibo.cn/api/container/getIndex?type=uid&value="+str(1792951112)
res = requests.get(actual_url).text

if not res:
  print("抓取完成...")
try:
  res_json = json.loads(res)
  # 读取微博账号的粉丝数
  followers = res_json["data"]["userInfo"]["followers_count_str"][:-1]
  print(followers)
except Exception:
  print("抓取数据格式异常！！！")

today = date.today()
day = today.strftime("%Y-%m-%d")


with open("xz_weibo_followers.txt", "a") as g:
    g.write(day+","+followers+"\n")
    content = g.read()

put_file("xz_weibo_followers.txt", content)

print(day)
