

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    
    if s[-2:] == "AM":
        if int(s[:2]) == 12:
            s="00"+s[2:8]
            return (s)
        else:
            return (s[:-2])

    elif s[-2:] == 'PM':
        if int(s[:2]) == 12:
            print(s[0:8])
        else:
            return (str(int(s[:2])+12)+s[2:8])



if __name__ == '__main__':
    

    s = input()

    result = timeConversion(s)
    print(result)
