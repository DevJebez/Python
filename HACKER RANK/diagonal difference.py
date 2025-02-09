import math 

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    rl,lr=0,0
    size = len(arr)-1
    print("len :",size)
    g = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                lr += arr[i][j]
                g+=1
                print("lr:",lr,"\n","g:",g)
            if j == size:
                print("calculating right to left diagonal")
                rl += arr[i][j]
                size -=1
                print("rl:",rl,"\n","size",size)
    return abs(lr-rl)
            


    

if __name__ == '__main__':
    
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    print(arr)

    result = diagonalDifference(arr)
    print("the result : ", result)
