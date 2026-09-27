nums = [2,2,1,1,1,2,2]

majority = 0

current = 1

num = nums[0]

nums.sort()

for i in range(0,len(nums)-1):
  
  if nums[i]==nums[i+1]:
    
    current+=1
    
    if current>majority:
      
      majority = current
      
      num = nums[i]
    
  else:
    
    current = 1
    
print(num)
    