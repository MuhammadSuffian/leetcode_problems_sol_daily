def xorOperation():
    n=5
    start=0
    count=0
    nums=[]
    xor=0
    while(count!=n):
        nums.append(start+2*count)
        count+=1
        xor=xor^nums[count-1]
    print(nums)
    print(xor)

xorOperation()
