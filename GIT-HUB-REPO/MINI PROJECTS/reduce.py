from functools import reduce
nums=[1,2,3,4,5]
product_list= reduce(lambda x,y: x*y,nums)
print(product_list)