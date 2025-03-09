def valid_paranthese(s):
    stack = []
    for i in s:
        if len(stack) == 0 and i in ")}]":
            return False
        if i in '{[(':
            stack.append(i)
            print(stack)
        else:
            top = stack[-1]
            print(stack)
            if (len(stack) != 0) and (top == '{' and i == '}') or (top == '[' and i == ']') or (top == '(' and i == ')'):
                stack.pop()
            else:
                return False 
    return len(stack)
s = ")"
print(valid_paranthese(s))



def revision(arr):
    stack = []
    for i in arr:
        if len(stack) == 0 and i in ")}]":
            return False
        if i in "([{":
            stack.append(i)
        else:
            top = stack[-1]
            if len(stack) !=  0 and (top == i):
                stack.pop()
            else:
                return False
            
def revision1(s):
    stack = [] 
    closeToOpen = {"}":"{", "]": "[",")":"("}
    for i in s:
        print(i)
        print(i in closeToOpen)
        if i in closeToOpen:
            if stack and stack[-1] == closeToOpen[i]:
                stack.pop()
            else:
                return False 
        else:
            stack.append(i)
    return True if not stack else False

print(revision1("{}"))