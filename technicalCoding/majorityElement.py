# Given an array of size N, find the majority element. The majority element is the element that appears more than floor(N/2) times.
# You may assume that the array is non-empty and the majority element always exist in the array.


# PSEUDOCODE:
# counter{}: to store each element and frequency
# iterate through the given array and update counter{}
# iterate the counte{} and return the key with higest value


    # counter{}: to store each element and frequency
    # iterate through the given array and update counter{}
    # iterate the counte{} and return the key with higest value
def majorityElement(self, A):
    counter = {}
        
    for element in A:
        if element not in counter:
            counter[element] = 1
        else:
            counter[element] += 1
        
        for element, count in counter.items():
            if count > len(A) // 2:
                return element