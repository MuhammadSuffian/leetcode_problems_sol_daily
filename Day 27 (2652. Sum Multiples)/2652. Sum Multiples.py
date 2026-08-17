def sumOfMultiples():
    print("Sol")
    n=3
    sum=0
    if(n<3):
        return 0
    for i in range(n+1):
        if i%3==0 or i%5==0 or i%7==0:
            sum=sum+i
            print(i)
    print("Sum: "+ str(sum))

sumOfMultiples()