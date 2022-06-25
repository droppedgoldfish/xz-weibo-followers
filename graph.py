import pandas as pd
import matplotlib.pyplot as plt
import datetime

url = "https://raw.githubusercontent.com/droppedgoldfish/xz-weibo-followers/main/xz_weibo_followers.txt"
df = pd.read_csv(url)

x = df["Date (YYYY-MM-DD)"]
y = df["Followers (tens of thousands)"]

x = [datetime.datetime.strptime(d, '%Y-%m-%d').date() for d in x]

plt.rcdefaults()
fig, ax = plt.subplots(1, figsize=(7,5))
ax.plot(x, y, marker='o', color="#911005")
ax.ticklabel_format(axis="y", useOffset=False)
ax.set_ylabel("Followers (tens of thousands)", size=12)
ax.set_xlabel("Date (YYYY-MM-DD)", size=12)
plt.xticks(rotation=90, size=8)
plt.yticks(size=8)
plt.title("Xiao Zhan's Weibo Followers (Recent)", size=15)
plt.show()
