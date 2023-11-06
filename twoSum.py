def twoSum(A, target):
    d = {}
    for i in A:
        d[i] = target - i
        if d[i] in d.keys():
            return (i, d[i])

def twoSumIndex(nums, target):
        pairs = []
        d = {}
        for i in nums:
            print(d)
            d[i] = target - i
            if d[i] in d:
                pairs.append(nums.index(d[i]))
                pairs.append(nums.index(i))
                break
        return pairs

def twoSumEnum(nums, target):
    values = {}
    for idx, value in enumerate(nums):
        if target - value in values:
            return [values[target - value], idx]
        else:
            values[value] = idx
        
# print(twoSum([1,5,8,3,4], 9))
# print(twoSumIndex([3, 3,2], 6))
print(twoSumEnum([3,2, 3], 6))