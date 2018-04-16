'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


import math

def p_u_10 (num):
  
  num_list = [2]

  for y in range(3, num, 2):
    
    counter = 1
    sq_rt = int(math.sqrt(y)) + 1
    
    for z in range(2, sq_rt):
      
      if ((y % z) == 0):
        break
      
      else:
        counter = counter + 1
 
    if (counter == (sq_rt - 1)):
      num_list.append(y)
  
  total = sum(num_list)
  print(total)
  return total
  
  
  
p_u_10(2000000)
