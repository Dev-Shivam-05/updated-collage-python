# declaring alphabets named function 
def alphabets(s):
    # spliting input and storing in another variable 
    w=s.split(" ")
    # sorting from a to z
    s1 = sorted(w)
    s2=" ".join(s1)
    print(s2)
s = input("Enter A String: ")
alphabets(s)