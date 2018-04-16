    '''
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
    '''
    
    def find_pythag_triple (sum_to_find):
  
  sum_abc = 0
  m = 2
  
  while (sum_abc <= sum_to_find):
    
    for n in range (1, m):
      
      k = 2
      a = m * m - n * n
      b = 2 * m * n
      c = m * m + n * n
      sum_abc = a + b + c
      sum_abc_2 = 0  
      
      if (sum_abc == 1000):
        
        return(a * b * c)
      
      while (sum_abc_2 <= sum_to_find):
        
        a = k * (m * m - n * n)
        b = k * (2 * m * n)
        c = k * (m * m + n * n)
        sum_abc_2 = a + b + c
        
        if (sum_abc_2 == 1000):
          
          return(a * b * c)
        
        k = k + 1
    
    m = m + 1

print(find_pythag_triple (1000))
