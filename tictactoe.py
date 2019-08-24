# Tic Tac Toe Game
#player1 = input("Please pick a marker 'X or 'O")

#position = int(input("Please enter a number to place your marker"))

# The display_board function takes in a parameter board as an argument and returns the board.

def display_board(board):
	print('\n'*100)
	board_print =  board[0] + ' | ' + board[1] + ' | ' + board[2] + '\n'
	board_print += board[3] + ' | ' + board[4] + ' | ' + board[5] + '\n'
	board_print += board[6] + ' | ' + board[7] + ' | ' + board[8] + '\n'
	return board_print
#print (display_board(['X','O','X','O','X','O','X','O','X']))
#test_board = ['X','O','X','O','X','O','X','O','X']

# The function choose_marker lets the user choose a marker and returns a tup which contains the markers for player1 and player2.
def choose_marker():
	marker = ''
	while (marker != 'X' and marker != 'O'):
		marker = input('Player 1, choose X or O:')
	player1 = marker
	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'
	return (player1, player2)

#The function place_marker places a mark on the board at the position passed in as an argument.
def place_marker(board, marker, position):
	board[position-1] = marker

#The function win_check checks if a mark wins the game.
def win_check(board,mark):
	if board[0] == mark and board[1] == mark and board[2] == mark:
		return True
	elif board[3] == mark and board[4] == mark and board[5] == mark:
		return True
	elif board[6] == mark and board[7] == mark and board[8] == mark:
		return True
	elif board[0] == mark and board[3] == mark and board[6] == mark:
		return True
	elif board[1] == mark and board[4] == mark and board[7] == mark:
		return True
	elif board[2] == mark and board[5] == mark and board[8] == mark:
		return True
	elif board[0] == mark and board[4] == mark and board[8] == mark:
		return True
	elif board[2] == mark and board[4] == mark and board[6] == mark:
		return True
	return False


#The function choose_first choose the player to make the first move randomly.
import random

def choose_first():
	first = random.randint(1,2)
	return 'player' + str(first)

#The function space_check checks weather the position is empty on the board.	
def space_check(board, position):
	if board[position-1] == " ":
		return True
	else:
		return False

#The function full_board_check checks weather the board is full.
def full_board_check(board):
	for i in range(len(board)):
		if board[i] == " ":
			return False
	return True

#The function player_choice lets the user choose a valid positon to place their marker on the board.
def player_choice(board):
	valid = False
	while valid == False:
		try:
			pos = int(input('Which position would you like to place your marker?'))
			if pos > 9 or pos < 1:
				print("Please enter a number between 1 and 9 inclusive!")
			elif space_check(board, pos) == False:
				print("position " + pos + "is already taken")
			else:
				valid = True
		except:
			print('Wrong input! Please choose a number between 1 and 9 inclusive!')
			continue
	return pos
#The function replay asks the user if they want to play again.
def replay():
	again = input("Press 'Y' to play again and press any key to quit.")
	if again == 'Y':
		return True
	else:
		return False

#Game Starts
#We start with an empty board
#call the choose_marker function to let the player choose their marker.
def play_game():
	print('Welcome to Tic Tac Toe!')
	board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	print(display_board(board))
	tup = choose_marker()
	player1_marker = tup[0]
	player2_marker = tup[1]
	n = choose_first()
	turn = n
	# We keep playing the game until the board becomes full or a player wins the game.
	while (full_board_check(board) == False):
		print('It is '+ turn + '\'s turn' )
		if turn == 'player1':
			mark = player1_marker
		else:
			mark = player2_marker
		pos = player_choice(board)
		place_marker(board, mark, pos)
		print('\n' + display_board(board) + '\n')
		if win_check(board, mark):
			print(turn +' is the winner!')
			break
		if full_board_check(board) == True:
			print ('It\'s a draw')
			break
		if turn == 'player1':
			turn = 'player2'
		else:
			turn = 'player1'
		print('It is '+ turn + '\'s turn' )
		if turn == 'player1':
			mark = player1_marker
		else:
			mark = player2_marker
		pos = player_choice(board)
		place_marker(board, mark, pos)
		print('\n' + display_board(board) + '\n')
		if win_check(board, mark):
			print(turn +' is the winner!')
			break
		if full_board_check(board) == True:
			print ('It\'s a draw')
			break
		if turn == 'player1':
			turn = 'player2'
		else:
			turn = 'player1'
	if replay():
		play_game()
	else:
		return
play_game()