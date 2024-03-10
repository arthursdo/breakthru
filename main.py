from enum import Enum
import tkinter as tk
import emoji

class Piece(Enum):
    EMPTY = 0
    SILVER = 1
    GOLD = 2
    FLAGSHIP = 3

class Breakthru:

    def __init__(self, player):
        self.player = player

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

        self.gui_board()

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


    def gui_board(self):
        # Dicionário para mapear os tipos de peças para emojis
        piece_to_emoji = {
            Piece.EMPTY: '   ',
            Piece.SILVER: ":blue_circle:",
            Piece.GOLD: ":yellow_circle:",
            Piece.FLAGSHIP: ":red_circle:"
        }


        #NOTE: Isa, se tu quiseres mudar a cor das peças, muda aqui, da pra usar o nome da cor ou o código hexadecimal (ex: "red" ou "#ff0000")
        piece_to_color = {
            Piece.EMPTY: "white",
            Piece.SILVER: "silver",
            Piece.GOLD: "gold",
            Piece.FLAGSHIP: "red"
        }

        # Cria a janela principal
        window = tk.Tk()
        window.title("Breakthru")

        # Cria o tabuleiro
        for i in range(self.rows):
            for j in range(self.cols):
                # Cria um frame para cada peça
                frame = tk.Frame(
                    master=window,
                    relief=tk.RAISED,
                    borderwidth=1
                )
                frame.grid(row=i, column=j)

                # Adiciona um label com o emoji correspondente à peça
                #label = tk.Label(master=frame, text=emoji.emojize(piece_to_emoji[self.board[i][j]]), font=("Arial", 32))
                label = tk.Label(master=frame, text='    ', font=("Arial", 32), bg="#ffffff")
                label.pack()

        # Inicia a janela principal
        window.mainloop()

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
