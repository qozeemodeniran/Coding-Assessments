""" 
Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be
removed to make the string a palindrome. There may be more than one solution, but any will do. If the word
is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to
remove
"""

def palindromeIndex(s):
    # Write your code here
    def is_palindrome(s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
        return True
        
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            if is_palindrome(s, i+1, len(s)-i-1):
                return i
            else:
                return len(s)-i-1
    
    return -1
    
    """def is_palindrome(s):
        return s==s[::-1]
    if is_palindrome(s):
        return -1
        
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if is_palindrome(t):
            return i
    return -1"""
        