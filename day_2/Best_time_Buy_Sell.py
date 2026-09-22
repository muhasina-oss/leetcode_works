prices = [7, 1, 5, 3, 6, 4]

profit = 0

for i in range(0,len(prices)):
    
  for j in range(i+1,len(prices)):
        
    difference = prices[j] - prices[i]
    
    if difference > profit:
      
      profit = difference
      
if profit == 0:
  
  print("0")
  
else:
  
  print(profit)  
    
    
    