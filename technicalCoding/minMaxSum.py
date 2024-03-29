# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

def miniMaxSum(arr):
    # Write your code here
    sorted_arr = sorted(arr) 
    
    minSum = sum(sorted_arr[:4])
    maxSum = sum(sorted_arr[-4:])
    
    print(str(minSum) + " " + str(maxSum))

# Test cases
miniMaxSum([1,2,3,4,5]) # 10 14
miniMaxSum([7,69,2,221,8974]) # 299 9271