
#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    dup_s=''
    temp = n//len(s)
    temp_2 = n%len(s)
    print(temp,temp_2)
    dup_s = s*temp
    dup_s = dup_s + s[:temp_2]
    print(dup_s.count('a'))

s = input().strip()

n = int(input().strip())
repeatedString(s,n)
