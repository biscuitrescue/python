#!/usr/bin/env python3

import customtkinter as ctk

colours = {
        "pink": "#f5c2e7",
        "rosewater": "#f5e0dc",
        "flamingo": "#f2cdcd",
        "mauve": "#cba6f7",
        "red": "#f38ba8",
        "orange": "#fab387",
        "yellow": "#f9e2af",
        "green": "#a6e3a1",
        "teal": "#94e2d5",
        "blue": "#89b4fa",
        "lavender": "#b4befe",
        "fg": "#cdd6f4",
        "bg": "#1e1e2e",
        "base1": "#313244",
        "mantle": "#181825"
        }

root = ctk.CTk()
exes, whys = 1100, 800
root.geometry(f"{exes}x{whys}")

frame = ctk.CTkFrame(
        root,
        fg_color=colours['base1'],
        width=exes,
        height=whys
        )
frame.pack()

start_timer_button = ctk.CTkButton(
        frame,
        text="Start timer",
        width=200,
        height=100
        )
start_timer_button.pack()


root.mainloop()
