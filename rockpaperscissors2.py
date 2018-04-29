from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
	print(f"Player wins: {player_wins} | Computer wins: {computer_wins}")
	print("...rock...")
	print("...paper...")
	print("...scissors")
	print("SHOOT!")

	player = input("Your choice: ")
	if player == "quit" or player == "q":
		break
	random_number = randint(0, 2)
	if (random_number == 0):
		computer = "rock"
	elif (random_number == 1):
		computer = "scissors"
	else:
		computer = "paper"
	print(f"Computer's choice: {computer}")


	if player == computer:
		print("It's a tie!")
	elif player == "rock":
		if computer == "paper":
			print("The computer wins!")
			computer_wins += 1
		elif computer == "scissors":
			print("The player wins!")
			player_wins += 1
	elif player == "paper":
		if computer == "rock":
			print("The player wins!")
			player_wins += 1
		elif computer == "scissors":
			print("The computer wins!")
			computer_wins += 1
	elif player == "scissors":
		if computer == "rock":
			print("The computer wins!")
			computer_wins += 1
		elif computer == "paper":
			print("The player wins!")
			player_wins += 1
	else:
		print("Something went wrong.")
if player_wins > computer_wins:
	print("Congrats, you won!")
elif player_wins == computer_wins:
	print("It's a tie!")
else:
	print("Oh no, the computer won!")