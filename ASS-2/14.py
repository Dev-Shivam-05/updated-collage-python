n = int(input("Enter a number: "))
s = int(input("Enter a number: "))
d = int(input("Enter a number: "))
if n>s:
    if n>d:
        print(n,"is gratest")
    else:
        print(d,"is greatest")
else:
    if s>d:
        print(s,"is gratest")
    else:
        print(d,"is greatest")                