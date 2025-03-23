def pwvld(p):
    if len(p) < 8:
        return False
    if not any(char.isupper() for char in p):
        return False
    if not any(char.islower() for char in p):
        return False
    if not any(char.isdigit() for char in p):
        return False
    if ' ' in p:
        return False
    return True

p = input("Enter your password: ")

if pwvld(p):
    print("Password is valid.")
else:
    print("Password is invalid.")