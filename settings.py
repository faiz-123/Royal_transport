from genral_methods import *
from tkinter import filedialog
import subprocess
from datetime import datetime


class Settings:
    def __init__(self,root):
        self.root = root
        self.root.title("LOGIN")
        self.root.resizable(False,False)
        self.root.wm_iconbitmap("profit.ico")
        self.root.state("zoomed")

        Set_Bg_Image(self, image_path=r"traonsport_images/settings.png")
        self.button_img= r"traonsport_images/login_btn.png"

        self.backup_img = Button_Image(self,img=self.button_img, w=260, h=80)
        self.backup_button = Button(self.root,text="BACKUP",font=("Arial", 20, "bold"),image=self.backup_img,borderwidth=0,activebackground="#ffffff",
                                    background="#ffffff",foreground="white",activeforeground="white",compound=CENTER,command=self.backup_code)
        self.backup_button.place(x=60,y=120,width=260,height=80)


    def backup_code(self):

        self.frame = Frame(self.root,bg='white',borderwidth=3,border=2,highlightcolor="black")
        self.frame.place(x=600,y=100,width=700,height=500)

        # *******************************************************************************************
        self.backup_root_entry = Entry(self.frame, font=("times new roman", 15, "bold"), justify=CENTER, bd=2)
        self.backup_root_entry.place(x=150, y=180, height=40, width=400)

        self.backup_root_browse_img = Button_Image(self.frame, img=self.button_img, w=230, h=60)
        self.browse_button = Button(self.frame, text="Browse", font=("Arial", 18, "bold"),compound=CENTER,command=self.browse_directory,border=3
                                           ,borderwidth=5,highlightthickness=2)
        self.browse_button.place(x=280, y=225, width=130, height=45)

        self.backup_img = Button_Image(self.frame,w=200, h=50)
        self.backup_button = Button(self.frame,text="Start Backup",font=("Arial", 20, "bold"),image=self.backup_img,borderwidth=0,activebackground="white",
                                    background="white",foreground="white",activeforeground="white",compound=CENTER,command=self.export_mysql_datbase)
        self.backup_button.place(x=245,y=280,width=200,height=50)


    def browse_directory(self):
        directory_path = filedialog.askdirectory(title="Select Backup Directory")
        if directory_path:
            self.backup_root_entry.delete(0, END)
            self.backup_root_entry.insert(0, directory_path)

    def export_mysql_datbase(self):
        if self.backup_root_entry.get():
            date = str((datetime.now().date()).strftime("%d_%m_%Y"))
            time = str(datetime.now().time().strftime("%H_%M_%S"))

            # Define database connection details
            host = "localhost"
            user = "root"
            password = "Python@123"
            database = "royal_transport"
            backup_file = "backup_" + date + "_" + time + ".sql"

            file_path = self.backup_root_entry.get()
            # Execute the mysqldump command
            command = f"mysqldump −h{host} −u{user} −p{password} {database} > {file_path}/{backup_file}"
            subprocess.run(command, shell=True)
            messagebox.showinfo("SUCCESS",f"Your Backup Is Completed Success Fully {backup_file}")
        else:
            messagebox.showerror("ERROR","Please Select File Location")


# root = Tk()
# setting_object=Settings(root)
# root.mainloop()