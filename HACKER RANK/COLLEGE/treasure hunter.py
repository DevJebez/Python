n=int(input())
ben=int(input())
black=int(input())
pirates=3
be=int((n*ben)/100)
bl=int(((n-be)*black)/100)
print("long ben's share:",be)
print("Black beard's share percentage:",bl)
print("Pirates share:",(n-(be+bl))//3)
