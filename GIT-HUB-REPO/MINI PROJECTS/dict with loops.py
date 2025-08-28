marks = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 65,
    "Eva": 78
}
print("Here is the list of students with their marks", marks)

lessthan_75 = 0
morethan_75 = 0

for i in marks.values():
    if i >= 75:
        morethan_75 = morethan_75 + 1
    if i <= 75:
        lessthan_75 = lessthan_75 + 1

print("Students having more than 75 marks are:",morethan_75)
print("Students having less than 75 marks are:",lessthan_75)
