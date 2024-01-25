# monotonic stack either increasing or decreasing strictly

""" 
Algorithm for monotonic increasing stack 
1. Iterate through each element in the array
2. Before pushing elements pop elements in the stack until
    2.1 If stack is not empty
    2.2 Stack's top is bigger than the element to be pushed
3.The push the element
"""


def monotonic_increasing_stack(arr,n):
    stk = []
    for i in range(n):
        while len(stk) > 0 and stk[len(stk)-1] > arr[i]:
            stk.pop()
        stk.append(arr[i])
    print("array : ",arr)
    print("stk : ",stk)
monotonic_increasing_stack([8,2,3,4,5,6,1],6)

def monotonic_decreasing_stack(arr,n):
    stk = []
    for i in range(n):
        while len(stk) > 0 and stk[len(stk)-1] < arr[i]:
            stk.pop()
        stk.append(arr[i])
    print("array : ",arr)
    print("stk : ",stk)
monotonic_decreasing_stack([1,2,3,4,5,6],6)


def next_greater_element(nums):
	stack = []
	result = [-1] * len(nums)
	
	for i in range(len(nums)):
		while stack and nums[i] > nums[stack[-1]]:
			index = stack.pop()
			result[index] = nums[i]
		stack.append(i)
	
	return result

# Example usage
nums = [4, 5, 2, 25, 7, 18]
result = next_greater_element(nums)
print("Input Array: ", nums)
print("Next Greater Elements: ", result)
