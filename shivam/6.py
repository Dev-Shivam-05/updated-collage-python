def password(p):
    if len(p) < 8:
        return False
    if not any (char.isupper() for char in p):
        return False
    if not any (char.islower() for char in p):
        return False
    if not any (char.isdigit() for char in p):
        return False
    if ' ' in p:
        return False
    return True
p = input ("Enter Your Password : ")

if password(p):
    print("Nice,Your Password Is Valid")
else:
    print("Sorry,Your Password Is Invalid")