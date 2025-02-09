
def circularArrayRotation(a, k, queries):
    if len(a)% k ==0:
        for i in range(len(queries)):
            queries[i] = a[queries[i]]
            return queries
    else:
        for i in range(k):
            temp = a[-1]
            for j in range(n-1,-1,-1):
                a[j] = a[j-1]
            a[j] = temp
        print("array after rotation",a)
        for i in range(len(queries)):
            queries[i] = a[queries[i]]
        return queries
def circularArrayRotation_optimized(a,k,queries):
    if k%n == 0:
        for i in range(len(queries)):
            queries[i] = a[queries[i]]
        return queries
    else:
        a = a[k%n:]  + a[:k%n]
        print("Array after rotation",a)
        for i in range(len(queries)):
            queries[i] = a[queries[i]]
        return queries
a = list(map(int,input("Enter the array:").split()))
n = int(input("Enter number of array elements : "))
k = int(input("Enter number of rotations:"))
queries = list(map(int,input("Enter queries:").split()))


result = circularArrayRotation_optimized(a,k,queries)
print(result)