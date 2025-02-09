def canPlaceFlowers(n,flowerbed):
    planted = 0
    for i in range(len(flowerbed)):
        if planted != n:
            current = flowerbed[i]
            back = 0 if i-1 < 0 else flowerbed[i-1]
            front = 0 if i+1 == len(flowerbed) else flowerbed[i+1]
            if current == 1:
                i += 1
            elif current == 0 and back == 0 and front == 0:
                print("I' th plant :",i)
                flowerbed[i] = 1 
                print(flowerbed,'\n')
                planted += 1
        elif planted == n:
            print("Planted :",planted)
            print(f"Flowerbed final :{flowerbed}")
            break 
    '''if planted == n:
        return flowerbed
    else: 
        return flowerbed'''
    
flowerbed = [1,0,0,0,0,0,0]
n= 3
canPlaceFlowers(n,flowerbed)
