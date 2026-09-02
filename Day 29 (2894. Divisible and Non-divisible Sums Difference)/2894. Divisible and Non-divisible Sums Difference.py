def differenceOfSums():
    n=10
    m=3
    i=1
    num1=0
    num2=0
    while(i!=n+1):
        if(i%m!=0):
            num1=num1+i
        else:
            num2=num2+i
        i+=1
    print(num1)
    print(num2)
    print(num1-num2)
   


differenceOfSums()