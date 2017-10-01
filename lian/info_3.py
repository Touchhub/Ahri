math=input("math:")
pe=input("pe:")
age=input("age:")
print(type(age))
job=input("job:")
name=input("name")
info='''
-------info of {0}-------
math={1}
pe={2}
age={3}
job={4}
'''.format(name,
           pe,
           age,
           job,
           math)

print(info)