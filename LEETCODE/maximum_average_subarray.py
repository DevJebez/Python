
def findMaxAverage(nums, k):
    left = 0
    right = k
    maximum_avg = 0
    while right <= len(nums):
        avg_k = sum(nums[left:right])/k
        left +=1 
        right +=1
        if avg_k > maximum_avg:
            maximum_avg = avg_k
    return maximum_avg 


def findMaxAverage1(nums,k):
    maximum_sum = sum(nums[:k])
    current_sum = sum(nums[:k])
    for i in range(k,len(nums)):
        current_sum += nums[i] - nums[i-k]
        maximum_sum = max(maximum_sum,current_sum)
    return maximum_sum/k
print(findMaxAverage1([1,12,-5,-6,50,3], k = 4))