"""
The XOR operation outputs 1 if the inputs are different, and 0 if they are the same

It can be represented as 

A XOR B = ( A OR B ) AND NOT (A AND B)
"""

x = 10 
y = 11 
print(x,":" ,bin(x)[2:])
print(y,":" ,bin(y)[2:])
result = x ^ y 
print(result)

def manual_xor(a,b):
    result = 0 # to store the result
    bit = 1 # 1->2->4->
    while a>0 and b>0:
        a_bit = a & 1 
        b_bit = b & 1
        xor_bit = (a_bit | b_bit) & ~(a_bit & b_bit)
        result = result | (xor_bit * bit)

        bit = bit<<1
        a = a>>1
        b = b>>1 
    return result

print(manual_xor(x,y))

"""
Given a list of numbers find the total XOR value between all possible subsets. 

Example 2:

Input: nums = [5,1,6]
Output: 28
Explanation: The 8 subsets of [5,1,6] are:
- The empty subset has an XOR total of 0.
- [5] has an XOR total of 5.
- [1] has an XOR total of 1.
- [6] has an XOR total of 6.
- [5,1] has an XOR total of 5 XOR 1 = 4.
- [5,6] has an XOR total of 5 XOR 6 = 3.
- [1,6] has an XOR total of 1 XOR 6 = 7.
- [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28

"""

def solution(values):
     pass 
values = [5,1,6]
solution(values)

