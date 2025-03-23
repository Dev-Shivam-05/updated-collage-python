# Userdifinded function 
x = int(input("Enter first number: "))  
y = int(input("Enter second number: "))   

def add():
    global x,y
    print("Sum: ",x+y)
def sub():
    global x,y
    print("Sub: ",x-y)  
def mul():
    global x,y
    print("Mul: ",x*y)
def div():  
    global x,y
    print("Div: ",x/y)  
def mod():
    global x,y
    print("Mod: ",x%y)
print("Use 1. Addition")   
print("Use 2. subtraction")
print("Use 3. multification")
print("Use 4. Division")
print("Use 5. Modulus") 
ch = int(input("Enter your choice: ")) 
if ch == 1:
    add()
elif ch == 2:
    sub()    
elif ch == 3:
    mul()
elif ch == 4:
    div()
elif ch == 5:  
    mod()    