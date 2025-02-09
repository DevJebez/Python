"""def adding_binary(A,B):
    C=[]
    carry=0
    for i in range(len(A)):  #0 to n-1
        element = (A[i] + B[i] + carry)
        if element >=2:
            C.append(element%2)
            carry = 1
        else:
            carry = 0
    C[len(A)] = carry
    print(C[::-1])
"""


def adding_binary(A,B):
    carry = 0 
    C=[]
    i , j = len(A)-1 , len(B) -1
    while i>=0 and j>=0 and carry:
        total = carry 
        if i>=0:
            total+= a[i]
            i-=1
        if j>=0:
            total += b[j]
            j-=1 
        result = total%2
        C.append(result)
        carry = total //2
    print(C[::-1])

adding_binary([1,0,0,1],[1,1,1,1])       




            

