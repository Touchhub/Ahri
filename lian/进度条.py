'''
import sys,time
for i in range(30):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.2)
    '''
import sys
f=open("yesteeday","r",encoding="utf-8")
f_new=open("yesterday2","w",encoding="utf-8")


for line in f:
    if "俗话说当断不断" in line:
       line=line.replace("俗话说当断不断","想又如何，眼不见心不烦，何不趁此当断")
    f_new.write(line)
f.close()
f_new.close()