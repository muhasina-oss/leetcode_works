numbers = [2,7,11,15]

target = 9

left = 0

right = len(numbers)-1

while left<right:
  
  total = numbers[right]+numbers[left]
  
  if total==target:
    
    print(left+1,right+1)
    break
  
  elif total > target:
    
    right-=1
    
  else:
    
    left+=1
