nums = [1, 2, 2, 3, 3, 4, 5]

p1 = 0
p2 = 1

while p2 < len(nums):

  if nums[p1] != nums[p2]:
    
      p1 += 1
      
      nums[p1] = nums[p2]

  p2 += 1

print(p1 + 1)