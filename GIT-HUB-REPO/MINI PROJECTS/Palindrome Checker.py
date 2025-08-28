word=input("Enter word: ")
def is_palindrome(word):
    if  word==word[::-1]:
        return True
    else:
        return False
print(is_palindrome(word))