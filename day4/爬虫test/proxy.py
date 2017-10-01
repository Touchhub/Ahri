import  requests
def GETHTML() :
    html=requests.get('http://www.baidu.com')
    print(html.status_code)
GETHTML()
import numpy
from bs4 import BeautifulSoup
import