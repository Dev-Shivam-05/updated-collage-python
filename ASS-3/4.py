def centerr(s):
    return print(s.center(30))
def vowel(s,s1):
    vowels="aeiouAEIOU"
    for i in vowels:
        s1=s.replace(i,'*')
        return print(s1)
s = str(input("Enter a string: "))
s1=str()
centerr(s)
vowel(s,s1)