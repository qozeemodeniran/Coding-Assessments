
""" 

Rules of the Game:
Initially, there are n towers, each of height m.
Players move in alternating turns.
In each turn, a player can choose a tower of height x and reduce its height to y, where 1 ≤ y < x and y evenly divides x.
If the current player is unable to make a move, they lose the game.
Objective:
Determine which player will win based on the given values of n and m.
If the first player wins, return 1; otherwise, return 2.
Example:
Given n = 2 and m = 6:
There are 2 towers, each 6 units tall.
Player 1 has two choices:
Remove 3 pieces from a tower to leave 3 (since 6 % 3 = 0).
Remove 5 pieces to leave both towers at 1 unit tall.
Player 2 matches the move.
Now the towers are both 1 unit tall.
Player 1 has only one move left: remove 1 piece.
Towers are now both 0 units tall.
Player 2 has no move and loses.


"""

def towerBreakers(n, m):
    # Write your code here
    if m == 1 or n % 2 == 0:
        return 2
    else:
        return 1