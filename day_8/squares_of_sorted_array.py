nums = [-4,-1,0,3,10]

squares=[0]*len(nums)

left = 0

position = len(nums)-1

right = len(nums)-1

while left<=right:
  
  if abs(nums[left])<abs(nums[right]):
    
    # squares.append(nums[right]**2)
    
    squares[position]=nums[right]**2
     
    right-=1
    
    position-=1
    
  else:
    
    squares[position]=nums[left]**2
    
    position-=1
    
    left+=1
    
print(squares)
    
    
    