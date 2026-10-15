# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

s = "ABAB"

k = 2

l=0

max_length = 0

max_frequency = 0

frequency = {}

for r in range(len(s)):
  
  frequency[s[r]] = frequency.get(s[r],0) + 1
  
  max_frequency = max(max_frequency,frequency[s[r]])
  
  while (r-l)+1 - max_frequency > k:
    
    frequency[s[l]] -=1
    
    l+=1
    
  max_length = max(max_length,r-l+1)

print(max_length)
