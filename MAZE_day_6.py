def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
while not at_goal():
    if wall_in_front() and right_is_clear():
        turn_right()
    if front_is_clear():
        move()
    
    if wall_on_right():
        turn_left()
