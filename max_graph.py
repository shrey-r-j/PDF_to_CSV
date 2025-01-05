import tkinter as tk
from io import StringIO
import sys
from main import tot_analysis
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from main import chem_graph
from main import mech_graph
from main import ep_graph
from main import bxe_graph
from main import bee_graph
from main import m1_graph
from main import m2_graph
from main import sme_graph
from main import pps_graph
from main import pbl_graph
from main import ws_graph
def redirect_stdout(text_widget):
    """Redirect standard output to the given Text widget."""
    sys.stdout = text_widget

def display_analysis():
    """Display the analysis of the data frames."""
    # Capture the output of the function in a StringIO object
    captured_output = StringIO()
    sys.stdout = captured_output
    tot_analysis()
    sys.stdout = sys.__stdout__

    # Display the captured output in the Text widget
    text_widget.insert(tk.END, captured_output.getvalue())

# Create the main window of the GUI
root = tk.Tk()

# Create a Text widget to display the output
text_widget = tk.Text(root)
text_widget.pack(expand=True, fill=tk.BOTH)

# Create a button to display the analysis
button = tk.Button(root, text="Display Maximum Marks Obtained", command=display_analysis)
button.pack(pady=10)

# Start the main loop of the GUI
root.mainloop()


def display_graph(subject):
    # Create a new figure and canv
    fig = Figure(figsize=(5, 4), dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Clear the previous plot
    fig.clf()

    # Display the selected subject's graph
    if subject == 'Chemistry':
        chem_graph()
    elif subject == 'Mechanics':
        mech_graph()
    elif subject == 'Physics':
        ep_graph()
    elif subject == 'BXE':
        bxe_graph()
    elif subject == 'BEE':
        bee_graph()
    elif subject == 'M1':
        m1_graph()
    elif subject == 'M2':
        m2_graph()
    elif subject == 'SME':
        sme_graph()
    elif subject == 'PPS':
        pps_graph()
    elif subject == 'PBL':
        pbl_graph()
    elif subject == 'Workshop':
        ws_graph()

# Create the main window
window = tk.Tk()
window.title('Subject Selector')

# Create a dropdown menu to select the subject
subject_var = tk.StringVar(window)
subject_var.set('Select Subject')
subject_options = ['Select Subject', 'Chemistry', 'Mechanics', 'Physics', 'BXE', 'BEE', 'M1', 'M2', 'SME', 'PPS', 'PBL', 'Workshop']
subject_dropdown = tk.OptionMenu(window, subject_var, *subject_options, command=lambda subject: display_graph(subject))
subject_dropdown.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# Run the main loop
window.mainloop()