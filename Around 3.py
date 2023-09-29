put()
while True:
    if front_is_clear():
        move()
    
#    if object_here("token"):
#        break
#    if object_here("apple"):
#        take()
    if wall_in_front() and wall_on_right():
        turn_left()
    elif right_is_clear():
        for i in range(3):
            turn_left()
            
    if object_here("token"):
        break

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
