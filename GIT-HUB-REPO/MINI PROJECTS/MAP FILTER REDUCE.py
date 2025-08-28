from functools import reduce
nums=[1,2,3,4,5,6]
even= list(filter(lambda x:x%2==0,nums))
square = list(map(lambda x:x**2,even))
product = reduce(lambda x,y:x*y,square)
print(even)
print(square)
print(product)
