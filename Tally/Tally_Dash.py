import tkinter as tk
from tkinter import *
import subprocess
import os

def New_REG():
    subprocess.run(["python", "Tally.py"])  # Run the Tally.py script in a new process

def Attend():
    subprocess.run(["python", "Tally_Attend.py"])  # Run the Tally_Attend.py script

def TallyDB():
    subprocess.run(["python", "TallyDB.py"])



def open_main():
    root.destroy()  # Close the Tally_Dash window
    subprocess.run(["python", "../Main.py"])

         
# Create the main window
root = tk.Tk()
root.title("Tally Dashboard")
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
bg_image = tk.PhotoImage(file="Images/Tally.png") 
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Load button images
button1_image = tk.PhotoImage(file="Images/Reg_Button.png")
button2_image = tk.PhotoImage(file="Images/Attend_Button.png")  
button3_image = tk.PhotoImage(file="Images/Progress_Button.png") 

# Create buttons
button1 = tk.Button(root,image=button1_image,width=178,height=178,bd=3, command= New_REG)
button1.place(x=155, y=240)

button2 = tk.Button(root,image=button2_image,width=178,height=178,bd=3,command= Attend)
button2.place(x=505, y=240)

button3 = tk.Button(root,image=button3_image,width=178,height=178,bd=3,command= TallyDB)
button3.place(x=855, y=238)


back_button_img=PhotoImage(file="Images/Back.png")
BackButon=Button(root,image=back_button_img,bd=0,width=40,height=40,fg="#deeefb",command=open_main)
BackButon.place(x=26,y=23)

# Run the GUI event loop
root.mainloop()
