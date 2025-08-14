def print_grid(grid):
  """Displays the current state of the Sudoku grid."""
  for row in grid:
      print(" ".join(str(cell) if cell != 0 else "." for cell in row))


def is_valid_input(grid, row, col, num):
  """Validates whether a number can be placed at the given position."""
  # Check the row
  if num in grid[row]:
      return False

  # Check the column
  if num in [grid[i][col] for i in range(9)]:
      return False

  # Check the 3x3 sub-grid
  start_row, start_col = (row // 3) * 3, (col // 3) * 3
  for i in range(start_row, start_row + 3):
      for j in range(start_col, start_col + 3):
          if grid[i][j] == num:
              return False

  return True


def is_grid_filled(grid):
  """Checks if the grid is completely filled."""
  for row in grid:
      if 0 in row:
          return False
  return True


def main():
  # Initialize the 9x9 grid
  grid = [[0 for _ in range(9)] for _ in range(9)]

  print("Welcome to Basic Sudoku!")
  print("Enter your moves in the format: row,column,number (e.g., 1,2,5)")
  print("Rows and columns are 1-indexed. Enter 'q' to quit.")
  print_grid(grid)

  while not is_grid_filled(grid):
      user_input = input("Enter your move: ")

      if user_input.lower() == 'q':
          print("Thanks for playing! Goodbye.")
          break

      try:
          # Parse input
          row, col, num = map(int, user_input.split(","))

          # Convert to 0-indexed
          row, col = row - 1, col - 1

          # Validate input ranges
          if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
              print("Error: Inputs must be in the range 1-9.")
              continue

          # Check if the cell is already filled
          if grid[row][col] != 0:
              print("Error: Cell is already filled. Choose another one.")
              continue

          # Validate placement
          if is_valid_input(grid, row, col, num):
              grid[row][col] = num
              print("Updated grid:")
              print_grid(grid)
          else:
              print("Error: Invalid move. The number conflicts with Sudoku rules.")

      except ValueError:
          print("Error: Invalid input format. Use the format row,column,number.")

  if is_grid_filled(grid):
      print("Congratulations! You've completed the Sudoku puzzle!")


if __name__ == "__main__":
  main()
