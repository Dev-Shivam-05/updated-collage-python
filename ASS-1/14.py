l=[1,2,3,4,5,6]
n=int(input("Enter a number from 1 to 6 : "))
i=0
while i<=5:
    if n==l[i]:
        print(n,'found on index',i)
        break
    else:
        print("Searching..")
    i+=1        