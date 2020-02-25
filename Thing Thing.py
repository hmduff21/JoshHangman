#boi you look like a purple sweet potato thats not even purple is magenta popi
import random
randomWords = ["ducks" , "jumbo" , "lucky" , "pills" , "flour"]
secret = random.choice (randomWords)
letter = ""
updateWord = []
print secret #only for tester
def initialize():
    print "We have a secret word"
    print "_ _ _ _ _"
def getLetter():
    print "Enter a letter"
    global letter
    letter = raw_input()
def ifWon():
    if secret == updateWord:
        print "you win"
    else:
        getLetter()
def main():
    initialize ()
    getLetter ()
    ifWon ()
main()

#def tester():
    #global updateWord
    #updateWord = raw_input()
    #if updateWord == secret:
        #print "yay"
    #else:
        #print "no"
