---------------HURDLE 1-------------------
def lompat():
    move()
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

for step in range(6):
    lompat()
-------------HURDLE 2---------------
def lompat():
    move()
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
    lompat()
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
-----------------------MAZE------------------------
kondisi():
    while wall_in_front()==False:
        move()
        if wall_in_front()==False and right_is_clear()==True:
            turn_right()
            move()
    if wall_in_front()==True and right_is_clear()==False:
        turn_left()
    elif wall_in_front()==True and right_is_clear()==True:
        turn_right()
        if is_facing_north():
            while wall_in_front()==False:
                move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while at_goal()==False:
    kondisi()
