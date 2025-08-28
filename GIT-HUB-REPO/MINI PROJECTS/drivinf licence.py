a=input("Enter your age:")

if a.isdigit():
    a=int(a)

    if a > 120:
        print("Invalid Age")
    elif a >= 18:
        print("You are eligible")
    else:
        print("You are not eligible")
else:
    print("Invalid input")