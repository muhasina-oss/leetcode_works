target = 7

nums = [2, 3, 1, 2, 4, 3]

l = 0

total = 0

result = float('inf')

for r in range(len(nums)):

    total += nums[r]

    while total >= target:

        result = min(r - l + 1, result)

        total -= nums[l]
        l += 1

if result == float('inf'):
  
    print(0)
    
else:
  
    print(result)