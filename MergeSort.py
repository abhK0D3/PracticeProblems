def Merge(A, left, mid, right):
    first_half = mid - left + 1
    sec_half = right - mid
    left_arr = [A[left + i] for i in range(first_half)]
    right_arr = [A[mid+1+i] for i in range(sec_half)]
    print(A)
    i = 0
    j = 0
    k = left
    
    while i < first_half and j < sec_half:
        if left_arr[i] <= right_arr[j]:
            A[k] = left_arr[i]
            i += 1
        else:
            A[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < first_half:
        A[k] = left_arr[i]
        i += 1
        k += 1

    while j < sec_half:
        A[k] = right_arr[j]
        j += 1
        k += 1

def MergeSort(A, left, right):
    if left < right:
        mid = (left + (right -1)) // 2
        MergeSort(A, left, mid)
        MergeSort(A, mid+1, right)
        print(left, mid, right)
        Merge(A, left, mid, right)

L = [5,2,4,1,3,7,2,6]
MergeSort(L, 0, 7)
# print([L[i] for i in range(len(L))])

