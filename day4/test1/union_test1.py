import re
f=open("综合素质评定学分测试","r",encoding="utf-8")
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
   print(lists[0])
   (student_ID,profession,innovate,moral,social_practice,other)=lists
   print(lists)
  # def test(*args):
   profession=float(profession)
   innovate=float(innovate)
   moral=float(moral)
   social_practice=float(social_practice)
   other=float(other)
     #  lists1=[student_ID,profession,innovate,moral,social_practice,other]
     #  return lists1
