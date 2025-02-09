""" 
Monotonic stack - either increasing or decreasing

[1] Monotonically increasing stack - Increasing from bottom
[2] Monotonically decreasing stack - Decreasing from bottom

Algorithm for monotonically increasing stack 
1. Iterate the given list of elements one by one
    1.1 Before pushing into the stack pop elements one by one until
        [1] Stack is empty
        [2] Stack's top is bigger than the element to be inserted 
    1.2 Then push the element into the stack 

"""

def increasing_stack(arr,n):
    stack = []
    for i in range(n):
        #two conditions - 
        #1. stack is empty 
        #2. All bigger elememts are popped 
        while len(stack) > 0  and stack[len(stack)-1] > arr[i]:
            stack.pop() 
        stack.append(arr[i])
    print("Input array : ",arr)
    print("Stack : ",stack)
def decreasing_stack(arr,n):
    stack = []
    for i in range(n):
        #two conditions - 
        #1. stack is empty 
        #2. All smaller elememts are popped 
        while len(stack) > 0  and stack[len(stack)-1]  < arr[i]:
            stack.pop() 
        stack.append(arr[i])
    print("Input array : ",arr)
    print("Stack : ",stack)

# solving problems 
#Next greater element in an array

def next_greater_element(numbers):
    stack = []
    result = [-1] * len(numbers)
    for i in range(len(numbers)):
        while stack and numbers[-1] > numbers[stack[-1]]:
            index = stack.pop()
            result[index] = numbers[i]
        stack.append(i)
        

    return result
numbers = [8,5,9,77,109]
print(next_greater_element(numbers))
print("Input Array: ", numbers)

    



