#对爬取数据的模型定义
# import re
# a='[1]="<img src=\'/d/file/20150826/4ccec5dd710dbd873a6972e1b8e7aff1.jpg\' alt=\'马来西亚的洋娃娃美女'
# print(a)
# print(type(a))
# reg=r'<img src=\'(.+?)\' alt=\'马来西亚的洋娃娃美女'
# reg=re.compile(reg)
# b=re.findall(reg,a)
# print(b[0])
import re,time
from urllib import request
html=request.urlopen('http://www.mm131.com/xiaohua/list_2_2.html').read().decode('gb2312')
print(html)