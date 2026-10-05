nums = [-2,1,-3,4,-1,2,1,-5,4]

maxSum = nums[0]

currentSum = 0

for num in nums:
  
  if currentSum < 0 :
    
    currentSum = 0
    
  currentSum+=num
  
  maxSum = max(currentSum,maxSum)
  
print(maxSum)

