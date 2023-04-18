import random
import tkinter as tk
from tkinter import ttk

sweet_messages = [
    "You are the sunshine in my life.",
    "I love you more than words can express.",
    "You make me a better person just by being in my life.",
    "You drive me insane but you're the only person i'd say hi to my lil demons for?  (prolly not the correct grammer but it sounded better this way).",
    "I miss youu so much :(.",
    "I can't imagine my life without you .",
    "You're all mine",
    "Being with you feels like coming home.",
]

def generate_message():
    
    message = random.choice(sweet_messages)

  
    popup = tk.Toplevel()
    popup.title("textt")
    popup.geometry("300x100")
    popup.resizable(False, False)
    label = tk.Label(popup, text=message, padx=10, pady=10)
    label.pack()

def send_message():

    selected_value = dropdown.get()
    checked_items = [var1.get(), var2.get(), var3.get()]

    
    message = f"Happy Anniversary, {selected_value}!\n\n"
    message += "Here are some things I love about you:\n"
    if checked_items[0]:
        message += "- Your smile\n"
    if checked_items[1]:
        message += "- Your armss\n"
    if checked_items[2]:
        message += "- tuffyy\n"

    popup = tk.Toplevel()
    popup.title("Heyy!")
    popup.geometry("400x300")
    popup.resizable(False, False)
    label = tk.Label(popup, text=message, padx=10, pady=10)
    label.pack()

# Create the main window
root = tk.Tk()
root.title("threeee")
root.geometry("300x250")
root.resizable(False, False)


dropdown_label = tk.Label(root, text="To: ")
dropdown_label.pack(side=tk.LEFT, padx=10, pady=10)
dropdown = ttk.Combobox(root, values=["my love", "my sweetheart", "my speedo","baby","jaaneman","rOckstar heh"], width=10)
dropdown.current(0)
dropdown.pack(side=tk.LEFT, padx=10, pady=10)


checklist_frame = tk.Frame(root)
checklist_frame.pack(side=tk.TOP, padx=10, pady=10)
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
check1 = tk.Checkbutton(checklist_frame, text="Your smile", variable=var1)
check1.pack(anchor=tk.W)
check2 = tk.Checkbutton(checklist_frame, text="Your sense of humor", variable=var2)
check2.pack(anchor=tk.W)
check3 = tk.Checkbutton(checklist_frame, text="Your kind heart", variable=var3)
check3.pack(anchor=tk.W)


send_button = tk.Button(root, text="Send Message", command=send_message)
send_button.pack(side=tk.TOP, padx=10, pady=10)


generate_button = tk.Button(root, text="Generate Message", command=generate_message)
generate_button.pack(side=tk.BOTTOM, padx=10, pady=10)

root.mainloop()


