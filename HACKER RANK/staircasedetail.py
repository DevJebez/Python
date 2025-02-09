

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    c=n
    c-=1
    print(n)
    for i in range(n):
        for j in range(n):
            if j == c:
                print("#"*(i+1))
                c-=1
            if j!=c:
                print("1",end="")
        print()
def staircase(n):
    c = n-1
    
    for i in range(n):
        for j in range(n):
            if j == 0:
                print(" "*c,end="")
            if j == c:
                print("#"*(i+1),end="")
                c-=1
        print()


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)