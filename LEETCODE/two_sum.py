def two_sum(nums,target):
    result = {}
    for i, num in enumerate(nums):
        if target-num in result:
            return result[target-num],i
    result[num] = i
if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for i in range(n)]
    t = int(input())
    print(two_sum(arr,t))
