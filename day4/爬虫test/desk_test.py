from urllib import request
from bs4 import BeautifulSoup
import os,re
#打开首页
response=request.urlopen('http://desk.zol.com.cn/meinv/')
#读取返回的html数据
html=response.read()
#解析图片集的url和title组成一个数据列表
soup=BeautifulSoup(html,'html.parser',from_encoding='gbk')
#print(soup)  获取所有的li标签及关键字参数
# (为甚么class标签要加下划线_): class作为一个类，用下划线区分

lis=soup.find_all('li',class_='photo-list-padding')
#print(lis)
info_list=[]
folder_path='F:/Game/test2/'
for li in lis:
    temp={}
    a=li.find_all("a")[0]
    img=li.find_all("img")[0]
    #href缺少域名，因此需要加上http://desk.zol.com.cn
    #域名拼接%s
    temp['url']='http://desk.zol.com.cn%s'%a['href']
    temp['title']=img['alt']
    info_list.append(temp)
    count=0
#print(len(info_list))
#循环数据表
for info in info_list:#对每一条数据的URL发送请求
    response1=request.urlopen((info['url']))
    htm=response1.read()
    #解析获取大图列表
    soup1=BeautifulSoup(htm,'html.parser',from_encoding='gbk')
    ul=soup1.find_all('ul',id='showImg')[0]
    li1=ul.find_all('li')
    temp_list=[]

    for i in li1:
            try:
                url=img['src']
            except Exception as e:
                url=img['srcs']
            temp_list.append(url)  #p = re.compile(r'\d{3}-\d{6}') print(p.findall('010-628888'))

            for i in temp_list:
                count+=1
                pan='http://desk.fd.zol-img.com.cn/t_s(.*?)c5/g5'
                out=re.sub(pan,'http://desk.fd.zol-img.com.cn/t_s1920x1200c5/g5',i)
                print(out,count)


            for item in temp_list:
                count+=1
                request.urlretrieve(item,folder_path+info['title']+str(count)+'.jpg')
                print(count)
# print("done")
    #新建文件夹
    # os.mkdir(info['title'])
    # j=1
    # for i1 in temp_list:
    #     img_data=request.urlopen(i1).read()
    #     with open('%s\\%s.jpg'%(info['title'],j),'wb') as f :
    #         f.write(img_data)
    #     j+=1





