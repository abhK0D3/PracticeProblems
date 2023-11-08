#Using List Comprehension
def reverseWords(s):
    sArr = list(s.split(' '))
    sArr = [word for word in sArr if word]
    reverseArr = [sArr[len(sArr) - i] for i in range(1, len(sArr)+1)]
    reverseStr = ' '.join(reverseArr)
    return reverseStr

print(reverseWords("  hello world  "))