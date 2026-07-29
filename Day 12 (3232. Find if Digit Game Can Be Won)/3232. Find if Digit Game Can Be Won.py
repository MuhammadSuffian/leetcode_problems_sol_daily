def canAliceWin():
    nums = [1,2,3,4,10]
    
    singleDigitSum=0
    doubleDigitSum=0
    for i in nums:
        if(len(str(i))==1):
            singleDigitSum=singleDigitSum+i
        else:
            doubleDigitSum=doubleDigitSum+i
    if(singleDigitSum==doubleDigitSum):
        return False
    else:
        return True



print("Output: "+str(canAliceWin()))