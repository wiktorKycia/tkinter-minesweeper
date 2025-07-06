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

def start_game():
    for widget in root.winfo_children():
        widget.destroy()
    label = tk.Label(root, text=f'rows={rows.get()}, columns={columns.get()}, mines={mines.get()}')
    label.pack()
    
    board = Board(rows.get(), columns.get(), mines.get())
    buttons = []
    
    frame = tk.Frame(root)
    for row in range(board.height):
        row_of_buttons = []
        for col in range(board.width):
            button = tk.Button(frame, width=1, height=1)
            button.grid(row=row, column=col)
            row_of_buttons.append(button)
        buttons.append(row_of_buttons)
    frame.pack(fill=tk.BOTH)

start_button = tk.Button(root, text="Start Game", command=start_game, padx=10, pady=5)
start_button.pack()

root.mainloop()