from genral_methods import *
from dashboard import *

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("LOGIN")
        self.root.resizable(False,False)
        self.root.wm_iconbitmap("profit.ico")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Set window dimensions
        window_width = 500  # Specify the desired width
        window_height = 550  # Specify the desired height

        # Calculate the X and Y coordinates for the window's top-left corner
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 4

        # Set the window's size and position
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        Set_Bg_Image(self, image_path=r"traonsport_images/login.png")
        img= r"traonsport_images/login_btn.png"

        # *******************************************************************************************
        self.username_entry = Entry(self.root, font=("times new roman", 25, "bold"), justify=CENTER, bd=0)
        self.username_entry.place(x=105, y=160, height=67, width=290)

        # *******************************************************************************************
        self.password_entry = Entry(self.root,show="*", font=("times new roman", 25, "bold"), justify=CENTER, bd=0)
        self.password_entry.place(x=105, y=280, height=65, width=290)
        self.password_entry.bind('<Return>',self.validate_password)

        self.update_img = Button_Image(self,img=img, w=230, h=60)
        self.update_button = Button(self.root,text="Login",font=("Arial", 20, "bold"),image=self.update_img,borderwidth=0,activebackground="#215096",
                                    background="#215096",foreground="white",activeforeground="white",compound=CENTER,command=self.validate_password)
        self.update_button.place(x=145,y=380,width=230,height=60)

    def validate_password(self,*var):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == '123' and password == '123':
            messagebox.showinfo("Login Successful", "Welcome To, PROFIT SOLUTIONS!")
            self.root.withdraw()
            dashboard_root = Toplevel()
            dashboard_obj= Dashboard(dashboard_root,self.root)
            dashboard_root.mainloop()

        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

root = Tk()
login_object=Login(root)
root.mainloop()