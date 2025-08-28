list=[1,2,3,4,5,6,7,8,9,10,11]
odd=0
even=0
total=0
for i in list:
    total=total+i
    if i%2!=0:
        odd=odd+i
        print(i)
    elif i%2==0:
        even=even+i
        print(i)

print("Total of odd = ",odd)
print("Total of even =",even)
print("Total of list =",total)