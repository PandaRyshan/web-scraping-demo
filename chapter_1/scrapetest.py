# coding=utf-8
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:
    print("It Worked!")

#bs = BeautifulSoup(html.read(), 'html.parser')
bs = BeautifulSoup(html.read(), 'lxml')
#print(html.read())
try:
    badContent = bs.h2
except AttributeError as e:
    print("Tag was not found")
else:
    if badContent is None:
        print("Tag was not found")
    print(badContent)
