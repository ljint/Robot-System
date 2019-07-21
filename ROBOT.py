import math
import sys
def move(command): #create  move function 
  x=0 #Start point(x,y)
  y=0
  a=0 #End point(a,b)
  b=0
  facing=0 # 0="north", 1="south", 2="east", 3="west"
  #on the radar, our robot away facing north at initial state
  for step in command.split(','): #set the input command
    order = step[0]
    num = int(step[1:])
    if order == 'F':
      while num > 0: #create a while loop, it will keep change the value depend on how many unit you had input
        if facing == 0: 
          b = b + 1 
        if facing == 1:
          b = b - 1 
        if facing == 2:
          a = a + 1 #when robot facing east, forward is x-axis adding
        if facing == 3:
          a = a - 1 #when robot facing west, forward is x-axis subtracting
        num = num -1
    if order == 'B':
      while num > 0:
        if facing == 0:
          b = b - 1 
        if facing == 1:
          b = b + 1
        if facing == 2:
          a = a - 1 #when robot facing east, backward is x-axis subtracting
        if facing == 3:
          a = a + 1 #when robot facing west, backward is x-axis adding
        num = num -1
    if order == 'R':
      while num > 0:
        if facing == 0: # when robot facing north, the right side will be east
          facing = 2
        elif facing == 1: # when robot facing south, the right side will be west
          facing = 3
        elif facing == 2: # when robot facing east, the right side will be south
          facing = 1
        elif facing == 3: # when robot facing west, the right side will be north
          facing = 0
        num = num -1
    if order == 'L':
      while num > 0:
        if facing == 0: # when robot facing north, the left side will be west
          facing = 3
        elif facing == 1: # when robot facing south, the left side will be east
          facing = 2
        elif facing == 2: # when robot facing east, the left side will be north
          facing = 0
        elif facing == 3: # when robot facing west, the left side will be south
          facing = 1
        num = num -1
        
  print ('Now your location is:(',a,',',b,')') # show the location where the robot are.
  print ('The minimum amount of distance back to start point:', abs(a-x)+abs(b-y)) # calculate the minimum amount of distance to get back the starting point.
   
move(sys.argv[1])
