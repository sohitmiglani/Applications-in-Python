# This is a game of chance. The input (1 or 2) determines whether it is your turn or not.
# Based on your turn, you have a 0.6 or a 0.5 chance respectively, of winning the first round. 
# The winner of the first 'n' rounds wins. 

def game_result(chance,n):
    my_score = 0 
    other_score = 0
    import random
    while my_score<n and other_score<n:
        if chance==1:
            x = random.random()
            if x < 0.6:
                my_score = my_score + 1
                chance = 1
            if x >= 0.6:
                other_score = other_score + 1 
                chance = 2
        if chance==2: 
            x = random.random()
            if x < 0.5:
                my_score = my_score + 1
                chance = 1
            if x >= 0.5:
                other_score = other_score + 1 
                chance = 2
    if my_score==21:
        print "You Win"
    if other_score==21:
        print "You Loose" 
    

