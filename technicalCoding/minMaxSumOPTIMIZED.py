# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

def miniMaxSum(arr):
    # Write your code here    
    minElement = min(arr)
    maxElement = max(arr)
    totSum = sum(arr)
    
    minSum = totSum - maxElement
    maxSum = totSum - minElement
    
    print(str(minSum) + " " + str(maxSum))
