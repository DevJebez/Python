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
    turns_back = 0
    turns_front = 0
    if p <= n//2:
        for i in range(1+2,n,2):
            turns_front+=1
            if p == i or p == i-1:
                break
    elif p > n//2:
        if n%2 == 0:
            if p == n:
                return turns_back
            else:
                for i in range(n,1,-2):
                    if i ==p  or i ==p-1:
                        return turns_back
                    turns_back+=1
        else:
            for i in range(n,1,-2):
                if i== p or p == i-1:
                    return turns_back
                turns_back += 1
            

        
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
