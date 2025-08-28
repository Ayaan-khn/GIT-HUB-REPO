def multi(*args):
    result=1
    for i in args:
            result=result*i
    return result
print(multi(1,24,4))

# import math
# print(math.prod([1, 24, 4]))