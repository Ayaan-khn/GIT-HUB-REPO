def power(base, exp):
    # if base or exp == str :
    #     return ("Invalid input")
    # else:
        return base ** exp


base = int(input("Enter base number: "))
exp = int(input("Enter exponent: "))
print(power(base, exp))
