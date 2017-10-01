num=[1,2,3,4]
a=0
for i in num:
    for j in  num:
        for k in  num:
            if(i!=k)and(i!=j)and(j!=k):
                a+=1
                print (i,j,k)

print(a)
