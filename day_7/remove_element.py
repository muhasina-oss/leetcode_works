nums = [0,1,2,2,3,0,4,2,2]

val = 2

p1 = 0

p2 = len(nums)-1    


while p1<p2:
  
  if nums[p1]==val:
    
    if nums[p2]!=val:
      
      nums[p1],nums[p2]=nums[p2],nums[p1]
      
      p1+=1
      
      p2-=1
      
    else:
      
      p2-=1
      
      
  else:
    
    p1+=1
    
print(nums)
      
