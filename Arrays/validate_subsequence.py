# Validate Subsequence 

# O(n) time , O(1) space
def validateSubsequence1(array, sequence):
    arrPointer = 0 
    seqPointer = 0
    while arrPointer < len(array) and seqPointer < len(sequence):
        if sequence[seqPointer] == array[arrPointer]:
            seqPointer += 1 
        arrPointer += 1 
    
    return seqPointer == len(sequence)
        

def validateSubsequence2(array, sequence):
    seqIndex = 0 
    for i in array:
        if seqIndex == len(sequence):
            break
        if i == sequence[seqIndex]:
            seqIndex += 1 
    return seqIndex == len(sequence)   

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(validateSubsequence2(array, sequence))