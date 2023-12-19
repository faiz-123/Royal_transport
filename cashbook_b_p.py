# from genral_methods import *
from cashbook_methods import *
from pdf2 import *

class CasbookDetail:
    def __init__(self,root,name='KATARIA BECHRAJI'):
        self.root = root
        self.name = name
        self.root.wm_iconbitmap("profit.ico")
        self.root.state("zoomed")
        self.root.resizable(False, False)
        self.root.title("CASHBOOK DETAIL")

        Set_Bg_Image(self,image_path=r"traonsport_images/cashbook_b_p.png")

        self.vehicle_var = StringVar()
        self.month_var = StringVar()
        self.radio_var=StringVar()
        self.p_radio_var = StringVar()
        self.payment_radio_status = False

        # *******************************************************************************************
        self.month_word = calendar.month_name[(datetime.now()).month].upper()

        # *******************************************************************************************
        self.vehicle_entry = Entry(self.root, font=("times new roman", 16, 'bold'),textvariable=self.vehicle_var,
                                bd=0, highlightthickness=0,justify=CENTER)
        self.vehicle_entry.place(x=595, y=27, height=33, width=365)
        self.vehicle_var.trace('w',partial(to_uppercase, self.vehicle_var))

        # *******************************************************************************************
        self.button_img = Button_Image(self, w=120, h=40)
        self.search_button = Button(self.root, text="SEARCH", font=("times new roman", 15, "bold"),
                                    image=self.button_img,borderwidth=0, activebackground="white",
                                    background="#FBFBFC", foreground="white",compound=CENTER,command=self.search_in_treeview)
        self.search_button.place(x=975, y=23, height=40)

        # *******************************************************************************************
        self.start_d = DateEntry(self.root, font=("times new roman", 15, "bold"), background='darkblue',
                             foreground='white', borderwidth=2, date_pattern='dd/mm/y',justify=CENTER)
        self.start_d.place(x=190, y=112, height=36,width=150)

        # *******************************************************************************************
        self.end_d = DateEntry(self.root,  font=("times new roman", 15, "bold"), background='darkblue',
                             foreground='white', borderwidth=2, date_pattern='dd/mm/y',justify=CENTER)
        self.end_d.place(x=350, y=112, height=36,width=150)

        # *******************************************************************************************
        self.ok_img = Button_Image(self, w=45, h=35)
        self.ok_button = Button(self.root, text="OK", font=("times new roman", 15, "bold"),
                                  image=self.ok_img,borderwidth=0, activebackground="#2664AD", background="#2664AD",
                                 foreground="white",compound=CENTER,command=self.cal_call)
        self.ok_button.place(x=512, y=113, height=35)

        # *******************************************************************************************
        self.pdf_img = Button_Image(self, w=180, h=50)
        self.pdf_button = Button(self.root, text="PDF VIEW", font=("times new roman", 15, "bold"),
                                  image=self.pdf_img,borderwidth=0, activebackground="#ffffff", background="#ffffff",
                                 foreground="white",compound=CENTER,command=self.pdf_genrate)
        self.pdf_button.place(x=690, y=720, height=50)

        # *******************************************************************************************
        self.booking_radio = Radiobutton(root, text="BOOKING",font=('times new roman',15,'bold'),bg='#2664AD',fg='darkblue',
                                    activebackground='#2664AD',value='BOOKING',variable=self.radio_var,command=self.radio_button_call)
        self.booking_radio.place(x=630,y=105)
        self.radio_var.set("BOOKING")

        # *******************************************************************************************
        self.payment_radio = Radiobutton(root, text="PAYMENT",font=('times new roman',15,'bold'),bg='#DFE1E9',fg='darkgreen',
                                    activebackground='#DEE0E8',value='PAYMENT',variable=self.radio_var,command=self.radio_button_call)
        self.payment_radio.place(x=800,y=105)

        # *******************************************************************************************
        list_of_month = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
        self.month_entry = ttk.Combobox(root, values=list_of_month, font=('times new roman', 15, 'bold'),
                                       justify=CENTER,textvariable=self.month_var)
        self.month_entry.place(x=1010, y=112, height=38, width=200)
        self.month_var.set(self.month_word)
        self.month_entry.bind('<<ComboboxSelected>>',self.month_call)

        # *******************************************************************************************

        self.name_label = Label(self.root,text=self.name,font=('times new roman',16,'bold'),fg='blue',bg='white')
        self.name_label.place(x=120,y=176)

        # *******************************************************************************************
        self.radio_button_call()

    def radio_button_call(self):

        if self.radio_var.get()=='BOOKING':
            if self.payment_radio_status:
                payment_radio_destroy(self)
            self.booking_radio.config(bg="#2664AD")
            self.payment_radio.config(bg="#DEE0E8")
            Set_Label_Image(self,image_path=r"traonsport_images/cashbook_booking.png")
            treeview_design(self)
            booking_tree_column_set(self)
            total_entries(self,data=0)
            str_data=return_str_dat(self,key='month')
            set_booking_values(self,str_data)

        elif self.radio_var.get() == 'PAYMENT':
            self.booking_radio.config(bg="#DEE0E8")
            self.payment_radio.config(bg="#2664AD")
            Set_Label_Image(self,image_path=r"traonsport_images/cashbook_payment.png")
            treeview_design(self)
            payment_tree_column_set(self)
            payment_total_entriy(self)
            str_data=return_str_dat(self,key='month')
            set_payment_values(self,str_data)

            self.design_payment_radiobuttons()

    def month_call(self,e):
        if self.radio_var.get() == 'BOOKING':
            str_data = return_str_dat(self,key='month')
            set_booking_values(self,str_data)

        elif self.radio_var.get() =='PAYMENT':
            str_data = return_str_dat(self,key='month')
            set_payment_values(self,str_data)

        if self.p_radio_var.get():
            self.payment_radio_buttons_call()

    def cal_call(self):
        if self.radio_var.get() == 'BOOKING':
            str_data = return_str_dat(self,key='cal')
            set_booking_values(self,str_data)
        elif self.radio_var.get() == 'PAYMENT':
            str_data = return_str_dat(self, key='cal')
            set_payment_values(self,str_data)

        if self.p_radio_var.get():
            self.payment_radio_buttons_call(key='cal')

    def payment_radio_buttons_call(self,**kwargs):
        key = kwargs.get('key','month')
        if self.p_radio_var.get()=='ADVANCE':
            str_data = return_str_dat(self, key=key)
            str_data = " payment_type='ADVANCE' and "+str_data
            set_payment_values(self,str_data)
        elif self.p_radio_var.get()=='BALANCE':
            str_data = return_str_dat(self, key=key)
            str_data = " payment_type='BALANCE' and "+str_data
            set_payment_values(self,str_data)
        elif self.p_radio_var.get()=='ALL':
            str_data = return_str_dat(self, key=key)
            set_payment_values(self,str_data)

    def design_payment_radiobuttons(self):

        # *******************************************************************************************
        self.advance_radio = Radiobutton(self.root, text="ADVANCE",font=('times new roman',10,'bold'),bg='#DFE1E9',fg='black',
                                    activebackground='#DEE0E8',value='ADVANCE',variable=self.p_radio_var,
                                         command=self.payment_radio_buttons_call)
        self.advance_radio.place(x=1250,y=80)

        # *******************************************************************************************
        self.balance_radio = Radiobutton(self.root, text="BALANCE",font=('times new roman',10,'bold'),bg='#DFE1E9',fg='black',
                                    activebackground='#DEE0E8',value='BALANCE',variable=self.p_radio_var,command=self.payment_radio_buttons_call)
        self.balance_radio.place(x=1250,y=105)

        # *******************************************************************************************
        self.all_radio = Radiobutton(self.root, text="ALL",font=('times new roman',10,'bold'),bg='#DFE1E9',fg='black',
                                    activebackground='#DEE0E8',value='ALL',variable=self.p_radio_var,command=self.payment_radio_buttons_call)
        self.all_radio.place(x=1250,y=130)
        self.p_radio_var.set('ALL')
        self.payment_radio_status = True

    def search_in_treeview(self):
        search_text = self.vehicle_var.get()
        self.tree.selection_remove(self.tree.get_children())

        for item in self.tree.get_children():
            values = self.tree.item(item, 'values')
            # print(values)
            if any(search_text.lower() in str(value).lower() for value in values):
                self.tree.selection_add(item)

    def pdf_genrate(self):
        values =[]
        for item in self.tree.get_children():
            values.append(self.tree.item(item, 'values'))

        if self.radio_var.get() == 'BOOKING':
            self.data = [(val[1],val[2],val[3],val[4][2:],val[5][2:],val[6][2:],val[7][2:],val[8][2:],val[9][2:],val[11][2:]) for val in values]
        elif self.radio_var.get() =='PAYMENT':
            self.data = [(val[1], val[2], val[3][2:], val[4], val[5]) for val in values]

        create_pdf_with_tree_data(self)


# aroot = Tk()
# object=CasbookDetail(aroot,name='KATARIA BECHRAJI')
# aroot.mainloop()









