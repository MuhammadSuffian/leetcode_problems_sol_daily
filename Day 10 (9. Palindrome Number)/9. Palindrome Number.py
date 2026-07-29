
def isPalindrome():
        x=121
        x=str(x)
        isPalindrome=True
        for i in range(int(len(x)/2)):
             if(x[i]!=x[len(x)-i-1]):
                isPalindrome=False
                break
        return isPalindrome
        
print("Word: "+str(isPalindrome()))

