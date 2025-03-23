# declaribng a function 
def cal():
    s =int(input("Enter A number: "))
    s2 =int(input("Enter Another number: "))
    print("Enter '+' for Adding Two Numbers")
    print("Enter '-' for Subtracting Two Numbers")
    print("Enter '*' for Multiplying Two Numbers")
    print("Enter '/' for Dividing Two Numbers")
    print("Enter '%' for Moduling Two Numbers")
    print("Enter '//' to Mol Two Numbers")
    o=input("Enter the opration to perform : ")
# using match case for performing opration
    match o:
        case '+':
            print(f"The Sum Of {s} + {s2} = {s + s2}")
        case '-':
            print(f"The Subtraction Of {s} - {s2} = {s - s2}")
        case '*':
            print(f"The Product of {s} - {s2} = {s * s2}")
        case '/':
            print(f"The Division of {s} / {s2} = {s / s2}")
        case '%':
            print(f"The Modulas of {s} % {s2} = {s % s2}")
        case '//':
            print(f"The Mol of {s} // {s2} = {s // s2}")
# using while loop with true that help to perform our program continouly
while True:
    y= str(input("Enter 0 to exit Or Press Any Key To Continue : "))
    if y == 0:
        break
    else:
        cal()
