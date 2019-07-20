import math
import sys
def move(command):
  x=0
  y=0
  a=1
  b=1
  for step in command.split(','):
    order = step[0]
    num = int(step[1:])
    if order == 'F':
      while num > 0:
        if a == 1:
          y = y + a * b
        else:
          x = x - a * b
        num = num -1
    if order == 'B':
      while num > 0:
        if a == 1:
          y = y - a * b
        else:
          x = x + a * b
        num = num -1

  print ('(',x,',',y,')')
  print (abs(x)+abs(y))
   
move(sys.argv[1])