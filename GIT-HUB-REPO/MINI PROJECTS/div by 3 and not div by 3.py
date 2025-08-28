num=[3,6,7,12,15,18,21]
div_3=0
notdiv_3=0
for i in num:
    print(i)
    if i%3==0:
        div_3=div_3+1
    elif i%3!=0:
        notdiv_3=notdiv_3+1

print("Total numbers divisible by 3 are:",div_3)
print("Total numbers not divisible by 3 are:",notdiv_3)