# Uni-2nd-Year-Software-Dev-Portfolio
This is an electronic portfolio showcasing what Ive learned so far on this module for a University Assignment Submission in 2nd Year
# PORTFOLIO EXERCISE SELECTION (Choose 3 out of 6):
1. Guessing Game (week 1 & 2)
2. Select any 2 of your completed in live session Guided activity sheet (from week 2 to week
5)
3. Scientific calculator (Week 3)
4. Personally identifiable information encryption, decryption, and conversion to binary,
decimal, octal, and hexadecimal (week 4)
5. Sudoku game (week 5)
6. Task management (week 5 & 6)

//
# [For each project, include a brief README file explaining
how the program works, how to run it, and any assumptions made]
# Guessing Game in Python

## Purpose:
This project implements a simple number guessing game where the player attempts to guess a randomly generated number within a specified range. The program provides feedback after each guess to help the player narrow down their options and tracks the number of attempts.

---

## Features:
1. **Random Number Generation**:
   - A random number is generated within a predefined range (1 to 100) using the `random` module.

2. **Player Interaction**:
   - Players are prompted to enter guesses.
   - Feedback is provided after each guess:
     - "Too low!" if the guess is below the number.
     - "Too high!" if the guess is above the number.
     - "Congratulations!" if the guess is correct.

3. **Attempts Limitation**:
   - Players have a maximum of 10 attempts to guess the number.
   - If the player uses all attempts without guessing correctly, the game reveals the secret number.

4. **Input Validation**:
   - Ensures the player's guess is within the valid range.
   - Handles non-integer inputs gracefully with appropriate error messages.

5. **Game Loop**:
   - The game continues until the player guesses the number or runs out of attempts.

---

## How to Run:
 **Playing the Game**:
   - Follow the prompts to guess the number.
   - Example input: `50` (Guessing the number 50).
   - After 10 incorrect attempts, the game will reveal the correct number.

---

### Specifications:
1. **Grid**:
   - The game uses a 9x9 grid where each cell starts as `0` (empty).
   
2. **Input**:
   - The player enters moves in the format: `row,column,number` (e.g., `1,2,5`).
   - Rows and columns are 1-indexed (1 for the first row, 1 for the first column).

3. **Validation**:
   - The program checks if:
     - The number is not already in the same row, column, or 3x3 sub-grid.
     - The cell is empty (not already filled).
   - Only numbers 1-9 are allowed.

4. **Grid Display**:
   - After each valid move, the grid is displayed with empty cells shown as `.`.

5. **Game End**:
   - The game ends when all cells are filled with valid numbers.
   - A congratulatory message is shown when the puzzle is completed.

6. **Error Handling**:
   - The program provides error messages for invalid moves, such as:
     - "Invalid move" for conflicting numbers.
     - "Cell already filled" if trying to overwrite a filled cell.
     - "Out of range" for numbers outside 1-9.






# Sudoku Game in Python

## Purpose:
This project implements a basic Sudoku game where players fill a 9x9 grid with numbers according to standard Sudoku rules. The program validates each input, updates the grid dynamically, and provides feedback on invalid moves. The game continues until the grid is completely filled with valid numbers.

---

## Features:
1. **Grid Representation**:
   - The Sudoku grid is represented as a 9x9 2D list.
   - Each cell is initialized to `0`, representing an empty space.
   
2. **User Interaction**:
   - Players enter their moves in the format: `row,column,number` (e.g., `1,2,5`).
   - Rows and columns are 1-indexed for user convenience.

3. **Input Validation**:
   - Ensures all inputs are integers within the range (1-9).
   - Validates moves against Sudoku rules:
     - No duplicates in the same row.
     - No duplicates in the same column.
     - No duplicates in the same 3x3 sub-grid.
   - Prevents overwriting of non-empty cells.

4. **Dynamic Grid Display**:
   - After each valid move, the updated grid is displayed.
   - Empty cells are shown as `.` for clarity.

5. **Game Completion**:
   - The game ends when all cells are filled with valid numbers.
   - A congratulatory message is displayed upon completion.

6. **Error Handling**:
   - Provides descriptive error messages for invalid inputs or moves.
   - Ensures smooth gameplay by handling incorrect formats or out-of-range values.

---

## How to Run:
 **Playing the Game**:
   - Follow the prompts to input your moves.
   - Example input: `1,3,7` (Places number 7 at row 1, column 3).
   - Enter `q` to quit the game at any time.

---

## Specifications:
1. **Number Range**:
   - The secret number is randomly selected from the range of 1 to 100.

2. **Maximum Attempts**:
   - Players are limited to 10 attempts to guess the number.

3. **Error Handling**:
   - Invalid inputs (non-integer or out-of-range values) are handled with descriptive error messages.
   - The player is not penalized with an additional attempt for invalid inputs.

4. **Game Flow**:
   - The program provides feedback on every guess until the correct number is guessed or all attempts are used.
   - At the end of the game, the correct number is displayed if the player fails to guess it.







# Task Manager in Python

## Purpose:
This project implements a simple task management system where users can add, view, and delete tasks associated with specific days of the week or months of the year. It allows users to organize tasks based on time periods and interact with them through a simple menu-driven interface.

---

## Features:
1. **Task Organization**:
   - Tasks can be associated with specific days of the week or months of the year.
   - The tasks for each day or month are stored in dictionaries:
     - `days_of_week`: A dictionary where each day of the week (Monday to Sunday) maps to a list of tasks.
     - `months_of_year`: A dictionary where each month (January to December) maps to a list of tasks.

2. **Task Management**:
   - **Add a Task**: Users can add tasks to a specific day of the week or month of the year.
   - **View Tasks**: Users can view all tasks for a specific day or month.
   - **Delete a Task**: Users can delete a specific task from a day or month.
   
3. **User Interface**:
   - The user interacts with the program through a text-based menu with options to add, view, or delete tasks.
   - The menu allows users to choose between adding tasks to days or months.
   
4. **Input Validation**:
   - The program validates user input to ensure the correct day or month is selected.
   - Proper error handling is implemented for invalid choices and non-existent tasks.
   
5. **Continuous Operation**:
   - The menu-driven interface loops until the user chooses to exit.

---

## How to Run:
**Using the Task Manager**:
   - Follow the menu options to manage tasks:
     - **Add a task**: Enter the time period and task details.
     - **View tasks**: Select the day or month to view tasks.
     - **Delete a task**: Choose the task you wish to delete from the list.

---

## Specifications:
1. **Dictionaries for Task Management**:
   - `days_of_week`: Maps each day (e.g., "Monday", "Tuesday") to a list of tasks for that day.
   - `months_of_year`: Maps each month (e.g., "January", "February") to a list of tasks for that month.

2. **Task Operations**:
   - **Add Task**: Prompts the user to input a task and adds it to the selected day or month.
   - **View Tasks**: Displays a list of tasks for the chosen day or month.
   - **Delete Task**: Prompts the user to choose a task to delete from the list.

3. **Error Handling**:
   - Validates user input for valid days and months.
   - Handles cases where the user inputs non-existent tasks or makes invalid choices.

4. **Exiting the Program**:
   - The program continues to show the menu until the user selects the option to exit.
