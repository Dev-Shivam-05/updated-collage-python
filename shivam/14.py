def words(s,c):
    s1=s.count(c)
    print("The occurnce of",c,"is : ",s1)
s=str(input("Enter a string : "))
c=str(input("Enter a word : "))
words(s,c)