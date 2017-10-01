from bs4 import BeautifulSoup
from urllib import request
import re,requests
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
url1=requests.get('http://www.xiaohuar.com/p-6-29.html',headers=header)
#url1=request.urlopen('http://www.xiaohuar.com/p-6-29.html')
htm1=url1.text
#print(htm1)
soup1=BeautifulSoup(htm1,'html.parser')
print(soup1)
lis1=soup1.find_all('img')
print(type(lis1))
src_link=[]
folder_path='F:/Game/test3/'
for i in lis1:
    print(i)
    print(type(i))
    srcs=i.get('src')
    print(type(srcs))
    srcs='http://www.xiaohuar.com%s'%srcs
    srcs=srcs.replace('small','')
    replace=re.findall('144\d+',srcs)
    replace=''.join(replace)
    srcs=srcs.replace(replace,'')
    print(srcs)
    break
    #srcs=srcs.replace(replace,'')
    #print(srcs)
    #t_s(.*?)c5
    #srcs=srcs.replace('144/d+','')
    src_link.append(srcs)
#print(src_link)
