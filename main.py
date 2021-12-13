#!/usr/bin/env python3
import random
import hangman_words
import hangman_art
import os

def clear_console():
	os.system('clear')

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6



#Create blanks
display = []
for _ in range(word_length):
	display += "_"

wrong_guesses = []

while not end_of_game:
	clear_console()
	print(hangman_art.logo)
	print(f"Wrong: {wrong_guesses}")
	print(hangman_art.stages[lives])
	print(f"{' '.join(display)}")
	guess = input("Guess a letter: ").lower()
	
	if guess in display:
		print(f"You have already guessed {guess}. Try again")
		
	#Check guessed letter
	for position in range(word_length):
		letter = chosen_word[position]		
		if letter == guess:
			display[position] = letter
			
	#Check if user is wrong.
	if guess not in chosen_word:
		wrong_guesses.append(guess)
		lives -= 1
		if lives == 0:
			end_of_game = True
			clear_console()
			print(hangman_art.logo)
			print(f"Wrong: {wrong_guesses}")
			print(hangman_art.stages[lives])
			print(f"{' '.join(display)}")			
			print("You lose.")
	
	#Check if user has got all letters.
	if "_" not in display:
		end_of_game = True
		print("You win.")
			
	