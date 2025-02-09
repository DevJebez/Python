
def MaxCoins(n,nums):
    d={}
    max_coins = 0
    for i in range(n):
        x = nums[i]%10 + nums[i] // 10
        if x not in d:
            d[x] = 1
            if d[x] > max_coins:
                max_coins = d[x]
        else:
            d[x] += 1
            if d[x] > max_coins:
                max_coins = d[x]
    print(d)
    return max_coins



def main():
    n = int(input())
    nums = list(map(int,input().split()))
    print(MaxCoins(n,nums))
main()