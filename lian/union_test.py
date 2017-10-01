def union(*args):
    args=lists
    (student_ID,profession,innovate,moral,social_practice,other)=args
    #(student_ID,profession,innovate,moral,social_practice,other)=lists
    sum1=(profession+innovate)*0.7
    sum2=(moral*0.5+social_practice*0.3+other*0.2)*0.3
    sum3=(sum1+sum2)
    return 0
def test(*args):
    n=0
    f=open("综合素质评定学分测试","a",encoding="utf-8")
    f.write(student_ID)
    f.write(":")
    for i in args:
        n+=1
        i='%.2f'%i
        if n==6:
            i="学生学业评价: "+i
            print(i)
        if n==7:
            i="学生操行评定: "+i
            print(i)
        if n==8:
            i="综合素质总分: "+i
            print(i)
        f.write(str(i))
        f.write(",")
    f.write('\n')
    f.close()
    return i
#test(profession,innovate,moral,social_practice,other,sum1,sum2,sum3)