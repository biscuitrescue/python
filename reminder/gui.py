#!/usr/bin/env python
# -*- coding: utf-8 -*-

from customtkinter import *
from PIL import Image

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


### Root window ###

root = CTk()

exes = 1000
whys = 600
root.configure(fg_color=colours['mantle'])
root.geometry(f"{exes}x{whys}")


### Button frame ###

button_fr = CTkFrame(
    root,
    fg_color=colours['mantle']
)

button_fr.place(
    relx=0,rely=0,
    relheight=1,relwidth=0.08
)

### Button definitions ###

## Home button 
icon_home = CTkImage(dark_image=Image.open('akonadi-phone-home.png'),size=(30,30))

home_bu = CTkButton(
    button_fr,
    corner_radius=10,
    fg_color='transparent',
    text_color=colours['fg'],
    hover_color=colours["base1"],
    text="H",
    image=icon_home
)

home_bu.place(
    rely=0.041,relx=0.1875,
    relheight=0.083,relwidth=0.625
)

## Add Button
icon_add = CTkImage(dark_image=Image.open('list-add.png'),size=(30,30))
add_bu = CTkButton(
    button_fr,
    corner_radius=10,
    fg_color='transparent',
    text_color=colours['fg'],
    hover_color=colours['base1'],
    text='+',
    image=icon_add
)

# Distance from home button = 25+50+80 

add_bu.place(
    rely=0.258,relx=0.1875,
    relheight=0.083,relwidth=0.625
)

## Checkbox Button

checkbox_bu = CTkButton(
    button_fr,
    corner_radius=10,
    fg_color='transparent',
    text_color=colours['fg'],
    hover_color=colours['base1'],
    text='C'
)

# Spacing from Add button = 20 (155+50+20)
checkbox_bu.place(
    rely=0.375,relx=0.1875,
    relheight=0.083,relwidth=0.625
)

## Status Button

status_bu = CTkButton(
    button_fr,
    corner_radius=10,
    fg_color='transparent',
    text_color=colours['fg'],
    hover_color=colours['base1'],
    text='S'
)

# Spacing from checkbox button = 20 (225+50+20)
status_bu.place(
    rely=0.491,relx=0.1875,
    relheight=0.083,relwidth=0.625
)

## Log Button

log_bu = CTkButton(
    button_fr,
    corner_radius=10,
    fg_color='transparent',
    text_color=colours['fg'],
    hover_color=colours['base1'],
    text='L'
)

# Spacing from Status button = 20 (295+50+20)
log_bu.place(
    rely=0.608,relx=0.1875,
    relheight=0.083,relwidth=0.625
)

welcome_fr = CTkFrame(
    root,
    fg_color=colours['bg'],
)

welcome_fr.place(
    relx=0.08, rely=0,
    relheight=1,relwidth=0.92
)

root.mainloop()
