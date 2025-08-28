a = input("Enter the number:")

if not a.isdigit():
    print("Invalid input")
elif a == 0:
    print("number is zero")
elif a < 0:
    print("number",a,"is negative")
else:
    print("number",a,"is positive")