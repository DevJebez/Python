def palindrom(n):
    reverse = 0
    temp =n
    while(n>0):
        reverse = reverse*10 + n%10
        print(reverse)
        n//=10
    if temp == reverse :
        print("Palindrome")
    else:
        print("Not a palindrom")

n= int(input("Enter a number :" ))
palindrom(n)
