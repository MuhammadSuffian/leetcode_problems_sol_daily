def containsDuplicate( nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))
        # for i in range(len(nums)):
        #         # if nums[i] in nums:
        #         if nums.count(nums[i])>1:
        #                 return True
        #         else: 
        #                 continue
        # return False
                        

print(containsDuplicate([1,2,3,4,1]))
                        
