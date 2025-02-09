#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    first =1
    last = n
    turns_front =0
    turns_back =0
    for i in range(first+2,last,2):
        if first == p:
            break
        else:
            turns_front +=1
            if i==p or p == i-1:
                break
    for i in range(last-2,first,-2):
        if n%2==0 and p == n:
            break
        elif n%2 == 0:       
            turns_back +=1
            if i==p or p== i-1:
                break
        else:
            if last == p or p == last -1:
                break 
            turns_back +=1
            if i==p or p == i+1:
                break
    return min(turns_back,turns_front)            
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
