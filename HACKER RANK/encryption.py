import math
def encryption_github(s):
    L = len(s)
    rows = int(math.floor(L**(0.5)))
    columns = int(math.ceil(L**(0.5)))
    output = ""
    for i in range(columns):
        k = i
        for j in range(k,L,columns):
            output+=s[j]
            print("output :",output)
        output+=" "
    return output
   # Print " " before starting new iteration
def encryption2(s):
    s=s.replace(" ","")
    sqrt_len = math.sqrt(len(s))
    grid = []
    grid_row = math.floor(sqrt_len)
    grid_col = math.ceil(sqrt_len)
    current_length = 1
    while current_length < len(s):
        grid.append(s[current_length-1:current_length+grid_row])
        current_length += grid_row+1
    ans =""
    max_len = max(len(s) for s in grid)
    
    # Iterate through each column index
    for i in range(max_len):
        for s in grid:
            # Print character if within bounds, else print a space
            if i < len(s):
                ans += s[i]
        ans+=" "  # Newline after each column
    return ans
def encryption_mine(s):
    l = len(s)
    res = ''
    step = math.ceil(math.sqrt(l))
    for i in range(step):
        while i < l:
            res += s[i]
            i+=step 
        res+= " "
    return res 





if __name__ == '__main__':
    inpu = input("Enter a string to encrpt :")
    result = encryption_mine(inpu)
    print(result)

