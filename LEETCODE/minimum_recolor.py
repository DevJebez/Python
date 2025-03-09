def solution(blocks,k):
    l = 0 
    r = k
    count_W= 0 
    min_operations = 0
    for i in range(k):
        if blocks[i] == "W":
            count_W +=1
    if count_W <= min_operations:
        min_operation = count_W
    while r< len(blocks):
        print("True")
        if blocks[l] == 'W':
            count_W -= 1
        if blocks[r] == 'W':
            count_W += 1
        print(f"min_operations : {min_operations}\ncount_W:{count_W}")
        if count_W <= min_operations:
            min_operations = count_W 
        r+=1 
        l+=1
    return min_operations


blocks1 = "WBBWWBBWBW"
blocks2 = "WBWBBBW"
blocks3 = "WBWW"
blocks4 = "BWWWBB"
k1 = 7
k2= 2
k3 = 2
k4 = 6
sample_test  ="WBBWWBBWBWWBBWWBBWBWWBBWWBBWBWWBBWWBBWBWWBBWWBBWBWWBBWWBBWBWWBBWWBBWBWWBBWWBBWBWWBBWWBBWBWWBBWWBBWBW"
print(solution(blocks4,k4))