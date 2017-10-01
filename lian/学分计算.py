while True:
    student_ID=input("学号： ")
    profession=float(input("专业成绩: "))
    innovate=float(input("创新分数: "))
    moral=float(input("德育素质: "))
    social_practice=float(input("社会实践: "))
    other=float(input("其他奖励和处罚分数: "))
    sum1=(profession+innovate)*0.7
    sum2=(moral*0.5+social_practice*0.3+other*0.2)*0.3
    sum3=(sum1+sum2)
    def test(*args):
        n=0
        f=open("综合素质评定学分","a",encoding="utf-8")
        f.write(student_ID)
        f.write(":")
        for i in args:
            n+=1
            i='%.2f'%i
            f.write(str(i))
            f.write(",")
            if n==6:
                print("学生学业评价: ",i)
            if n==7:
                print("学生操行评定: ",i)
            if n==8:
                print("综合素质总分: ",i)
        f.write('\n')
        f.close()
        return i
    test(profession,innovate,moral,social_practice,other,sum1,sum2,sum3)


    # def test(x):
    #     x='%.2f'%x
    #     return x
    # profession=test(profession)
    # innovate=test(innovate)
    # moral=test(moral)
    # social_practice=test(social_practice)
    # other=test(other)
    # sum1=test(sum1)
    # sum2=test(sum2)
    # sum3=test(sum3)

        # sum1='%.2f'%(sum1_)
        # sum2='%.2f'%(sum2_)
        # sum3='%.2f'%(sum3_)
        # profession='%.2f'%profession
        # innovate='%.2f'%innovate
        # moral='%.2f'%moral
        # social_practice='%.2f'%social_practice
        # other='%.2f'%other

    # line1=(("学号",student_ID),("专业成绩分",profession),("创新能力分",innovate),("德育素质分",moral),("社会实践分",social_practice))
    # line2=(("其他奖励和处罚分",other),("学生学业评价",sum1),("学生操行评定",sum2),("综合素质总分",sum3))
    # print(line1)
    # print(line2)
    # f=open("综合素质评定学分","a",encoding="utf-8")
    # f.write(str(line1))
    # f.write('\n')
    # f.write(str(line2))
    # f.write('\n')
    # f.close()
    # print("学生学业评价: ",sum1)
    # print("学生操行评定: ",sum2)
    # print("综合素质总分: ",sum3)