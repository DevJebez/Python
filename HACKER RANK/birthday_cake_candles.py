

# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    s=0
    m=candles[0]
    for i in range(len(candles)):
        if candles[i] > m:
            m =candles[i]
    for i in candles:
        if i == m:
            s+=1
    return s
if __name__ == '__main__':
    

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)
    print(result)
