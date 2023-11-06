def LowestCommonSubsequence(wordA, wordB):
    i = 0
    j = 0
    subAB = ''
    while i < len(wordA) and j < len(wordB) :
        if wordA[i] == wordB[j]:
            print(wordA[i])
            subAB += wordA[i]
            i += 1
        j += 1
    return i == len(wordA)
print(LowestCommonSubsequence("sabfez", "stabdgfz"))
