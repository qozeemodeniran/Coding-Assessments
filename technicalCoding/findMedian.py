# find the median of an arry

def findMedian(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        median = (sorted_arr[n//2] + sorted_arr[n//2 - 1]) / 2
    else:
        median = sorted_arr[n//2]
    return median