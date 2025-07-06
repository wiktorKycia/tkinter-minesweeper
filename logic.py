import numpy as np

class Board:
    def __init__(self, width:int, height:int, num_mines:int):
        """Initialize the game board."""
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = np.zeros((self.height, self.width), dtype=int)
    
    def create_mines(self) -> None:
        """Places mines on the board."""
        mine_positions = np.random.choice(self.width * self.height, self.num_mines, replace=False)
        print(mine_positions)
        for mine in mine_positions:
            x = mine % self.width
            y = mine // self.width
            self.board[y][x] = 1
        print(self.board)
    
    def count_mines_around(self, x:int, y:int) -> int:
        result = 0
        for i in range(max(y-1, 0), min(y+2, self.height)):
            for j in range(max(x-1, 0), min(x+2, self.width)):
                try:
                    if self.board[i][j] == 1:
                        result += 1
                except IndexError:
                    pass
        return result                

# b = Board(6, 4, 9)
# b.create_mines()
# print([[b.count_mines_around(i,j) for i in range(b.width)] for j in range(b.height)])