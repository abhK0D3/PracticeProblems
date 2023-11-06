def MergeStringsAlternately(word1, word2):
    wordResult = ''
    i = 0
    j = 0
    while i < len(word1):
        if j == len(word2):
            break
        wordResult += word1[i]+word2[j]
        i += 1
        j += 1
    while i < len(word1):
        wordResult += word1[i]
        i += 1
    while j < len(word2):
        wordResult += word2[j]
        j += 1
    return wordResult

print(MergeStringsAlternately('abc','pqrs'))