print("...rock...")
print("...paper...")
print("...scissors")
player_one_input = input("Player 1's choice: ")
print("***				NO CHEATING				***\n\n" * 30)
player_two_input = input("Player 2's choice: ")
print("SHOOT!")

if player_one_input == player_two_input:
	print("It's a tie!")
elif player_one_input == "rock":
	if player_two_input == "paper":
		print("Player 2 wins!")
	elif player_one_input == "scissors":
		print("Player 1 wins!")
elif player_one_input == "paper":
	if player_two_input == "rock":
		print("Player 1 wins!")
	elif player_two_input == "scissors":
		print("Player 2 wins!")
elif player_one_input == "scissors":
	if player_two_input == "rock":
		print("Player 2 wins!")
	elif player_two_input == "paper":
		print("Player 1 wins!")
else:
	print("Something went wrong.")