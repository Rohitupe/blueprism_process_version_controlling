import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("USERNAME_bp")
password = os.getenv("PASSWORD_bp")
bp_software_folderpath = os.getenv("BP_Software_FolderPath")

def run_blueprism_cli(action, name):
    # Replace these stubs with your actual CLI commands
    if action == "Import Process":
        working_dir = r"\Blue Prism\Process_Objects"
        cli_command = f'"{bp_software_folderpath}" /import "{name}" /overwrite /user {username} {password}'
    elif action == "Import Release":
        working_dir = r"\Blue Prism\Package_Release"
        cli_command = f'"{bp_software_folderpath}" /importrelease "{name}" /overwrite /user {username} {password}'
    elif action == "Export Process":
        working_dir = r"\Blue Prism\Process_Objects"
        cli_command = f'"{bp_software_folderpath}" /export "{name}" /user {username} {password}'
    elif action == "Export Package":
        working_dir = r"\Blue Prism\Package_Release"
        cli_command = f'"{bp_software_folderpath}" /exportpackage "{name}" /user {username} {password}'
    else:
        messagebox.showerror("Error", "Unknown action selected.")
        return

    try:
        print(cli_command)
        if action == "Export Package":
            p = subprocess.Popen(cli_command, text=True, shell=True, cwd= os.getcwd() + working_dir)
            p.communicate()
            messagebox.showinfo("Result", "Package Exported.")
        else:
            p = subprocess.Popen(cli_command, stdout=subprocess.PIPE, text=True, shell=True, cwd=os.getcwd() + working_dir)
            output, _ = p.communicate()
            messagebox.showinfo("Result", output)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def on_execute():
    action = action_var.get()
    name = name_entry.get().strip()
    if not name:
        messagebox.showwarning("Input Required", "Please enter a name.")
        return
    run_blueprism_cli(action, name)

def update_label(*args):
    action = action_var.get()
    if "Process" in action or "Object" in action:
        name_label.config(text="Process / Object Name:")
    else:
        name_label.config(text="BP Release / Skill Name:")

root = tk.Tk()
root.title("Blue Prism CLI GUI")

tk.Label(root, text="Select Action:").grid(row=0, column=0, padx=10, pady=10)
action_var = tk.StringVar()
action_dropdown = ttk.Combobox(
    root, textvariable=action_var,
    values=["Import Process", "Import Release", "Export Process", "Export Package"],
    state="readonly"
)
action_dropdown.grid(row=0, column=1, padx=10, pady=10)
action_dropdown.current(0)
action_dropdown.bind("<<ComboboxSelected>>", update_label)

name_label = tk.Label(root, text="Process / Object Name:")
name_label.grid(row=1, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=10)

execute_btn = tk.Button(root, text="Execute", command=on_execute)
execute_btn.grid(row=2, column=0, columnspan=2, pady=20)

# Set initial label based on default selection
update_label()

root.mainloop()