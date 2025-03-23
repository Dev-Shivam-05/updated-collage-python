l="Yaashh Bhakta"
n=str(input("Enter a number from : "))
i=0
c=0
while i<len(l):
    if n==l[i]:
        print(n,'found on index',i)
        c+=1
    i+=1        
print(n,"Occures",c,'times')      