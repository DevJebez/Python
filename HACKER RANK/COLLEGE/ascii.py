k=int(input())
sq=k*k
temp=0
g=len(str(sq))//2
if g%2==0:
    temp=sq%(10*g)
    print(temp)
    sq=sq//g
    if temp+sq==k:
        print("Karprekar number")
