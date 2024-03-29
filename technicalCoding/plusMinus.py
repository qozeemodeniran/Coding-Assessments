# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

def plusMinus(arr):
    # Write your code here
    arr_len = len(arr)
    positive_numbers = []
    negative_numbers = []
    zero_numbers = []
    
    for ele in arr:
        if ele >= 1:
            positive_numbers.append(ele)
        elif ele < 0:
            negative_numbers.append(ele)
        else:
            zero_numbers.append(ele)
            
    positive_ratio = round( len(positive_numbers) / arr_len, 6)
    negative_ratio = round(len(negative_numbers) / arr_len, 6)
    zero_ratio = round(len(zero_numbers) / arr_len, 6)
    
    print(positive_ratio)
    print(negative_ratio)
    print(zero_ratio)