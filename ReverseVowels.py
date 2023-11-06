#Inital BruteForce
def reverseVowels_Brute(s):
    sArr= []
    indexArr = []
    resultString = ''
    for i in range(len(s)):
        if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            indexArr.append(i)
    i = 0
    j = 0
    while i < len(s):
        if (s[i] in ['a', 'e', 'i', 'o', 'u']):
            sArr.append(s[indexArr[len(indexArr)-j-1]])
            j += 1
            i += 1
        else:
            print(s[i])
            sArr.append(s[i])
            i += 1
    return (resultString.join(sArr))

#Two Pointers: Preferred Implementation 
def reverseVowels_Pointers(s):
    s = list(s)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    left = 0
    right = len(s) - 1
    while left < right:
        while (left < right and s[left] not in vowels):
            left += 1
        while (left < right and s[right] not in vowels):
            right -= 1
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return (''.join(s))


#List Comprehension
def reverseVowels_LC(s):
    s = list(s)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowelArrReversed = [x for x in s[::-1] if x in vowels]
    resultStr = ''
    vowelIndex = 0
    for i in s:
        if i not in vowels:
            resultStr += i
        else:
            resultStr += vowelArrReversed[vowelIndex]
            vowelIndex += 1
    return resultStr

    
    

print(reverseVowels_Brute('leetcode'))
print(reverseVowels_Pointers('leetcode'))
print(reverseVowels_LC('leetcode'))

