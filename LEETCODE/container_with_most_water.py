def container_with_most_water(nums):
    max_rectangle = 0 
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            amount = min(nums[i],nums[j]) * (j-i)
            max_rectangle = max(max_rectangle,amount)
    return max_rectangle

print(container_with_most_water([1,8,6,2,5,4,8,3,7]))


 

