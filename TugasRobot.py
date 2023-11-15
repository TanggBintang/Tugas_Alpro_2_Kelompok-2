#######-------------HURDLE 3-----------------#########
def lompat():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while at_goal()==False:
    if wall_in_front():
        lompat()
    elif not wall_in_front():
        move()
#######-------------HURDLE 4-----------------#########
def lompat():
    turn_left()
    while right_is_clear()==False:
        move()
    turn_right()
    move()
    turn_right()
    while wall_in_front()==False:
        move()
    turn_left()
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while at_goal()==False:
    if wall_in_front():
        lompat()
    elif not wall_in_front():
        move()
