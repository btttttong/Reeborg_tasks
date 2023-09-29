put()
while True:
    move()
    if wall_in_front() or object_here():
        turn_left()
        turn_left()
        if object_here(): 
            take()
            move()
        if not object_here():
            put()
        else:
            turn_left()
            turn_left()
            turn_left()
            break
            
while True:
    move()
    if wall_in_front() or object_here():
        turn_left()
        turn_left()
        if object_here(): 
            take()
            move()
        if not object_here():
            put()
        else:
            turn_left()
            break
            
            
            
            
     
        
        
    

    
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
