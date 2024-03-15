from enum import Enum
import tkinter as tk
import emoji
import copy

class Piece(Enum):
    EMPTY = 0
    SILVER = 1
    GOLD = 2
    FLAGSHIP = 3

class Breakthru:

    def __init__(self, playerm, isCopy=False):
        # Define the player's team
        self.player = player # G for GOLD and S for SILVER
        self.aiPlayer = "G" if self.player == "S" else "S" # Define the AI player
        self.isCopy = isCopy

        #TODO: Implementar a escolha aleatória do jogador inicial
        self.current_player = player #Define the current player
        self.winner = None  # Define the winner
        self.silver_pieces = 12 # Number of SILVER pieces
        self.gold_pieces = 8 # Number of GOLD pieces (excluding the FLAGSHIP)
        self.states_explored = 0 # Number of states explored by the AI

        # Config variables
        self.save_click = None # Save the first click to move the piece
        self.buttonSize = 2 # Size of the buttons in the GUI

        # Define the size of the board
        self.rows = 7
        self.cols = 7  # The board is square

        if not isCopy:
            self.window = tk.Tk()
            self.window.title(self.__class__.__name__) #Sim, escrever isso como string é mais facil, mas sla, isso tai pra usar né
            self.window.title(f"{self.__class__.__name__} - {self.current_player} turn") # Define the title of the window for the current player
            #self.window.geometry("500x500")

        # Initialize the board with EMPTY pieces
        self.board = [[Piece.EMPTY for _ in range(self.cols)] for _ in range(self.rows)]

        # Set up the GUI
        self.buttons = []
        for i in range(self.rows):
            row_buttons = []
            for j in range(self.cols):
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
        if not isCopy:
            self.buttons[center][center] = self.generate_botton(center, center, Piece.FLAGSHIP, self.buttons[center][center])

        # Place the SILVER pieces
        for i in range(0, self.rows):
            row_buttons = []
            # Primeira e última linhas (índice 0 e 6)
            if i == 0 or i == self.rows - 1:
                # Coloca as peças SILVER nas colunas 3, 4 e 5
                for j in [2, 3, 4]:
                    self.board[i][j] = Piece.SILVER
                    if not isCopy:
                        self.buttons[i][j] = self.generate_botton(i, j, Piece.SILVER, self.buttons[i][j])
            # Linhas do meio
            else:
                # Coloca peças SILVER apenas nas colunas extremas das linhas 3, 4 e 5
                if i in [2, 3, 4]:
                    self.board[i][0] = Piece.SILVER
                    self.board[i][self.cols - 1] = Piece.SILVER
                    if not isCopy:
                        self.buttons[i][0] = self.generate_botton(i, 0, Piece.SILVER, self.buttons[i][0])
                        self.buttons[i][self.cols - 1] = self.generate_botton(i, self.cols - 1, Piece.SILVER, self.buttons[i][self.cols - 1])

        if not isCopy:
            self.window.mainloop()

    def copy_game_state(self):
        new_game = Breakthru(self.player, isCopy=True)
        new_game.board = copy.deepcopy(self.board)
        new_game.current_player = self.current_player
        new_game.aiPlayer = self.aiPlayer

        return new_game

    def generate_botton(self, row, col, piece, button=None):
        if self.isCopy:
            return

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

        piece_to_player = {
            Piece.SILVER: "S",
            Piece.GOLD: "G",
            Piece.FLAGSHIP: "G",
            Piece.EMPTY: "E"
        }

        if self.save_click  is None:
            if piece_to_player[self.board[row][col]] != self.current_player and self.board[row][col] != Piece.EMPTY:
                print_error("Não é a sua vez!")
                return

            if self.board[row][col] == Piece.EMPTY:
                print_error("Célula vazia!")
                return
            self.save_click=row, col

        elif self.save_click:
            if not self.is_move_valid(self.save_click[0], self.save_click[1], row, col):
                #print_error("Movimento inválido!")
                self.save_click = None # Reseta o save_click
                return
            self.move_piece(self.save_click[0], self.save_click[1], row, col, bypass=True)
            self.save_click = None # Reseta o save_click

            self.ai_move()

    def lock_ui(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.buttons[i][j].config(state="disabled")

    def unlock_ui(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.buttons[i][j].config(state="normal")

    def move_piece(self, row, col, new_row, new_col, bypass=False):

        if not bypass and not self.is_move_valid(row, col, new_row, new_col):
            print_error("Movimento inválido!")
            return

        if self.board[new_row][new_col] == (Piece.SILVER or Piece.GOLD):
            if self.board[new_row][new_col] == Piece.SILVER:
                self.silver_pieces -= 1
            elif self.board[new_row][new_col] == Piece.GOLD:
                self.gold_pieces -= 1

        # Move a peça para a nova posição
        self.board[new_row][new_col] = self.board[row][col]
        self.board[row][col] = Piece.EMPTY

        if not self.isCopy:
            # Atualiza a interface gráfica
            self.buttons[new_row][new_col] = self.generate_botton(new_row, new_col, self.board[new_row][new_col], self.buttons[new_row][new_col])
            self.buttons[row][col] = self.generate_botton(row, col, self.board[row][col], self.buttons[row][col])

        # Atualiza o jogador atual
        self.current_player = "G" if self.current_player == "S" else "S"

        if not self.isCopy:
            self.window.title(f"{self.__class__.__name__} - {self.current_player} turn")


        # Verifica se o jogo acabou
        if self.is_game_over():
            print("O jogo acabou!")
            self.window.destroy()
            print("Obrigado por jogar!")


    def is_move_valid(self, start_row, start_col, end_row, end_col):
        piece_to_player = {
            Piece.SILVER: "S",
            Piece.GOLD: "G",
            Piece.FLAGSHIP: "G",
            Piece.EMPTY: "E"
        }

        # Verifica se as coordenadas de início e fim estão dentro do tabuleiro
        if not (0 <= start_row < self.rows and 0 <= start_col < self.cols and
                0 <= end_row < self.rows and 0 <= end_col < self.cols):
            return False  # Fora do tabuleiro

        # Verifica se a peça inicial não é vazia
        if self.board[start_row][start_col] == Piece.EMPTY:
            print_error("Célula inicial vazia")
            return False  # Nenhuma peça na célula inicial

        # Verifica se a célula final é vazia ou contém uma peça do mesmo time
        if self.board[end_row][end_col] != Piece.EMPTY and piece_to_player[self.board[start_row][start_col]] == piece_to_player[self.board[end_row][end_col]]:
            print_error("Célula final ocupada por peça da mesma cor")
            return False  # Célula final ocupada por peça da mesma cor

        # Verifica se a peça não está se movendo para a mesma célula
        if start_row == end_row and start_col == end_col:
            print_error("Célula inicial e final são as mesmas")
            return False  # Sem movimento

        #Movimento na horaizontal e vertical
        if (start_row == end_row or start_col == end_col) and abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1 and self.board[end_row][end_col] == Piece.EMPTY:
            print("Movimento válido 1")
            return True

        #Ataque na diagonal
        if abs(start_row - end_row) == abs(start_col - end_col) and piece_to_player[self.board[start_row][start_col]] != piece_to_player[self.board[end_row][end_col]] and self.board[end_row][end_col] != Piece.EMPTY:
            print("Movimento válido 2")
            return True

        print("Movimento inválido 3")
        return False  # Se nenhuma condição de movimento válido for atendida

    def is_game_over(self):
        # Encontra a posição do FLAGSHIP primeiro
        flagship_position = None
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == Piece.FLAGSHIP:
                    flagship_position = (i, j)
                    break  # Só há uma peça FLAGSHIP, então podemos parar quando encontrá-la
            if flagship_position is not None:
                break

        # Se não encontramos a FLAGSHIP, ela foi capturada
        if flagship_position is None:
            print("O jogador SILVER venceu!")
            self.winner = "S"
            return True

        # Verifica se o FLAGSHIP chegou à borda oposta
        i, j = flagship_position
        if i == 0 or i == self.rows - 1 or j == 0 or j == self.cols - 1:
            print("O jogador GOLD venceu!")
            self.winner = "G"
            return True

        #TODO: Não ta funcionando
        # Verifica se o FLAGSHIP está cercado por peças SILVER nas diagonais
        for di, dj in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            ni, nj = i + di, j + dj
            # Verifica se o índice está dentro dos limites do tabuleiro
            if 0 <= ni < self.rows and 0 <= nj < self.cols:
                if self.board[ni][nj] != Piece.SILVER:
                    # Se alguma diagonal não é SILVER, então o FLAGSHIP não está totalmente capturado
                    return False

        # Se todas as diagonais são SILVER, então o FLAGSHIP está capturado
        print("O jogador SILVER venceu!")
        return True

    def get_valid_moves(self, i, j):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        valid_moves = []

        # Para simplificar, consideramos que todas as peças podem se mover em todas as direções.
        # Você deve ajustar esta lógica com base nas regras de movimento das suas peças.
        for di, dj in directions:
            ni, nj = i + di, j + dj

            # Verifica se o movimento está dentro dos limites do tabuleiro.
            if 0 <= ni < self.rows and 0 <= nj < self.cols:
                # Verifica se o movimento é válido de acordo com as regras do seu jogo.
                # Por exemplo, a célula de destino está vazia ou contém uma peça adversária que pode ser capturada.
                # Isso deve ser adaptado para as regras específicas do seu jogo.
                if self.is_move_valid(i, j, ni, nj):
                    valid_moves.append((ni, nj))

        return valid_moves

    def evaluate(self, player):
        gold_witout_flagship = self.gold_pieces - 1
        if player == "G":
            return gold_witout_flagship - self.silver_pieces
        else:
            return self.silver_pieces - gold_witout_flagship

    def generate_all_possible_moves(self, player):
        piece_to_player = {
            Piece.SILVER: "S",
            Piece.GOLD: "G",
            Piece.FLAGSHIP: "G",
            Piece.EMPTY: "E"
        }

        moves = []
        for i in range(self.rows):
            for j in range(self.cols):
                if piece_to_player[self.board[i][j]] == player:
                    piece_moves = self.get_valid_moves(i, j)
                    for (k, l) in piece_moves:
                        moves.append((i, j, k, l))
        return moves

    def minimax(self, game, depth, alpha, beta, maximizingPlayer):
        game.states_explored += 1

        if depth == 0 or game.is_game_over():
            return game.evaluate(game.current_player), None

        if maximizingPlayer:
            maxEval = float('-inf')
            posible_moves = game.generate_all_possible_moves(game.aiPlayer)
            best_move = next(iter(posible_moves), None) # Pega o primeiro elemento da lista, se não houver, retorna None

            for move in posible_moves:
                board_copy = game.copy_game_state()
                evaluation, moveDepth = game.minimax(board_copy, depth - 1, alpha, beta, False)

                if evaluation >= maxEval:
                    maxEval = evaluation
                    best_move = move

                alpha = max(alpha, evaluation)

                if beta <= alpha:
                    break

            return maxEval, best_move
        else:
            minEval = float('inf')
            posible_moves = game.generate_all_possible_moves(game.current_player)
            best_move = next(iter(posible_moves), None) # Pega o primeiro elemento da lista, se não houver, retorna None

            for move in posible_moves:
                board_copy = game.copy_game_state()
                evaluation, moveDepth = game.minimax(board_copy, depth - 1, alpha, beta, True)

                if evaluation < minEval:
                    minEval = evaluation
                    best_move = move

                beta = min(beta, evaluation)

                if beta <= alpha:
                    break

            return minEval, best_move

    def minimax_with_alpha_beta(self, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.is_game_over():
            return self.evaluate(self.current_player), None

        if maximizing_player == self.current_player:
            max_eval = float('-inf')
            best_move = None
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.board[i][j] == self.current_player:
                        piece_moves = self.get_valid_moves(i, j)
                        for (k, l) in piece_moves:
                            new_board = copy.deepcopy(self.board)
                            self.simulate_move(new_board, i, j, k, l)
                            eval, _ = self.minimax_with_alpha_beta(depth - 1, alpha, beta,
                                                                   "S" if self.current_player == "G" else "G")

                            if eval > max_eval:
                                max_eval = eval
                                best_move = (i, j, k, l)
                            alpha = max(alpha, eval)
                            if beta <= alpha:
                                break
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.board[i][j] == ("S" if self.current_player == "G" else "G"):
                        piece_moves = self.get_valid_moves(i, j)
                        for (k, l) in piece_moves:
                            new_board = copy.deepcopy(self.board)
                            self.simulate_move(new_board, i, j, k, l)
                            eval, _ = self.minimax_with_alpha_beta(depth - 1, alpha, beta, self.current_player)

                            if eval < min_eval:
                                min_eval = eval
                                best_move = (i, j, k, l)
                            beta = min(beta, eval)
                            if beta <= alpha:
                                break
                if beta <= alpha:
                    break
            return min_eval, best_move

    def ai_move(self):
        self.lock_ui()
        board_copy = self.copy_game_state()
        _, move = self.minimax(board_copy, 5, float('-inf'), float('inf'), True)
        if move:
            self.move_piece(*move)
        self.unlock_ui()

class bcolors:
    ERROR = '\033[91m'
    NORMAL = '\033[0m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
def print_error(message):
    print(f"{bcolors.ERROR}Erro: {message} {bcolors.ENDC}")


if __name__ == "__main__":

    print("Bem-vindo ao Breakthru!")
    print("O jogo começa com as peças GOLD no centro e as peças SILVER nas extremidades.")
    print("O objetivo do jogo é mover o FLAGSHIP para a borda oposta do tabuleiro.")
    print("As peças SILVER devem capturar o FLAGSHIP antes que ele alcance a borda oposta.")
    print("O jogador Inicial é escolhido aleatoriamente.")
    print("Boa sorte!")
    print("*******************************************************************************")
    print("Escolha com qual time tu vais jogar: [S]ILVER ou [G]OLD?")

    player = "S"
    while player not in ["S", "G"]:
        player = input().upper()

    game = Breakthru(player)
    #ame.print_board()
