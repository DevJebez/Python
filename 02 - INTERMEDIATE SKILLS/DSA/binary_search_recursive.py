def  recursive_binary_search(List,target):
    if len(List) == 0:
        return False
    else:
        mid = (len(List))//2
        if List[mid] == target:
            return True
        else:
            if List[midpoint]<target:   
                return recursive_binary_search(List[mid+1:],target)
            else:
                return recursive_binary_search(List[:mid],target) # its List[:mid] cause not mid-1 cause internally
                #it is done as mid-1 as slicing always upto n-1
def verify(result):
    print("Target found : ",result)
numbers = [1,2,3,4,5,6,7,8,9]
result = recursive_binary_search(numbers,5)
verify(result)