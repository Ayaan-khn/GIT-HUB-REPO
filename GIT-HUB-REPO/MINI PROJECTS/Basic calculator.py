a = input("Enter a number:")
b = input("Enter another number:")
op = input("Enter the operator:")

if not a.isdigit():
    print("Invalid input")
elif not b.isdigit():
    print("Invalid input")
else:
    if op == "+":
        print("Answer:", float(a) + float(b))
    elif op == "-":
        print("Answer:", float(a) - float(b))
    elif op == "*":
        print("Answer:", float(a) * float(b))
    elif op == "/":
        if b == 0:
            print("Error can not divide by zero")
        else:
            print("Answer:", float(a) / float(b))
    else:
        print("Invalid syntax")
