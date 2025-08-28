
l=[1,2,"mike","zone",1.1,1.2,True,False,(8+7j)]

l_bool = []
l_int = []
l_float = []
l_str = []
l_other = []

for i in l:

    if type(i) == bool:
        l_bool.append(i)
    elif type(i) == float:
        l_float.append(i)
    elif type(i) == int:
        l_int.append(i)
    elif type(i) == float:
        l_float.append(i)
    elif type(i) == str:
        l_str.append(i)
    else:
        l_other.append(i)

    print(l_bool)
    print(l_int)
    print(l_float)
    print(l_str)
    print(l_other)