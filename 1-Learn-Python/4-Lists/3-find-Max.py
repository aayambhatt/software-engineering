def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num>max_so_far:
            max_so_far = num
    return max_so_far
        
nums = [4,5,6,7,1,34,7,85,32,1]
print(find_max(nums))
