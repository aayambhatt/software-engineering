def remove_nonints(nums):
    nonint_list = []
    for num in nums:
        if type(num)==int:
            nonint_list.append(num)

    return nonint_list
