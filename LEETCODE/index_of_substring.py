def index_of_substring(haystack, needle):
    index = -1 
    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                break
            if j == len(needle) - 1 : # we reach the end of the needle and they are equal. 
                return i 
    return index

h1 ="sadbutsad"
n1 ="sad"

h2 = "leetcode"
n2 = "leeto"

print(index_of_substring(h1,n1))