def even(*args):
    count=0
    for i in args:
        if i%2==0:
            count += 1
    return count
print(even(1,2,3,4,5,6,7))