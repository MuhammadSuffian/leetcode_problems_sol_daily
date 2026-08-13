def numberOfEmployeesWhoMetTarget():
     hours = [5,1,4,2,2] 
     target = 6
     
     count=0
     for i in hours:
          if i>=target:
               count+=1
     return count


print("Output: "+ str(numberOfEmployeesWhoMetTarget()))