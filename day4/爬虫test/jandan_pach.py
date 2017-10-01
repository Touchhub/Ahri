import requests,urllib.request
from bs4 import BeautifulSoup
count=0
for ci in range(10,60):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    source_code=requests.get('http://jandan.net/ooxx/page-%s'%ci ,headers=header)
#print(source_code)
    plain_test=source_code.text
#print(plain_test)
    Soup=BeautifulSoup(plain_test,"lxml")
#print(Soup)
    download_link=[]
    folder_path='F:/Game/test/'
    for pic_tag in Soup.find_all('img'):
        pic_link='http:'+pic_tag.get('src')
        print(pic_link)
        download_link.append(pic_link)
        print(count)
    print('done')
#print(download_link)

    for item in download_link:
        count+=1
        urllib.request.urlretrieve(item,folder_path+item[-10:])
        print(count)
print("done")