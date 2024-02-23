import time

# Define colors using hexadecimal values
redColor = 0xff0000
greenColor = 0x00ff00
blueColor = 0x0000ff


# Define the Game class
class Game:
    def __init__(self, bb, neoPin, neoCount):
        # Initialize game parameters
        self.bb = bb
        self.neoPin = neoPin
        self.neoCount = neoCount
        self.board = [[]]  # Initialize an empty board
        self.player_moves = {"x": [], "o": []}  # Store moves made by each player
        # Define square configurations for the tic-tac-toe grid
        self.SQUARES = {
            1: [(177, 205, 211, 235, 238, 210, 204, 180), (178, 179, 206, 209, 237, 236, 212, 203)],
            2: [(110, 114, 140, 148, 145, 141, 115, 107), (109, 108, 113, 142, 146, 147, 139, 116)],
            3: [(17, 45, 51, 75, 78, 50, 44, 20), (18, 19, 46, 49, 77, 76, 52, 43)],
            4: [(182, 200, 216, 230, 233, 215, 199, 185), (183, 184, 201, 214, 232, 231, 217, 198)],
            5: [(105, 119, 135, 153, 150, 136, 120, 102), (104, 103, 118, 137, 151, 152, 134, 121)],
            6: [(22, 40, 56, 70, 73, 55, 39, 25), (23, 24, 41, 54, 72, 71, 57, 38)],
            7: [(187, 195, 221, 225, 228, 220, 194, 190), (188, 189, 196, 219, 227, 226, 222, 193)],
            8: [(100, 124, 130, 158, 155, 131, 125, 97), (99, 98, 123, 132, 156, 157, 129, 126)],
            9: [(27, 35, 61, 65, 68, 60, 34, 30), (28, 29, 36, 59, 67, 66, 62, 33)]
        }
        # Define square borders for highlighting
        self.SQUARE_BORDERS = {
            1: [170, 171, 172, 173, 174, 175, 176, 240, 241, 242, 243, 244, 245, 176, 207, 208, 239, 181, 202, 213,
                234],
            2: [80, 81, 82, 83, 84, 85, 170, 171, 172, 173, 174, 175, 111, 112, 143, 144, 106, 117, 138, 149],
            3: [10, 11, 12, 13, 14, 15, 80, 81, 82, 83, 84, 85, 16, 47, 48, 79, 21, 42, 53, 74],
            4: [165, 166, 167, 168, 169, 170, 245, 246, 247, 248, 249, 250, 181, 202, 213, 234, 186, 197, 218, 229],
            5: [85, 86, 87, 88, 89, 90, 165, 166, 167, 168, 169, 170, 106, 117, 138, 149, 101, 122, 133, 154],
            6: [5, 6, 7, 8, 9, 10, 85, 86, 87, 88, 89, 90, 21, 42, 53, 74, 26, 37, 58, 69],
            7: [160, 161, 162, 163, 164, 165, 250, 251, 252, 253, 254, 255, 186, 197, 218, 229, 191, 192, 223, 224],
            8: [90, 91, 92, 93, 94, 95, 160, 161, 162, 163, 164, 165, 101, 122, 133, 154, 96, 127, 128, 159],
            9: [0, 1, 2, 3, 4, 5, 90, 91, 92, 93, 94, 95, 26, 37, 58, 69, 31, 32, 63, 64]
        }

    # Method to check if a player has won
    def check_win(self, player):
        # Define winning combinations
        winning_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
            [1, 5, 9], [3, 5, 7]  # Diagonals
        ]
        # Check if any winning combination is present in player's moves
        for combination in winning_combinations:
            if all(square in self.player_moves[player] for square in combination):
                return True, combination  # Return True if winning combination found
        return False, None  # Otherwise, return False

    # Method to convert cell number to row and column
    def cell_number_to_row_col(self, cell_number):
        row = (cell_number - 1) // 3
        col = (cell_number - 1) % 3
        return row, col

    # Method to highlight square borders
    def set_square_borders(self, square_num, color):
        borders = self.SQUARE_BORDERS.get(square_num)
        if borders:
            for val in borders:
                self.bb.Neo.SetColor(val, color)

    # Method to set square item (X or O) and color
    def set_square(self, square_num, item, color):
        square = self.SQUARES.get(square_num)
        if square:
            for index, val in enumerate(square[0 if item == 'x' else 1]):
                self.bb.Neo.SetColor(val, color)

    # Method to draw external borders of the grid
    def draw_external_borders(self, color):
        for z in range(0, 16):
            self.bb.Neo.SetColor(z, color)
            self.bb.Neo.SetColor(z + 240, color)

    # Method to draw horizontal rows of the grid
    def draw_rows(self, color):
        for z in range(0, 16, 5):
            for x in range(0, 256, 32):
                self.bb.Neo.SetColor(x + z, color)
                self.bb.Neo.SetColor(x + 31 - z, color)

    # Method to draw vertical columns of the grid
    def draw_columns(self, color):
        for z in range(80, 96):
            self.bb.Neo.SetColor(z, color)
        for z in range(160, 176):
            self.bb.Neo.SetColor(z, color)

    # Method to highlight winning lights
    def winning_lights(self, item, color, combination):
        # Highlight the winning combination
        item = item
        color = color
        toggle_time = 0.05
        toggle_count = 20
        self.draw_external_borders(blueColor)
        self.draw_rows(blueColor)
        self.draw_columns(blueColor)
        self.bb.Neo.Show(self.neoPin, self.neoCount)
        # Toggle the colors for visual effect
        for i in range(toggle_count):
            self.set_square(combination[0], item, 0x000000)
            self.set_square(combination[1], item, 0x000000)
            self.set_square(combination[2], item, 0x000000)
            self.bb.Neo.Show(self.neoPin, self.neoCount)
            time.sleep(toggle_time)
            self.set_square(combination[0], item, color)
            self.set_square(combination[1], item, color)
            self.set_square(combination[2], item, color)
            self.bb.Neo.Show(self.neoPin, self.neoCount)
            time.sleep(toggle_time)

    # Method to color square borders
    def coloring_square_borders(self, color, square_number):
        self.draw_external_borders(blueColor)
        self.draw_rows(blueColor)
        self.draw_columns(blueColor)
        self.bb.Neo.Show(self.neoPin, self.neoCount)
        for i in range(1, 10):
            if square_number == str(i):
                self.set_square_borders(i, color)
                self.bb.Neo.Show(self.neoPin, self.neoCount)
                break

    # Method to print the current state of the board in console and on microcomputer LCD screen
    def print_board(self):
        self.bb.Display.Clear(0)
        x = 10
        y = 10
        print("_______________________________")
        for i in range(3):
            row = [str(i * 3 + j + 1) if cell == ' ' else cell for j, cell in enumerate(self.board[i])]
            print(" | ".join(row))
            self.bb.Display.DrawTextScale(" | ".join(row), 1, x, y, 2, 1)
            if i < 2:
                print("-" * 9)
                self.bb.Display.DrawTextScale("-" * 9, 1, x, y + 10, 2, 1)
            y += 20
        self.bb.Display.Show()

    # Method to check if the game is over
    def is_game_over(self):
        # Check rows, columns, and diagonals for a win or a tie
        for row in self.board:
            if row.count(row[0]) == 3 and row[0] != ' ':
                return True

        for col in range(3):
            check = []
            for row in self.board:
                check.append(row[col])
            if check.count(check[0]) == 3 and check[0] != ' ':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        # Check for tie
        for row in self.board:
            for val in row:
                if val == ' ':
                    return False
        return True

    # Method to evaluate the current state of the game
    def evaluate(self):
        # Check for winning conditions
        for row in self.board:
            if row.count('O') == 3:
                return 1    # Player O wins
            if row.count('X') == 3:
                return -1   # Player X wins

        for col in range(3):
            check = []
            for row in self.board:
                check.append(row[col])
            if check.count('O') == 3:
                return 1    # Player O wins
            if check.count('X') == 3:
                return -1   # Player X wins

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 'O':
            return 1    # Player O wins
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 'X':
            return -1   # Player X wins

        if self.board[0][2] == self.board[1][1] == self.board[2][0] == 'O':
            return 1    # Player O wins
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == 'X':
            return -1   # Player O wins

        return 0    # It's a tie

    # Method to implement the minimax algorithm for AI move selection
    def minimax(self, depth, is_maximizing, alpha, beta):
        if self.is_game_over():
            return self.evaluate()

        if is_maximizing:
            max_eval = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'O'
                        evaluation = self.minimax(depth + 1, False, alpha, beta)
                        self.board[i][j] = ' '
                        max_eval = max(max_eval, evaluation)
                        alpha = max(alpha, evaluation)
                        if beta <= alpha:
                            break
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'X'
                        evaluation = self.minimax(depth + 1, True, alpha, beta)
                        self.board[i][j] = ' '
                        min_eval = min(min_eval, evaluation)
                        beta = min(beta, evaluation)
                        if beta <= alpha:
                            break
            return min_eval

    # Method for AI to make a move using the minimax algorithm
    def bot_move(self):
        best_eval = -float('inf')
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    evaluation = self.minimax(0, False, -float('inf'), float('inf'))
                    self.board[i][j] = ' '
                    if evaluation > best_eval:
                        best_eval = evaluation
                        best_move = (i, j)

        return best_move

    # Method to run the game
    def do_game(self):
        # Initialize the game state
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.bb.Display.Clear(0)
        self.draw_external_borders(blueColor)
        self.draw_rows(blueColor)
        self.draw_columns(blueColor)
        self.bb.Neo.Show(self.neoPin, self.neoCount)
        self.print_board()
        arena = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]  # Available squares
        moves_made = 0  # Track number of moves
        self.bb.Button.Enable('a', True)  # Enable button 'a' for user input
        while len(arena) > 0:  # Continue until all squares are filled
            while True:
                index = 0
                while True:
                    self.coloring_square_borders(redColor, arena[index])  # Highlight square
                    if self.bb.Button.JustPressed('a'):  # Check for button press
                        square = arena[index - 1]  # Get selected square
                        row, col = self.cell_number_to_row_col(int(square))
                        self.board[row][col] = 'X'  # Set player's move
                        break
                    index = (index + 1) % len(arena)  # Move to next square
                    time.sleep(0.5)  # Delay for visual effect
                if square in arena:  # Check if selected square is available
                    moves_made += 1
                    for i in range(1, 10):
                        if square == str(i):
                            self.set_square(i, "x", redColor)  # Mark player's move on the board
                            self.player_moves["x"].append(i)  # Record player's move
                            break
                    break
                else:
                    print("try another square")  # Prompt user to try another square
                    continue
            self.bb.Neo.Show(self.neoPin, self.neoCount)  # Update NeoPixel display
            arena.remove(square)  # Remove selected square from available squares
            self.print_board()  # Print the updated board
            time.sleep(1)  # Delay for visual effect

            x_has_won, x_winning_combination = self.check_win("x")  # Check if player X has won
            y_has_won, y_winning_combination = self.check_win("o")  # Check if player O has won

            if x_has_won:  # If player X has won
                print("Player X wins with combination:", x_winning_combination)  # Print winning message
                self.bb.System.Println("Player X wins with")
                self.bb.System.Println(f"combination:{x_winning_combination}")  # Print winning combination
                self.winning_lights("x", redColor, x_winning_combination)  # Highlight winning combination
                self.bb.Neo.Clear()  # Clear NeoPixel display
                break
            if y_has_won:  # If player O has won
                print("Player Y wins with combination:", y_winning_combination)  # Print winning message
                self.bb.System.Println("Player Y wins with")
                self.bb.System.Println(f"combination:{y_winning_combination}")  # Print winning combination
                self.winning_lights("o", greenColor, y_winning_combination)  # Highlight winning combination
                self.bb.Neo.Clear()  # Clear NeoPixel display
                break
            if moves_made == 9:  # If all squares are filled (tie)
                print("It's a tie!")  # Print tie message
                self.bb.System.Println("It's a tie!")  # Print tie message
                self.bb.Neo.Clear()  # Clear NeoPixel display
                break
            if len(arena) > 0:  # If there are available squares
                bot_row, bot_col = self.bot_move()  # Get AI move
                self.board[bot_row][bot_col] = 'O'  # Set AI move on the board
                square = str(bot_row * 3 + bot_col + 1)  # Get square number
                time.sleep(0.5)  # Delay for visual effect
            if len(arena) > 0:  # If there are available squares
                moves_made += 1
                for i in range(1, 10):
                    if square == str(i):
                        self.set_square(i, "o", greenColor)  # Mark AI's move on the board
                        self.player_moves["o"].append(i)  # Record AI's move
                        break
                else:
                    print("try another square")  # Prompt user to try another square

                self.bb.Neo.Show(self.neoPin, self.neoCount)  # Update NeoPixel display
                x_has_won, x_winning_combination = self.check_win("x")  # Check if player X has won
                y_has_won, y_winning_combination = self.check_win("o")  # Check if player O has won
                self.print_board()  # Print the updated board
                if x_has_won:  # If player X has won
                    print("Player X wins with combination:", x_winning_combination)  # Print winning message
                    self.bb.System.Println("Player X wins with")
                    self.bb.System.Println(f"combination:{x_winning_combination}")  # Print winning combination
                    self.winning_lights("x", redColor, x_winning_combination)  # Highlight winning combination
                    self.bb.Neo.Clear()  # Clear NeoPixel display
                    break
                if y_has_won:  # If player O has won
                    print("Player Y wins with combination:", y_winning_combination)  # Print winning message
                    self.bb.System.Println("Player Y wins with")
                    self.bb.System.Println(f"combination:{y_winning_combination}")  # Print winning combination
                    self.winning_lights("o", greenColor, y_winning_combination)  # Highlight winning combination
                    self.bb.Neo.Clear()  # Clear NeoPixel display
                    break
                if moves_made == 9:  # If all squares are filled (tie)
                    print("It's a tie!")  # Print tie message
                    self.bb.System.Println("It's a tie!")  # Print tie message
                    self.bb.Neo.Clear()  # Clear NeoPixel display
                    break
                if len(arena) != 0:  # If there are available squares
                    arena.remove(square)  # Remove selected square from available squares
        self.bb.Neo.Show(self.neoPin, self.neoCount)  # Update NeoPixel display
