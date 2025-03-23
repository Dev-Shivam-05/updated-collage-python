s = str(input("Enter a string: "))
w=s.split()
a=''.join(w[0].upper() for w in w)
print(a)