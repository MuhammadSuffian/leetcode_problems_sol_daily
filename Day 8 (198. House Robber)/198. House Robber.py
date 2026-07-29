def rob():
    nums = [1,2,3,1]
    r1=0
    r2=0
    for i in nums:
        temp=max(r1+i,r2)
        r1=r2
        r2=temp
    return r2




print("Output: "+str(rob()))