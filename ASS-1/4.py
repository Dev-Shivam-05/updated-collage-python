# Globle Variable
x = 10
def fn():
    global x
    x = 20
    print("X: ",x)
fn()    
print("X: ",x)
