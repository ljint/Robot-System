import math
import sys
def move(command):
  x=0
  y=0
  a=0
  b=0
  facing=0 # 0="north", 1="south", 2="east", 3="west"
  for step in command.split(','):
    order = step[0]
    num = int(step[1:])
    if order == 'F':
      while num > 0:
        if facing == 0:
          b = b + 1
        if facing == 1:
          b = b - 1
        if facing == 2:
          a = a + 1
        if facing == 3:
          a = a - 1
        num = num -1
    if order == 'B':
      while num > 0:
        if facing == 0:
          b = b - 1
        if facing == 1:
          b = b + 1
        if facing == 2:
          a = a - 1
        if facing == 3:
          a = a + 1
        num = num -1
    if order == 'R':
      while num > 0:
        if facing == 0:
          facing = 2
        elif facing == 1:
          facing = 3
        elif facing == 2:
          facing = 1
        elif facing == 3:
          facing = 0
        num = num -1
    if order == 'L':
      while num > 0:
        if facing == 0:
          facing = 3
        elif facing == 1:
          facing = 2
        elif facing == 2:
          facing = 0
        elif facing == 3:
          facing = 1
        num = num -1
        
  print ('(',a,',',b,')')
  print (abs(a-x)+abs(b-y))
   
move(sys.argv[1])
