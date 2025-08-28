s=input("Enter a string: ")
def str_rev(s):
    if len(s)==0:
        return ""
    return s[-1] + str_rev(s[:-1])
print(str_rev(s))