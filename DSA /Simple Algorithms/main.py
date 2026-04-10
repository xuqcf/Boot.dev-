def summed(nums):
    
    sum = 0

    if len(nums) == 0:
        return 0

    for num in nums:
        sum += num
    return sum
