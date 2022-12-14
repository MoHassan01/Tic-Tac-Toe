# -*- coding: utf-8 -*-
"""Mohamed Hassan TTT

"""

def create_empty_board():
  global board
  board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""## Show Board"""

def show_board(board):
  i = 0
  for i in range(len(board)):
    print(board[i], end="     ")
    if i in [2, 5]:
      print("\n\n")

"""## Set Players"""

def set_players():
  x = 'X'
  y = 'O'
  print(f"Player 1: {x}\nPlayer 2: {y}")

set_players()

"""## Take Input"""

def take_input(board, player):
  if player == 'O':
    num = int(input("Enter the number representing the desired position: "))
    while board[num - 1] not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
      num = int(input("Kindly enter a right position: "))
    board[board.index(num)] = 'O'
  if player == 'X':
    num = int(input("Enter the number representing the desired position: "))
    while board[num - 1] not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
      num = int(input("Kindly enter a right position: "))
    board[board.index(num)] = 'X'
  return board

"""## Check Full Board"""

def check_full_board(board):
  global w1, w2, w3, w4, w5, w6, w7, w1
  w1 = (board[0] == board[1] == board[2])
  w2 = (board[3] == board[4] == board[5])
  w3 = (board[6] == board[7] == board[8])
  w4 = (board[0] == board[3] == board[6])
  w5 = (board[1] == board[4] == board[7])
  w6 = (board[2] == board[5] == board[8])
  w7 = (board[0] == board[4] == board[8])
  w8 = (board[2] == board[4] == board[6])
  if w1 or w2 or w3 or w4 or w5 or w6 or w7 or w8:
    return True
  else:
    return False

"""## Let's Play"""

def play():
  create_empty_board()
  show_board(board)
  print("\n")
  set_players()
  global i
  for i in range(len(board) - 1):
    while check_full_board(board) == False:
      show_board(board)
      print('\n')
      i += 1
      if i == 10:
        return ('Draw!')
        break
      print("Player 1 Turn:\n")
      player = 'X'
      take_input(board, player)
      if check_full_board(board) == True:
        show_board(board)
        print('\n')
        print("Congrats! Player 1 wins.")
        break
      show_board(board)
      print('\n')
      i += 1
      if i == 10:
        return ('Draw!')
        break
      print("Player 2 Turn:\n")
      player = 'O'
      take_input(board, player)
      if check_full_board(board) == True:
        show_board(board)
        print('\n')
        print("Congrats! Player 2 wins.")
        break

if __name__ == '__main__':
    play()