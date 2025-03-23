def card(s):
    s1=str(s)
    m="*"*(len(s1)-4)+(s1[-4:])
    print(m)
s=int(input("Enter card number: "))
card(s)    