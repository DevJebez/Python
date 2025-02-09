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