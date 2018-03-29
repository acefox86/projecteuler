
'''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Problem 1 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
If we list all the natural numbers below 10 that are 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
these multiples is 23.
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Find the sum of all the multiples of 3 or 5 below 1000.
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''

sum = 0

for x in range(0, 1000):
  if ((x%3) == 0):
    sum = sum + x
  elif ((x%5) == 0):
    sum = sum + x

print("answer: " , sum)

'''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Problem 2 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Each new term in the Fibonacci sequence is generated by
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
adding the previous two terms. By starting with 1 and 2,
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
the first 10 terms will be:
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
By considering the terms in the Fibonacci sequence whose
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
values do not exceed four million, find the sum of the
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
even-valued terms.
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''

sum_of_evens = 2
numOne = 1
numTwo = 2
fib_num = 0

while ((numOne + numTwo) < 4000000):
  fib_num = numOne + numTwo
  if ((fib_num % 2) == 0) :
    sum_of_evens += fib_num
  numOne = numTwo
  numTwo = fib_num
  
print("answer: " , sum_of_evens)
  
  
'''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Problem 3 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
The prime factors of 13195 are 5, 7, 13 and 29.
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
What is the largest prime factor of the number 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
600851475143 ?
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''

import sys
import math

def is_factor_prime(list_of_numbers, factor):
  is_prime = False
  for y in list_of_numbers:
    if ((factor % y) == 0):
      return is_prime
  is_prime = True
  return is_prime

def find_largest_prime_factor(num):
  
  found_largest_prime = False
  largest_prime = 0
  list_of_numbers = []
  square_root = int(math.sqrt(num))

  while (found_largest_prime == False):

    for x in range(3, square_root, 2):
      if ((num % x) == 0):
        factor = x
        factor_prime = is_factor_prime(list_of_numbers, factor)
        if (factor_prime == True):
          largest_prime = factor
      list_of_numbers.append(x)
      found_largest_prime = True
  return largest_prime

print(find_largest_prime_factor(600851475143), "!")

'''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Problem 4
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
A palindromic number reads the same both ways. The 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
largest palindrome made from the product of two 2-digit
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
numbers is 9009 = 91 × 99.
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Find the largest palindrome made from the product of 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
two 3-digit numbers.
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''

def factor_check(plndrm, dgts):
  
  start = int("9" * dgts)
  
  for x in range (start, 0, -1):
    
    if ((int(plndrm) % x) == 0):
      
      string = str(int((int(plndrm)/x)))
      
      if (len(string) == dgts):
        
        print(x)
        return True
  
  return False

def largest_palindrome(digits):
  
  zeros = digits - 1
  num = 1 * (10 ** zeros)
  mx = int("9" * digits) ** 2
  mn = num * num
  
  for x in range(mx, mn, -1):
    
    ptntl_plndrm = str(x)
    length = len(ptntl_plndrm)
    index_1 = 0
    index_2 = length - 1
    plndrm_ness = True
    
    while (index_1 < (int(length / 2))):
      
      if (ptntl_plndrm[index_1]==ptntl_plndrm[index_2]):
      
            index_1 += 1
            index_2 -= 1
      else:
      
        plndrm_ness = False
        break
      
    if (plndrm_ness == True):
      
      plndrm_ness = factor_check(ptntl_plndrm, digits)
      if (plndrm_ness == True):
      
        return ptntl_plndrm
    
  return "no palindrome"
  
print("answer" , largest_palindrome(3))

'''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Problem 5
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
2520 is the smallest number that can be divided by each
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
of the numbers from 1 to 10 without any remainder.
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
What is the smallest positive number that is evenly 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
divisible by all of the numbers from 1 to 20?
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''

def smlst_pstv_nmbr (top_num):
   
  found_num = False
  test_num = 2520
  while (found_num == False):
    print(test_num)
    counter = 1
    num_list = []
    for x in range(top_num, 1, -1):
      if ((test_num % x) != 0):
        test_num += 2520
        break
      else:
        num_list.append(x)
        counter = counter + 1
      if (counter == top_num):
        num_list.append(1)
        found_num = True
        return test_num
        
  
print(smlst_pstv_nmbr(20))

'''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Problem 6
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
The sum of the squares of the first ten natural numbers
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
is, 12 + 22 + ... + 102 = 385
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
The square of the sum of the first ten natural numbers
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
is, (1 + 2 + ... + 10)2 = 552 = 3025
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Hence the difference between the sum of the squares of
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
the first ten natural numbers and the square of the sum
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
is 3025 − 385 = 2640. Find the difference between the 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
sum of the squares of the first one hundred natural
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
numbers and the square of the sum.
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''

def sum_of_squares (topNum):
  sum = 0
  for x in range(1, topNum + 1):
    sum += (x**2)
  return(sum)
  
def square_of_sum (topNum):
  sum = 0
  for x in range(1, topNum + 1):
    sum += x
  return(sum ** 2)
  
sm_sq = sum_of_squares (100)
sq_sm = square_of_sum (100)
print(sq_sm - sm_sq)

'''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Problem 7
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
By listing the first six prime numbers: 2, 3, 5, 7, 11,
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
and 13, we can see that the 6th prime is 13.
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
What is the 10 001st prime number?
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
def n_prime (num):
  prime_count = 1;
  prime_list = [2]
  x = 3
  while (prime_count < num):
    x_is_prime = check_prime(x)
    if (x_is_prime == True):
      prime_list.append(x)
      prime_count += 1
    x += 2
      
  return(prime_list[-1])    
      
def check_prime (x):
  num_count = 1
  for y in range (2 , x):
    if ((x % y) == 0):
      return False
    else:
      num_count += 1
    
    if (num_count == (x - 1)):
      return True
  
print(n_prime(10001)) 

'''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Problem 8
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
The four adjacent digits in the 1000-digit number that
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
have the greatest product are 9 × 9 × 8 × 9 = 5832.
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Find the thirteen adjacent digits in the 1000-digit 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
number that have the greatest product. What is the 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
value of this product?
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
def grtst_djcnt_dgts(num_digits):
  int_list = []
  
  big_num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
  bgst_prdct = 1
  
  for x in range(0, len(big_num)):
    if (len(int_list) < num_digits):
      int_list.append(big_num[x])
    if (len(int_list) == num_digits):
      int_list.pop(0)
      int_list.append(big_num[x])
    product = 1
    for y in range(0, len(int_list)):
      product *= int(int_list[y])
    if (product > bgst_prdct):
      bgst_prdct = product
     
  return bgst_prdct
  
print(grtst_djcnt_dgts(13))

'''
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Problem 8
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
A Pythagorean triplet is a set of three natural 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
numbers, a < b < c, for which,
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
a2 + b2 = c2
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
For example, 32 + 42 = 9 + 16 = 25 = 52.
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
There exists exactly one Pythagorean triplet for which
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
a + b + c = 1000.
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Find the product abc.
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
'''
