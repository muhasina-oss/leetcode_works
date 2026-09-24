nums = [0,1,0,3,12]

moved_list = []

count = 0

for num in nums:
  
  if num==0:
    
    count+=1
    
  else:
    
    moved_list.append(num)
    
for c in range(0,count):
  
  moved_list.append(0)
  
print(moved_list)
    
