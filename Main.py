import tkinter as tk
from tkinter import PhotoImage
import os
import subprocess


def open_script(folder, script):
    # Save the current working directory
    original_dir = os.getcwd()
    try:
        # Change to the target directory
        os.chdir(folder)
        # Run the script
        subprocess.run(["pythonw", script])
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Always return to the original directory
        os.chdir(original_dir)


def open_mscit():
    open_script("MSCIT", "MSCIT_Dash.py")


def open_tally():
    open_script("Tally", "Tally_Dash.py")


def open_autocad():
    open_script("CAD", "CAD_Dash.py")


def open_dtp():
    open_script("DTP", "DTP_Dash.py")


def open_c():
    open_script("C", "C_Dash.py")


def open_cpp():
    open_script("CPP", "CPP_Dash.py")

def open_emp():
    open_script("Employee", "EMP_Dash.py")

def open_enq():
    open_script("ENQ", "ENQ_Dash.py")
    
# Create the main window (root)
root = tk.Tk()
root.geometry("1200x600+75+35")
root.title("Main Window")

# Set background image
bg_image = PhotoImage(file="MainIMG/BGG.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Buttons for different scripts
msc_image = PhotoImage(file="MainIMG/MSCIT.png")
msc_button = tk.Button(root, image=msc_image, command=open_mscit)
msc_button.place(x=160, y=130)

tally_image = PhotoImage(file="MainIMG/Tally.png")
tally_button = tk.Button(root, image=tally_image, command=open_tally)
tally_button.place(x=500, y=130)

autocad_image = PhotoImage(file="MainIMG/Auto.png")
autocad_button = tk.Button(root, image=autocad_image, command=open_autocad)
autocad_button.place(x=845, y=130)

dtp_image = PhotoImage(file="MainIMG/DTP.png")
dtp_button = tk.Button(root, image=dtp_image, command=open_dtp)
dtp_button.place(x=162, y=290)

c_image = PhotoImage(file="MainIMG/C.png")
c_button = tk.Button(root, image=c_image, command=open_c)
c_button.place(x=500, y=290)

cpp_image = PhotoImage(file="MainIMG/CPP.png")
cpp_button = tk.Button(root, image=cpp_image, command=open_cpp)
cpp_button.place(x=844, y=290)

emp_image = PhotoImage(file="MainIMG/Employee.png")
emp_button = tk.Button(root, image=emp_image, command=open_emp) 
emp_button.place(x=300, y=460)

enq_image = PhotoImage(file="MainIMG/ENQ.png")
enq_button = tk.Button(root, image=enq_image, command=open_enq)  
enq_button.place(x=680, y=460)

root.mainloop()
