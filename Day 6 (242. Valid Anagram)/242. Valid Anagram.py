def isAnagram( s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
                return False
        else:
                ascii=96
                for i in range(26):
                        ascii=ascii+1
                        if t.count(chr(ascii))==s.count(chr(ascii)):
                                continue
                        else:
                                return False
                        
                return True


print(isAnagram("anagram","nagaram"))