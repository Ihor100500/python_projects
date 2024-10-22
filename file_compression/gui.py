from calendar import c
import tkinter as tk
from compressmodule import compress,decompress
from tkinter import filedialog

def open_file():
    filename = filedialog.askopenfilename(initialdir='/', title = 'Select a file')
    return filename

window = tk.Tk()

window.title('Compression engine')
window.geometry('600x400')

compress_button = tk.Button(window, text = 'Compress',command = lambda:compress(open_file(), "compressed_output.txt"))
compress_button.grid(row=2, column=2)

decompress_button = tk.Button(window, text = 'Decompress',command = lambda:decompress(open_file(), "decompressed_output.txt"))
decompress_button.grid(row=3, column=2)

window.mainloop()