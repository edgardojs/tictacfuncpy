# Tic Tac Toe by Christian Thompson
# Using Loops, Functions and Lists

#Import

import os
import time

#Define the Board

board = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


#Print the header

def print_header():
    print """
    
/$$$$$$$$ /$$                 /$$$$$$$$                        /$$$$$$$$                 
|__  $$__/|__/                |__  $$__/                       |__  $$__/                 
   | $$    /$$  /$$$$$$$         | $$  /$$$$$$   /$$$$$$$         | $$  /$$$$$$   /$$$$$$ 
   | $$   | $$ /$$_____/         | $$ |____  $$ /$$_____/         | $$ /$$__  $$ /$$__  $$
   | $$   | $$| $$               | $$  /$$$$$$$| $$               | $$| $$  \ $$| $$$$$$$$
   | $$   | $$| $$               | $$ /$$__  $$| $$               | $$| $$  | $$| $$_____/
   | $$   | $$|  $$$$$$$         | $$|  $$$$$$$|  $$$$$$$         | $$|  $$$$$$/|  $$$$$$$
   |__/   |__/ \_______/         |__/ \_______/ \_______/         |__/ \______/  \_______/
   
   1 | 2 | 3         To play Tic-Tac-Toe, you need to get three in a row...      1 | 2 | 3
   4 | 5 | 6           Your choices are defined, they must be 1 to 9...          4 | 5 | 6
   7 | 8 | 9                              Have Fun!                              7 | 8 | 9     
   
   """
#Define the print_board function

def print_board():
    
    print board[1],'|',board[2],'|',board[3]
    print "----------"
    print board[4],"|",board[5],"|",board[6]
    print "----------"
    print board[7],"|",board[8],"|",board[9]

def is_winner(board, player):
	if board[1] == player and board[2] == player and board[3] == player or \
		board[4] == player and board[5] == player and board[6] == player or \
		board[7] == player and board[8] == player and board[9] == player or \
		board[1] == player and board[5] == player and board[9] == player or \
		board[1] == player and board[4] == player and board[7] == player or \
		board[2] == player and board[5] == player and board[8] == player or \
		board[3] == player and board[6] == player and board[9] == player or \
		board[3] == player and board[5] == player and board[7] == player:
			
			return True
	else: 
		return False

def is_board_full(board):
	if " " in board:
		return False
	else:
		return True
   
while True:
        
	os.system("clear")
	print_header()
	print_board()
    
#Get player X Input
	
	choice = raw_input("Please choose an empty space for X:")
	choice = int(choice)

	
#Check to see if space is empty first

	if board[choice] == " ": 
		board[choice] = "X"
	else:
		print "Sorry, this spot is taken"
		time.sleep(1)

#Check for X win

	if is_winner(board,"X"):	
		os.system("clear")
		print_header()
		print_board()
		print "~~X WINS~~"
		break
#Check for a tie (if the board is full)
	
	if is_board_full(board):
		
		os.system("clear")
		print_header()
		print_board()
	
	
#If the board is full, do something
	
	
		print "Its a tie!"
		break
		
#Get player O input
		
	os.system("clear")
	print_header()
	print_board()
		
		
	choice = raw_input("Please choose an empty space for O:")
	choice = int(choice)
#Check to see if space is empty first

	if board[choice] == " ": 
		board[choice] = "O"
	else:
		print "Sorry, this spot is taken"
		time.sleep(1)

#Check for O win

	
	if is_winner(board,"O"):
	
		os.system("clear")
		print_header()
		print_board()
		print "~~O WINS~~"
		break
#Check for a tie (if the board is full)

	if is_board_full(board):
	
		os.system("clear")
		print_header()
		print_board()
	
	
#If the board is full, do something
	
	
		print "Its a tie!"
	
		break
