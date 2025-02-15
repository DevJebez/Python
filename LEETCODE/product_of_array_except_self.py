def Solution(nums):
    result = [1] * len(nums)
    prefix = 1 
    postfix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    for i in range(len(nums)-1,-1,-1):
        result[i] *= postfix
        postfix *= nums[i]
    return result 


print(Solution([1,2,3,4,5,6,7,8]))
