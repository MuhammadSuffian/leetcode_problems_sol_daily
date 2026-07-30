def arraySign():
    nums = [-1,-2,-3,-4,3,2,1]

    
    product=1
    for i in nums:
        product=product*i
    
    if(product>0):
        return 1
    elif(product==0):
        return 0
    else: 
        return -1





print("Output: "+str(arraySign()))