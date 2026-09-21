nums = [2,3,5,7,9]

target = 8

for num in nums:
  
  difference = target - num
  
  if difference in nums and difference!=num:
    
    print(nums.index(num),nums.index(difference))
    
    break
  