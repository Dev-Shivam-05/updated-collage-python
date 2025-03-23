def alpha(s):
    w=s.split(" ")
    s1=sorted(w,key=str.lower)
    s2=" ".join(s1)
    print(s2)
s=str(input("Enter a sentance: "))
alpha(s)