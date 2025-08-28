a=input("Enter a number:")
if not a.isdigit:
    print("Invalid number")
else:
    a=int(a)
    if a%2 ==0:
        print("Number",a,"is even")
    else:
        print("Number",a,"is odd")
