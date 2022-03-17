#!/usr/bin/env python3
from tkinter import *
from PIL import ImageTk, Image
# Calling the Tk (The initial constructor of tkinter)
root = Tk()
# We will make the title of our app as Image Viewer
root.title("Image Viewer")
root.configure(background="#282a36")
# The geometry of the box which will be displayed
# on the screen
root.geometry("500x300")
# Adding the images using the pillow module which
# has a class ImageTk We can directly add the
# photos in the tkinter folder or we have to
# give a proper path for the images
image_no_1 = ImageTk.PhotoImage(Image.open("/home/karttikeya/.wall/img.png"))
label = Label(image=image_no_1, bg='#282a36')
# We have to show the the box so this below line is needed
label.place(x=0,y=0,height=300,width=500)
# We will have three button back ,forward and exit
# button_back = Button(root, text="Back", command=back, state=DISABLED)
# root.quit for closing the app
# button_exit = Button(root, text="Exit",
                     # command=root.quit)
# button_forward = Button(root, text="Forward",
                        # command=lambda: forward(1))
# grid function is for placing the buttons in the frame
# button_back.grid(row=5, column=0)
# button_exit.grid(row=5, column=1)
# button_forward.grid(row=5, column=2)
root.mainloop()
