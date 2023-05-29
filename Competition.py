'''
  2 Teams are competing against each other.
  5 members from Team-1 compete against 5 members from Team-2.
  Their results are given in the form of ten integers - X1, X2,..., X10
    -> X1 and X2 is the scoreline of the match between the 1st member from both teams
    -> X3 and X4 is the scoreline of the match between the 2nd member from both teams
    -> X5 and X6 is the scoreline of the match between the 3rd member from both teams and so on
  The team with the highest total score wins.
  In case the total score of both teams is the same, then it is a draw.
  Output the winner of the contest or if the game is a draw.
  Print a single line containing integer - 0 if the game is draw or 1 if the Team-1 wins or 2 if Team-2 wins.
'''

for t in range(int(input())):
  
  a = list(map(int, input().split()))
  
  e,o = 0,0
  
  for i in range(len(a)):
    
    if i%2 == 0:
      e += a[i]
      
    else:
      o += a[i]
  
  if e > o:
    print(1)
    
  elif e < o:
    print(2)
    
  else:
    print(0)
