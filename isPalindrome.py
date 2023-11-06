def checkPalindrome(n):
    reverse = 0
    temp = n
    while (temp != 0):
        reverse = (reverse * 10) + (temp % 10)
        # print(reverse)
        temp = temp // 10
        # print(temp)
      
    return (reverse == n)

print(checkPalindrome(121))