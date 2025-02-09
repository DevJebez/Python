

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
# 1 - 0,4 2 -3,3

""" 4 8 12  
    6,9,12"""
""" 3,6,9,12
    6,8,10,12""" 

""" 21 6 47 3 """
def kangaroo(x1, v1, x2, v2):
    if x1 <= 10000 and x2 <= 10000 and v1 <= 10000 and v2 <=10000 and v1 >= 1 and v2>=1:
        if x2>x1 and v2>v1:
            return "NO" 
        else:
            i=1
            j=1
            s1 = (x1+v1)
            s2 = (x2+v2)
            while i>0 and j>0:
                if s1 != s2:
                    s1 += v1
                    s2 += v2 
                    i+=1
                    j+=1
                else:
                    i = -1
                    j= -1
            return 'YES'
            
            



            
            


        
if __name__ == '__main__':
    

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    kangaroo(x1, v1, x2, v2)
