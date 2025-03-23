def anagramm():
    s= str(input("Enter a string: "))
    s1= str(input("Enter a string: "))
    s=s.replace(" ","").lower()
    s1=s.replace(" ","").lower()
    return sorted(s)==sorted(s1)
print(anagramm())