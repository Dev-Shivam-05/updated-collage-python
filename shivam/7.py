# taking input from user 
s = str(input("Enter a String : "))
# using split-function on input 
x = s.split()
# using join-function and upper function together 
a = ''.join(x[0].upper() for x in x)
# printing a
print(a)