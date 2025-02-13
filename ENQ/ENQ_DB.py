import tkinter as tk
from tkinter import ttk, PhotoImage, Button
import pandas as pd
import textwrap



# Load Excel data
df = pd.read_excel('Enquiry.xlsx')

# Create main window
root = tk.Tk()
root.title("Enquiry Data")
root.geometry("1200x600")  # Set the window size and position
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

# Create a frame for the Treeview and Scrollbars
frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

# Create a Canvas for scrollable area
canvas = tk.Canvas(frame)
canvas.grid(row=0, column=0, sticky="nsew")

# Add a vertical Scrollbar
v_scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
v_scrollbar.grid(row=0, column=1, sticky="ns")

# Add a horizontal Scrollbar
h_scrollbar = tk.Scrollbar(frame, orient="horizontal", command=canvas.xview)
h_scrollbar.grid(row=1, column=0, sticky="ew")

# Configure Canvas for Scrollbars
canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

# Create a Frame inside Canvas
content_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Function to wrap text to whole words
def wrap_text(text, width):
    return textwrap.fill(text, width)

# Add Headers (with wrapped text for "Student Name")
columns = list(df.columns)
header_frame = tk.Frame(content_frame, bg="lightblue")
header_frame.pack(fill="x")
for column in columns:
    label = tk.Label(header_frame, text=column, bg="lightblue", font=("Arial", 10, "bold"), width=20)
    label.pack(side="left", padx=5, pady=5)

# Add Rows Dynamically
for _, row in df.iterrows():
    row_frame = tk.Frame(content_frame)
    row_frame.pack(fill="x", padx=5, pady=2)
    for i, column in enumerate(columns):
        value = row[column]
        if column == "Student Name":  # Adjust to match your column name
            value = wrap_text(str(value), 20)  # Wrap text to whole words
            label = tk.Label(row_frame, text=value, justify="left", anchor="w", font=("Arial", 10), width=20, wraplength=200)
        else:
            label = tk.Label(row_frame, text=value, justify="center", font=("Arial", 10), width=20)
        label.pack(side="left", padx=5, pady=5)

# Update Scrollable Region Dynamically
def update_scroll_region(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Bind Resize Event
content_frame.bind("<Configure>", update_scroll_region)


# Configure Frame Grid
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Run the Tkinter Event Loop
root.mainloop()
