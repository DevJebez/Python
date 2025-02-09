"""
LIST COMPREHENSIONS
"""

#SYNTAX : newlist = [expression for item in iterable if condition == True]

x=[i for i in range(10) if i%2==0]
print(x)

y=['Jebez',"Joel",'Vishal','Ashim','Harrish']
y1  = [name if name == 'Jebez' else "others" for name in y]
print(y1)

matrix = [[j for j in range(3)]for i in range(3)]
print(matrix)

letters = [i for i in "Jebez Oswald K"] 
print(letters)


#time analysis
import time
def for_loop(n):
    a=[]
    for i in range(n):
        a.append(i**4)
    return a
def list_comprehension(n):
    return [i**4 for i in range(n)]

start = time.time()
g = for_loop(10**6)
endtime = time.time()
print("Time complexity of for loop :",round(endtime - start,2))

start = time.time()
g = list_comprehension(10**6)
endtime = time.time()
print("Time complexity of list comprehension :",round(endtime - start),2)

n=3
permutations = [i for i in range(n) for j in range(n) for k in range(n)]
print(permutations)