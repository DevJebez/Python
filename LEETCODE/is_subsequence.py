def is_subsequence(s,t):
    i = 0 
    j = 0
    new = ''
    while i< len(s) and j < len(t):
        if s[i] == t[j]:
            new += t[j]               
            i+=1 
            j+=1
        else:
            j+=1
    if new == s:
        return True
    else:
        return False
    
def is_subsequence1(s,t):
    if s == "":
        return True 
    if t == "":
        return False 
    i = 0 # s pointer
    for j in range(len(t)): # t pointer
        if s[i] == t[j]:
            i+=1 
            if i == len(s):
                return True 
    return False 
    