from random import randint

def hangman():      
    name = input('what is your name? \n')
    print("hello ",name,' its time to play hangman')
    print('start guessing')
    #determine the number of chances
    turns = 10
    #variable to hold the guessed word
    guesses = " "
    guessed = []
    guess=' '
    #word to guess
    list = ['war','haqeekat','dhoom','baby','murder','stone','disturbance','makeover','moveon','iteration','secret'
            'distribution','uncommon','enchanted','next','fact']
    word = list[randint(0,14)]
    #guessing charecter by charecter
    while turns > 0:
        failed = 0
        #guess = input('\n guess the charecter \t')
        for char in word:
            if char in guesses:
                print(char,end=' ')               
            else:
                print("_",end=' ')
                failed += 1
        if guess not in guessed:
            guessed.append(guess)  
        if failed == 0:
            print('you won \n')
            print('the word is ',word)
            break
        guess = input('\n guess the charecter \t')
        guesses += guess
        #checking for the charecter in the word
        if guess not in word:
            if guess not in guessed:
                turns -= 1
                print('wrong guess')
            else: 
                print('already guessed')
                print(guessed)
        print('you are left with ', turns , 'guesses')
        if turns == 0:
            print('game over you hav lost \n')
            print('the word is ',word)
again = 'yes'
while again=='yes':
    hangman()
    again = input('do u want to play again?  (yes/no)').lower