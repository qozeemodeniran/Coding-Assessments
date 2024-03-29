"""
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
"""

def caesarCipher(s, k):
    # Write your code here
    result = ""
    for char in s:
        ascii_val = ord(char)
        if 65 <= ascii_val <= 90:  # Uppercase letters
            result += chr((ascii_val - 65 + k) % 26 + 65)
        elif 97 <= ascii_val <= 122:  # Lowercase letters
            result += chr((ascii_val - 97 + k) % 26 + 97)
        else:  # Non-letter characters
            result += char
    return result