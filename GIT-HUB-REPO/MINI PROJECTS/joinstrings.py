def join(*args):
    join2=""
    for i in args:
        join2 = join2+" "+i
    return join2
print(join("mt","kr","lala"))