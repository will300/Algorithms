from random import choice, randint

class Board:

    def __init__(self):
        self.squares = [[None, None, None],
                        [None, None, None],
                        [None, None, None]]
        self.free_squares = [(0, 0), (0, 1), (0, 2),
                             (1, 0), (1, 1), (1, 2),
                             (2, 0), (2, 1), (2, 2)]

    def random_play(self):

        ctrs = choice([[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]])

        for i in range(9):
            player = ctrs.pop()
            move = self.free_squares.pop(randint(0, len(self.free_squares) - 1))
            self.squares[move[0]][move[1]] = player
            if self.has_won(player):
                print(self)
                print(f"Player {player} has won")
                return 
        print(self)
        print("Draw")

    def has_won(self, player):
        # check rows
        for row in self.squares:
            if row == [player] * 3: return True

        # check columns
        for col in range(3):
            if [self.squares[0][col], 
                self.squares[1][col], 
                self.squares[2][col]] == [player] * 3: return True

        # check diagonals
        if [self.squares[0][0], 
            self.squares[1][1], 
            self.squares[2][2]] == [player] * 3: return True

        if [self.squares[0][2], 
            self.squares[1][1], 
            self.squares[2][0]] == [player] * 3: return True

        return False

    def __repr__(self):
 
        output = ""
        for row in self.squares:
            output += str(row)
            output += "\n"
        return output


board = Board()
board.random_play()          

        
