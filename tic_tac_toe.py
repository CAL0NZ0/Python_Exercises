# This is Tic-Tac-Toe. Enough said.

def horiz():
  print(" --- " * board_size)

def vert():
  print("|    " * (board_size + 1))

if __name__ == '__main__':
  board_size = int(input('Enter a board size: '))

  for x in range(board_size):
    horiz()
    vert()
  horiz()

