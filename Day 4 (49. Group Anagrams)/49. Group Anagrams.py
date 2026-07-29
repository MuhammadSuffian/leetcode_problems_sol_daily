from collections import defaultdict

def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)
        print(groups)
        for s in strs:
            key = tuple(sorted(s))
            groups[key].append(s)

        return list(groups.values())

#         rlist=[]
#         for str in strs:
#                 temp_list=[str]
#                 strs.remove(str)
#                 for t in strs:
#                         if isAnagram(str,t):
#                                 temp_list.append(t)
#                                 strs.remove(t)
#                 rlist.append(temp_list)
#         if strs:
#             rlist.append(strs)
#         return rlist



#         # print(len(strs))
#         # strs.remove(strs[0])
#         # print(len(strs))

# def isAnagram( s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         if len(s)!=len(t):
#                 return False
#         else:
#                 ascii=96
#                 for i in range(26):
#                         ascii=ascii+1
#                         if t.count(chr(ascii))==s.count(chr(ascii)):
#                                 continue
#                         else:
#                                 return False
                        
#                 return True


print(groupAnagrams(["a","a","a"]))
        