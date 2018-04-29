import random

random_number = random.randint(1,10)
guess = None

while True:
	guess = int(input("Pick a number between 1 and 10\n"))
	if guess < random_number:
		print("Your number is too low, Try again.\n")
	elif guess > random_number:
		print("Your number is too low, Try again.\n")
	else:
		print("You guessed the number correctly!\n")
		play_again = input("Do you want to play again? y/n\n")
		if play_again == "y":
			random_number = random.randint(1,10)
			guess = None
		else:
			print("Thank you for playing!\n")
			break

print(f"The random number was {random_number}!")