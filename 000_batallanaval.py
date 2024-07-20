import random

class BattleshipGame:
    def __init__(self):
        self.board_size = 5
        self.num_ships = 3
        self.board = [['~'] * self.board_size for _ in range(self.board_size)]
        self.ships = []
        self.setup_ships()

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def setup_ships(self):
        while len(self.ships) < self.num_ships:
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            if (row, col) not in self.ships:
                self.ships.append((row, col))

    def is_valid_guess(self, row, col):
        return 0 <= row < self.board_size and 0 <= col < self.board_size

    def make_guess(self, row, col):
        if (row, col) in self.ships:
            self.board[row][col] = 'X'
            self.ships.remove((row, col))
            print("¡Tocado!")
        else:
            self.board[row][col] = 'O'
            print("Agua")

    def play(self):
        print("¡Bienvenido a Batalla Naval!")
        while len(self.ships) > 0:
            self.print_board()
            try:
                guess_row = int(input("Adivina fila (0-4): "))
                guess_col = int(input("Adivina columna (0-4): "))
                if not self.is_valid_guess(guess_row, guess_col):
                    print("Coordenadas no válidas. Inténtalo de nuevo.")
                    continue
                self.make_guess(guess_row, guess_col)
            except ValueError:
                print("Entrada no válida. Por favor ingresa números.")
        print("¡Has hundido todos los barcos enemigos!")
        self.print_board()

if __name__ == "__main__":
    game = BattleshipGame()
    game.play()
