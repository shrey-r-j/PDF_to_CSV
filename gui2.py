# import tkinter as tk
# from tkinter import filedialog

# selected_file_path = ""  # Global variable to store the selected file path

# def open_pdf():
#     global selected_file_path
#     selected_file_path = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
#     if selected_file_path:
#         # Pass the selected_file_path to my_function or use it directly
#         my_function(selected_file_path)

# def my_function(file_path):
#     # Do something with the file_path
#     print(f"Selected PDF file: {file_path}")

# root = tk.Tk()
# root.title("PDF Opener")

# button = tk.Button(root, text="Open PDF", command=open_pdf)
# button.pack(pady=10)

# root.mainloop()

# # Now you can use selected_file_path wherever needed
# print("Path of the opened file:", selected_file_path)

import tkinter as tk
from tkinter import filedialog
import os

selected_file_path = ""  # Global variable to store the selected file path
selected_folder_path = ""  # Global variable to store the selected folder path

def open_pdf():
    global selected_file_path
    selected_file_path = filedialog.askopenfilename(filetypes=[('PDF Files', '*.pdf')])
    if selected_file_path:
        # Pass the selected_file_path to my_function or use it directly
        my_function(selected_file_path)

def select_folder():
    global selected_folder_path
    selected_folder_path = filedialog.askdirectory()
    if selected_folder_path:
        # Ensure the directory exists (like your original code)
        if not os.path.exists(selected_folder_path):
            os.makedirs(selected_folder_path)
        print(f"Selected folder: {selected_folder_path}")
        
        # Here you can add your logic to save CSV files to the selected folder
        save_csv_to_folder(selected_folder_path)

def my_function(file_path):
    # Do something with the file_path
    print(f"Selected PDF file: {file_path}")

def save_csv_to_folder(folder_path):
    # Example logic for saving CSV files in the selected folder
    csv_file_path = os.path.join(folder_path, "example.csv")
    with open(csv_file_path, 'w') as file:
        file.write("Column1, Column2, Column3\n")
        file.write("Data1, Data2, Data3\n")
    print(f"CSV file saved to {csv_file_path}")

root = tk.Tk()
root.title("PDF Opener")

# Button to open a PDF file
button_open_pdf = tk.Button(root, text="Open PDF", command=open_pdf)
button_open_pdf.pack(pady=10)

# Button to select folder for storing files
button_select_folder = tk.Button(root, text="Select Folder", command=select_folder)
button_select_folder.pack(pady=10)

root.mainloop()

# Now you can use selected_file_path and selected_folder_path wherever needed
print("Path of the opened file:", selected_file_path)
print("Path of the selected folder:", selected_folder_path)

