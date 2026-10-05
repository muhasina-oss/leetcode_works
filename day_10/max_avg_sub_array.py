nums = [1,12,-5,-6,50,3]

k = 4

window_sum_avg = (sum(nums[:k]))/k

max_avg = window_sum_avg

for i in range(k,len(nums)):
  
  window_sum_avg = (window_sum_avg - nums[i-k] + nums[i])/k
  
  if window_sum_avg > max_avg :
    
    max_avg = window_sum_avg
    
print(max_avg)
 