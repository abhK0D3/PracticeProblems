def canPlaceFlowers(flowerbed, n):
    if (n == 0):
        return True
    for i in range(len(flowerbed)):
        if (n > 0):
            if (i >= 1 and i < len(flowerbed)-1) and (flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0):
                flowerbed[i] = 1
                n -= 1
            elif (i == 0 and len(flowerbed) > 1):
                if (flowerbed[i] == 0 and flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                print(n, i)
            elif (i == len(flowerbed)-1):
                if (flowerbed[i] == 0 and flowerbed[i-1] == 0 and i == len(flowerbed)-1):
                    flowerbed[i] = 1
                    n -= 1 
             
    return (not n)

def canPlaceFlowersAlso(flowerbed, n):
    if n == 0:
        return True
    for i in range(len(flowerbed)): ##works because once i == 0 is true, it does not check right operand for out of bounds
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            n -= 1
    return not n
print(canPlaceFlowers([0,0,1,0,0], 1))
print(canPlaceFlowersAlso([0,0,1,0,0], 2))
