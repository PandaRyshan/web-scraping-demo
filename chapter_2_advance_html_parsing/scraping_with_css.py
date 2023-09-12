from urllib.request import urlopen
from bs4 import BeautifulSoup

import re


host = "https://www.pythonscraping.com/"
path = "pages/page3.html"
# html = urlopen("https://www.pythonscraping.com/pages/warandpeace.html")
# bs = BeautifulSoup(html.read(), "lxml")
# name_list = bs.find_all("span", {"class": "green"})

html = urlopen(host + path)
bs = BeautifulSoup(html.read(), "lxml")

# soup = bs.find("table", {"id": "giftList"}).descendants
# notice the diff between from .children vs .descendants
# for child in soup:
#     print(child)

# find all gifts img
rs = bs.find_all("img", {"src": re.compile(r'/img/gifts/img*')})
for img in rs:
    print(img["src"].replace("../", host))

# find table's tr
print(bs.find("table", {"id": "giftList"}).tr)

# find siblings
print()
