#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
import random

def show_random_compliment():
    compliments = [
        "You're beautiful inside and out.",
        "You light up my life.",
        "You make my heart skip a beat.",
        "You're my soulmate.",
        "I'm so lucky to have you in my life.",
        "You're my best friend and my love.",
        "You make every day better just by being you."
    ]
    messagebox.showinfo("Compliment of the Day", random.choice(compliments))

root = tk.Tk()
root.title("Valentine's Day Gift")
root.geometry("400x200")
root.configure(background="pink")

header = tk.Label(root, text="To my beloved Tanvi,", font=("Helvetica", 20), bg="pink")
header.pack()

valentine_gift = tk.Button(root, text="Show your gift!", command=show_random_compliment, font=("Helvetica", 16), bg="white", bd=0)
valentine_gift.pack()

root.mainloop()
