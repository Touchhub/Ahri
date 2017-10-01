#最终储存的数据
from bs4 import BeautifulSoup
import requests
#header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
response=requests.get('http://www.xiaohuar.com/p-1-122.html')
#print(req.cookies)
html=response.text
#print(html)
soup=BeautifulSoup(html,'html.parser')
data=soup.find_all('li',class_='photoli')
print(type(data))
links=[]
for line in data:
    img=line.img.attrs['src']
    alt=line.img.attrs['alt']
    link='http://www.xiaohuar.com'+img
    print(img,alt,link)
    links.append(link)
count=0
print(links)
count=0
for link in links:
    count+=1
    img_data=requests.get(link).content #content  以二进制的方式(content而非text)保存图片源地址内容
    with open('F:\\Game\\test3\\%s.jpg'%count,'wb') as f :
        f.write(img_data) # 写入二进制内容
print("done")
#






