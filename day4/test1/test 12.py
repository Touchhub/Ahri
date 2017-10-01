#判断101-200之间有多少个素数，并输出所有素数。
# h=0          leap 循环
# leap=1
# from math import sqrt
# from sys import stdout
# for m in range(101,201):
#     k=int(sqrt(m+1))
#     for i in range(2,k+1):
#         if m%i==0:
#             leap=0
#             break
#     if leap==1:
#         print('%-4d'%m)
#         h+=1
#         if h%10==0:
#             print("")
#     leap=1
# print('The total is %d'%h)

# 集合解法
'''
l=[]
for i in range(101,201):
    for j in range(2,i-1):
        if i%j==0:
            break
    else:
        l.append(i)
print(l)
print("总数为：%d"%len(l))
'''
 #pop()删除

from  math import  sqrt
l=[]
for x in range(101,201):
    l.append(x)
    for i in range(2,int(sqrt(x))+1):
        if x%i==0:
            l.pop()
            break
n=len(l)
print(l)
print('总数为：%d'%n)

