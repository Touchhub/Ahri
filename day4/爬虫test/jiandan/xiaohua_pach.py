#spider 蜘蛛
from bs4 import BeautifulSoup
from urllib import request
import re,requests
#header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
url1=request.urlopen('http://www.xiaohuar.com/p-6-29.html').read
html=BeautifulSoup(url1,'html.parser')
ht=html.find_all('script', type='text/javascript')
count=0
reg=r'<img src=\'(.+?).jpg'
reg=re.compile(reg)
folder_path='F:/Game/test3/'
a=str(ht)
a=a.split('photosr')
b=a[2:-4]
print(b)
print(type(b))
links=[]
count=0
for i in b:
    #print(i)
    c=str(i).split("\\")[1][1:]
    c='http://www.xiaohuar.com'+c
    print(c)
    #request.urlretrieve(c,folder_path+str(count)+'.jpg')
    links.append(c)
print(links)
for link in links:
    count+=1
    request.urlretrieve(link,folder_path+str(count)+'.jpg')

# reg=r'<img src=(.+?) alt=\'马来西亚的洋娃娃美女'
# reg=re.compile(reg)
# c=re.findall(reg,b[1])
# print(c)
# # for i in b:
#     #print(i)
#     c=re.findall(reg,str(i))
#     print(c)
# print(c)
# links=[]
# for link in ht :
#     i=re.findall(reg,str(link))
#     links.append(i)
# print(type(i))
# print(links)