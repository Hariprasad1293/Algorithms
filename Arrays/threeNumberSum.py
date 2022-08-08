# Triplet sum 
# O(n^2) time O(n) space

def threeNumberSum(arr, target):
    arr.sort()
    res = []
    n = len(arr)
    for i in range(n-2):
        curr = i
        left = curr + 1 
        right = n - 1 
        while left < right:
            newTriplet = arr[curr] + arr[left] + arr[right]
            if newTriplet == target:
                res.append([arr[curr], arr[left], arr[right]])
                left += 1 
                right -= 1
            elif newTriplet < target:
                left += 1
            else:
                right -= 1 
    return res




arr = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
print(threeNumberSum(arr, target))
# [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]