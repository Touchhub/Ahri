while True:
    student_ID=input("学号： ")
    print(len(student_ID),type(student_ID))
    if len(student_ID)<=1:
        student_ID=str(0)+str(student_ID)
        print(type(student_ID))
    profession=float(input("专业成绩: "))
    innovate=float(input("创新分数: "))
    moral=float(input("德育素质: "))
    social_practice=float(input("社会实践: "))
    other=float(input("其他奖励和处罚分数: "))
    sum1_=(profession+innovate)*0.7
    sum2_=(moral*0.5+social_practice*0.3+other*0.2)*0.3
    sum3_=(sum1_+sum2_)
    sum1='%.2f'%(sum1_)
    sum2='%.2f'%(sum2_)
    sum3='%.2f'%(sum3_)
    profession='%.2f'%profession
    innovate='%.2f'%innovate
    moral='%.2f'%moral
    social_practice='%.2f'%social_practice
    other='%.2f'%other
    line1=(("学号",student_ID),("专业成绩分",profession),("创新能力分",innovate),("德育素质分",moral),("社会实践分",social_practice))
    line2=(("其他奖励和处罚分",other),("学生学业评价",sum1),("学生操行评定",sum2),("综合素质总分",sum3))
    print(line1)
    print(line2)
    f=open("综合素质评定学分测试","a",encoding="utf-8")
    f.write(str(line1))
    f.write('\n')
    f.write(str(line2))
    f.write('\n')
    f.close()
    print("学生学业评价: ",sum1)
    print("学生操行评定: ",sum2)
    print("综合素质总分: ",sum3)