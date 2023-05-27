'''
  In an exam center - A students have to sit on seats assigned by their id number.
  Each bench has 5 seats and can take 5 students with id 1 to 5 sit in the Bench1, 6 to 10 sit on the bench2 and so on.
  Student with id number B skips the exam. Hence, students with id B+1 sits in the seat assigned to B. 
  Every subsequent student then shifts to the previous seat.
  Due to the above, some students are no longer sitting on the original Bench assigned to them.
  Help determine the invigilator how many students are seated on a Bench different than assigned.
'''

t = int(input())

for i in range(t):
  n,k = map(int, input().split())
  
  if (k % 5 == 0):
    tar = int(k / 5)
    
  else:
    tar = int(k / 5) + 1
    
  if (n % 5 == 0):
    grp = int(n / 5)
    
  else:
    grp = int(n / 5) + 1
    
  print(grp - tar)
