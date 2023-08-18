class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.player_scores = {"X": 0, "O": 0}

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i], "|", self.board[i + 1], "|", self.board[i + 2])
            if i < 6:
                print("---------")

    def check_winner(self):
        win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

        for pattern in win_patterns:
            if self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]] != " ":
                return self.board[pattern[0]]

        if " " not in self.board:
            return "tie"

        return None

    def play(self):
        while True:
            self.print_board()
            position = int(input(f"Player {self.current_player}, choose a position (1-9): ")) - 1

            if self.board[position] == " ":
                self.board[position] = self.current_player
                winner = self.check_winner()

                if winner:
                    if winner == "tie":
                        print("Tie!")
                    else:
                        print(f"Player {winner} wins!")
                        self.player_scores[winner] += 1

                    self.print_board()
                    play_again = input("Want to play again? (yes/no): ")
                    if play_again.lower() == "no":
                        print("Scores:")
                        print(f"Player X: {self.player_scores['X']} wins")
                        print(f"Player O: {self.player_scores['O']} wins")
                        break

                    self.board = [" " for _ in range(9)]
                    self.current_player = "X" if self.current_player == "O" else "O"
                else:
                    self.current_player = "X" if self.current_player == "O" else "O"
            else:
                print("Position is taken. Choose a different position.")


if __name__ == "__main__":
    game = TicTacToe()
    game.play()