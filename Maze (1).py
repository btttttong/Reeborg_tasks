think(100)
while not at_goal():
    if wall_in_front():
        turn_left()
    elif front_is_clear():
        move()
        if right_is_clear():
            turn_left()
            turn_left()
            turn_left()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
