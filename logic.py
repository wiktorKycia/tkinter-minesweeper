from __future__ import annotations
import numpy as np

class Board:
    def __init__(self, width:int, height:int, num_mines:int):
        """Initialize the game board."""
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = np.zeros((self.height, self.width), dtype=int)
        self.reset_mines()
    
    def reset_mines(self) -> None:
        """Places mines on the board."""
        self.board = np.zeros((self.height, self.width), dtype=int)
        mine_positions = np.random.choice(self.width * self.height, self.num_mines, replace=False)
        print(mine_positions)
        for mine in mine_positions:
            x = mine % self.width
            y = mine // self.width
            self.board[y][x] = 1
        print(self.board)
    
    def count_mines_around(self, x:int, y:int) -> int:
        """Counts the number of mines around a point of given coordinates"""
        result = 0
        for i in range(max(y-1, 0), min(y+2, self.height)):
            for j in range(max(x-1, 0), min(x+2, self.width)):
                try:
                    if self.board[i][j] == 1:
                        result += 1
                except IndexError:
                    pass
        return result



from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import Displayer
import tkinter as tk

class Tile:
    def __init__(self, displayer: Displayer, coords:tuple[int,int], bomb: bool, is_discovered: bool = False, content: str|None = None) -> None:
        self.widget: tk.Widget
        
        self.displayer: Displayer = displayer
        
        self.x: int
        self.y: int
        self.x, self.y = coords
        
        self.bomb: bool = bomb
        self.discovered: bool = is_discovered
        
        self.content: str
        
        if is_discovered:
            self.widget = tk.Label(self.displayer.frame, width=1, height=1)
            self.content = content if content else ""
            self.widget.config(text=self.content)
        else:
            self.widget = tk.Button(self.displayer.frame, width=1, height=1)
            self.widget.config(command=lambda: self.discover(self.displayer.board))
    
    def discover(self, board:Board) -> None:
        self.discovered = True
        self.widget = tk.Label(self.displayer.frame, width=1, height=1)
        if self.bomb:
            self.widget.config(text="x")
        else:
            self.widget.config(text=board.count_mines_around(self.x, self.y))
        self.display()

    def display(self) -> None:
        self.widget.grid(row=self.y, column=self.x)
