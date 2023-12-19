import tkinter as tk
from tkinter import messagebox
import subprocess
import datetime

def backup_database():
    # MySQL database connection parameters
    host = 'localhost'
    user = 'root'
    password = 'Python@123'
    database = 'royal_transport'

    # Set the path where you want to save the backup file
    backup_path = 'D:/t_e_21/data_backup/'

    # Generate a timestamp for the backup file
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f'{backup_path}backup_{timestamp}.sql'

    # Construct the mysqldump command
    mysqldump_cmd = [
        'mysqldump',
        '-h', host,
        '-u', user,
        '-p' + password,
        database,
        '--result-file=' + backup_file
    ]

    # Execute the mysqldump command
    try:
        subprocess.run(mysqldump_cmd, check=True)
        messagebox.showinfo('Backup Successful', f'Backup saved to {backup_file}')
    except subprocess.CalledProcessError as e:
        messagebox.showerror('Backup Error', f'Failed to create backup - {e}')

# Create the main window
root = tk.Tk()
root.title('MySQL Backup Tool')

# Create a button to trigger the backup
backup_button = tk.Button(root, text='Backup Database', command=backup_database)
backup_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
