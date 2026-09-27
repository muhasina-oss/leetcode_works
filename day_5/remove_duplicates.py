nums = [1,2,2,3,3,4,5]

p1 = len(nums)-1


while p1-1>=0:
  
  if nums[p1]==nums[p1-1]:
    
    nums.remove(nums[p1])
    
  p1-=1
  
print(len(nums))
  
  