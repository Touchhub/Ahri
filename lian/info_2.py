math=input("math:")
pe=input("pe:")
age=int(input("age:"))
print(type(age))
job=input("job:")
name=input("name: ")
info2='''
-------info of %s-------
_math: %s
_pe: %s
-age: %s
_job: %s
''' % (name,math,pe,age,job)
print(info2)