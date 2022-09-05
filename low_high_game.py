# Emily Snodgrass 10/6/21

# LoHiGame
# goal: guess the random integer between 1 and 20 in 4 trys
# The program randomly chooses an integer between 1 and 20 inclusive and then gives
# the user 4 chances to guess the hidden number. After each incorrect answer the program
# says weather the guess was too high or too low. If the user does not guess the number
# after 4 trys, the program tells the user that they are out of guesses and lose. The secret number
# is then revealed.  If any guess correctly guesses the hidden number,
# the program tells the user that they win and reveals the secret number.
# loops are not used

import random
import math


x = math.floor(20*random.random()) + 1
#print("x = " , x)

print("Guess a number between 1 and 20: ")
guess = float(input())

if (guess == x):
  print("You win! The number is", x)
  
else:
	print("Sorry wrong number!")
	if (guess > x):
		print("Your guess is too High")
	else:
		print("Your guess is too Low")
	print("Try again! What's your next guess?")
	guess = float(input())

	if (guess == x):
		print("You win! The number is", x)
	else:
		print("Sorry wrong number!")
		if (guess > x):
			print("Your guess is too High")
		else:
			print("Your guess is too Low")
		print("Try again! What's your next guess?")
		guess = float(input())

		if (guess == x):
			print("You win! The number is", x)
		else:
			print("Sorry wrong number!")
			if (guess > x):
				print("Your guess is too High")
			else:
				print("Your guess is too Low")
			print("Try again! What's your next guess?")
			guess = float(input())

			if (guess == x):
				print("You win! The number is", x)
			else:
				print("Sorry, you loose :(")