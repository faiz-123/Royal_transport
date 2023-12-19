from genral_methods import *
from ledger_entry import *

class Booking:
    def __init__(self,root):

        self.root = root
        self.root.wm_iconbitmap("profit.ico")
        self.root.state("zoomed")
        self.root.resizable(False,False)
        self.root.title("BOOKING")
        self.name_var = StringVar()
        self.bill_no_var =IntVar()
        self.vehicle_var = StringVar()
        self.source_var = StringVar()
        self.dest_var = StringVar()
        self.freight_var = IntVar()
        # self.hold_amnt_var = IntVar()
        self.majuri_var = IntVar()
        self.adv_var = IntVar()
        self.adv_mode = StringVar()
        self.bal_var = IntVar()
        self.tapal_var = IntVar()
        self.total_bal_var =IntVar()
        self.date_var = StringVar()
        self.des =False
        self.hld_tr = False
        self.disabled=False
        self.style =None

        Set_Bg_Image(self,image_path=r"traonsport_images/booking.png")
        self.button_img = Button_Image(self, w=150, h=45)

        # *******************************************************************************************
        self.name_entry_design(state='normal')

        # *******************************************************************************************
        self.holding_design(state='disabled')

        # *******************************************************************************************
        self.button_design()

# *******************************************************************************************
    def name_entry_design(self,state):

        # *******************************************************************************************
        self.billno_entry = Entry(self.root, font=("times new roman", 20, 'bold'),
                                bd=0, highlightthickness=0, fg="red",
                                 state='readonly',textvariable=self.bill_no_var,justify=CENTER)
        self.billno_entry.place(x=193, y=112, height=27, width=88)
        self.bill_no_set()

        # *******************************************************************************************
        self.date = DateEntry(self.root, width=10, font=("times new roman", 15, "bold"), background='#11124D',
                             foreground='white', state=state,borderwidth=2, date_pattern='dd/mm/y')
        self.date.place(x=1145, y=108, height=35)

        # *******************************************************************************************
        self.get_data_from_database('ledger_entry',index=1)
        self.name_entry = Entry(self.root, font=("times new roman", 15, 'bold'),
                                bd=0, highlightthickness=0,state=state,textvariable=self.name_var)
        self.name_entry.place(x=195, y=159, height=34, width=460)
        self.name_entry.bind('<KeyPress>',partial(self.create_listbox,width=490,x=195,y=195,table_name='ledger_entry',
                                                  px=660,py=160,var=self.name_var,obj=self.name_entry))
        self.name_entry.bind('<Button-1>',partial(self.create_listbox,width=490,x=195,y=195,table_name='ledger_entry',
                                                  px=660,py=160,var=self.name_var,obj=self.name_entry))
        self.name_var.trace('w',partial(self.trace_data,self.name_var))
        self.name_entry.bind('<Down>', partial(self.press_down,'name'))
        self.name_entry.bind('<Tab>',partial(self.press_tab,table_name='ledger_entry',var=self.name_var))

        # *******************************************************************************************

        self.get_data_from_database('vehicle_entry', index=1)
        self.vehical_entry = Entry(self.root, font=("times new roman", 15, 'bold'),
                                   bd=0, highlightthickness=0,state=state,textvariable=self.vehicle_var)
        self.vehical_entry.place(x=1150, y=159, height=33, width=260)
        self.vehical_entry.bind('<KeyPress>', partial(self.create_listbox, width=290, x=1150, y=195,var=self.vehicle_var,
                                                      table_name='vehicle_entry',px=1415,py=160,obj=self.vehical_entry))
        self.vehical_entry.bind('<Button-1>', partial(self.create_listbox, width=290, x=1150, y=195,var=self.vehicle_var,
                                                      table_name='vehicle_entry',px=1415,py=160,obj=self.vehical_entry))
        self.vehicle_var.trace('w', partial(self.trace_data, self.vehicle_var))
        self.vehical_entry.bind('<Down>', partial(self.press_down,'vehicle'))
        self.vehical_entry.bind('<Tab>', partial(self.press_tab, table_name='vehicle_entry', var=self.vehicle_var))
        self.vehical_entry.bind('<Return>', partial(self.press_tab, table_name='vehicle_entry', var=self.vehicle_var))

        self.get_data_from_database('city_entry', index=1)
        self.source_entry = ttk.Combobox(self.root,
                                         values=self.data_list,font=('times new roman',12,'bold'),state=state,textvariable=self.source_var)
        self.source_entry.place(x=42, y=248, height=36, width=135)
        self.source_var.trace('w', partial(self.trace_data, self.source_var))
        self.source_entry.bind('<Button-1>', self.destroye_listbox)
        self.source_entry.bind('<Tab>', partial(self.press_tab, table_name='city_entry', var=self.source_var))
        self.source_entry.bind('<Return>', partial(self.press_tab, table_name='city_entry', var=self.source_var))

        # *******************************************************************************************
        self.get_data_from_database('city_entry', index=1)
        self.destination_entry = ttk.Combobox(self.root, values=self.data_list,font=('times new roman',12,'bold'),state=state,textvariable=self.dest_var)
        self.destination_entry.place(x=187, y=248, height=36, width=135)
        self.destination_entry.bind('<Button-1>', self.destroye_listbox)
        self.dest_var.trace('w',  partial(self.trace_data, self.dest_var))
        self.destination_entry.bind('<Tab>', partial(self.press_tab, table_name='city_entry', var=self.dest_var))
        self.destination_entry.bind('<Return>', partial(self.press_tab, table_name='city_entry', var=self.dest_var))

        # ******************************************************************************************************
        self.freight_entry = Entry(self.root, font=("times new roman", 15, "bold"),state=state, justify=LEFT, bd=0,textvariable=self.freight_var)
        self.freight_entry.place(x=337, y=248, height=36, width=125)
        self.freight_var.trace('w',partial(to_digit,self.freight_entry,self.freight_var))
        self.freight_entry.bind('<KeyRelease>',self.calculate_balance_and_set)
        self.freight_entry.bind('<Button-1>', self.destroye_listbox)

        # *******************************************************************************************
        self.majuri_entry = Entry(self.root, font=("times new roman", 15, "bold"),textvariable=self.majuri_var
                                  ,justify=LEFT, bd=0,state= state)
        self.majuri_entry.place(x=920, y=248, height=36, width=125)
        self.majuri_var.trace('w',partial(to_digit,self.majuri_entry,self.majuri_var))
        self.majuri_entry.bind('<KeyRelease>',self.calculate_balance_and_set)

        # *******************************************************************************************
        self.adv_amount_entry = Entry(self.root, font=("times new roman", 15, "bold"),state=state,textvariable=self.adv_var, justify=LEFT, bd=0)
        self.adv_amount_entry.place(x=1067, y=248, height=36, width=125)
        self.adv_var.trace('w',partial(to_digit,self.adv_amount_entry,self.adv_var))
        self.adv_amount_entry.bind('<Button-1>', self.destroye_listbox)
        self.adv_amount_entry.bind('<KeyRelease>', self.calculate_balance_and_set)

        # *******************************************************************************************
        self.get_data_from_database('payment_mode', index=1)
        self.a_p_mode_entry = ttk.Combobox(self.root, values=self.data_list,font=('times new roman',12,'bold'),state=state,textvariable=self.adv_mode)
        self.a_p_mode_entry.place(x=1208, y=248, height=36, width=135)
        self.a_p_mode_entry.bind('<Button-1>', self.destroye_listbox)
        self.adv_mode.trace('w', partial(self.trace_data, self.adv_mode))
        self.a_p_mode_entry.bind('<Tab>', partial(self.press_tab, table_name='payment_mode', var=self.adv_mode))
        self.a_p_mode_entry.bind('<Return>', partial(self.press_tab, table_name='payment_mode', var=self.adv_mode))

        # *******************************************************************************************
        self.balance_entry = Entry(self.root, font=("times new roman", 15, "bold"),textvariable=self.bal_var,state='readonly',
                                   justify=LEFT, bd=0)
        self.balance_entry.place(x=1360, y=248, height=36, width=125)
        self.balance_entry.bind('<Button-1>', self.destroye_listbox)

        # *******************************************************************************************
        self.tapal_entry = Entry(self.root, font=("times new roman", 15, "bold"),textvariable=self.tapal_var,state=state,
                                   justify=LEFT, bd=0)
        self.tapal_entry.place(x=1360, y=312, height=35, width=125)
        self.tapal_entry.bind('<KeyRelease>',self.calculate_balance_and_set)

        # *******************************************************************************************
        self.total_entry = Entry(self.root, font=("times new roman", 15, "bold"),state='readonly',
                                   justify=LEFT, bd=0,textvariable=self.total_bal_var)
        self.total_entry.place(x=1360, y=376, height=35, width=125)

    def holding_design(self,state):
        self.hold_amnt_var = IntVar()
        # self.majuri_var = IntVar()
        self.h_start_d = DateEntry(self.root, font=("times new roman", 15, "bold"), background='darkblue',
                             foreground='white', borderwidth=2, date_pattern='dd/mm/y',state= state)
        self.h_start_d.place(x=478, y=248, height=36,width=135)

        # *******************************************************************************************
        self.h_end_d = DateEntry(self.root,  font=("times new roman", 15, "bold"), background='darkblue',
                             foreground='white', borderwidth=2, date_pattern='dd/mm/y',state= state)
        self.h_end_d.place(x=624, y=248, height=36,width=135)

        # *******************************************************************************************
        self.holding_entry = Entry(self.root, font=("times new roman", 15, "bold"), justify=LEFT,
                                   bd=0,textvariable=self.hold_amnt_var,state= state)
        self.holding_entry.place(x=775, y=248, height=36, width=125)
        self.hold_amnt_var.trace('w',partial(to_digit,self.holding_entry,self.hold_amnt_var))
        self.holding_entry.bind('<KeyRelease>',partial(self.calculate_balance_and_set))

    def button_design(self):

        self.edit_button = Button(self.root, text="EDIT", font=("times new roman", 15, "bold"),
                                    image=self.button_img,
                                    borderwidth=0, activebackground="white", background="white", foreground="white",
                                    compound=CENTER,command=self.edit_data)
        self.edit_button.place(x=360, y=630, height=45)

        # *******************************************************************************************

        self.clear_button = Button(self.root, text="CLEAR", font=("times new roman", 15, "bold"), image=self.button_img,
                                   borderwidth=0, activebackground="white", background="white", foreground="white",
                                   compound=CENTER,command=self.clear_all_entry)
        self.clear_button.place(x=530, y=630, height=45)

        # *******************************************************************************************

        self.save_button = Button(self.root, text="SAVE", font=("times new roman", 15, "bold"), image=self.button_img,
                                  borderwidth=0, activebackground="white", background="white", foreground="white",
                                  compound=CENTER,command=self.save_booking_data_into_db)
        self.save_button.place(x=700, y=630, height=45)

        # *******************************************************************************************

        self.print_button = Button(self.root, text="PRINT", font=("times new roman", 15, "bold"),
                                    image=self.button_img,
                                    borderwidth=0, activebackground="white", background="white", foreground="white",
                                    compound=CENTER)
        self.print_button.place(x=870, y=630, height=45)

        # *******************************************************************************************

        self.lastbill_button = Button(self.root, text="LAST BILL", font=("times new roman", 15, "bold"),
                                    image=self.button_img,
                                    borderwidth=0, activebackground="white", background="white", foreground="white",
                                    compound=CENTER,command=self.last_bill_populate)
        self.lastbill_button.place(x=1040, y=630, height=45)

        # *******************************************************************************************

        self.holding_button = Button(self.root, text="HOLDINGS", font=("times new roman", 15, "bold"),
                                    image=self.button_img,
                                    borderwidth=0, activebackground="white", background="white", foreground="white",
                                    compound=CENTER,command=self.add_holdings)
        self.holding_button.place(x=620, y=695, height=45)

        # *******************************************************************************************

        self.open_button = Button(self.root, text="OPEN", font=("times new roman", 15, "bold"),
                                    image=self.button_img,
                                    borderwidth=0, activebackground="white", background="white", foreground="white",
                                    compound=CENTER,command=self.add_open)
        self.open_button.place(x=800, y=695, height=45)

        self.poligon_img = Button_Image(self, img=r"traonsport_images/poligon_left.png", w=20, h=25)
        self.name_poligon_button = Button(self.root, image=self.poligon_img, borderwidth=0,
                                     activebackground="white", background="white", foreground="white",
                                     compound=CENTER,command=partial(self.create_listbox,width=490,x=195,y=195,table_name='ledger_entry',
                                                  px=660,py=160,obj=self.name_entry,event=''))
        self.name_poligon_button.place(x=660, y=160, height=34)

        self.vehicle_poligon_button = Button(self.root, image=self.poligon_img, borderwidth=0,
                                     activebackground="white", background="white", foreground="white",
                                     compound=CENTER,command=partial(self.create_listbox, width=290, x=1150, y=195,var=self.vehicle_var,
                                                      table_name='vehicle_entry',px=1415,py=160,obj=self.vehical_entry,event=''))
        self.vehicle_poligon_button.place(x=1415, y=160, height=34)

