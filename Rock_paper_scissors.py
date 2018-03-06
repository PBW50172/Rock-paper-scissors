import random

userhand = input("Rock, paper or scissors:")

computerhand = random.random()

if computerhand <= .33:
    computerhand = 'rock'

elif computerhand <= .66:
    computerhand = 'paper'

else:
    computerhand = 'scissors'
    

def game(first, second):
    
    if first == second:
        print 'You chose', first
        print 'Computer chose', second
        print 'It is a tie'
    
    elif first == 'rock':
        if second == 'scissors':
            
            print 'You chose', first
            print 'Computer chose', second
            print 'You win'
           
        else:
           
            print 'You chose', first
            print 'Computer chose', second
            print 'You lose'
            
            
    elif first == 'paper':
        if second == 'rock':
            print 'You chose', first
            print 'Computer chose', second
            print 'You win'
            
         
        else:
            print 'You chose', first
            print 'Computer chose', second
            print 'You lose'
            
            
   
    elif first == 'scissors':
        if second == 'paper':
            print 'You chose', first
            print 'Computer chose', second
            print 'You win'
            
         
        else:
            print 'You chose', first
            print 'Computer chose', second
            print 'You lose'
            
            


print game(userhand, computerhand)
            
            
            


