# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if not array:
        return False
    if query == array[0]:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) < 2:
        return True
    if text[0] != text [-1]:
        return False
    return is_palindrome(text[1: -1])


# digit_match
def digit_match(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    
    if not num1 or not num2:
        return 0
    
    count = 1 if num1[-1] == num2[-1] else 0
          
    return digit_match(num1[:-1], num2[:-1]) + count

