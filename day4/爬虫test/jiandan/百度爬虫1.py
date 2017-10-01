import requests,re
from bs4 import BeautifulSoup

response=requests.get('http://www.mm131.com/xiaohua/').text
soup=BeautifulSoup(response,'html.parser',from_encoding='utf-8')
reg=r'<a target="_blank" href="(.+?)">(.+?)</a>'
reg=re.compile(reg)
