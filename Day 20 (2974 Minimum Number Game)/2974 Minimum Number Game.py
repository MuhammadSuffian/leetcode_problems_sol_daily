def numberGame(nums):
    a=[2,5] 
    visited=[]
    # while a:
    for i in range(int(len(a)/2)):
        min1=min(a) #Alice picked 
        a.remove(min1)
        min2=min(a) #Bob picked
        a.remove(min2)
        visited.append(min2)
        visited.append(min1)
    return visited



print("output: "+str(numberGame([5,4,2,3])))