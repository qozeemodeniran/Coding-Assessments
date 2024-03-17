import re
# implemeting a function in python to check if a string is a palindrome or not
def is_palindrome(s):
#    remove non-alphanumeric characters and convert to lower case
    # s = ''.join(e for e in s if e.isalnum()).lower()
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
#    check if the string is equal to its reverse
    return s == s[::-1]

# test the function
test_string = "A man, a plan, a canal, Panama"
print(is_palindrome(test_string))

test_string = "Able was I, ere I saw Elba" 
print(is_palindrome(test_string))

test_string = "zamzam"
print(is_palindrome(test_string))
