for x in range(1,10):
    for y in range(0,10):
        for z in range (0,10):
            s1=100*x+10*y+z
            s2=pow(x,3) + pow(y,3) + pow(z,3)
            if s1 == s2 :
                print("水仙花数有：%7d" %s1)

print(int(115/10)%10)
a=115/10
a=int(a)
print(a)
