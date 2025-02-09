def selection_sort(data,n):
    for i in range(0,n-1):
        min = data[i]
        pos = i #pointer  
        for j in range(i+1,n):
            if data[j] < min :
                min = data[j]
                pos = j
        data[i],data[pos] = data[pos],data[i]
        print(data)
    print("Sorted List :")
    print(data)
data = [4,3,6,8,1]
selection_sort(data,len(data))