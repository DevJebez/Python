import math
def printFactors(N):
    x = 1
    print(math.sqrt(N))
    while x <= math.sqrt(N):
        print("x:",x)
        if N % x == 0:
            print("Yes n%x == 0")
            if N / x == x :
                print ("N/x ==",x,end=" ")
            else:
                print ('x : ',x , int(N/x), end=" ")
        x = x + 1
 
N = int(input("Enter the value of N"))
printFactors(N)