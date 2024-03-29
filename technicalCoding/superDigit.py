""" 
We define super digit of an integer  using the following rules:

Given an integer, we need to find the super digit of the integer.

If x has only 1 digit, then its super digit is x.
Otherwise, the super digit of  is x equal to the super digit of the sum of the digits of x.
"""

def superDigit(n, k):
    # Calculate the super digit of n
    x = sum(int(digit) for digit in str(n)) % 9
    # Multiply by k and calculate the super digit again
    x = x * k % 9
    # The super digit of n is equal to n mod 9, except when n is a multiple of 9. In that case, the super digit is 9.
    return x if x else 9