import tkinter as tk
root = tk.Tk()
root.geometry("450x400")
root.title("minesweeper")

label = tk.Label(root, text="Welcome to Minesweeper!")
label.pack(pady=20)

def start_game():
    for widget in root.winfo_children():
        widget.destroy()

start_button = tk.Button(root, text="Start Game", command=start_game, padx=10, pady=5)
start_button.pack()

root.mainloop()