# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product 

K,M = map(int,input().split())
lists = []
for _ in range(K):
    data = list(map(int, input().strip().split()))
    lists.append(data[1:])
    
combinations = product(*lists)
max_value = 0
for i in combinations:
    value = sum(x**2 for x in i) % M
    max_value = max(value,max_value)
    
print(max_value)