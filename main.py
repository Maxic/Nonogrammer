import tkinter as tk
from tkinter import messagebox, Button
from nonogram import Nonogram
from image import Img
import numpy as np

# #####  DEFINE GRID HERE  ###### #
ROWS = 10
COLS = 10
# Visual size of grid box
GRID_SIZE = 40

# Initialize
nonogram = Nonogram()
img = Img()
tiles = [[0 for _ in range(COLS)] for _ in range(ROWS)]


def create_grid(event=None):
    w = grid.winfo_width()  # Get current width of canvas
    h = grid.winfo_height()  # Get current height of canvas
    grid.delete('grid_line')  # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, GRID_SIZE):
        grid.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, GRID_SIZE):
        grid.create_line([(0, i), (w, i)], tag='grid_line')


def callback_grid(event):
    # Get rectangle diameters
    col_width = int(grid.winfo_width()/COLS)
    row_height = int(grid.winfo_height()/ROWS)

    # Calculate column and row number
    col = event.x//col_width
    row = event.y//row_height

    # If the tile is not filled, create a rectangle
    if not tiles[row][col]:
        tiles[row][col] = grid.create_rectangle(col*col_width, row*row_height, (col+1)*col_width, (row+1)*row_height, fill="black")
    else:
        grid.delete(tiles[row][col])
        tiles[row][col] = None


def callback_generate():
    # Generate nonogram and destroy window.
    nonogram_definition = nonogram.generate_nonogram_from_matrix(np.array(tiles))
    # if nonogram.solve(nonogram_definition): TODO: Implement solver
    img.draw_nonogram(nonogram_definition)
    messagebox.showinfo("Completed", "Succes! \nYour Nonogram puzzle is saved as Nonogram.bpm in this directory.")
    root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    grid = tk.Canvas(root, width=COLS * GRID_SIZE, height=ROWS * GRID_SIZE, background='white')
    button = Button(root, text="Generate", command=callback_generate)

    grid.pack()
    button.pack()
    grid.bind('<Configure>', create_grid)
    grid.bind("<Button-1>", callback_grid)

    root.mainloop()
