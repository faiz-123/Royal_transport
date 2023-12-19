from payment_backend import *

class Payment:
    def __init__(self,root):
        self.root = root
        self.root.wm_iconbitmap("profit.ico")
        self.root.title("PAYMENT ENTRY")
        self.root.state("zoomed")
        self.root.resizable(False,False)

        # ******* Variable Define*******
        self.payment_mode = StringVar()
        self.name_var = StringVar()
        self.vehicle_var = StringVar()
        self.type_var = StringVar()
        self.t_bills_var = IntVar()
        self.amount_var = IntVar()
        self.p_bills_var = IntVar()
        self.balance_var = IntVar()

        self.frame =None
        self.label =None

        self.total_balance = 0
        self.t_bills =0
        self.bal_data =[]
        self.adv_data=[]
        self.tapal_data =[]


        self.data_list = []
        self.des = False
        self.entries = False

        Set_Bg_Image(self, image_path=r"traonsport_images/payment.png")
        self.button_img = Button_Image(self, w=150, h=45)

        # *******************************************************************************************

        self.date = DateEntry(self.root, width=10, font=("times new roman", 15, "bold"), background='#11124D',
                             foreground='white',borderwidth=0, date_pattern='dd/mm/y',justify=CENTER)
        self.date.place(x=1190, y=37, height=38,width=220)

        # *******************************************************************************************

        self.data_list = get_data_from_database(table_name='payment_mode', index=1)
        self.mode_entry = ttk.Combobox(root, values=self.data_list, font=('times new roman', 15, 'bold'),
                                       justify=CENTER,textvariable=self.payment_mode)
        self.mode_entry.place(x=220, y=37, height=38, width=359)
        self.payment_mode.trace('w', partial(trace_data,self, self.payment_mode))
        self.mode_entry.bind('<Tab>', partial(press_tab,self, table_name='payment_mode', var=self.payment_mode))

        # *******************************************************************************************

        self.name_entry = Entry(self.root, font=("times new roman", 15, 'bold'),textvariable=self.name_var,
                                bd=0, highlightthickness=0)
        self.name_entry.place(x=225, y=96, height=34, width=320)
        widget_bind(self,event='name')

        # *******************************************************************************************

        self.vehical_entry = Entry(self.root, font=("times new roman", 15, 'bold'),
                                   bd=0, highlightthickness=0,textvariable=self.vehicle_var)
        self.vehical_entry.place(x=735, y=96, height=34, width=235)
        widget_bind(self,event='vehicle')

        # *******************************************************************************************

        self.balance_label = Label(self.root,text='', font=("times new roman", 20, "bold"),bd=0,fg='red',bg='white')
        self.balance_label.place(x=785, y=50, height=30, width=180)

        # *******************************************************************************************

        self.type_entry = ttk.Combobox(root, values=['ADVANCE', 'BALANCE', 'TAPAL'],
                                       font=('times new roman', 15, 'bold'),textvariable=self.type_var,justify=CENTER)
        self.type_entry.place(x=1188, y=95, height=37, width=220)
        self.type_var.trace('w', partial(trace_data, self, self.type_var))
        self.type_entry.bind("<<ComboboxSelected>>", self.payment_methods)

        # *******************************************************************************************

        self.amount_entry = Entry(self.root, font=("times new roman", 20, "bold"),textvariable=self.amount_var,  justify=CENTER, bd=0)
        self.amount_entry.place(x=225, y=150, height=31, width=340)
        self.amount_var.trace('w', partial(to_digit, self.amount_entry, self.amount_var))
        self.amount_entry.bind('<KeyRelease>',partial(subtract_balance,self))

        # *******************************************************************************************

        self.p_bills_entry = Entry(self.root, font=("times new roman", 20, "bold"), textvariable=self.p_bills_var,justify=CENTER, bd=0)
        self.p_bills_entry.place(x=735, y=150, height=31, width=75)
        self.p_bills_entry.bind('<KeyRelease>',self.entry_set)

        # *******************************************************************************************

        self.balance_entry = Entry(self.root, font=("times new roman", 20, "bold"), textvariable=self.balance_var, justify=CENTER, bd=0,fg='red')
        self.balance_entry.place(x=1195, y=150, height=31, width=205)
        self.balance_var.trace('w', partial(to_digit, self.balance_entry, self.balance_var))

        # *******************************************************************************************

        self.t_bills_entry = Entry(self.root, font=("times new roman", 20, "bold"), textvariable=self.t_bills_var ,fg='red',justify=CENTER, bd=0)
        self.t_bills_entry.place(x=927, y=150, height=31, width=75)


        # *******************************************************************************************

        self.clear_button = Button(self.root, text="CLEAR", font=("times new roman", 15, "bold"), image=self.button_img,
                                   borderwidth=0, activebackground="white", background="white", foreground="white",
                                   compound=CENTER,command=self.clear_entry)
        self.clear_button.place(x=420, y=750, height=45)

        # *******************************************************************************************

        self.save_button = Button(self.root, text="SAVE", font=("times new roman", 15, "bold"), image=self.button_img,
                                  borderwidth=0, activebackground="white", background="white", foreground="white",
                                  compound=CENTER,command=self.save)
        self.save_button.place(x=610, y=750, height=45)

        # *******************************************************************************************

        self.settlement_button = Button(self.root, text="SETTLEMENT", font=("times new roman", 15, "bold"), image=self.button_img,
                                   borderwidth=0, activebackground="white", background="white", foreground="white",
                                   compound=CENTER,command=self.settlement_payment)
        self.settlement_button.place(x=800, y=750, height=45)

        # *******************************************************************************************

        self.clear_all_button = Button(self.root, text="CLEAR ALL", font=("times new roman", 15, "bold"), image=self.button_img,
                                   borderwidth=0, activebackground="white", background="white", foreground="white",
                                   compound=CENTER,command=self.clear_all)
        self.clear_all_button.place(x=990, y=750, height=45)


        # *******************************************************************************************

        self.poligon_img = Button_Image(self, img=r"traonsport_images/poligon_left.png", w=20, h=25)
        self.name_poligon_button = Button(self.root, image=self.poligon_img, borderwidth=0,
                                          activebackground="white", background="white", foreground="white",compound=CENTER
                                          ,command=partial(create_name_list,self,event=''))
        self.name_poligon_button.place(x=546, y=97, height=31,width=27)

        # *******************************************************************************************

        self.vehicle_poligon_button = Button(self.root, image=self.poligon_img, borderwidth=0,
                                             activebackground="white", background="white", foreground="white",compound=CENTER)
                                             # ,command=create_vehicle_list)
        self.vehicle_poligon_button.place(x=972, y=97, height=31,width=27)

    def payment_methods(self,event):
        if self.name_var.get():
            if self.type_var.get()=='ADVANCE':
                self.adv_payment_amount = []
                self.adv_total_payment = []
                advance_payment_methods(self)
                self.entries=True

            elif self.type_var.get() =='BALANCE' or self.type_var.get() =='MAJURI':
                self.bal_payment_amount = []
                self.bal_total_payment =[]
                balance_payment_methods(self)
                self.entries = True

            elif self.type_var.get() == 'TAPAL':
                self.tapal_payment_amount = []
                self.tapal_total_balance = []
                tapal_payment_methods(self)
                self.entries = True

    def entry_set(self,event):
        if self.type_var.get()=='ADVANCE':
            advance_entries_set(self)

        elif self.type_var.get() == 'BALANCE':
            balance_entries_set(self)

        elif self.type_var.get() == 'TAPAL':
            tapal_entries_set(self)

    def save(self):
        flag=True
        if self.type_var.get() == 'ADVANCE':
            if not check_negative_value(self):
                self.amount_entry.focus_set()
                flag=False
                return

            if not verify_amount_and_entries_values(self):
                flag=False
                return
            if flag:
                advance_save_call(self)

        elif self.type_var.get() == 'BALANCE' or self.type_var.get() == 'MAJURI':
            if not check_negative_value(self):
                self.amount_entry.focus_set()
                flag=False
                return

            if not verify_amount_and_entries_values(self):
                flag=False
                return
            if flag:
                balance_save_call(self)

        elif self.type_var.get() == 'TAPAL':
            if not check_negative_value(self):
                self.amount_entry.focus_set()
                flag=False
                return

            if not verify_amount_and_entries_values(self):
                flag=False
                return
            if flag:
                tapal_save_call(self)

    def clear_entry(self):
        response  = messagebox.askyesno("Question", "Do you want to Clear All Entry!")
        if response:
            if self.type_var.get() == 'ADVANCE':
                for i in range(len(self.adv_payment_amount)):
                    self.adv_payment_amount[i].set(0)
                    self.adv_total_payment[i].set(self.adv_data[i][-1])

            elif self.type_var.get() == 'BALANCE':
                for i in range(len(self.bal_payment_amount)):
                    self.bal_payment_amount[i].set(0)
                    self.bal_total_payment[i].set(self.bal_data[i][-1])

            elif self.type_var.get() == 'TAPAL':
                for i in range(len(self.tapal_payment_amount)):
                    self.tapal_payment_amount[i].set(0)
                    self.tapal_total_balance[i].set(self.tapal_data[i][-1])
            self.p_bills_var.set(0)
            self.amount_entry['state']='normal'

    def clear_all(self):
        response  = messagebox.askyesno("Question", "Do you want to Clear All Entry!")
        if response:
            if self.entries:
                self.frame.destroy()
                self.label.destroy()
            self.payment_mode.set('')
            self.balance_label.config(text='')
            self.name_var.set('')
            self.vehicle_var.set('')
            self.type_var.set('')
            self.amount_var.set(0)
            self.p_bills_var.set(0)
            self.t_bills_var.set(0)
            self.balance_var.set(0)
            self.amount_entry['state']='normal'

    def settlement_payment(self):
        response = messagebox.askyesno("Question", "Do you want to Clear All Entry!")
        if response:
            if self.type_var.get() =='ADVANCE':
                settle_amount_defination(self, db_data=self.adv_data, payment_amount=self.adv_payment_amount,
                                         total_amount=self.adv_total_payment)
            elif self.type_var.get() =='BALANCE':
                settle_amount_defination(self,db_data=self.bal_data,payment_amount=self.bal_payment_amount,total_amount=self.bal_total_payment)

            elif self.type_var.get() =="TAPAL":
                settle_amount_defination(self, db_data=self.tapal_data, payment_amount=self.tapal_payment_amount,
                                         total_amount=self.tapal_total_balance)



root = Tk()
payment_object=Payment(root)
root.mainloop()