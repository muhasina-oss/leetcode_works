nums = [-1,0,1,2,-1,-4]

nums.sort()

total =0 

i = 0

while i < len(nums)-2:
  
  j = i+1
  
  k = len(nums)-1
  
  while j<k:
    
    total = nums[i]+nums[j]+nums[k]
    
    if total==0:
      
      print(nums[i],nums[j],nums[k])
      
      j+=1
      
      k-=1
      
    elif total<0:
      
      j+=1
      
    else:
      
      k-=1
      
  i+=1
      
      
