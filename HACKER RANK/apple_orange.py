

import math
import os
import random
import itertools
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    g = [s,t,a,b]
    apples_r, oranges_r = [],[]
    total_apples , total_oranges = 0,0
    if max(g) == b:
        for i in range(len(apples)):
            apples[i] += a
            apples_r.append(apples[i])
        for j in range(len(oranges)):
            oranges[j] += b 
            oranges_r.append(oranges[j])
        print(apples_r)
        print(oranges_r)
        print("s",s)
        print("t",t)

        for i in apples_r:
            if i>=s and i <=t:
                total_apples+=1
        for j in oranges_r:
            if j <=s and j>=t:
                total_oranges+=1
    print(total_apples)
    print(total_oranges)


    
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
