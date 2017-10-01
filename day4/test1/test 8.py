# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"% (j,i,i*j),end="  ")
#     print("")
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("""%d*%d=%d""" % (i,j,i*j),end=" ")
#     print()
'''
for i in range (1,10):
    for j in range(1,i+1):
        print ("{}*{}={}".format(j,i,j*i),end=" ")
    print("\n")
'''
for i in range(1,10):
    l=[]
    for j in range(1,i+1):
        l.append(str(j)+"*"+str(i)+"="+str(i*j))
    print(" ".join(l))