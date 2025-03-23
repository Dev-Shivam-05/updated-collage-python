l=[1,2,3,4,5,6,2,2,3,5,2]
n=int(input("Enter a number from 1 to 6 : "))
i=0
c=0
while i<len(l):
    if n==l[i]:
        print(n,'found on index',i)
        c+=1
    else:
        print("Searching..")
    i+=1        
print(c)    