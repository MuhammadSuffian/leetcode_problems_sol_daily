def sortedSquares():
    nums = [-4,-1,0,3,10]
    output=[]
    for i in nums:
        output.append(i*i)
    output.sort()
    print(output)

sortedSquares()
