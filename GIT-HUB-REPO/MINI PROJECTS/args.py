def multiply_numbers(*args):
    result = 1
    for i in args:
        result = result * i
    return result

print(multiply_numbers(2, 3, 4))
print(multiply_numbers(5, 10))
print(multiply_numbers(7))

