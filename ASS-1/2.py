# two level of indentation
x = int(input("Enter a number: "))
if x >= 10:
    if x >= 20:
        print("x is greater than 20")
    else:
        print("x is greater than 10 but less than 20")
else:
    print("x is not greater than 10")                