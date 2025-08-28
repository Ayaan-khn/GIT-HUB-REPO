amount = input("Enter the amount:")

if not amount.isdigit():
    print("ERROR: Invalid Amount")
else:
    amount = int(amount)
    print("Total MRP:", amount)

    if amount <= 1000:
        print("Total discount on MRP:", amount, "is", amount / 100 * 5)
    elif amount <= 3000:
        print("Total discount on MRP:", amount, "is", amount / 100 * 10)
    elif amount <= 5000:
        print("Total discount on MRP:", amount, "is", amount / 100 * 15)
    else:
        print("Total discount on MRP:", amount, "is", amount / 100 * 20)

