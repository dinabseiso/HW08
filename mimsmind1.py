#! usr/bin/env python
# mimsmind1.py

### Imports go here

import sys
from random import randint 


### Body

def getDigits():
	if len(sys.argv) != 2 : 
		digits = 3
	else :
		digits = sys.argv[1]
	digits = int(digits)
	max_tries = 2**digits + digits 												# Compute the maximum number of tries allowed. 
	random_number = randint(1, (10**digits - 1))
	print ("Let's play the mimsmind0 game. You have %d tries." % max_tries)		# Be nice, and let them know how many tries they have.
	return random_number, digits, max_tries										# Create the tuple for grabbing the values later!

def guessingGame():
	random_number, digits, max_tries = getDigits()								# Pull from getDigits() the variables you need.
	guess = raw_input("Guess a %d-digit number: " % digits )
	tries = 1
	while (tries <= max_tries) : 
		check = True
		while check == True: 
			try : 																# Utilize a try-except clause to catch non-numeric inputs.
				guess = int(guess)
				guess_string = str(guess)
				random_number_string = str(random_number)
				check = False
			except ValueError : 
				guess = raw_input("That's not a %d-digit number. Try again, please: " % digits)
				tries += 1
		if len(random_number_string) == len(guess_string): 
			if (random_number != guess) and (tries != max_tries):				# If they have tries left, do some work.
				bulls = 0														# Work being checking how close they were, digit-by-digit.
				cows = 0
				for i in range(digits): 										# Iterate through the digits.
					if guess_string[i] == random_number_string[i]:				# Will check for same-place matching.
						bulls += 1
					elif guess_string[i] in random_number_string : 				# Will check for existence.
						cows += 1
				guess = raw_input("{} bull(s), {} cow(s). Try again: " .format(bulls, cows))	# .format() as a different way to reflect held values.
				tries += 1
			elif (random_number != guess) and (tries == max_tries):				# But if they do not have tries left, end the game.
				print ("I'm sorry! You ran out of guesses. Better luck next time. (The number was {} by the way.)" .format(random_number))
				exit(0)															# Exit the game assuredly. 
			else: 
				print ("Congratulations! You guessed the correct number in {} tries." .format(tries) )	# If they guessed correctly, let them know!
				exit(0)															# Exit the game assuredly. Otherwise, will be stuck in the while loop.
		else : 
			guess = raw_input("Incorrect number of digits. Please enter a %d-digit number: " % digits) 	# Remind them of the digits they need to enter.
			tries +=1


### Define main() here

def main():
	guessingGame()


### Boilerplate for calling main()


if __name__ == "__main__" :
	main()