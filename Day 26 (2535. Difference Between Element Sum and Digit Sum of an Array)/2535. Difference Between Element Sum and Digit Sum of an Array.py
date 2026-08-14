def differenceOfSum():
    nums = [1,15,6,3]
    element_sum=0
    digit_sum=0
    for n in nums:
        element_sum=element_sum+n
        for k in str(n):
            digit_sum=digit_sum+int(k)

    print("Element Sum: "+ str(element_sum))
    print("Digit Sum: "+ str(digit_sum))
    diff= element_sum-digit_sum
    print("Diff: "+ str(diff))
    return abs(diff)


differenceOfSum()