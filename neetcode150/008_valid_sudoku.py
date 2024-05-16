def is_valid_sudoku(board):
  """
  Checks if a Sudoku board is valid.

  Args:
      board: A list of lists representing the Sudoku board.

  Returns:
      True if the board is valid, False otherwise.
  """
  n = 9
  # Check rows
  for row in board:
    seen = set()
    for num in row:
      if num == ".":
        continue
      if num in seen:
        return False
      seen.add(num)

  # Check columns
  for col in range(n):
    seen = set()
    for row in range(n):
      num = board[row][col]
      if num == ".":
        continue
      if num in seen:
        return False
      seen.add(num)

  # Check sub-boxes
  sub_box_size = 3
  for start_row in range(0, n, sub_box_size):
    for start_col in range(0, n, sub_box_size):
      seen = set()
      for row in range(start_row, start_row + sub_box_size):
        for col in range(start_col, start_col + sub_box_size):
          num = board[row][col]
          if num == ".":
            continue
          if num in seen:
            return False
          seen.add(num)
  return True

# Example usage (valid board)
board = [
  ["5", "3", ".", ".", "7", ".", ".", ".", "."],
  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
  [".", "9", "8", ".", ".", ".", ".", "6", "."],
  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
  [".", 6, ".", ".", ".", ".", "2", "8", "."],
  [".", ".", ".", 4, "1", 9, ".", ".", "5"],
  [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

if is_valid_sudoku(board):
  print("Valid Sudoku board")
else:
  print("Invalid Sudoku board")

