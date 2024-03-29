""" 
Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.
"""

def gridChallenge(grid):
    # Write your code here
    sorted_grid = [''.join(sorted(row)) for row in grid]
    
    for col in zip(*sorted_grid):
        if list(col) != sorted(col):
            return 'NO'
            
    return 'YES'
