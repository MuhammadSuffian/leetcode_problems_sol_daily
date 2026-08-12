def firstPalindrome():
    words =["abc","car","ada","racecar","cool"]

    for w in words:
        isPalindrome=True
        for i in range(int(len(w)/2)):
            # print(str(w[i])+"  "+str(w[len(w)-1]))
            if(w[i]!=w[len(w)-i-1]):
                isPalindrome=False
                break
        if(isPalindrome):
            return isPalindrome
        
print("Word: "+str(firstPalindrome()))


# def isPalindrome():
#     word="racecar1"
#     isPalindrome=True
#     for i in range(int(len(word)/2)):
#         # print(str(word[i])+"  "+str(word[len(word)-1-i]))
#         if(word[i]!=word[len(word)-i-1]):
#             isPalindrome=False
#             break
#     return isPalindrome
        
# print("Word: "+str(isPalindrome()))



#leetcode submission"
class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for w in words:
            isPalindrome=True
            for i in range(int(len(w)/2)):
                if(w[i]!=w[len(w)-i-1]):
                    isPalindrome=False
                    break
            if(isPalindrome):
                return w
        return ""
        

        