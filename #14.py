'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def fnd_lngst_chn (highest_num):
  
  num_for_max = 0
  max_chain = 0
  for x in range(1, highest_num):
    starting_num = x
    chain_length = 1
    while (x > 1):
      chain_length = chain_length + 1
      if(((x)%2) == 0):
        x = int(x / 2)
      else:
        x = (x * 3) + 1
    
    if(chain_length > max_chain):
      num_for_max = starting_num
      max_chain = chain_length
    
  return(num_for_max)
  
  
print(fnd_lngst_chn(1000000))
