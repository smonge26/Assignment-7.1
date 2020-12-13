# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Sigfredo Monge
# Creation Date: Dec 3 2020
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''
You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. In the other cave 
the dragon is greedy and hungry, and will eat you on sight.
''') # arranged the paragph to print evenly on the screen 
	print()

def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input('cave: ') # added cave to prompt the user on the screen
	return cave # removed s

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print ('Gobbles you down in one bite!') # print was missing ()

playAgain = 'yes'
while playAgain == 'yes' :    # this while was missing == , also removed the or y since its asking the user to input yes, 
	displayIntro()            # another way could have been asking the same for no and prompt the user to enter y or n as well
	caveNumber = chooseCave() # chosencave needed capital C on cave
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no" :
		print("Thanks for planing")