# *******************************************************************************************

    def bill_no_set(self):
        self.get_data_from_database('booking_entry', index=0)
        if not self.data_list:
            self.bill_no_var.set(1)
        else:
            self.bill_no_var.set((int(self.data_list[-1])+1))

    def name_entry_state(self,state):
        self.billno_entry['state']=state
        self.name_entry['state']=state
        self.vehical_entry['state']=state
        self.date['state']=state
        self.source_entry['state']=state
        self.destination_entry['state']=state
        self.freight_entry['state']=state
        self.majuri_entry['state']=state
        self.adv_amount_entry['state']=state
        self.a_p_mode_entry['state']=state
        self.balance_entry['state']=state
        self.tapal_entry['state']=state
        self.total_entry['state']=state

    def holding_entry_state(self,state):
        self.h_start_d['state']=state
        self.h_end_d['state']=state
        self.holding_entry['state']=state

    def press_tab(self,event, **kwargs):
        if self.des:
            self.destroye_listbox()


        table_name = kwargs.get('table_name','ledger_entry')
        var = kwargs.get('var',self.name_var)

        indx = kwargs.get('indx',1)
        self.get_data_from_database(tabel_name=table_name,index=indx)
        if var.get() and var.get() not in self.data_list:
            response = messagebox.askyesno("Question", "Do you want to Save This Name!")
            if response:
                if table_name == 'ledger_entry':
                    l_root = Toplevel()
                    l_obj = LedgerEntry(l_root)
                    l_root.mainloop()
                elif table_name == 'vehicle_entry':
                    query = f"INSERT INTO `royal_transport`.`vehicle_entry` (`vehicle_number`) VALUES ('{self.vehicle_var.get()}');"
                    # print(query)
                    if execute_query(query=query):
                        messagebox.showinfo('MESSAGE', 'SAVED SUCCEFUllY!')
                elif table_name == 'city_entry':
                    query = f"INSERT INTO `royal_transport`.`city_entry` (`city_name`) VALUES ('{var.get()}');"
                    # print(query)
                    if execute_query(query=query):
                        messagebox.showinfo('MESSAGE', 'SAVED SUCCEFUllY!')
                        self.get_data_from_database(tabel_name='city_entry',index=1)
                        self.source_entry['values']=self.data_list
                        self.destination_entry['values'] = self.data_list
                elif table_name == 'payment_mode':
                    query = f"INSERT INTO `royal_transport`.`payment_mode` (`mode`) VALUES ('{var.get()}');"
                    # print(query)
                    if execute_query(query=query):
                        messagebox.showinfo('MESSAGE', 'SAVED SUCCEFUllY!')

    def create_listbox(self,event,**kwargs):
        width = kwargs.get('width',380)
        x = kwargs.get('x',300)
        y = kwargs.get('y', 300)
        var = kwargs.get('var',self.name_var)
        table_name = kwargs.get('table_name',None)
        obj = kwargs.get('obj',None)
        px = kwargs.get('px', 300)
        py = kwargs.get('py', 70)
        if self.disabled:
            return
        self.get_data_from_database(tabel_name=table_name,index=1)

        if self.des:
            self.destroye_listbox()
        self.listbox = Listbox(self.root, height=10, font=("Helvetica", 13), bd=1, relief=SOLID, highlightthickness=0,
                               bg='white', highlightcolor='black')
        self.listbox.place(x=x, y=y, width=width)
        self.des = True
        self.listbox.bind('<Return>', partial(self.select_value,var=var,obj=obj))
        self.listbox.bind('<Double-Button-1>', partial(self.select_value,var=var,obj=obj))
        self.listbox.bind('<Tab>', partial(self.select_value,var=var,obj=obj))
        obj.focus()
        self.search(var=var)


        self.poligon = Button_Image(self,img=r"traonsport_images/poligon_down.png", w=25, h=20)
        self.poligon_btn = Button(self.root,image=self.poligon,borderwidth=0,
                                     activebackground="white", background="white",
                                  foreground="white",compound=CENTER,command=self.destroye_listbox)
        self.poligon_btn.place(x=px, y=py, height=34)

        # print(self.des)

    def search(self,**kwargs):
        var = kwargs.get('var',self.name_var)
        obj = kwargs.get('obj',self.source_entry)
        search_str = var.get()  # user entered string
        if self.des:
            self.listbox.delete(0, END)  # Delete all elements of Listbox
            for i,element in enumerate(sorted(self.data_list)):
                if search_str in element:
                # if (re.match(search_str, element, re.IGNORECASE)):
                    self.listbox.insert(END,element)  # add matching options to Listbox
        else:
            self.get_data_from_database('city_entry', index=1)
            data = [dat for dat in self.data_list if var.get() in dat]
            if str(var) == 'PY_VAR3':
                self.source_entry['values'] = data
            elif str(var) == 'PY_VAR4':
                self.destination_entry['values'] = data

    def destroye_listbox(self, *event):
        if self.des:
            self.listbox.destroy()
            self.poligon_btn.destroy()
            self.des = False

    def select_value(self, my_widget,var,obj):  # On selection of option
        # print('select value')
        my_w = my_widget.widget
        index = int(my_w.curselection()[0])  # position of selection
        value = my_w.get(index)  # selected value
        var.set(value)  # set value for string variable of Entry
        self.listbox.delete(0, END)  # Delete all elements of Listbox
        self.destroye_listbox()
        obj.focus_set()

    def press_down(self,key,event):  # down arrow is clicked
        if key == 'name':
            self.create_listbox(width=490,x=195,y=195,table_name='ledger_entry',
                                     px=660,py=160,var=self.name_var,obj=self.name_entry,event='')
        elif key == 'vehicle':
            self.create_listbox( width = 280, x = 1150, y = 195, var = self.vehicle_var,
            table_name = 'vehicle_entry', px = 1415, py = 160, obj = self.vehical_entry,event='')


        if self.des:
            self.listbox.focus()  # move focus to Listbox
            self.listbox.selection_set(0)  # select the first option

    def trace_data(self,*args):
        var = args[0]
        to_uppercase(var)
        self.search(var=var)

    def get_data_from_database(self,tabel_name,index):
        self.data = fetch_data(table_name=tabel_name)
        if index=='all':
            self.data_list = self.data
        else:
            self.data_list = [dat[index] for dat in self.data]

        # print(self.data_list)
        # print(self.name_list)

    def set_bal_value(self,key,event):
        if key == 'freight' and self.freight_entry.get():
            if self.freight_entry.get()=='':
                val = self.hold_amnt_var.get() + self.majuri_var.get() - self.adv_var.get()
                self.bal_var.set(val)
            else:
                val = self.freight_var.get() + self.hold_amnt_var.get() + self.majuri_var.get() - self.adv_var.get()
                self.bal_var.set(val)

        elif self.adv_amount_entry.get()=='' and key =='advance':
            self.bal_var.set(self.freight_var.get())

        elif key == 'advance' and self.adv_amount_entry.get():
            val = self.freight_var.get() - self.adv_var.get()
            self.bal_var.set(val)

        elif key == 'holding' and self.holding_entry.get().isdigit():
            val = self.freight_var.get() + self.hold_amnt_var.get()
            if self.majuri_entry.get().isdigit():
                val+=self.majuri_var.get()
            if self.adv_var.get():
                val= val - self.adv_var.get()
            self.bal_var.set(val)

        elif key =='majuri' and self.majuri_entry.get().isdigit():
            val = self.freight_var.get() +  self.majuri_var.get()
            if self.holding_entry.get().isdigit():
                val+=self.hold_amnt_var.get()
            if self.adv_var.get():
                val = val - self.adv_var.get()
            self.bal_var.set(val)

    def calculate_balance_and_set(self,event):
        # print(self.freight_entry.get().isdigit())
        if self.freight_entry.get().isdigit():
            fre_val = self.freight_var.get()
        else:
            fre_val = 0

        if self.holding_entry.get().isdigit():
            h_val = self.hold_amnt_var.get()
        else:
            h_val = 0

        if self.majuri_entry.get().isdigit():
            m_val = self.majuri_var.get()
        else:
            m_val = 0

        if self.adv_amount_entry.get().isdigit():
            a_val = self.adv_var.get()
        else:
            a_val = 0

        val = fre_val + h_val + m_val - a_val
        # print(val)
        self.bal_var.set(val)

        if self.tapal_entry.get().isdigit():
            t_val = self.tapal_var.get()
        else:
            t_val = 0

        tapal_val = val - t_val
        self.total_bal_var.set(tapal_val)

    def save_booking_data_into_db(self):
        if self.freight_entry.get() == '':
            self.freight_entry.insert(END, 0)
        if self.name_var.get() and self.vehicle_var.get() and self.source_var.get() and self.dest_var.get() and self.freight_var.get():
            self.get_data_from_database(tabel_name='booking_entry',index=0)
            if self.bill_no_var.get() not in self.data_list:
                response = messagebox.askyesno("Question", "Do you want to Save This BOOKING!")
                if response:
                    if self.adv_amount_entry.get()=='':
                        self.adv_amount_entry.insert(END,0)
                    if self.tapal_entry.get()=='':
                        self.tapal_entry.insert(END,0)
                    if self.majuri_entry.get()=='':
                        self.majuri_entry.insert(END,0)

                    query= f"""
                                INSERT INTO `royal_transport`.`booking_entry` (`date`, `name`, `vehicle_no`, `src_dest`,
                                 `freight`, `majuri_amount`, `adv_date`, `adv_amount`, `adv_type`, `balance`,`tapal`, `total_balance`)
                                  VALUES (STR_TO_DATE('{self.date.get()}', '%d/%m/%Y'), '{self.name_var.get()}', '{self.vehicle_var.get()}', '{self.source_var.get()+ ' - '+self.dest_var.get()}', 
                                  '{self.freight_entry.get()}', '{self.majuri_var.get()}', '{self.date.get()}','{self.adv_var.get()}',
                                  '{self.adv_mode.get()}','{self.balance_entry.get()}','{self.tapal_var.get()}', '{self.total_bal_var.get()}');
                                """
                    # print(query)
                    if execute_query(query=query):
                        messagebox.showinfo('MESSAGE', 'SAVED SUCCEFUllY!')
            else:
                response = messagebox.askyesno("Question", "Do you want to UPDATE This Data!")
                if response:
                    if self.adv_amount_entry.get()=='':
                        self.adv_amount_entry.insert(END,0)
                    if self.tapal_entry.get()=='':
                        self.tapal_entry.insert(END,0)
                    if self.majuri_entry.get()=='':
                        self.majuri_entry.insert(END,0)

                    query = f"""
                            UPDATE `royal_transport`.`booking_entry` SET `date` = STR_TO_DATE('{self.date.get()}', '%d/%m/%Y'), 
                            `name` = '{self.name_var.get()}',`vehicle_no` = '{self.vehicle_var.get()}', 
                            `src_dest` = '{self.source_var.get()} - {self.dest_var.get()}', `freight` = '{self.freight_var.get()}',
                            `hld_date` = '{self.h_start_d.get()} to {self.h_end_d.get()}', `hld_amount` = '{self.hold_amnt_var.get()}', 
                            `majuri_amount` = '{self.majuri_var.get()}',`adv_date` = '{self.date.get()}', `adv_amount` = '{self.adv_var.get()}',
                             `adv_type` = '{self.adv_mode.get()}',  `balance` = '{self.bal_var.get()}',`tapal` = '{self.tapal_var.get()}', 
                             `total_balance` = '{self.total_bal_var.get()}'  WHERE (`bill_no` = '{self.bill_no_var.get()}');
                            """

                    # print(query)
                    if execute_query(query=query):
                        messagebox.showinfo('MESSAGE', 'SAVED SUCCEFUllY!')
        else:
            messagebox.showerror('ERROR',"Please Enter Mandotory Entries!")

    def clear_all_entry(self):
        response = messagebox.askyesno("Question", "Do you want to Clear All Entry!")
        if response:
            self.tree_destroy()
            self.name_entry_state(state='normal')
            self.holding_design(state='normal')
            self.bill_no_set()
            self.name_var.set('')
            self.vehicle_var.set('')
            self.source_var.set('')
            self.dest_var.set('')
            self.freight_var.set(0)
            self.hold_amnt_var.set(0)
            self.majuri_var.set(0)
            self.adv_var.set(0)
            self.adv_mode.set('')
            self.bal_var.set(0)
            self.tapal_var.set(0)
            self.total_bal_var.set(0)

            self.holding_entry_state(state='disabled')
            self.disabled=False


    def tree_design(self,key):
        columns = ('bill_no','date','vehicle_no','src_des','balance')
        self.h_tree = ttk.Treeview(self.root,columns=columns ,show='headings',selectmode='browse')

        self.h_tree.column("bill_no", anchor=CENTER,width=60,minwidth=60)
        self.h_tree.column("date", anchor=CENTER,width=130,minwidth=130)
        self.h_tree.column("vehicle_no", anchor=CENTER,width=160,minwidth=160)
        self.h_tree.column("src_des", anchor=CENTER,width=250,minwidth=250)
        self.h_tree.column("balance", anchor=CENTER, width=100, minwidth=100)


        self.h_tree.heading("bill_no", text="BILL NO")
        self.h_tree.heading("date", text="DATE")
        self.h_tree.heading("vehicle_no", text="VEHICLE NO")
        self.h_tree.heading("src_des", text="ROUTE")
        self.h_tree.heading("balance", text="BALANCE")


        self.h_tree.tag_configure('T', font=("times new roman",15))

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Treeview.Heading', background="#2664AD",foreground="white",
                        font=("times new roman", 11,"bold"),releif=FLAT)
        self.style.map('Treeview.Heading',background=[('active','#2664AD')])

        self.h_tree.place(x=337,y=310,width=860,height=270)
        self.vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.h_tree.yview)
        self.vsb.place(x=1182, y=340, height=240)
        self.h_tree.configure(yscrollcommand=self.vsb.set)
        self.hld_tr =True
        self.h_tree.bind("<Double-1>",partial(self.populate_value_entrybox,key))
        self.h_tree.bind("<Return>", partial(self.populate_value_entrybox,key))

    def add_holdings(self):
        self.get_data_from_database(tabel_name='booking_entry',index=2)
        if self.name_entry.get() and self.name_entry.get() in self.data_list:
            response = messagebox.askyesno("Question", "Do you want to ADD Holdings!")
            if response:
                query = fr"""SELECT bill_no,date,vehicle_no,src_dest,balance FROM royal_transport.booking_entry 
                            where name='{self.name_entry.get()}' and hld_amount=0;"""
                self.populate_treeview(query=query,key='holding')
        else:
            messagebox.showerror('ERROR',"Booking is Not available with this Name!")

    def add_open(self):
        self.get_data_from_database(tabel_name='booking_entry',index=2)
        name = set(self.data_list)
        self.get_data_from_database(tabel_name='booking_entry', index=3)
        vehicle = set(self.data_list)
        if self.name_entry.get() and self.name_entry.get() in name:
            response = messagebox.askyesno("Question", "Do you want to OPEN BOOKING!")
            if response:
                query = fr"""SELECT bill_no,date,vehicle_no,src_dest,balance FROM royal_transport.booking_entry
                            where name='{self.name_entry.get()}';"""
                if self.vehicle_var.get() and self.vehicle_var.get() in vehicle:
                    query = fr"""SELECT bill_no,date,vehicle_no,src_dest,balance FROM royal_transport.booking_entry
                                where name='{self.name_entry.get()}' and vehicle_no='{self.vehicle_var.get()}';"""
                self.populate_treeview(query=query,key='open')
        else:
            messagebox.showerror('ERROR',"Booking is Not available with this Name!")

    def last_bill_populate(self):
        self.clear_all_entry()
        self.get_data_from_database('booking_entry',index='all')
        data = self.data_list[-1]
        self.set_entry_value_from_db(data=data)

        self.name_entry_state(state='disabled')
        # self.billing_entry_state(state='disabled')
        self.holding_entry_state(state='disabled')
        self.disabled = True

    def set_entry_value_from_db(self,data):
        self.bill_no_var.set(data[0])
        self.name_var.set(data[2])
        self.vehicle_var.set(data[3])
        s_d = data[4].split('-')
        self.source_var.set(s_d[0])
        self.dest_var.set(s_d[1])
        self.freight_var.set(data[5])
        self.hold_amnt_var.set(data[7])
        self.majuri_var.set(data[8])
        self.adv_var.set(data[10])
        self.adv_mode.set(data[11])
        self.bal_var.set(data[12])
        self.tapal_var.set(data[14])
        self.total_bal_var.set(data[15])


        self.date['state'] = 'normal'
        self.date.set_date(data[1])
        self.date['state'] = 'readonly'



        if data[6]:
            h_d = data[6].split(' to ')
            self.h_start_d['state']='normal'
            self.h_end_d['state']='normal'
            self.h_start_d.set_date(h_d[0])
            self.h_end_d.set_date(h_d[1])
            self.h_start_d['state']='readonly'
            self.h_end_d['state']='readonly'

    def populate_treeview(self,query,key):
        self.name_entry_state(state='disabled')
        self.holding_entry_state(state='disabled')
        data = fetch_colum_data(query=query)
        # print(data)
        if data:
            self.tree_design(key=key)
            self.h_tree.delete(*self.h_tree.get_children())  # Clear the Treeview before repopulating
            for record in data:
                self.h_tree.insert("", "end", values=record, tags='T')
        else:
            messagebox.showerror('INFO','There is no holding bills is there with This Name!')

    def populate_value_entrybox(self,key,event):
        selected_item = self.h_tree.selection()
        if selected_item:
            self.name_entry_state(state='disabled')
            self.holding_design(state='normal')

            values = self.h_tree.item((selected_item[0]), "values")
            query = f"""
                    SELECT * FROM royal_transport.booking_entry where bill_no='{values[0]}';
                    """
            data = fetch_colum_data(query=query)
            # print(data)
            self.set_entry_value_from_db(data=data[0])
            self.tree_destroy()
            if key=='open':
                self.holding_entry_state(state='disabled')

    def tree_destroy(self):
        if self.hld_tr:
            self.style.theme_use('vista')
            self.h_tree.destroy()
            self.vsb.destroy()
            self.hld_tr = False

    def edit_data(self):
        self.tree_destroy()
        if self.name_entry.get():
            response = messagebox.askyesno("Question", "Do you want to EDIT This Data!")
            if response:
                self.name_entry_state(state='normal')
                if self.holding_entry.get()!='None':
                    self.holding_entry_state(state='normal')

    def add_holdings_into_db(self,data):

        if self.holding_entry.get()!='None':
            response = messagebox.askyesno("Question", "Do you want to Add Holdings!")
            if response:
                h_date = self.h_start_d.get() + ' to ' + self.h_end_d.get()
                amount = self.hold_amnt_var.get() + self.majuri_var.get() + data[-1]
                query = f"""
                        UPDATE `royal_transport`.`booking_entry` SET `hld_date` = '{h_date}',
                         `hld_amount` = '{self.hold_amnt_var.get()}', `majuri_amount` = '{self.majuri_var.get()}', `balance` = '{amount}' WHERE (`bill_no` = '{data[0]}');
                        """
                # print(query)
                execute_query(query=query)
                messagebox.showinfo('MESSAGE', 'SAVED SUCCEFUllY!')
                query = fr"""
                                    SELECT * FROM royal_transport.booking_entry where bill_no='{data[0]}';
                                    """
                data = fetch_colum_data(query=query)
                # print(data)
                self.holding_design(state='readonly')
                self.set_entry_value_from_db(data=data[0])



# root = Tk()
# booking_object=Booking(root)
# root.mainloop()



