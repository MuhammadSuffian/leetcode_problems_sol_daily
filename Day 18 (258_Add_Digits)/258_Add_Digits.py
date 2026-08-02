def addDigits(num):
    print("Input: "+str(num))
    len1=len(str(num))
    
    while (len1!=1):
        str1=str(str(num))
        num=0
        for i in str1:
            num=int(i)+num   
        len1=len(str(num))
    print("Output:"+ str(num))    

addDigits(38)
