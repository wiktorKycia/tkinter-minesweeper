import numpy as np

class Board:
    def __init__(self, width, height, num_mines):
        """Initialize the game board."""
        self.width = width
        self.height = height
        self.num_mines = num_mines
    
    def create_board(self):
        """Create a board with mines and numbers."""
        # Initialize the board with zeros
        board = np.zeros((self.height, self.width), dtype=int)
        # Place mines randomly
        mine_positions = np.random.choice(self.width * self.height, self.num_mines, replace=False)
        print(mine_positions)
        for mine in mine_positions:
            x = mine % self.width
            y = mine // self.height
            board[y][x] = 1
        print(board)
                

b = Board(10, 10, 20)
b.create_board()