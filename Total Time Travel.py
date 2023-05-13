'''
  You are about to drive to your vacation destination.
  You open Google Maps - it shows you that the estimated distance is A minutes at your normal pace.
  You are in a hurry and do the following
    -> At normal pace, in B minutes - you would have reached the rest point
    -> You drive at 2× the normal pace and reach the rest point in half the time
    -> After the rest point - you drive at your normal pace again
  What is your total travel time?
'''

A,B = map(int, input().split())

Time_Travel = (A-(B-B/2))

print(int(Time_Travel))
