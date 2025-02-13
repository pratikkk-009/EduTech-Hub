import pandas as pd
from datetime import date
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from PIL import Image, ImageTk
from tkinter import Button


    
# File Path
excel_file = "CPP.xlsx"

# Load Students Data
try:
    students_df = pd.read_excel(excel_file, sheet_name="Sheet")
    students_df.columns = students_df.columns.str.strip()  # Normalize column names
    if "Registration No." not in students_df.columns or "Name" not in students_df.columns:
        raise KeyError("The 'Sheet' must have columns: 'Registration No.' and 'Name'.")
    print("Students DataFrame Loaded:")
    
except Exception as e:
    messagebox.showerror("Error", f"Failed to load students data: {e}")
    students_df = pd.DataFrame(columns=["Registration No.", "Name"])

# Create or load attendance data
try:
    attendance_df = pd.read_excel(excel_file, sheet_name="Attendance")
    attendance_df.columns = attendance_df.columns.str.strip()  # Normalize column names
    attendance_df.set_index("Registration No.", inplace=True)
    print("Attendance DataFrame Loaded:")
   
except Exception as e:
    print(f"Attendance data not found or invalid: {e}")
    attendance_df = students_df.set_index("Registration No.")[["Name"]]
    print("Created Attendance DataFrame:")    

# Get today's date
today_date = date.today().isoformat()

# Ensure today's column exists
if today_date not in attendance_df.columns:
    attendance_df[today_date] = None

# Tkinter GUI for Attendance
root = tk.Tk()
root.title("C++ Attendance Tracker")
root.geometry("1200x600")  # Set window size

# Set background color for the root window to light yellow
root.configure(bg="#f9fcae")  # Light yellow background

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width, window_height = 1200, 600
x_cord = int((screen_width / 2) - (window_width / 2))
y_cord = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_cord}+{y_cord}")

# Create a custom style for ttk.Frame to set the background color
style = ttk.Style()  # Ensure style object is created first
style.configure("TFrame", background="#f9fcae")  # Set background color for ttk.Frame

# Scrollable Canvas Setup
canvas = tk.Canvas(root, bg="#f9fcae")  # Set background color for the canvas
scrollable_frame = ttk.Frame(canvas, style="TFrame")  # Apply custom style to the scrollable frame
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

attendance_vars = {}
tk.Label(scrollable_frame, text="Mark Attendance for Tally", font=("Arial", 18, "bold"), bg="#f9fcae").pack(pady=15)

# Create 5 columns of checkboxes
columns = 5
rows = len(students_df)
for i in range(0, rows, columns):
    row_frame = tk.Frame(scrollable_frame, bg="#f9fcae")  # Set background color for each row frame
    row_frame.pack(fill="x", padx=2, pady=2)
    
    # Create checkboxes for each column in the row
    for j in range(columns):
        index = i + j
        if index < rows:
            student = students_df.iloc[index]
            var = tk.IntVar()
            tk.Checkbutton(
                row_frame,
                text=student['Name'],
                variable=var,
                font=("Arial", 13),
                height=2,  # Bigger checkbox height
                width=15,  # Bigger checkbox width
                padx=10,
                pady=5,
                indicatoron=True,
                bg="#f9fcae",  # Set background for each checkbox
            ).pack(side="left", padx=10)
            attendance_vars[student['Registration No.']] = var

# Mark Attendance Function
def mark_attendance():
    for student_id, var in attendance_vars.items():
        attendance_df.at[student_id, today_date] = "Present" if var.get() == 1 else "Absent"
    try:
        with pd.ExcelWriter(excel_file, mode='a', if_sheet_exists='replace') as writer:
            students_df.to_excel(writer, sheet_name="Sheet", index=False)
            attendance_df.reset_index().to_excel(writer, sheet_name="Attendance", index=False)
        messagebox.showinfo("Success", "Attendance saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save attendance: {e}")


# Submit Button
tk.Button(
    root,
    text="Submit Attendance",
    command=mark_attendance,
    font=("Arial", 12, "bold"),
    bg="#ffc010",
    fg="black",
    padx=7,
    pady=5
).pack(pady=10, padx=100)

root.mainloop()
