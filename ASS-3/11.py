def long(s):
    w=s.split(" ")
    l=str(max(w,key=len))
    print(l)
s=str(input("Enter a sentance: "))
long(s)