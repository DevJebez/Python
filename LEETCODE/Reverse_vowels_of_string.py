def Reverse_vowels_of_string(string):
    n = len(string)
    d = []
    v_count = 0
    for i in range(n):
        if string[i].lower() in 'aeiou':
            d.append(i)
            v_count += 1
    string_list = list(string)
    d_copy = sorted(d,reverse= True)

    for i in range(v_count):
        string_list[d[i]] = string[d_copy[i]]
    return ''.join(string_list)
    
print(Reverse_vowels_of_string("IceCreAm"))
    


def method1(string):
    v = [] 
    for i in string:
        if i in 'AEIOUaeiou':
            v.append(i) 
    result = ''
    for i in string:    
        if  i in 'AEIOUaeiou':
            result += v.pop()
        else:
            result += i
    return result
print(method1("Leetcode"))


def method2(string):
    v = [i for i in string if i in 'AEIOUaeiou']
    result = [i if i not in 'AEIOUaeiou' else v.pop() for i in string]
    return ''.join(result)

print(method2("Leetcode"))