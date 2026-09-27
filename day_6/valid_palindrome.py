s = "A man, a plan, a canal: Panama"

word = []

for w in s:
  
  if w.isalnum():
    
    word.append(w.lower())
    
left = 0

right = len(word)-1
 
ref_list = word.copy()
    
while left<right:
  
  word[left],word[right]=word[right],word[left]
  
  right-=1
  
  left+=1
  
print(word==ref_list)


    

  

