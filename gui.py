import os
import tkinter as tk

from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('300x150')


def select_file():
    filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=os.getcwd(),
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename,
    )

    index = filename.rfind('/')
    file = filename[index+1]

    root.destroy()

    return file


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)


# run the application
root.mainloop()

if __name__ == "__main__":
    root.mainloop()
