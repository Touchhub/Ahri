'''
f=open("yesteeday",'a',encoding="utf-8")#文件句柄
f.write("\n有情方知张国荣，\n俗话说当断不断，必受其乱。\n所欲不曾似所念，今生也就此次，不愿在悲悲切切")
f.close()
f=open("yesteeday",'r',encoding="utf-8")
for line in f:
   print(line.strip())
'''

