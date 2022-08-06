# Find 3 largest numbers 

# O(n) time , O(1) space
def findThreeLargestNumbers1(array):
    res = [None, None, None]
    for num in array:
        updateRes(res, num)
    return res


def updateRes(res, num):
    if res[2] is None or num > res[2]:
        shiftAndUpdate(2, res, num)
    elif res[1] is None or num > res[1]:
        shiftAndUpdate(1, res, num)
    elif res[0] is None or num > res[0]:
        shiftAndUpdate(0, res, num)
        
def shiftAndUpdate(index, res, num):
    for i in range(index+1):
        if i == index:
            res[i] = num
        else:
            res[i] = res[i+1]


def findThreeLargestNumbers2(array):
    array.sort()
    n = len(array)
    return [array[n-3], array[n-2], array[n-1]]
    
    
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
# [18, 141, 541]
print(findThreeLargestNumbers2(array))