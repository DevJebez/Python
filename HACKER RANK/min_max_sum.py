
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

#using functions

def miniMaxSum(arr):
    s=[]
    n = len(arr)-1
    for i in range(len(arr)):
        s.append(sum(arr)-arr[n])
        n=n-1
    print(min(s))
    print(max(s))

#without using functions

def w_miniMaxSum(arr):
    mi=ma=arr[0]
    s=0
    for i in arr:
        if i<mi:
            mi = i
        elif i>ma:
            ma=i
        s+=i
    print(s-ma,s-mi)        


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    w_miniMaxSum(arr)
