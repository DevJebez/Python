a=int(input())
if a>=100 or a<=999:
    s=a//10
    s=a%10
    if s%3==0:
        print("Trendy Number")
    else:
        print("Not a Trendy Number")
else:
    print("Invalid Number")
