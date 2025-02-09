from collections import Counter

def anagram_solution1(s,t):
    
    if len(s) != len(t):
        return False

    countS,countT = {},{}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i],0) # to avoid key error
        countT[t[i]] = 1 + countT.get(t[i],0)
    for c in countS:
        if countS[c] != countT.get(c,0):
            return False
    return True


def anagram_solution2(s,t):
    return Counter(s) == Counter(t)

def anagram_solution3(s,t):
    return sorted(s) == sorted(t)


def demo_collections(c = "JosephsCollegeOfEngineering"):
    counter_c = Counter(c)
    print(counter_c)

s = 'anagram'
t = 'aangram'

if anagram_solution2(s,t) == True:
    print("Are anagram")
else:
    print("Anagram")    

#demo of Counter in collections
demo_collections()
