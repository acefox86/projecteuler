'''
2 to the 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 to the 1000?
'''

def find(num, exp):
  times = num
  final = 0
  x = 1
  while(x < exp):
    num = num * times
    x = x + 1
    final = num

  real_final = 0
  final_str = str(final)
  for x in final_str:
    real_final = real_final + int(x)
  return real_final

print(find(2, 1000))
