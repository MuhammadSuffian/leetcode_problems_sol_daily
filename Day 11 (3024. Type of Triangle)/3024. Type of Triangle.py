
def triangleType( nums):
        if ((nums[0] + nums[1] > nums[2]) and 
            (nums[1] + nums[2] > nums[0]) and 
            (nums[2] + nums[0] > nums[1])):

            if (nums[0] == nums[1] == nums[2]):
                return "equilateral"
            elif ((nums[0] != nums[1]) and (nums[1] != nums[2]) and (nums[0] != nums[2])):
                return "scalene"
            elif ((nums[0] == nums[1]) or (nums[1] == nums[2]) or (nums[0] == nums[2])):
                return "isosceles"
        else:
            return "none"
        
print("Type: "+str(triangleType([3,3,3])))