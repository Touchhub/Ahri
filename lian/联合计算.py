import re
f=open("test_score","r",encoding="utf-8")
for line in f:
   line_score=re.split(",|:",line)
   #print(line_score,type(line_score))
   n=0
   lists=[]
   for i in line_score:
    n+=1
    if n<7:
        #print(i)
        lists.append(i)
   print(lists)
   (student_ID,profession,innovate,moral,social,other)=lists
   import union_test
   union_test.union(profession,innovate,moral,social_practice,other,sum1,sum2,sum3)
   #test(profession,innovate,moral,social_practice,other,sum1,sum2,sum3)
test()
