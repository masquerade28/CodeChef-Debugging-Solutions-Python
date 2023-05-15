'''
  A is your initial energy level.
  You have one of two optins
    -> Take the force multiplier tablet which converts your energy into A x B OR
    -> Take the force additive tablet which converts your energy into A + B
  You want to minimize your energy.
  Output the minimum energy possible - you will necessarily consume one of the 2 tablets
'''

for t in range(int(input())):
  
  x, m, d = map(int, input().split())
  
  multiplier = x * m
  additive = x + d
  
  print(min(multiplier, additive))
