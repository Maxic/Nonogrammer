import tkinter as tk
from tkinter import *
from nonogram import Nonogram
from image import img
import numpy as np


# Set number of rows and columns
ROWS = 15
COLS = 15
GRIDSIZE =14

# Create a grid of None to store the references to the tiles
tiles = [[0 for _ in range(COLS)] for _ in range(ROWS)]
nonogram = Nonogram()
img = img()

def create_grid(event=None):
    w = grid.winfo_width() # Get current width of canvas
    h = grid.winfo_height() # Get current height of canvas
    grid.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, GRIDSIZE):
        grid.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, GRIDSIZE):
        grid.create_line([(0, i), (w, i)], tag='grid_line')

def callbackGrid(event):
    # Get rectangle diameters
    col_width = int(grid.winfo_width()/COLS)
    row_height = int(grid.winfo_height()/ROWS)

    # Calculate column and row number
    col = event.x//col_width
    row = event.y//row_height
    # If the tile is not filled, create a rectangle
    if not tiles[row][col]:
        # FUCKING MAGIC WHATEVER
        #tiles[row][col] = grid.create_rectangle(event.x,event.y,event.x+10,event.y+10,fill="black")

        tiles[row][col] = grid.create_rectangle(col*col_width, row*row_height, (col+1)*col_width, (row+1)*row_height, fill="black")
    else:
        grid.delete(tiles[row][col])
        tiles[row][col] = None

def callbackGenerate():
    nonogramDefinition = nonogram.generateNonogramFromMatrix(np.array(tiles))
    img.drawNonogram(nonogramDefinition)
    root.destroy()


# Create the window, a canvas and the mouse click event binding
root = tk.Tk()
grid = tk.Canvas(root, width=COLS*GRIDSIZE, height=ROWS*GRIDSIZE, background='white')
button = Button(root, text="Generate", command=callbackGenerate)

grid.pack()
button.pack()
grid.bind('<Configure>', create_grid)
grid.bind("<Button-1>", callbackGrid)

root.mainloop()