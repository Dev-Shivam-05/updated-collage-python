def centerr(s):
    return print(s.center(50))
def vowels(s,s1):
    vowels = "aeiouAEIOU"
    for i in vowels:
        s1=s.replace(i,"*")
        return print(s1)
s = (input("Enter a String : "))
s1=str()
centerr(s)
vowels(s,s1)