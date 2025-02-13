import pandas as pd
from datetime import datetime, date
import tkinter as tk
from tkinter import ttk, messagebox

# File Path
excel_file = "MSCIT.xlsx"

# Load Students Data
try:
    students_df = pd.read_excel(excel_file, sheet_name="Sheet")
    students_df.columns = students_df.columns.str.strip()  # Normalize column names
    if "Registration No." not in students_df.columns or "Name" not in students_df.columns:
        raise KeyError("The 'Sheet' must have columns: 'Registration No.' and 'Name'.")
except Exception as e:
    messagebox.showerror("Error", f"Failed to load students data: {e}")
    students_df = pd.DataFrame(columns=["Registration No.", "Name"])

# Create or load attendance data
try:
    attendance_df = pd.read_excel(excel_file, sheet_name="Attendance")
    attendance_df.columns = attendance_df.columns.str.strip()  # Normalize column names
    attendance_df.set_index("Registration No.", inplace=True)
except Exception as e:
    attendance_df = students_df.set_index("Registration No.")[["Name"]]
    today_date = date.today().strftime('%d-%m-%Y')
    attendance_df[today_date] = None

# Ensure today's column exists
today_date = date.today().strftime('%d-%m-%Y')
if today_date not in attendance_df.columns:
    attendance_df[today_date] = None

# Tkinter GUI for Attendance
root = tk.Tk()
root.title("MS-CIT Attendance Tracker")
root.geometry("600x800")
root.configure(bg="#f9fcae")

# Scrollable Canvas Setup
canvas = tk.Canvas(root, bg="#f9fcae")
scrollable_frame = ttk.Frame(canvas)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

attendance_vars = {}

# Title
tk.Label(
    scrollable_frame, 
    text="Mark Attendance for MS-CIT", 
    font=("Arial", 18, "bold"), 
    bg="#f9fcae"
).pack(pady=15)

# Create Checkboxes for Each Student
for index, student in students_df.iterrows():
    var = tk.IntVar()
    tk.Checkbutton(
        scrollable_frame,
        text=f"{student['Name']} ({student['Registration No.']})",
        variable=var,
        font=("Arial", 13),
        bg="#f9fcae",
        anchor="w",
        padx=10
    ).pack(fill="x", padx=10, pady=5)
    attendance_vars[student['Registration No.']] = var

# Mark Attendance Function
def mark_attendance():
    today_date = datetime.today().strftime('%d-%m-%Y')
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
).pack(pady=20)

root.mainloop()
