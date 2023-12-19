import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\fbabuna\AppData\Local\Programs\Python\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\fbabuna\AppData\Local\Programs\Python\Python311\tcl\tk8.6"

executables = [cx_Freeze.Executable("Profit_Solution.py", base=base, icon='profit.ico')]


cx_Freeze.setup(
    name = "Profit Solution",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":['profit.ico','tcl86t.dll','tk86t.dll','traonsport_images','cashbook_pdf','icon']}},
    version = "1.0",
    description = "Royal Transport  | Developed By Faiz Babuna",
    executables = executables
    )