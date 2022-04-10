from tkinter import *
from random import shuffle
import copy
from tkinter import messagebox
from SudokuGenerator import *

root = Tk()
root.title('Sudoku')


#define a function that checks filled out cells against the solution
def check_solution():
    global new_puzzle

    result = any(e[0].get() == '' for e in entries)

    if result == False:    
        for e in entries:
            if str(e[0].get()) == str(new_puzzle.fullgrid[e[1]][e[2]]):
                e[0].config(font=("Courier", 20), bg="white")
            else:
                e[0].config(font=("Courier", 20), bg="red")
    else:
        messagebox.showwarning(title=None, message="First, fill all the empty boxes")

def handle_click(event):
    for e in entries:
        e[0].config(bg="white")

#create grid and buttons
button_1 = Button(root, text = 'Check Solution', padx = 40, pady = 20, relief="raised", command = check_solution)
button_1.grid(row=10, column=7, columnspan=2)

grid = [[0 for i in range(9)] for j in range(9)]

new_puzzle = SudokuGenerator()

entries=[]

#Define interface for the puzzle
for t in range(9):
    for i in range(9):
        if int(new_puzzle.grid[t][i]) <1:
            e = Entry(root, width=5, bg = 'white', bd=1, fg="gray", justify = CENTER)
            e.config(font=("Courier", 20))
            e.grid(row = t, column = i, ipady=14)
            e.bind("<1>", handle_click)
            entries.append((e,t,i))
        else:
            l = Label(root,
              width=5, height=2,
              bd = 1,
              relief="sunken",
              bg = 'white',
              text = str(new_puzzle.grid[t][i]).replace('0',' '))

            l.config(font=("Courier", 20))
            l.grid(row = t, column = i)

root.mainloop()
