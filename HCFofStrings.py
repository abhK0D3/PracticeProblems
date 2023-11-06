def hcfStrings(str1, str2):
    if (str1 + str2 != str2 + str1):
        return('')
    else:
        hcf = hcfInt(len(str1), len(str2))
        return(str1[:hcf])
def hcfInt(a, b):
    if (b == 0):
        return a
    else:
        return hcfInt(b, a % b)
print(hcfStrings('abab','ababab'))