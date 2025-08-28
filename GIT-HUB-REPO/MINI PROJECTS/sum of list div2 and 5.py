numbers = [2, 5, 8, 11, 14, 17, 20]
total_of_the_list = 0
div_by_2 = 0
div_by_5 = 0
for i in numbers:
    total_of_the_list = total_of_the_list + i
    if i % 2 == 0:
        div_by_2 = div_by_2 + i
for i in numbers:
    if i % 5 == 0:
        div_by_5 = div_by_5 + i

print(total_of_the_list)
print(div_by_2)
print(div_by_5)
