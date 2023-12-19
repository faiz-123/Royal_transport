from genral_methods import *
from cashbook_b_p import *


class Cashbook:
    def __init__(self,root):

        self.root = root
        self.root.wm_iconbitmap("profit.ico")
        self.root.state("zoomed")
        self.root.resizable(False,False)
        self.root.title("CASHBOOK")

        self.name_var = StringVar()

        Set_Bg_Image(self,image_path=r"traonsport_images/cashbook.png")
        self.button_img = Button_Image(self, w=130, h=40)

        self.name_entry = Entry(self.root, font=("times new roman", 17, 'bold'),textvariable=self.name_var,
                                bd=0, highlightthickness=0)
        self.name_entry.place(x=565, y=38, height=33, width=375)
        self.name_var.trace('w', partial(self.trace_data, self.name_var))

        self.search_button = Button(self.root, text="SEARCH", font=("times new roman", 15, "bold"),
                                  image=self.button_img,
                                  borderwidth=0, activebackground="white", background="white", foreground="white",
                                  compound=CENTER,command=self.search_in_treeview)
        self.search_button.place(x=990, y=35, height=40)


        self.tree = ttk.Treeview(self.root,columns=('id', 'name','a_bills','b_bills') ,show='headings',selectmode='browse')

        self.tree.column("id", anchor=CENTER,width=60,minwidth=10)
        self.tree.column("name", anchor=NW,width=600,minwidth=600)
        self.tree.column("a_bills", anchor=NW)
        self.tree.column("b_bills", anchor=CENTER)



        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="NAME")
        self.tree.heading("a_bills", text="BALANCE BAKI")
        self.tree.heading("b_bills", text="BALANCE BILLS")


        self.tree.tag_configure('T', font=("times new roman",16,'bold'),foreground='black')

        s = ttk.Style()
        s.theme_use('clam')
        # Configure the style of Heading in Treeview widget

        s.configure('Treeview',rowheight=35)
        s.configure('Treeview.Heading' ,background="#2664AD",foreground="white",
                        font=("times new roman", 15,"bold"),releif=FLAT)

        s.map('Treeview.Heading',background=[('active','#2664AD')])
        s.configure('C', rowheight=30)



        self.tree.place(x=32,y=85,width=1470,height=690)
        vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        vsb.place(x=1480, y=120, height=655,width=20)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.bind("<Double-1>", self.populate_cahbook_value)
        self.tree.bind("<Return>", self.populate_cahbook_value)
        self.display_cashbook_details()

    def trace_data(self,*args):
        var = args[0]
        to_uppercase(var)

    def display_cashbook_details(self):
        name_query = "SELECT distinct name FROM royal_transport.booking_entry ORDER BY name ASC;"
        name_list = fetch_colum_data(query=name_query)
        if name_list:
            for i in range(len(name_list)):
                name = name_list[i][0]
                query1 = f"SELECT sum(total_balance),count(bill_no) FROM royal_transport.booking_entry where name='{name}' and total_balance!=0;"
                data = fetch_colum_data(query=query1)[0]
                balance_baki = format_currency(data[0])
                bal_bill =data[1]
                self.tree.insert("", "end",values=(f"{i+1}",(" "*5)+name, " "*10+str(balance_baki),bal_bill),tags='T')

    def populate_cahbook_value(self,e):
        name = ''
        item = self.tree.selection()
        if item:
            values = self.tree.item(item, 'values')
            name =values[1].strip()
        self.root.withdraw()
        second_root = Toplevel()
        second_obj = CasbookDetail(second_root,name)
        second_root.protocol("WM_DELETE_WINDOW", partial(self.exitt, second_root))

        second_root.mainloop()

    def search_in_treeview(self):
        search_text = self.name_var.get()
        self.tree.selection_remove(self.tree.get_children())

        for item in self.tree.get_children():
            values = self.tree.item(item, 'values')
            if any(search_text.lower() in str(value).lower() for value in values):
                self.tree.selection_add(item)

    def exitt(self,d_root):
        sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=d_root)
        if sure == True:
            d_root.destroy()
            self.root.deiconify()
            self.root.state('zoomed')



# root = Tk()
# cashbook_object=Cashbook(root)
# root.mainloop()

