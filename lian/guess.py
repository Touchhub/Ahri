count=0
while count<3:
    guess_age=int(input("guess age"))
    if guess_age==age_of_olboy:
        print("yes ,you got it.")
        break
    elif guess_age>age_of olboy:
        print("think smallar...")
    else:
        print("think bigger...")
        count +=1
        if count==3:
            countinu_