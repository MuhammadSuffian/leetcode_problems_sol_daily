def productExceptSelf( nums):
    res=[]
    for i in range(len(nums)):
        temp=1
        for j in range(len(nums)):
            if i!=j:
                temp=temp*nums[j]
        res.append(temp)
    return res

print(productExceptSelf([1,2,3,4]))