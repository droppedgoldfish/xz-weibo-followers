import requests
import random
import json
from datetime import date

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

f = open("/Users/vivzhong/xz-weibo-followers/xz_weibo_followers.txt", "a")
f.write(day+","+followers+"\n")
f.close()

print(day)
