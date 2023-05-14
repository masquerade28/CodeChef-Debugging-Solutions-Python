'''
  You and your friend are at positions A and B on the X axis.
  You want to meet at a restaurant for lunch - all restaurants are located on integer locations on the same X axis.
  In order to minimise both your effort, you and your friend decides to meet at a restaurant such that the maximum distance travelled by either of you is minimised.
  To Clarify - Suppose you choose the restaurant at C. You need to find the minimum value of max(abs(A-C),abs(B-C)) across all possible choices of C. 
'''

T = int(input())

for i in range(T):
  
  X,Y = map(int, input().split())
  
  if (X > Y):   
    d = X-Y
    
  else:  
    d = Y-X
    
  if (d % 2 == 0):
    ans = int((d)/2)
  
  else:
    ans = int((d+1)/2)
  
  print(ans)  
