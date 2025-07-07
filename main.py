import tkinter as tk

from logic import Board

root = tk.Tk()
root.geometry("450x400")
root.title("minesweeper")

label = tk.Label(root, text="Welcome to Minesweeper!")
label.pack(pady=20)


frame = tk.Frame(root)
frame.pack()


label_rows = tk.Label(frame, text="rows")
label_rows.grid(row=0, column=0)

label_columns = tk.Label(frame, text="columns")
label_columns.grid(row=1, column=0)

label_mines = tk.Label(frame, text="mines")
label_mines.grid(row=2, column=0)

rows = tk.IntVar()
rows.set(10)

columns = tk.IntVar()
columns.set(10)

mines = tk.IntVar()
mines.set(20)

entry_rows = tk.Spinbox(frame, from_=1, to=100, width=5, textvariable=rows)
entry_rows.grid(row=0, column=1)

entry_columns = tk.Spinbox(frame, from_=1, to=100, width=5, textvariable=columns)
entry_columns.grid(row=1, column=1)

max_mines = int(rows.get() * columns.get() * 0.35)

entry_mines = tk.Spinbox(frame, from_=1, to=max_mines, width=5, textvariable=mines)
entry_mines.grid(row=2, column=1)

class Tile:
    def __init__(self, board:Board, frame:tk.Frame, coords:tuple[int,int], bomb: bool, is_discovered: bool = False, content: str|None = None) -> None:
        self.widget: tk.Widget
        
        self.x: int
        self.y: int
        self.x, self.y = coords
        
        self.bomb: bool = bomb
        self.discovered: bool = is_discovered
        
        self.content: str
        
        if is_discovered:
            self.widget = tk.Label(frame, width=1, height=1)
            self.content = content if content else ""
            self.widget.config(text=self.content)
        else:
            self.widget = tk.Button(frame, width=1, height=1)
            self.widget.config(command=lambda: self.discover(board))
    
    def discover(self, board:Board) -> None:
        self.widget = tk.Label(frame, width=1, height=1)
        if self.bomb:
            self.widget.config(text="x")
        else:
            self.widget.config(text=board.count_mines_around(self.x, self.y))
    
    
    
        

class Displayer:
    def __init__(self, board: Board) -> None:
        self.board: Board = board
        self.buttons:list[list] = []
        self.frame = tk.Frame(root)
    
    def clear_frame(self) -> None:
        for widget in self.frame.winfo_children():
            widget.destroy()
    
    def setup_frame(self) -> None:
        for row in range(self.board.height):
            row_of_buttons = []
            for col in range(self.board.width):
                button = tk.Button(self.frame, width=1, height=1)
                button.config(command=lambda: self.discover_tile(x=col, y=row))
                button.grid(row=row, column=col)
                row_of_buttons.append(button)
            self.buttons.append(row_of_buttons)
        self.frame.pack(fill=tk.BOTH)
    
    def discover_tile(self, x:int, y:int) -> None:
        label = tk.Label(frame)
        if self.board.board[y][x] == 1:
            label.config(text="x")
        else:
            label.config(text=self.board.count_mines_around(x, y))
        self.buttons[y][x] = label
        
        self.clear_frame()
        self.setup_frame()

start_button = tk.Button(root, text="Start Game", command=start_game, padx=10, pady=5)
start_button.pack()

root.mainloop()