# task One 
                #Hangman Game.

import random
print("Welcome to hangman game.")

words = ("butterfly", "camel", "cat", "caterpillar", "cattle", "chicken", "great", "Umberalla", "apple")
#f = open("file.txt", "r")
#data = f.readline()
#words = data.split()
word = random.choice(words)
word = word.upper()

total_chances = 10
guessed_word = "-"*len(word)

while total_chances != 0:
    print(guessed_word)
    letter = input("Guess a letter: ").upper()
    if letter in word:
        for index in range(len(word)):
            if word[index] == letter:
                guessed_word = guessed_word[:index]+letter+guessed_word[index+1:]
             #print(guessed_word)
        if guessed_word == word:
            print("congratulation you won!!")
            break
        
    else:  
        total_chances -= 1
        print("Incorrect guess")
        print("the remaining chances are: ", total_chances)
else:         
    print("game over")
    print("you lose")
    print("print the chances are exhausted")
print("The correct word is:", word)         