import subprocess
from datetime import datetime
import tkinter as tk
from tkinter import filedialog


def export_mysql_datbase():
    date = str((datetime.now().date()).strftime("%d_%m_%Y"))
    time = str(datetime.now().time().strftime("%H_%M_%S"))

    # Define database connection details
    host = "localhost"
    user = "root"
    password = "Python@123"
    database = "royal_transport"
    backup_file = "backup_"+date+"_"+time+".sql"
    print(backup_file)
    # Execute the mysqldump command
    command = f"mysqldump −h{host} −u{user} −p{password} {database} > {backup_file}"
    subprocess.run(command, shell=True)



def browse_directory():
    directory_path = filedialog.askdirectory(title="Select Backup Directory")
    if directory_path:
        entry_directory_path.delete(0, tk.END)
        entry_directory_path.insert(0, directory_path)


# GUI
root = tk.Tk()
root.title("MySQL Database Backup")

# Entry Widgets
entry_directory_path = tk.Entry(root, width=30, borderwidth=2)

# Labels
tk.Label(root, text="Backup Directory:").grid(row=4, column=0)

# Entry Widgets Placement
entry_directory_path.grid(row=4, column=1)

# Buttons
tk.Button(root, text="Browse", command=browse_directory).grid(row=4, column=2, pady=5)
# tk.Button(root, text="Backup Database", command=backup_database).grid(row=5, column=1, pady=(10, 0))

root.mainloop()
