import re,time
from urllib import request
html=request.urlopen('http://www.mm131.com/xiaohua/list_2_2.html').read().decode('gb2312')
reg=r'<a target="_blank" href="(.+?)">(.+?)</a>'
reg=re.compile(reg)
ht=re.findall(reg,str(html))
folder_path='F:/Game/test2/'
#print(ht)

links=[]
a=0
for i in ht:
    if 'xiaohua' in i[0]:
        a+=1
        links.append(i[0])
        #print(i[0],i[1])
links=set(links)
#print(links)
n=0
for link in links:
    html_link=request.urlopen(link).read().decode('gbk')
    #print(html_link)
    reg2=r'href=(.+? )class="page-en">(.+)'
    reg2=re.compile(reg2)
    lin=re.findall(reg2,str(html_link))
    a=(lin[0][1].split('h'))
    b=(lin[0][0].split('_'))
    #print(lin)
    #print(lin[0][0])
    b[0]=b[0][1:]
    print(b[0])
    a=(len(a)/2)
    for i in range(1,int(a)+1):
        n+=1
        print(i)
        down_links='http://img1.mm131.com/pic/%s/%s.jpg'%(str(b[0]),str(i))
        print(down_links)
        request.urlretrieve(down_links,folder_path+str(n)+'.jpg' )
    #print((link1[0][1]))