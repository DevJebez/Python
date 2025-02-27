def solution(nums,val):
    pointer1 = 0
    for pointer2 in range(len(nums)):
        if nums[pointer2] != val:
            nums[pointer1] = nums[pointer2]
            pointer1 += 1
    print(f"Nums : {nums}")

nums = [1,2,3,4,5,2,2,2,4,4,5]
val = 2 

solution(nums,val)
