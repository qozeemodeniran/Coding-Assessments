# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):
    # Write your code here
    diag1 = 0
    diag2 = 0
    
    matrixLength = len(arr)
    
    for i in range(matrixLength):
        diag1 += arr[i][i]
        diag2 += arr[i][matrixLength-i-1]
        
        absoluteDifference = abs(diag1 - diag2)
        
    return absoluteDifference