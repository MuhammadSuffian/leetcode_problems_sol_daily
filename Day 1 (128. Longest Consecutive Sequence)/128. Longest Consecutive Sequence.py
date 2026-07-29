def longestConsecutive(nums):
        unique_nums = list(set(nums))
        length=0
        print("Unique Set",unique_nums)
        print("Min:",min(unique_nums))
        print("Max:",max(unique_nums))
        for i in unique_nums:
                print("Currenlty on ",i)
                if i==min(unique_nums):
                        continue
                
                else:
                        # print(i)
                        print(i-unique_nums[i-1])
                        if i-unique_nums[i-1]==1:
                               length=length+1
                        else:
                                length=0 
        return length

print("Length:",longestConsecutive([100,4,200,1,3,2]))

