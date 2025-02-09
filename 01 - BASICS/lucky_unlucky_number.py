def lucky_numbers(u,l,d):
    lucky=[]
    for i in range(u,l):
        temp = i
        s=0
        x = temp%10
        while temp>0 and x!= d:
            rem1 = temp%10
            s+=rem1
            rem2 = (temp//10)%10
            if rem2 > rem1:
                temp//=10
            else:
                break



