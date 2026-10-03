nums = [2, 0, 2, 1, 1, 0]

# # Result
# [0, 0, 1, 1, 2, 2]

left = 0

right = len(nums)-1

i = 0

while i <=right:
      
    if nums[i]==0:
    
      nums[i],nums[left] = nums[left],nums[i]
      
      left+=1
           
    elif nums[i]==2:
      
      nums[i],nums[right] = nums[right],nums[i]
      
      right-=1
      
      i-=1
      
    i+=1
      
print(nums)