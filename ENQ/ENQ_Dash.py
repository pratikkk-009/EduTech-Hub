import tkinter as tk
from tkinter import *
import subprocess
import os

def New_ENQ():
    subprocess.run(["python", "ENQ.py"])  

def ENQDB():
    subprocess.run(["python", "ENQ_DB.py"])

def open_main():
    root.destroy()  
    subprocess.run(["python", "../Main.py"])

         
# Create the main window
root = tk.Tk()
root.title("Enquiry")
root.geometry("1200x600")
# Set window size (resolution: 1200x600)
window_width = 1200
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate center position
position_top = int(screen_height / 2 - window_height / 2)
position_left = int(screen_width / 2 - window_width / 2)

# Set the window geometry with center position
root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

# Set background image
bg_image = tk.PhotoImage(file="Images/Enq.png") 
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Load button images
button1_image = tk.PhotoImage(file="Images/Reg_Button.png")
button3_image = tk.PhotoImage(file="Images/View.png") 

# Create buttons
button1 = tk.Button(root,image=button1_image,width=224,height=225,bd=3, command= New_ENQ)
button1.place(x=260, y=200)

button3 = tk.Button(root,image=button3_image,width=224,height=225,bd=3,command= ENQDB)
button3.place(x=740, y=200)


back_button_img=PhotoImage(file="Images/Back.png")
BackButon=Button(root,image=back_button_img,bd=0,width=40,height=40,fg="#deeefb",command=open_main)
BackButon.place(x=26,y=23)

# Run the GUI event loop
root.mainloop()
