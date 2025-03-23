def concat(a,a1):
    if a1== "":
        return a
    else:
        a2 = a+" "+a1
        return a2

a = str(input("Enter a string : "))
a1 = str(input("Enter a string : "))
print(a)
print(a1)
print(concat(a,a1))