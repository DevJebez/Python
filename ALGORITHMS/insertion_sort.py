def insertion_sort(data,n):
    for i in range(1,n):
        temp = data[i]
        j = i  - 1
        while temp<data[j] and j>=0:
            data[j+1] = data[j]
            j = j - 1
            print(data)
        data[j+1] = temp 
        print(data)
    print("Sorted list:")
    print(data)
insertion_sort([5,4,3,2,1],5)