n = int(input("your Age: "))
s = str(input("Are You a Citizen? (Yes/No): "))
if n>=18:
    if s=="Yes":
        print("You Are Eligible to Vote")
    else:
        print("You Are not Eligible to vote")    
else:
    print("You Are not Eligible to vote")         