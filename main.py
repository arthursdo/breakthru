from enum import Enum
import tkinter as tk


class Piece(Enum):
    EMPTY = 0
    SILVER = 1
    GOLD = 2
    FLAGSHIP = 3

class Breakthru:
    def __init__(self):

        # Define initial state of the game


        # Define the size of the board
        self.rows = 7
        self.cols = 7  # The board is square

        # Initialize the board with EMPTY pieces
        self.board = [[Piece.EMPTY for _ in range(self.cols)] for _ in range(self.rows)]

        # Set up the GOLD pieces in the middle
        center = self.rows // 2
        for i in range(center - 1, center + 2):
            for j in range(center - 1, center + 2):
                self.board[i][j] = Piece.GOLD

        # Place the FLAGSHIP in the center
        self.board[center][center] = Piece.FLAGSHIP

        # Place the SILVER pieces
        for i in range(0, self.rows):
            # Primeira e última linhas (índice 0 e 6)
            if i == 0 or i == self.rows - 1:
                # Coloca as peças SILVER nas colunas 3, 4 e 5
                for j in [2, 3, 4]:
                    self.board[i][j] = Piece.SILVER
            # Linhas do meio
            else:
                # Coloca peças SILVER apenas nas colunas extremas das linhas 3, 4 e 5
                if i in [2, 3, 4]:
                    self.board[i][0] = Piece.SILVER
                    self.board[i][self.cols - 1] = Piece.SILVER


    def print_board(self):
        # Dicionário para mapear os tipos de peças para emojis
        piece_to_emoji = {
            Piece.EMPTY: '   ',
            Piece.SILVER: '🔵',
            Piece.GOLD: '🟡',
            Piece.FLAGSHIP: '🔴'
        }

        # Cabeçalho do tabuleiro com números das colunas
        header = '  ' + ' '.join(f' {i}  ' for i in range(1, self.cols + 1))
        print(header)

        # Imprimir o tabuleiro com as linhas numeradas
        for i, row in enumerate(self.board):
            print('+' + '---+' * self.cols)
            row_str = "|".join(piece_to_emoji[piece].center(3) if piece != Piece.EMPTY else '   ' for piece in row)
            print(f"{i + 1} |" + row_str + '|')
        print('+' + '---+' * self.cols)

if __name__ == "__main__":
    game = Breakthru()
    game.print_board()
