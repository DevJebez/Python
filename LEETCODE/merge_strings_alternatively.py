def merge_strings(s1,s2):
    i = 0
    result = ''
    while i < min(len(s1),len(s2)):
        result += s1[i] + s2[i]
        i += 1 
    if len(s1) > len(s2):
        result += s1[i:]
    else:
        result += s2[i:]
    return result 


def merge_strings1(s1,s2):
    m = min(len(s1),len(s2))
    r = ''
    for i in range(m):
        r += s1[i]+ s2[i]
    r += s1[i]+ s2[i]
    return r



s1 = 'abcdefg'
s2 = 'pqrst'


print(merge_strings(s1,s2))
print(merge_strings1(s1,s2))