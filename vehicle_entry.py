from genral_methods import *
from tkinter import ttk

class VehicleEntry:
    def __init__(self,root):
        self.root = root
        self.root.title("VEHICLE ENTRY")
        self.root.wm_iconbitmap("profit.ico")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - 1020) // 2  # Center horizontally
        y = (screen_height - 700) // 3  # Center vertically

        # Set the size and position of the new window
        self.root.geometry("1020x700+{}+{}".format(x, y))
        self.root.resizable(False, False)
        self.vehicle_var = StringVar()

        Set_Bg_Image(self,image_path=r"traonsport_images/vehicle.png")

        self.vehicle_entry = Entry(self.root,font=("times new roman",20,"bold"),justify=CENTER, bd=0,textvariable=self.vehicle_var)
        self.vehicle_entry.place(x=145,y=280,height=45,width=220)
        self.vehicle_var.trace('w',partial(to_uppercase,self.vehicle_var))

# *******************************************************************************************

        self.tree = ttk.Treeview(self.root,columns=('id', 'vehicle_no') ,show='headings',selectmode='browse')

        self.tree.column("id", anchor=CENTER,width=60,minwidth=60)
        self.tree.column("vehicle_no", anchor=CENTER,width=436,minwidth=436)

        self.tree.heading("id", text="ID")
        self.tree.heading("vehicle_no", text="VEHICLE NUMBER")
        self.tree.tag_configure('T', font=("times new roman",15,'bold'))

        s = ttk.Style()
        s.theme_use('clam')
        # Configure the style of Heading in Treeview widget
        s.configure('Treeview.Heading', background="#2664AD",foreground="white",
                        font=("times new roman", 15,"bold"),releif=FLAT)
        s.map('Treeview.Heading',background=[('active','#2664AD')])

        s.configure('Treeview', rowheight=30)

        self.tree.place(x=453,y=145,width=450,height=360)
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        vsb.place(x=890, y=180, height=323)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.bind("<Double-1>", self.populate_value_entrybox)


# *******************************************************************************************
        self.button_img = Button_Image(self,w=150,h=45)
        self.add_button = Button(self.root,text="ADD",font=("times new roman",20,"bold") ,image=self.button_img,
                        borderwidth=0,activebackground="white",background="white",foreground="white",
                                 compound=CENTER,command=self.insert_into_database)
        self.add_button.place(x=180,y=360)

# *******************************************************************************************

        self.clear_button = Button(self.root,text="CLEAR",font=("times new roman",15,"bold") ,image=self.button_img,
                        borderwidth=0,activebackground="white",background="white",foreground="white",
                                 compound=CENTER,command=self.clear_vehicle_entry)
        self.clear_button.place(x=180,y=420)

# *******************************************************************************************
#         self.update_img= Button_Image(self,w=150,h=45)
        self.update_button = Button(self.root,text="UPDATE",font=("times new roman",15,"bold") ,image=self.button_img,
                        borderwidth=0,activebackground="white",background="white",foreground="white",
                                    compound=CENTER,command=self.update_value_in_database)
        self.update_button.place(x=510,y=510)

# *******************************************************************************************
#         self.delete_img= Button_Image(self,w=150,h=45)
        self.delete_button = Button(self.root,text="DELETE",font=("times new roman",15,"bold") ,image=self.button_img,
                        borderwidth=0,activebackground="white",background="white",foreground="white",
                                    compound=CENTER,command=self.delete_value_from_database)
        self.delete_button.place(x=700,y=510)
        self.populate_treeview()

    def insert_into_database(self):
        val = self.vehicle_entry.get()
        vehicle_numbers = get_data_from_database(table_name='vehicle_entry',index=1)

        if val in vehicle_numbers:
            messagebox.showwarning('WARNING', "Vehicle Number Is Already Available!")

        elif val:
            response = messagebox.askyesno("Question", "Do you want to Save This Number!",parent=self.root)
            if response:
                query = f"INSERT INTO `royal_transport`.`vehicle_entry` (`vehicle_number`) VALUES ('{self.vehicle_var.get()}');"
                # print(query)
                execute_query(query=query)
                self.populate_treeview()
        else:
            messagebox.askretrycancel('MISSING',"Please Enter Valid Vehicle Number")

    def populate_treeview(self):

        data = fetch_data(table_name='vehicle_entry')
        # print(data)
        self.tree.delete(*self.tree.get_children())  # Clear the Treeview before repopulating
        for record in data:
            self.tree.insert("", "end", values=record, tags='T')

    def populate_value_entrybox(self,event):

        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item((selected_item[0]),"values")
            # print(values)
            self.vehicle_var.set(values[1])

    def update_value_in_database(self):

        selected_item = self.tree.selection()
        if selected_item:
            response = messagebox.askyesno("Question", "Do you want to Update!")
            if response:
                values = self.tree.item((selected_item[0]),"values")
                query=f""" UPDATE `royal_transport`.`vehicle_entry` SET `vehicle_number` = '{self.vehicle_var.get()}' WHERE (`id` = '{values[0]}'); """
                # print(query)
                if execute_query(query=query):
                    messagebox.showinfo("Success", "Data Updated successfully.")
                self.populate_treeview()
        else:
            messagebox.askretrycancel('WARNING', 'There Is No Updated Value In Entry Box!')

    def delete_value_from_database(self):
        selected_item = self.tree.selection()
        if selected_item:
            response = messagebox.askyesno("Question", "Do you want to Delete!")
            if response:
                values = self.tree.item((selected_item[0]),"values")
                query=f"""DELETE FROM `vehicle_entry` WHERE (`id` = '{values[0]}')"""
                if execute_query(query=query):
                    messagebox.showinfo("Success", "Data Deleted successfully.")
                    self.populate_treeview()
        else:
            messagebox.askretrycancel('WARNING','There Is No Value In Entry Box!')

    def clear_vehicle_entry(self):

        self.vehicle_var.set('')

# root = Tk()
# vehicle_object=VehicleEntry(root)
# root.mainloop()