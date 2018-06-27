# -*- coding: utf-8 -*-
"""

Ejercicio. Tic-tac-toe

We are going to build a program that allows us to play tic-tac-toe on the terminal


In a nutshell, the tic-tac-toe board can be thought of 3 lists inside another one

board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
]

por ejemplo, si queremos ver cual es el estado de la casilla de arriba a la 
izquerda, podemos acceder haciendo tablero[[0,0]]

We have 2 players, and each player will alternate in choosing a different slot on the board,
and placing either an "X"  (player 1) or "O" (player 2)

The game will have to validate that the new coordinates chosen by the current player 
are valid, i.e., they need to be empty and be inside the board.


Hint: You can use a deque (in the module collections) to rotate between player 1 and 2
"""

# board = [[1,2,3], 
# 		[3,4,5],
# 		[6,7,8]]

# board = list(range(0,10))



# winning_comb = [["0","0","0"],["1","1","1"]["2","2","2"],["0","1","2"],["2","1","0"]]
# player_one = 'X'
# player_two = 'Y'

# print ('Welcome to Tic Tace Toe')

# def choose_move():
# 	print ('please choose a spot')
# 	while True: 





# # def player (move): if move 


# def game():
#     pass





# if __name__ == "__main__":
#     game()

# x = list(range(0,10))
# print (x)


board = [None] + list(range(1,10))
winning_comb = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

def draw():
		print(board[7], board[8], board[9])
		print(board[4], board[5], board[6])
	    print(board[1], board[2], board[3])
	    print()

def choose():
	while True: 
		try: 
			a = int(input())
			if a in board: 
				return a 
			else: 
				print ("\nInvalid move. Try again")
		except ValueError: 
			print ("\nNot a number")

def game():
	for a, b, c in winning_comb:
		if board[a] == board[b] == board[c]:
			print ("Player {0} wins!\n".format(board[a]))
			return True
	if sum((pos == 'X' or pos == 'O') for pos in board) == 9:
		print("Tie\n")
		return True 

for player in 'XO' * 9:
	draw()
	if is_game_over():
		break
	print("Player {0} pick ")
	board[choose_number()] = player

while True: 
	tic_tac_toe()
	if input("play again (y/n)\n") != "y"
		break 





