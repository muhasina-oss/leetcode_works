fruits = [1,2,3,2,2]

l,max_result = 0,0

count = {}

for r in range(len(fruits)):
  
  count[fruits[r]] = count.get(fruits[r],0)+1
  
  while len(count)>2:
    
    count[fruits[l]] -=1
    
    if count[fruits[l]]==0:
      
      del count[fruits[l]]
      
    l+=1
    
  max_result = max(max_result,r-l+1)
  
print(max_result)