authou='zhenyu'

product_list=[
    ('iphone',5800),
    ('Sunsung s7',5688),
    ('Watch',199),
    ('Coffee',32),
    ('Mac Pro',9800),
    ('Bicycle',1200),
]
shopping_list=[]
salary=int(input("input your salary: "))
while True:
    for index,item in enumerate(product_list):
        print(index,item)
    user_choise=input("选择要买的商品>>>: ")
    if user_choise.isdigit():
        user_choise=int(user_choise)
        if user_choise<len(product_list)and user_choise>=0:
            p_item=product_list[user_choise]
            if p_item[1]<=int(salary):
                shopping_list.append(p_item)
                salary-=p_item[1]
                print("Added %s into shopping_cart your current balance is %s" %(p_item,salary))
            else:
                print("\033[32;1m你的余额还有[%s]\033[0m" %salary)
        else:
            print("product code [%s] is not exist!" % user_choise)
    elif user_choise=='q':
        print("-------shopping list-------")
        for p in shopping_list:
            print(p)
        print("your current balance: ",salary)