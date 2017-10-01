list_1=[1,3,4,5,3,5,6,7,9]
list_1=set(list_1)
list_2=set([2,6,0,4,5,55,66])
print(list_1,list_2,type(list_1))
#交集
print( list_1.intersection(list_2) )
#并集
print(list_1.union(list_2))
#差集
print(list_2.difference(list_1))
print(list_1.difference(list_2))
#子集
print(list_1.issubset(list_2))
#父集
print(list_2.issuperset(list_2))
#反向差集
print(list_2.symmetric_difference(list_1))