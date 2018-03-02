'''
The line of x's is to make searching a little harder...
'''

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
Find the sum of all the multiples of 3 or 5 below 1000
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.
'''

sum = 0

for x in range(0, 1000):
  if ((x%3) == 0):
    sum = sum + x
  elif ((x%5) == 0):
    sum = sum + x

print("answer: " , sum)
