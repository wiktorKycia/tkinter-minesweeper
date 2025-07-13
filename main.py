import tkinter as tk

from logic import Board, Tile

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

class Displayer:
    def __init__(self, board: Board) -> None:
        self.board: Board = board
        self.tiles: list[list] = []
        self.frame = tk.Frame(root)

    def clear_frame(self) -> None:
        for widget in self.frame.winfo_children():
            widget.destroy()

    def setup_frame(self) -> None:
        for y in range(self.board.height):
            row_of_tiles = []
            for x in range(self.board.width):
                bomb = self.board.board[y][x] == 1
                tile = Tile(self, coords=(x, y), bomb=bomb)
                tile.display()
                row_of_tiles.append(tile)
            self.tiles.append(row_of_tiles)
        self.frame.pack(fill="both")

def start_game() -> None:
    for widget in root.winfo_children():
        widget.destroy()
    board = Board(width=columns.get(), height=rows.get(), num_mines=mines.get())
    displayer = Displayer(board)

    displayer.clear_frame()
    displayer.setup_frame()


start_button = tk.Button(root, text="Start Game", command=start_game, padx=10, pady=5)
start_button.pack()

root.mainloop()