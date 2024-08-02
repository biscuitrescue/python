#!/usr/bin/env python3

import tkinter as tk
from catppuccin import Flavour


class Window(tk.TK):
    def __init__(self):
        pass


root = tk.Tk()
root.configure(background=f'#{Flavour.mocha().base.hex}')
root.geometry('1400x800')

root.mainloop()
