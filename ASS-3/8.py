def cal():
    n=int(input("Enter number: "))
    n1=int(input("Enter another number: "))
    print("+ for add")
    print("- for sub")
    print("* for mul")
    print("/ for div")
    print("// for mol")
    s=input("What you want to do: ")
    match s:
        case '+':
            print(n+n1)
        case '-':
            print(n-n1)
        case '*':
            print(n*n1)
        case '/':
            print(n/n1)
        case '//':
            print(n%n1)  
while True:
    y= str(input("Write 0 to exit and Enter to Continue: "))
    if y=='0':
        break
    else:
        cal()