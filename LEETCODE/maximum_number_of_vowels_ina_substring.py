def brute_force(s,k):
    vowels = 'aeiou'
    count = 0
    res = 0
    for i in range(len(s) - k + 1 ):
        count = 0
        for j in range(k):
            if s[i+j]  in vowels: 
                count+=1
        if(count > res):
            res = count
    return res

#using sliding window technique
def solution(s,k):
    n = len(s)
    l = 0 
    r = k
    count = 0 
    res= 0
    vowels = "aeiou"
    for i in range(k):
        if s[i] in vowels:
            count += 1
    if count > res:
        res = count
    while r < n:
        if(s[l] in vowels):
            count -= 1
        if(s[r] in vowels):
            count +=1
        if count > res:
            res = count
        l+=1 
        r+=1
    return res
s1 = "abciiidef"
k1 = 3
#s = "leetcode", k = 3
#s = "aeiou", k = 2
s = "tryhard"
k = 4

print(solution(s1,k1))
