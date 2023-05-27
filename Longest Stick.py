'''
  You are given 3 sticks of length A, B and C.
  You have an option to join the 1st and the 3rd stick to form a longer stick.
  Output the longest achievable stick length
'''

t = int(input())

for i in range(t):
  a, b, c = map(int, input().split())
  
  if b > (a+c):
    print(b)
    
  else:
    print(a+c)
