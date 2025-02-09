import math
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    p,ne,z=0,0,0
    for i in arr:
        if i>0:
            p+=1
        if i<0:
            ne+=1
        if i==0:
            z+=1
    print("{:.6f}".format(p/n))
    print("{:.6f}".format(ne/n))
    print("{:.6f}".format(z/n))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
