# binary search 

""" Algorithm 
1.Sort the given list
2.Calculate mid index position and check list[mid] == target . If yes return mid
3.If no check list[mid] > lower bound ; lower bound = mid . ELSE upper bound = mid 
4.Repeat step 2 and 3 until the value is returned 
""" 

'''
#using for loop 
def binary_search(List,target):
    lower_bound = 0
    upper_bound = len(List)-1
    mid = (lower_bound + upper_bound)//2
    for i in range(lower_bound,len(List)):
        if List[mid] == target :
            return mid
        elif List[mid] > target :
            upper_bound = mid 
        elif List[mid] < target:
            lower_bound = mid 
        mid = (lower_bound + upper_bound)//2
    

List = [2,4,5,9,77,666,999,1056]
result = binary_search(List ,666)
if result is not None:
    print("Element found at index : ",result)
else : 
    print("Element not found in the list")
'''
#using while loop 

def binary_search_while(List,target):
    lower_bound = 0
    upper_bound = len(List)-1
    while lower_bound <= upper_bound:
        mid = (lower_bound + upper_bound)//2
        if List[mid] == target:
            return mid 
        else: 
            if List[mid] < target:
                lower_bound = mid +1
            else: 
                upper_bound = mid -1 
    return None 
List = [1,5,55,99,745,1236,7895,8888]
result = binary_search_while(List,8889)
if result is not None :
    print("Element at the index : ",result )
else:
    print("not found ")
