def concat(s,s1,s2):
    if s1=="":
        return s
    else:
        s2=s+" "+s1
        print(s2)
        
s = str(input("Enter the string :"))
s1 = str(input("Enter the string :"))
s2=str()
print(s)
print(s1)
concat(s,s1,s2)