# here the following functions are provided by the exercise
# turn_left(), at_goal(), move(), front_is_clear(), right_is_clear(), wall_in_front(), wall_in_right()
# read the README.md file to know how to use this code

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def is_right_clear():
    if right_is_clear() == True:
        return True
    else:
        return False

def is_front_clear():
    if front_is_clear() == True:
        return True
    else:
        return False

while not at_goal():
    if is_right_clear() == True:
        turn_right()
        move()
    elif is_front_clear() == True:
        move()
    else:
        turn_around()
        if is_right_clear() == True:
            turn_right()
            move()
