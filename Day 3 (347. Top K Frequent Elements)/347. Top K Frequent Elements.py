def topKFrequent( nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        rList=[]
        unique_items = set(nums)
        for num in unique_items:
                if nums.count(num)>=k:
                        rList.append(num)
        return rList
                        
        
print(topKFrequent([1,2,1,2,1,2,3,1,3,2], k = 2))