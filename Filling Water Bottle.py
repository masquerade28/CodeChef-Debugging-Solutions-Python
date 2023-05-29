'''
  There are N people standing in queue to fill up their water bottles.
  You are at the Bth position from the start of the queue.
  It takes C minutes for primary school students to fill their bottle and D minutes for high school students to fill their bottles. 
  You are in high school.
  The queue is represented as a binary list Q1, Q2,...,QN of length N where :
    -> Q = 0 denotes a primary school student 
    -> Q = 1 denotes a secondary school student
  Determine the time when you will have filled your water bottle.
'''

for t in range(int(input())):
  
  N,B,C,D = map(int, input().split())
  
  A = list(map(int, input().split()))
  
  l = 0
  
  for i in range(N):
    
    if (i==B):
      break
      
    else:
      
      if (A[i]==0):
        l += C
        
      else:
        l += D
        
  print(l)
