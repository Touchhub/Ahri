math=input("math:")
pe=input("pe:")
age=input("age:")
print(type(age))
job=input("job:")
name=input("name")
info='''
-------info of {_name}-------
math={_math}
pe={_pe}
age={_age}
job={_job}
'''.format(_name=name,
           _pe=pe,
           _age=age,
           _job=job,
           _math=math)

print(info)