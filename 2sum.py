# given an array of integers, return two numbers that sume of to a target

def TwoSums(arr, target):
    compliments = set()
    for i in arr:
        compliment = target - i
        if compliment in compliments:
            return compliment, i
        compliments.add(compliment)
            
    return False

print(TwoSums([1, 2, 4, 4], 8))