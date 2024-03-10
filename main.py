from enum import Enum
import tkinter as tk
import emoji

class Piece(Enum):
    EMPTY = 0
    SILVER = 1
    GOLD = 2
    FLAGSHIP = 3

class Breakthru:
    emoji.emojize(":passenger_ship:")

    def __init__(self, player):
        # Define the player's team
        self.player = player # G for GOLD and S for SILVER

        #TODO: Implementar a escolha aleatória do jogador inicial
        self.current_player = player #Define the current player

        # Config variables
        self.save_click = None # Save the first click to move the piece
        self.buttonSize = 2 # Size of the buttons in the GUI

        # Define the size of the board
        self.rows = 7
        self.cols = 7  # The board is square

        self.window = tk.Tk()
        self.window.title(self.__class__.__name__) #Sim, escrever isso como string é mais facil, mas sla, isso tai pra usar né
        #self.window.geometry("500x500")

        # Initialize the board with EMPTY pieces
        self.board = [[Piece.EMPTY for _ in range(self.cols)] for _ in range(self.rows)]

        # Set up the GUI
        self.buttons = []
        for i in range(self.rows):
            row_buttons = []
            for j in range(self.cols):
                #button = tk.Button(self.window, width=self.buttonSize*2, height=self.buttonSize, text=" ", font=("Arial", 32), bg="white",command=lambda l=i, c=j: self.onClickListner(l, c))
                #button.grid(row=i, column=j)
                button = self.generate_botton(i, j, Piece.EMPTY)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        # Set up the GOLD pieces in the middle
        center = self.rows // 2
        for i in range(center - 1, center + 2):
            for j in range(center - 1, center + 2):
                self.board[i][j] = Piece.GOLD
                self.buttons[i][j] = self.generate_botton(i, j, Piece.GOLD, self.buttons[i][j])

        # Place the FLAGSHIP in the center
        self.board[center][center] = Piece.FLAGSHIP
        self.buttons[center][center] = self.generate_botton(center, center, Piece.FLAGSHIP, self.buttons[center][center])

        # Place the SILVER pieces
        for i in range(0, self.rows):
            row_buttons = []
            # Primeira e última linhas (índice 0 e 6)
            if i == 0 or i == self.rows - 1:
                # Coloca as peças SILVER nas colunas 3, 4 e 5
                for j in [2, 3, 4]:
                    self.board[i][j] = Piece.SILVER
                    self.buttons[i][j] = self.generate_botton(i, j, Piece.SILVER, self.buttons[i][j])
            # Linhas do meio
            else:
                # Coloca peças SILVER apenas nas colunas extremas das linhas 3, 4 e 5
                if i in [2, 3, 4]:
                    self.board[i][0] = Piece.SILVER
                    self.board[i][self.cols - 1] = Piece.SILVER
                    self.buttons[i][0] = self.generate_botton(i, 0, Piece.SILVER, self.buttons[i][0])
                    self.buttons[i][self.cols - 1] = self.generate_botton(i, self.cols - 1, Piece.SILVER, self.buttons[i][self.cols - 1])

        self.window.mainloop()

        #self.gui_board()

    def generate_botton(self, row, col, piece, button=None):

        # Dicionário para mapear os tipos de peças para emojis
        piece_to_emoji = {
            Piece.EMPTY: '   ',
            Piece.SILVER: ":passenger_ship:",
            Piece.GOLD: ":passenger_ship:",
            Piece.FLAGSHIP: ":ship:"
        }

        piece_to_color = {
            Piece.EMPTY: "white",
            Piece.SILVER: "silver",
            Piece.GOLD: "gold",
            Piece.FLAGSHIP: "yellow"
        }

        if piece == Piece.EMPTY:
            button = tk.Button(self.window, width=self.buttonSize * 2, height=self.buttonSize, text=" ",
                               font=("Arial", 32), bg=piece_to_color[piece], command=lambda l=row, c=col: self.onClickListner(l, c))
            button.grid(row=row, column=col)
            return button

        button = tk.Button(self.window, width=self.buttonSize * 2, height=self.buttonSize,
                           text=emoji.emojize(piece_to_emoji[Piece.FLAGSHIP]), font=("Arial", 32), bg=piece_to_color[piece],
                           command=lambda l=row, c=col: self.onClickListner(l, c))
        button.grid(row=row, column=col)
        return button

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

    def onClickListner(self, row, col):
        print(f"Button clicked at {row}, {col}")

        if self.save_click  is None:
            self.save_click=row, col

        elif self.save_click:
            self.move_piece(self.save_click[0], self.save_click[1], row, col)
            self.save_click = None

    def move_piece(self, row, col, new_row, new_col):
        # Verifica se a peça está se movendo para uma posição válida
        #if not self.is_valid_move(row, col, new_row, new_col):
        #    print("Movimento inválido!")
        #    return

        # Move a peça para a nova posição
        self.board[new_row][new_col] = self.board[row][col]
        self.board[row][col] = Piece.EMPTY

        # Atualiza a interface gráfica
        self.buttons[new_row][new_col] = self.generate_botton(new_row, new_col, self.board[new_row][new_col], self.buttons[new_row][new_col])
        self.buttons[row][col] = self.generate_botton(row, col, self.board[row][col], self.buttons[row][col])


        # Atualiza a interface gráfica
        #self.gui_board()

if __name__ == "__main__":

    print("Bem-vindo ao Breakthru!")
    print("O jogo começa com as peças GOLD no centro e as peças SILVER nas extremidades.")
    print("O objetivo do jogo é mover o FLAGSHIP para a borda oposta do tabuleiro.")
    print("As peças SILVER devem capturar o FLAGSHIP antes que ele alcance a borda oposta.")
    print("O jogador Inicial é escolhido aleatoriamente.")
    print("Boa sorte!")
    print("*******************************************************************************")
    print("Escolha com qual time tu vais jogar: [S]ILVER ou [G]OLD?")

    player = "G"
    while player not in ["S", "G"]:
        player = input().upper()

    game = Breakthru(player)
    #ame.print_board()
