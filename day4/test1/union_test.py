#(student_ID,profession,innovate,moral,social_practice,other)
from union_test1  import *
sum1=(profession+innovate)*0.7
sum2=(moral*0.5+social_practice*0.3+other*0.2)*0.3
sum3=(sum1+sum2)
print(student_ID,profession,innovate,moral,social_practice,other,sum1,sum2,sum3)
lines=(student_ID,profession,innovate,moral,social_practice,other,sum1,sum2,sum3)
#定义函数写入文件
def score(*args):
    lines=(student_ID,profession,innovate,moral,social_practice,other,sum1,sum2,sum3)
    with open('test_score',"w",encoding='utf-8') as f :
        for i in lines:
            f.write(str(i))
    return lines

score(student_ID,profession,innovate,moral,social_practice,other,sum1,sum2,sum3)

