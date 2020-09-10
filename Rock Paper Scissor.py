from random import randint


def getUser():
    print('Rock \t Paper \t Scissor: ') 
    userIn = input('enter your choice\n').lower()
    if( userIn == 'rock'or userIn == 'paper'or userIn =='scissor'):
        print('You Entered  \t',userIn)
        return(userIn)
    else:
        print('\n enter a valid choice \n')
        return getUser()

def getComp():
    t = ['rock','paper','scissor']
    compIn = t[randint(0,2)]
    print('Computer entry  ',compIn)
    return(compIn)

def calc(user, comp):
    if user == comp:
        print("DRAW!")
    elif user == 'rock':
        if comp == 'paper':            
            print("YOU LOSE - ",comp, "smothers",user)
            return 'loss'            
        else:
            print("YOU WIN -",user, "smashes",comp)
            return 'win'            
    elif user == 'paper':
        if comp == 'scissor':
            print("YOU LOSE - ", comp, "slices", user)
            return 'loss'
        else:
            print("YOU WIN -", user, "smothers", comp)
            return 'win'
    else:
        if comp == 'rock':
            print("YOU LOSE - ", comp, "smashes", user)
            return 'loss'
        else:
            print("YOU WIN -", user, "slices", comp)
            return 'win'

again = 'yes'
win = 0
loss = 0

while again != 'no':
    res = calc(getUser(), getComp())
    if res == 'win':
        win = win + 1
    elif res == 'loss':
        loss = loss + 1
    again = input('Would you like to play again?  (yes/no)\n').lower()

if win > loss:
    print('PLAYER WINS')
    print('Player Score : ',win,'  Computer Score :',loss)

elif loss > win:
    print('PLAYER LOSSES')
    print('Computer Score : ',loss,'  Player Score :',win)

else:
    print('ITS A TIE')
    print('Computer Score : ',loss,'  Player Score :',win)

print('Thank you for playing.')