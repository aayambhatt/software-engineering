def quick_sort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)

        quick_sort(nums, low, pi-1)
        quick_sort(nums, pi+1, high)


def partition(nums, low, high):
    pivot = nums[high] # pivot is last element
    i = low-1 # i is -1, smaller element index

    for j in range(low, high):
        if nums[j] < pivot:
            i+=1
            nums[i], nums[j] = nums[j], nums[i]

     # place pivot in correct position
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i+1
    
