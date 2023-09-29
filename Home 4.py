while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        if right_is_clear():
            turn_left()
            turn_left()
            turn_left()
        else:
            turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
