from bs4 import BeautifulSoup
from urllib import request
import re
for page in range(40,58):
    url1=request.urlopen('http://www.521609.com/daxuexiaohua/list3%s.html'%page)
    htm1=url1.read()
    soup1=BeautifulSoup(htm1,'html.parser',from_encoding='gbk')
    #print(soup1)
    lis1=soup1.find_all('img')
    src_link=[]
    folder_path='F:/Game/test3/'
    for i in lis1:
        srcs=i.get('src')
        srcs='http://www.521609.com%s'%srcs
        srcs=srcs.replace('-lp','')
        src_link.append(srcs)
    #print(src_link)
    count=0
    for down in src_link:
        count+=1
        request.urlretrieve(down,folder_path+str(page)+str(count)+'.jpg')
        print(count)
    print('done')

