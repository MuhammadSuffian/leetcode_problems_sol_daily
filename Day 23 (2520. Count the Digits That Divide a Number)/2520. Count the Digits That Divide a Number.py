
def countDigits():
    num="1248"
    count=0
    for i in num:
        if (int(num)%int(i))==0:
            count+=1
    return count

print("Output: "+ str(countDigits()))    