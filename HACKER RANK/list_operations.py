if __name__ == '__main__':
    N = int(input())
    arr = [] 
    for i in range(N):
        x = input().strip().split()
        if x[0] == 'append':
            arr.append(int(x[1]))
        if x[0] == 'print':
            print(arr)
        if x[0] == 'remove':
            arr.remove(int(x[1]))
        if x[0] == 'insert':
            arr.insert(int(x[1]), x[2])
        if x[0] == 'sort':
            arr.sort() 
        if x[0] == 'reverse':
            arr.sort(reverse=True)
        if x[0] == 'pop':
            arr.pop() 
                