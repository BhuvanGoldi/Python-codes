from random import randint

def getUser():
    print('head \t or \t tail: ') 
    userIn = input('enter your choice\n').lower()
    if( userIn == 'head'or userIn == 'tail'):
        print('Your Guess   ',userIn)
        return(userIn)
    else:
        print('\n enter a valid choice \n')
        return getUser()

def getComp():
    t = ['tail','head']
    compIn = t[randint(0,1)]
    print('Actual Fall  ',compIn)
    return(compIn)

def calc(user, comp):
    if user == comp:
        print('You Have Guessed It Right')
        return 'win'
    else:
        print('You Have Guessed It Wrong')
        return 'loss'
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
    print('Number Of Correct Guesses : ',win,'  Number Of Wrong Guesses :',loss)

elif loss > win:
    print('PLAYER LOSSES')
    print('Number Of Correct Guesses : ',win,'  Number Of Wrong Guesses :',loss)

else:
    print('ITS A TIE')
    print('Number Of Correct Guesses : ',win,'  Number Of Wrong Guesses :',loss)

print('Thank you for playing.')