def longest_common_prefix(strs):
    strs = sorted(strs)
    first,last = strs[0], strs[-1]
    min_length = min(len(first),len(last))
    current_index = 0
    while current_index < min_length and first[current_index] == last[current_index]:
        current_index +=1 
    if current_index == 0:
        return ""
    else:
        return first[:current_index]


test_case1 = ["flower","flow","flight"]
test_case2 = ["dog","racecar","car"]
print(longest_common_prefix(f"Output:{test_case1}"))
print(longest_common_prefix(f"Output:{test_case2}"))