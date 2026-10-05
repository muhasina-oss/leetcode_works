height = [1,8,6,2,5,4,8,3,7]

left = 0

right = len(height)-1

max_water = 0 

while left < right:
  
  width = right - left
  
  hght = min(height[left],height[right])
  
  water = width * hght
  
  if max_water < water:
    
    max_water = water
  
  if height[left]<height[right]:
    
    left+=1
    
  else:
    
    right-=1
    
print(max_water)