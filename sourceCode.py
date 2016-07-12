words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
import random

def getRandomWord(wordList):
    wordIndex  = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]


def displayBoard(missedLetters, correctLetters, secretWord):
    print "Missed Letters: "
    for i in missedLetters :
        print i,
    print 
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            OrgBlanks = ''
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
            
    for i in blanks:
        print i,
    print 
def playAgain():
    ans = raw_input("Do you want to play again? (yes or no)")
    ans = ans.lower()
    return ans.startswith('y')

print "H A N G M A N"
word = getRandomWord(words)
correctLetters = ''
missedLetters = ''
gameIsDone = False
guessesLeft = 7

print playAgain()
while True:

    displayBoard(missedLetters,correctLetters,word)
    print "you have " + str(guessesLeft) + " guesses left."
    guess = raw_input("Guess a letter: ")
    guess = guess.lower()
    if len(guess) != 1:
        print "Please enter a single letter."
    elif guess in correctLetters + missedLetters :
        print "You have already gussed that letter"
    elif guess not in "abcdefghijklmnopqrstuvwxyz":
        print "Please enter a LETTER."
    else :
        if guess in word:
            correctLetters = correctLetters + guess
            displayBoard(missedLetters,correctLetters,word)
            won = True
            for i in range(len(word)):
                if word[i] not in correctLetters:
                    won = False
                    break
            if won :
                print "Yes! the secret word is " +word+ ", you WON! "
                gameIsDone = True
                break
        else:
            missedLetters = missedLetters + guess
            guessesLeft -= 1
            displayBoard(missedLetters,correctLetters,word)
            if len(missedLetters) == 7 :
                print "Game over.. LOSER! the secret word is: " + word
                gameIsDone = True
                break
##    if gameIsDone:
##        if playAgain:
##            word = getRandomWord(words)
##            correctLetters = ''
##            missedLetters = ''
##            gameIsDone = False
##            guessesLeft = 7
##        else:
##            break
