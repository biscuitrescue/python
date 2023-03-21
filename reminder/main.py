#!/usr/bin/env python3

from customtkinter import *
from module import *

# set_appearance_mode("System")  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

colours = {
    "pink":"#f5c2e7",
    "rosewater":"#f5e0dc",
    "flamingo":"#f2cdcd",
    "mauve":"#cba6f7",
    "red":"#f38ba8",
    "orange":"#fab387",
    "yellow":"#f9e2af",
    "green":"#a6e3a1",
    "teal":"#94e2d5",
    "blue":"#89b4fa",
    "lavender":"#b4befe",
    "fg":"#cdd6f4",
    "bg":"#1e1e2e",
    "base1":"#313244",
    "mantle":"#181825"
}


root = CTk()

exes = 1400
whys = 800
root.configure(fg_color=colours['mantle'])
root.geometry(f"{exes}x{whys}")


home_bu = CTkButton(
    root,
    corner_radius=10,
    fg_color='transparent',
    text_color=colours['fg'],
    border_width=1,
    border_color=colours["mantle"],
    hover_color=colours["base1"],
    text="H",
    height=50,
    width=50,
    anchor="center",
    border_spacing=0,
)

home_bu.place(
    y=25,x=25
)

welcome_fr = CTkFrame(
    root,
    fg_color=colours['bg'],
    width=exes-100, height=whys
)

welcome_fr.place(
    x=100, y=0,
)

root.mainloop()
