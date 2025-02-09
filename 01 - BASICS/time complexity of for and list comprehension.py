import time
def for_loop(n):
    a=[]
    for i in range(n):
        a.append(i**4)
    return a
def list_comprehension(n):
    return [i**4 for i in range(n)]

start = time.time()
g = for_loop(10**9)
endtime = time.time()
print("Time complexity of for loop :",round(endtime - start,2))

start = time.time()
g = list_comprehension(10**9)
endtime = time.time()
print("Time complexity of list comprehension :",round(endtime - start),2)
