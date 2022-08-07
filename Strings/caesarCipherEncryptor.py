# Caesar Cipher Encryptor


# O(n) time , O(n) space 
def caesarCipherEncryptor1(input_str, key):
    newCode = []
    newKey = key % 26
    for alphabet in input_str:
        newCode.append(findNewCode(alphabet, newKey))
    return "".join(newCode)
    
def findNewCode1(alphabet, newCode):
    newAlphabet = ord(alphabet) + newCode
    if newAlphabet <= 122:
        return chr(newAlphabet)
    else:
        return chr(96 + newAlphabet % 122)


# O(n) time O(n) space
def caesarCipherEncryptor2(input_str, key):
    newCode = []
    newKey = key % 26
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    for alphabet in input_str:
        newCode.append(findNewCode2(alphabet, newKey, alphabets))
    return "".join(newCode)
    
def findNewCode2(alphabet, newKey, alphabets):
    newAlphabet = alphabets.index(alphabet) + newKey
    if newAlphabet <= 25:
        return alphabets[newAlphabet]
    else:
        return alphabets[-1 + newAlphabet % 25]

input_str = "xyz"
key = 2
print(caesarCipherEncryptor2(input_str, key))