def InsertionSort(Array_Num):
    for i in range(1, len(Array_Num)):
        num_key = Array_Num[i]
        j = i - 1
        while (j >= 0) and Array_Num[j] > num_key:
            Array_Num[j+1] = Array_Num[j]
            j = j-1
        Array_Num[j+1] = num_key
       
    return Array_Num

print(InsertionSort([5,2,4,3,1,6]))