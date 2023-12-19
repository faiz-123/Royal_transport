from genral_methods import *

class LedgerEntry:
    def __init__(self,root):
        self.root = root
        self.root.wm_iconbitmap("profit.ico")
        self.root.title("TRANSPOTER ENTRY")
        self.root.resizable(False,False)

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - 1020) // 2  # Center horizontally
        y = (screen_height - 700) // 3  # Center vertically

        # Set the size and position of the new window
        self.root.geometry("1020x700+{}+{}".format(x, y))

        Set_Bg_Image(self,image_path=r"traonsport_images/ledger.png")
        self.name_var=StringVar()
        self.city_var=StringVar()
        self.contact_var=IntVar()

# *******************************************************************************************
        self.name_entry = Entry(self.root,font=("times new roman",17,"bold"),justify=LEFT,bd=0,textvariable=self.name_var)
        self.name_entry.place(x=90,y=142,height=40,width=260)
        self.name_var.trace('w',partial(to_uppercase,self.name_var))

        self.city_entry = Entry(self.root,font=("times new roman",18,"bold"),justify=LEFT, bd=0,textvariable=self.city_var)
        self.city_entry.place(x=435,y=142,height=40,width=200)
        self.city_var.trace('w',partial(to_uppercase,self.city_var))

        self.contact_entry = Entry(self.root,font=("times new roman",18,"bold"),justify=LEFT, bd=0,textvariable=self.contact_var)
        self.contact_entry.place(x=722,y=142,height=40,width=200)
        self.contact_var.trace('w',partial(to_digit,self.contact_entry,self.contact_var))

# *******************************************************************************************

        self.button_img = Button_Image(self, w=150, h=45)
        self.add_button = Button(self.root, text="ADD", font=("times new roman", 15, "bold"), image=self.button_img,
                                 borderwidth=0, activebackground="white", background="white", foreground="white",
                                 compound=CENTER,command=self.insert_data_into_db)
        self.add_button.place(x=460, y=210)

# *******************************************************************************************
        self.tree = ttk.Treeview(self.root,columns=('id','name','location','contact') ,show='headings',selectmode='browse')

        self.tree.column("id", anchor=CENTER,width=5,minwidth=5)
        self.tree.column("name", anchor=NW,width=300,minwidth=300)
        self.tree.column("location", anchor=CENTER,width=150,minwidth=150)
        self.tree.column("contact", anchor=CENTER,width=150,minwidth=150)

        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="NAME")
        self.tree.heading("location", text="LOCATION")
        self.tree.heading("contact", text="CONTACT")

        self.tree.tag_configure('T', font=("times new roman",15,'bold'))

        s = ttk.Style()
        s.theme_use('clam')

        s.configure('Treeview', rowheight=25)

        s.configure('Treeview.Heading', background="#2664AD",foreground="white",
                        font=("times new roman", 15,"bold"),releif=FLAT)

        s.map('Treeview.Heading',background=[('active','#2664AD')])

        self.tree.place(x=50,y=270,width=920,height=280)
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        vsb.place(x=955, y=305, height=245)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.bind("<Double-1>", self.populate_entries)

# *******************************************************************************************
#         self.button_img = Button_Image(self, w=150, h=45)
        self.update_button = Button(self.root, text="UPATE", font=("times new roman", 15, "bold"), image=self.button_img,
                                 borderwidth=0, activebackground="white", background="white", foreground="white",
                                 compound=CENTER,command=self.update_value_in_database)
        self.update_button.place(x=250, y=565)

# *******************************************************************************************

        # self.delete_img = Button_Image(self, w=150, h=45)
        self.delete_button = Button(self.root, text="DELETE", font=("times new roman", 15, "bold"), image=self.button_img,
                                 borderwidth=0, activebackground="white", background="white", foreground="white",
                                 compound=CENTER,command=self.delete_value_from_database)
        self.delete_button.place(x=450, y=565)

# *******************************************************************************************

        # self.clear_img = Button_Image(self, w=150, h=45)
        self.clear_button = Button(self.root, text="CLEAR", font=("times new roman", 15, "bold"), image=self.button_img,
                                 borderwidth=0, activebackground="white", background="white", foreground="white",
                                 compound=CENTER,command=self.clear_entries)
        self.clear_button.place(x=650, y=565)
        self.populate_treeview()

    def insert_data_into_db(self):
        val = self.name_var.get()
        name = get_data_from_database(table_name='ledger_entry',index=1)

        if val in name:
            messagebox.showwarning('WARNING', "Name Is Already Available!")

        elif val:
            response = messagebox.askyesno("Question","Do you want to Save This Name!", parent=self.root)
            if response:
                query = f'''INSERT INTO `ledger_entry` (`name`, `city`, `mobile_no`)
                        VALUES ('{self.name_var.get()}', '{self.city_var.get()}', '{self.contact_var.get()}');
                        '''
                if execute_query(query=query):
                    messagebox.showinfo("Success", f"Data Saved successfully."+" "*20, parent=self.root)
                self.populate_treeview()
        else:
            messagebox.askretrycancel('MISSING', 'Mandotary Argument Missing NAME!')

    def clear_entries(self):
        self.name_var.set('')
        self.city_var.set('')
        self.contact_var.set(0)
        self.name_entry.focus_set()

    def populate_treeview(self):
        data = fetch_data(table_name='ledger_entry')
        self.tree.delete(*self.tree.get_children())  # Clear the Treeview before repopulating
        for record in data:
            self.tree.insert("", "end", values=record, tags='T')

    def populate_entries(self,event):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item((selected_item[0]),"values")
            self.name_var.set(item_values[1])
            self.city_var.set(item_values[2])
            self.contact_var.set(int(item_values[3]))

    def update_value_in_database(self):
        if not self.name_entry.get():
            messagebox.askretrycancel('WARNING', 'There Is No Updated Value In Box!')
            return
        selected_item = self.tree.selection()
        if selected_item:
            response = messagebox.askyesno("Question", "Do you want to Update!")
            if not response:
                return
            item_values = self.tree.item((selected_item[0]),"values")
            query=f""" UPDATE `ledger_entry` SET `name` = '{self.name_var.get()}', 
                        `city` = '{self.city_var.get()}', `mobile_no` = '{self.contact_var.get()}' WHERE (`id` = '{item_values[0]}')"""
            # print(query)
            if execute_query(query=query):
                messagebox.showinfo("Success", "Data Updated successfully.")
            self.populate_treeview()
        else:
            messagebox.askretrycancel('WARNING','Select Data from table for update')

    def delete_value_from_database(self):
        selected_item = self.tree.selection()
        if selected_item:
            response = messagebox.askyesno("Question", "Do you want to Delete!")
            if not response:
                return
            item_values = self.tree.item((selected_item[0]),"values")
            query=f"""DELETE FROM `ledger_entry` WHERE (`id` = '{item_values[0]}')"""

            if execute_query(query=query):
                messagebox.showinfo("Success", "Data Deleted successfully.")
            self.populate_treeview()
        else:
            messagebox.askretrycancel('WARNING','Select Name from table for Delete')

# root = Tk()
# ledger_object=LedgerEntry(root)
# root.mainloop()