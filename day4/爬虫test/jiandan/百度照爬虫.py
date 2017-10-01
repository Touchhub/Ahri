import urllib
from urllib import request
import re,time
previous='https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E7%BE%8E%E5%A5%B3&pn=20'
html=request.urlopen(previous).read()
reg=r'"objURL":"(.+?)"'
reg=re.compile(reg)
i=0
for link in re.findall(reg,str(html)):  #html=(.+?).read   html的类型需要改成str
    i+=1
    s=link.split('.')[-1]
    print('>>>正在下载第%s张图片'%i)
    print(link)
    try:
        request.urlretrieve(link,'F:\\Game\\test5\\%s.%s'%(i,s))
    except:
        continue


