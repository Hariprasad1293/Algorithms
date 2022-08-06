# Two Number Sum 

# O(n*2) - time, O(1) - space
def twoNumberSum1(array, targetSum):
    for i in range(len(array) - 1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

# O(n) time , O(n) space 
def twoNumberSum2(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []

# O(n(log(n)) time, O(1) space 
def twoNumberSum3(array, targetSum):
    array.sort()
    leftPointer = 0 
    rightPointer = len(array) - 1 
    while leftPointer < rightPointer:
        currentSum = array[leftPointer] + array[rightPointer]
        if currentSum == targetSum:
            return [array[leftPointer], array[rightPointer]]
        elif currentSum < targetSum:
            leftPointer += 1 
        elif currentSum > targetSum:
            rightPointer -= 1 
    return []
    
    
    
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(twoNumberSum3(array, targetSum))