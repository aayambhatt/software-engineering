def merge_sort(nums):
    if len(nums)<2:
        return nums

    mid = len(nums)//2

    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)



def merge(first, second):
    result = []
    n = len(first)
    m = len(second)
    i, j = 0, 0

    while i < n and j < m:
        if first[i]<second[j]:
            result.append(first[i])
            i+=1
        else:
            result.append(second[j])
            j+=1

    while i < n:
        result.append(first[i])
        i+=1
    while j < m :
        result.append(second[j])
        j+=1

    return result
        
