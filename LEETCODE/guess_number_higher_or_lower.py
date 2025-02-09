def guess(result,pick):
    if result == pick:
        return 0
    elif result > pick :
        return -1 
    elif result < pick :
        return 1 

def higher_or_lower(n,pick):
    high = n 
    low = 1
    while high >= low:
        mid = (high+low)//2
        print(mid)
        if guess(mid,pick) == 0:
            return mid == pick
        elif guess(mid,pick) == 1:
            low = mid+1
        elif guess(mid,pick) == -1:
            high = mid-1
    return False
print(higher_or_lower(100,5)) 

