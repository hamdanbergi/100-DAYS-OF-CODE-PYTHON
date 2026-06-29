### The following code is the solution to the maze section on the website "Reeborg's World" which ispart of the curriculum in Dr.Angela Yu's "100 Days of Code Python Bootcamp" available on Udemy 


def turn_right(): #the exercise requires you to create your own function for turning right 
    turn_left() # predefined function for turning left 
    turn_left()
    turn_left()
    
while not at_goal(): #while loop to keep the code running until target is reached 
    if wall_in_front() and right_is_clear(): #condition and instruction for code to follow
        turn_right()
    elif front_is_clear():
        move()
    elif wall_on_right():
        turn_left()
    else:
        pass
