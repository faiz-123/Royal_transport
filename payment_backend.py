from genral_methods import *

def create_listbox(self, event, **kwargs):
    width = kwargs.get('width', 380)
    x = kwargs.get('x', 300)
    y = kwargs.get('y', 300)
    var = kwargs.get('var', self.name_var)
    table_name = kwargs.get('table_name', None)
    obj = kwargs.get('obj', None)
    px = kwargs.get('px', 300)
    py = kwargs.get('py', 70)
    font_size = kwargs.get('font_size', 10)
    index = kwargs.get('index', 1)
    query = kwargs.get('query', None)
    data = kwargs.get('data', None)

    if data:
        self.data_list = data
    else:
        self.data_list = set(get_data_from_database(table_name, index=index))

    destroye_listbox(self, event='')
    self.listbox = Listbox(self.root, height=font_size, font=("Helvetica", 10), bd=1, relief=SOLID,
                           highlightthickness=0,
                           bg='white', highlightcolor='black')
    self.listbox.place(x=x, y=y, width=width)
    self.des = True
    self.listbox.bind('<Return>', partial(select_value, self, var=var, obj=obj))
    self.listbox.bind('<Double-Button-1>', partial(select_value, self, var=var, obj=obj))
    self.listbox.bind('<Tab>', partial(select_value, self, var=var, obj=obj))
    obj.focus_set()
    search(self, var=var)

    self.poligon = Button_Image(self, img=r"traonsport_images/poligon_down.png", w=25, h=20)
    self.poligon_btn = Button(self.root, image=self.poligon, borderwidth=0,
                              activebackground="white", background="white",
                              foreground="white", compound=CENTER, command=partial(destroye_listbox, self, event=''))
    self.poligon_btn.place(x=px, y=py,height=33,width=25)

def create_name_list(self,event):
    if not self.payment_mode.get():
        messagebox.askretrycancel('ERROR','Please Enter Payment Mode CASH / BANK!')
        return
    if not self.des:
        create_listbox(self, width = 345, x = 225, y = 133, table_name = 'ledger_entry',
        px = 546, py = 97, var = self.name_var, obj = self.name_entry, event = '')

def create_vehicle_list(self,event):
    if self.name_var.get():
        query = f"SELECT distinct vehicle_no FROM royal_transport.booking_entry where name='{self.name_var.get()}';"
        data = fetch_colum_data(query=query)
        data = [dat[0] for dat in data]
        create_listbox(self, width=260, x=740, y=133,var=self.vehicle_var,table_name='vehicle_entry',
                       px=972, py=97,obj=self.vehical_entry,data=data, event='')

def press_down(self,event,key):
    if key=='name':
        create_name_list(self,event='')
    elif key=='vehicle':
        create_vehicle_list(self,event='')
    if self.des:
        self.listbox.focus()  # move focus to Listbox
        self.listbox.selection_set(0)

def get_data_from_database(table_name,index):
    data = fetch_data(table_name=table_name)
    if index=='all':
        data_list = data
    else:
        data_list = [dat[index] for dat in data]

    return data_list

def press_tab(self,event, **kwargs):
    data = get_data_from_database(table_name='payment_mode',index=1)
    if self.payment_mode.get() and self.payment_mode.get() not in data:
        response = messagebox.askyesno("Question", "Do you want to Save This Name!")
        if response:
            query = f"INSERT INTO `royal_transport`.`payment_mode` (`mode`) VALUES ('{self.payment_mode.get()}');"
            # print(query)
            if execute_query(query=query):
                messagebox.showinfo('MESSAGE','SAVED SUCCEFUllY!')

def search(self,var):

    search_str = var.get()  # user entered string
    if self.des:
        self.listbox.delete(0, END)  # Delete all elements of Listbox
        for i,element in enumerate(sorted(self.data_list)):
            if search_str in element:
                self.listbox.insert(END,element)  # add matching options to Listbox

def destroye_listbox(self,event):
    if self.des:
        self.listbox.destroy()
        self.poligon_btn.destroy()
        self.des = False

def select_value(self, my_widget,var,obj):  # On selection of option
    my_w = my_widget.widget
    index = int(my_w.curselection()[0])  # position of selection
    value = my_w.get(index)  # selected value
    var.set(value)  # set value for string variable of Entry
    self.listbox.delete(0, END)  # Delete all elements of Listbox
    obj.focus_set()

    if self.des:
        destroye_listbox(self,event='')

    if self.name_var.get() and not self.vehicle_var.get():
        if self.name_var.get():
            booking_query = f"SELECT sum(total_balance) FROM royal_transport.booking_entry where name='{self.name_var.get()}';"
            balance = fetch_colum_data(booking_query)
            if balance[0]:
                self.balance_var.set(balance[0][0])
                self.total_balance = balance[0][0]
                self.balance_label.config(text=balance[0][0])


    elif self.name_var.get() and self.vehicle_var.get():
        booking_query = f"SELECT sum(total_balance) FROM royal_transport.booking_entry wher" \
                            f"e name='{self.name_var.get()}' and vehicle_no='{self.vehicle_var.get()}';"
        balance = fetch_colum_data(booking_query)
        if balance[0]:
            self.balance_var.set(balance[0][0])
            self.total_balance = balance[0][0]
            self.balance_label.config(text=balance[0][0])
    self.balance_entry['state']='readonly'

def trace_data(self,*args):
    var = args[0]
    to_uppercase(var)
    search(self,var=var)

def widget_bind(self,event):
    if event=='name':
        self.name_var.trace('w', partial(trace_data, self, self.name_var))
        self.name_entry.bind('<Button-1>', partial(create_name_list, self))
        self.name_entry.bind('<KeyPress>', partial(create_name_list, self))
        self.name_entry.bind('<Down>', partial(press_down, self, key='name'))
        self.name_entry.bind('<Tab>', partial(destroye_listbox, self))
    elif event=='vehicle':
        self.vehicle_var.trace('w', partial(trace_data, self, self.vehicle_var))
        self.vehical_entry.bind('<Button-1>', partial(create_vehicle_list,self))
        self.vehical_entry.bind('<KeyPress>', partial(create_vehicle_list,self))
        self.vehical_entry.bind('<Down>', partial(press_down,self,key='vehicle'))
        self.vehical_entry.bind('<Tab>',partial(destroye_listbox,self))

def subtract_balance(self,event):
    if self.total_balance is None:
        self.amount_entry['state'] = 'disabled'
        return

    elif self.amount_entry.get().isdigit() and self.amount_var.get():
        data = self.total_balance - self.amount_var.get()
        if data<0:
            self.balance_var.set(self.total_balance)
        else:
            self.balance_var.set(data)
    elif self.amount_entry.get()=="":
        self.balance_var.set(self.total_balance)

def frameDesign(self):

    self.wr = Frame(self.root,bg='white')
    mycan = Canvas(self.wr,bg='white',width=1450)
    mycan.pack(side=LEFT, fill=Y)
    # mycan.place(x=0,y=0,width=500,height=490)

    self.yscr = Scrollbar(self.wr, orient='vertical', command=mycan.yview)
    self.yscr.pack(side=RIGHT, fill="y")
    mycan.configure(yscrollcommand=self.yscr.set)

    mycan.bind('<Configure>', lambda e: mycan.configure(scrollregion=mycan.bbox('all')))

    self.frame = Frame(mycan,bg='white')
    mycan.create_window((0, 0), window=self.frame, anchor="nw")
    # wr.pack(side=LEFT,fill='both')
    self.wr.place(x=28, y=230,width=1470,height=498)

def get_data_from_db(self,key):
    if key =='ADVANCE':
        query = ""
        if self.name_var.get() and not self.vehicle_var.get():
            query = f"SELECT bill_no,vehicle_no,src_dest,balance,adv_amount,total_balance FROM royal_transport.booking_entry where name='{self.name_var.get()}' and adv_amount=0;"
        elif self.name_var.get() and self.vehicle_var.get():
            query = f"SELECT bill_no,vehicle_no,src_dest,balance,adv_amount,total_balance FROM royal_transport.booking_entry where name='{self.name_var.get()}' and vehicle_no='{self.vehicle_var.get()}' and adv_amount=0;"
        # print(query)
        data = fetch_colum_data(query=query)
        return data

    elif key=='BALANCE':
        query = ""
        if self.name_var.get() and not self.vehicle_var.get():
            query = f"SELECT bill_no,vehicle_no,src_dest,balance,balance_paid,total_balance FROM royal_transport.booking_entry where name='{self.name_var.get()}' and total_balance!=0;"
        elif self.name_var.get() and self.vehicle_var.get():
            query = f"SELECT bill_no,vehicle_no,src_dest,balance,balance_paid,total_balance FROM royal_transport.booking_entry where name='{self.name_var.get()}' and vehicle_no='{self.vehicle_var.get()}' and total_balance!=0;"
        # print(query)
        data = fetch_colum_data(query=query)
        return data

    elif key == 'TAPAL':
        query = ""
        if self.name_var.get() and not self.vehicle_var.get():
            query = f"SELECT bill_no,vehicle_no,src_dest,balance,balance_paid,tapal,total_balance FROM royal_transport.booking_entry where name='{self.name_var.get()}' and tapal=0;"
        elif self.name_var.get() and self.vehicle_var.get():
            query = f"SELECT bill_no,vehicle_no,src_dest,balance,balance_paid,tapal,total_balance FROM royal_transport.booking_entry where name='{self.name_var.get()}' and vehicle_no='{self.vehicle_var.get()}' and tapal=0;"
        # print(query)
        data = fetch_colum_data(query=query)
        return data

#************ ADVANCE ******************************

def advance_payment_methods(self):
    self.adv_data = get_data_from_db(self, 'ADVANCE')
    self.t_bills = len(self.adv_data)
    self.t_bills_var.set(self.t_bills)
    self.t_bills_entry['state'] = 'readonly'
    self.image = PhotoImage(file=r"traonsport_images/adv_label.png")
    self.label = Label(self.root, image=self.image)
    self.label.place(x=765, y=210, anchor="center")
    frameDesign(self)
    for i, dat in enumerate(self.adv_data):
        adva_data_entries(self, i, dat)
        advance_state_readonly(self)

def adva_data_entries(self,i,dat):

    adv_paym = IntVar()
    self.adv_payment_amount.append(adv_paym)

    t_bal =IntVar()
    self.adv_total_payment.append(t_bal)

    self.adv_id = Label(self.frame,text=str(i+1),font=('times new roman',15,'bold'),bg='white',justify=CENTER)
    self.adv_id.grid(row=i,column=0,padx=10)

    self.adv_bill = Entry(self.frame, font=("times new roman", 15, "bold"), justify=CENTER, bd=5,width=10)
    self.adv_bill.grid(row=i,column=1,padx=12)

    self.adv_vehicle = Entry(self.frame, font=("times new roman", 13, "bold"), justify=CENTER, bd=5,width=25)
    self.adv_vehicle.grid(row=i,column=2,padx=10)

    self.adv_src_dest = Entry(self.frame, font=("times new roman", 12, "bold"), justify=CENTER, bd=5,width=40)
    self.adv_src_dest.grid(row=i, column=3, padx=10)

    self.adv_bal = Entry(self.frame, font=("times new roman", 15, "bold") ,justify=CENTER,fg='red' ,bd=5,width=20)
    self.adv_bal.grid(row=i, column=4, padx=10)

    self.adv_amount = Entry(self.frame, font=("times new roman", 15, "bold"),textvariable=adv_paym,justify=CENTER,fg='green', bd=5,width=20)
    self.adv_amount.grid(row=i, column=5, padx=10)
    self.adv_amount.bind('<KeyRelease>',partial(advance_total_entries,self,i))

    self.adv_t_b_amnt = Entry(self.frame, font=("times new roman", 15, "bold"),textvariable=t_bal,justify=CENTER, bd=5,width=18)
    self.adv_t_b_amnt.grid(row=i, column=6, padx=10)

    self.adv_bill.insert(0,dat[0])
    self.adv_vehicle.insert(0,dat[1])
    self.adv_src_dest.insert(0,dat[2])
    self.adv_bal.insert(0,dat[3])
    self.adv_t_b_amnt.delete(0,END)
    self.adv_t_b_amnt.insert(0,dat[5])

def advance_state_readonly(self):
    self.adv_bill['state'] = 'readonly'
    self.adv_vehicle['state'] = 'readonly'
    self.adv_src_dest['state'] = 'readonly'
    self.adv_bal['state'] = 'readonly'
    self.adv_t_b_amnt['state'] = 'readonly'

def advance_total_entries(self,i,event):
    try:
        if self.adv_payment_amount[i].get():
            data = self.adv_data[i][-1] - self.adv_payment_amount[i].get()
            self.adv_total_payment[i].set(data)
    except:
        self.adv_total_payment[i].set(self.adv_data[i][-1])

def advance_entries_set(self):
    if self.p_bills_entry.get().isdigit() and self.amount_entry.get().isdigit() and self.p_bills_var.get() and not self.p_bills_var.get() > self.t_bills:
        data = round(self.amount_var.get() / self.p_bills_var.get(), 2)
        for i in range(self.p_bills_var.get()):
            self.adv_payment_amount[i].set(data)
            new_bal = self.adv_data[i][-1] - data
            self.adv_total_payment[i].set(new_bal)

def advance_save_call(self):
    check_payment_entries(self.adv_payment_amount)
    data = [dat for dat in self.adv_payment_amount if dat.get()]
    if data:
        response = messagebox.askyesno("Question", "Do you want to Save ADVNACE Payment!")
        if response:
            sum =0
            booking_querys =[]
            total_amount =0
            tmp ={}
            for i in range(len(self.adv_payment_amount)):
                if self.adv_payment_amount[i].get() and self.adv_payment_amount[i].get()!='':
                    bill_no =self.adv_data[i][0]
                    amount = self.adv_payment_amount[i].get()
                    data = get_balance_db(bill_no)
                    balance = data[0] - amount
                    total = balance - data[1] - data[2]

                    tmp.update({bill_no:amount})
                    sum+=amount
                    update_query = f"UPDATE `royal_transport`.`booking_entry` SET `adv_date` = '{self.date.get()}', `adv_amount` = '{amount}', " \
                                       f"`adv_type` = '{self.payment_mode.get()}', `balance` = '{balance}', `total_balance` = '{total}' WHERE (`bill_no` = '{bill_no}');"

                    booking_querys.append(update_query)

            if not self.vehicle_var.get():
                self.vehicle_var.set(tmp)

            pay_query = f"""INSERT INTO `royal_transport`.`payment_entry` (`date`, `name`,`vehicle_no`, `amount`, `payment_mode` , `payment_type`) VALUES (STR_TO_DATE('{self.date.get()}', '%d/%m/%Y'),  '{self.name_var.get()}','{self.vehicle_var.get()}', '{sum}', '{self.payment_mode.get()}', '{self.type_var.get()}');"""
            booking_querys.append(pay_query)
            # print(booking_querys[-1])

            if booking_querys:
                for query in booking_querys:
                    execute_query(query)
                messagebox.showinfo('SUCCESS',"Payment Saved successfully ")
    else:
        messagebox.showerror("ERROR", "Payment Entry Not Given!")

#************ BALANCE ******************************

def bal_data_entries(self,i,dat):

    bal_paym = IntVar()
    self.bal_payment_amount.append(bal_paym)

    t_bal =IntVar()
    self.bal_total_payment.append(t_bal)


    self.bal_id = Label(self.frame,text=str(i+1),font=('times new roman',15,'bold'),bg='white',justify=CENTER)
    self.bal_id.grid(row=i,column=0,padx=5)

    self.bal_bill = Entry(self.frame, font=("times new roman", 15, "bold"), justify=CENTER, bd=5,width=10)
    self.bal_bill.grid(row=i,column=1,padx=8)

    self.bal_vehicle = Entry(self.frame, font=("times new roman", 13, "bold"), justify=CENTER, bd=5,width=20)
    self.bal_vehicle.grid(row=i,column=2,padx=10)

    self.bal_src_dest = Entry(self.frame, font=("times new roman", 12, "bold"), justify=CENTER, bd=5,width=38)
    self.bal_src_dest.grid(row=i, column=3, padx=10)

    self.bal = Entry(self.frame, font=("times new roman", 15, "bold") ,justify=CENTER,fg='red' ,bd=5,width=15)
    self.bal.grid(row=i, column=4, padx=10)

    self.bal_paid_amnt = Entry(self.frame, font=("times new roman", 15, "bold"),justify=CENTER, bd=5,width=15)
    self.bal_paid_amnt.grid(row=i, column=5, padx=10)

    self.bal_amount = Entry(self.frame, font=("times new roman", 15, "bold"),textvariable=bal_paym,justify=CENTER,fg='green', bd=5,width=17)
    self.bal_amount.grid(row=i, column=6, padx=5)
    self.bal_amount.bind('<KeyRelease>',partial(balance_total_entries,self,i))

    self.bal_t_b_amnt = Entry(self.frame, font=("times new roman", 15, "bold"),textvariable=t_bal,justify=CENTER, bd=5,width=15)
    self.bal_t_b_amnt.grid(row=i, column=7, padx=5)

    self.bal_bill.insert(0,dat[0])
    self.bal_vehicle.insert(0,dat[1])
    self.bal_src_dest.insert(0,dat[2])
    self.bal.insert(0,dat[3])
    self.bal_paid_amnt.insert(0,dat[4])
    self.bal_t_b_amnt.delete(0,END)
    self.bal_t_b_amnt.insert(0,dat[5])

def bal_state_readonly(self):
    self.bal_bill['state'] = 'readonly'
    self.bal_vehicle['state'] = 'readonly'
    self.bal_src_dest['state'] = 'readonly'
    self.bal['state'] = 'readonly'
    self.bal_paid_amnt['state'] = 'readonly'
    self.bal_t_b_amnt['state'] = 'readonly'

def balance_total_entries(self,i,event):
    try:
        if self.bal_payment_amount[i].get():
            data = self.bal_data[i][-1] - self.bal_payment_amount[i].get()
            self.bal_total_payment[i].set(data)
    except:
        self.bal_total_payment[i].set(self.bal_data[i][-1])

def balance_payment_methods(self):
    self.bal_data = get_data_from_db(self, 'BALANCE')
    self.t_bills = len(self.bal_data)
    self.t_bills_var.set(self.t_bills)
    self.t_bills_entry['state'] = 'readonly'
    self.image = PhotoImage(file=r"traonsport_images/bal_label.png")
    self.label = Label(self.root, image=self.image)
    self.label.place(x=765, y=210, anchor="center")
    frameDesign(self)
    for i, dat in enumerate(self.bal_data):
        bal_data_entries(self, i, dat)
        bal_state_readonly(self)

def balance_entries_set(self):
    if self.p_bills_entry.get().isdigit() and self.amount_entry.get().isdigit() and self.p_bills_var.get() and not self.p_bills_var.get() > self.t_bills:
        data = round(self.amount_var.get() / self.p_bills_var.get(), 2)
        for i in range(self.p_bills_var.get()):
            self.bal_payment_amount[i].set(data)
            new_bal = self.bal_data[i][-1] - data
            self.bal_total_payment[i].set(new_bal)

def balance_save_call(self):
    check_payment_entries(self.bal_payment_amount)
    data = [dat.get() for dat in self.bal_payment_amount if dat.get()]
    if data:
        response = messagebox.askyesno("Question", "Do you want to Save BALANCE Payment!")
        if response:
            sum =0
            balance_querys =[]
            total_amount =0
            tmp ={}
            for i in range(len(self.bal_payment_amount)):
                if self.bal_payment_amount[i].get() and self.bal_payment_amount[i].get()!='':
                    # print(self.bal_data[i],self.bal_payment_amount[i].get())
                    bill_no = self.bal_data[i][0]
                    amount = self.bal_payment_amount[i].get()
                    data = get_balance_db(bill_no)
                    tmp.update({bill_no:amount})
                    balance_paid = data[1] + amount
                    total_balance = data[0] - balance_paid - data[2]

                    query1 = f"UPDATE `royal_transport`.`booking_entry` SET `balance_paid` = '{balance_paid}', `total_balance` = '{total_balance}' WHERE (`bill_no` = '{bill_no}');"

                    balance_querys.append(query1)

                    sum += amount

            if not self.vehicle_var.get():
                self.vehicle_var.set(tmp)

            bal_query = f"INSERT INTO `royal_transport`.`payment_entry` (`date`, `name`, `vehicle_no`, `amount`, `payment_mode`, `payment_type`) VALUES (STR_TO_DATE('{self.date.get()}', '%d/%m/%Y'), '{self.name_var.get()}', '{self.vehicle_var.get()}', '{sum}', '{self.payment_mode.get()}', '{self.type_var.get()}');"
            balance_querys.append(bal_query)

            if balance_querys:
                for query in balance_querys:
                    execute_query(query)
                messagebox.showinfo('SUCCESS', "Payment Saved successfully ")
    else:
        messagebox.showerror("ERROR", "Payment Entry Not Given!")

#************ TAPAL ******************************

def tapal_data_entries(self,i,dat):

    tapal_paym = IntVar()
    self.tapal_payment_amount.append(tapal_paym)

    t_bal =IntVar()
    self.tapal_total_balance.append(t_bal)

    self.tapal_id = Label(self.frame,text=str(i+1),font=('times new roman',15,'bold'),bg='white',justify=CENTER)
    self.tapal_id.grid(row=i,column=0,padx=5)

    self.tapal_bill = Entry(self.frame, font=("times new roman", 15, "bold"), justify=CENTER, bd=5,width=10)
    self.tapal_bill.grid(row=i,column=1,padx=8)

    self.tapal_vehicle = Entry(self.frame, font=("times new roman", 13, "bold"), justify=CENTER, bd=5,width=20)
    self.tapal_vehicle.grid(row=i,column=2,padx=10)

    self.tapal_src_dest = Entry(self.frame, font=("times new roman", 12, "bold"), justify=CENTER, bd=5,width=38)
    self.tapal_src_dest.grid(row=i, column=3, padx=10)

    self.tapal_bal = Entry(self.frame, font=("times new roman", 15, "bold") ,justify=CENTER,fg='red' ,bd=5,width=15)
    self.tapal_bal.grid(row=i, column=4, padx=10)

    self.tapal_bal_paid = Entry(self.frame, font=("times new roman", 15, "bold") ,justify=CENTER,fg='red' ,bd=5,width=15)
    self.tapal_bal_paid.grid(row=i, column=5, padx=10)

    self.tapal_amount = Entry(self.frame, font=("times new roman", 15, "bold"),textvariable=tapal_paym,justify=CENTER, bd=5,width=17)
    self.tapal_amount.grid(row=i, column=6, padx=10)
    self.tapal_amount.bind('<KeyRelease>',partial(tapal_total_entries,self,i))

    self.tapal_t_b_amnt = Entry(self.frame, font=("times new roman", 15, "bold"),textvariable=t_bal,justify=CENTER, bd=5,width=15)
    self.tapal_t_b_amnt.grid(row=i, column=7, padx=10)
    # print(dat)
    self.tapal_bill.insert(0,dat[0])
    self.tapal_vehicle.insert(0,dat[1])
    self.tapal_src_dest.insert(0,dat[2])
    self.tapal_bal.insert(0,dat[3])
    self.tapal_bal_paid.insert(0,dat[4])
    self.tapal_t_b_amnt.delete(0,END)
    self.tapal_t_b_amnt.insert(0,dat[6])

def tapal_state_readonly(self):
    self.tapal_bill['state'] = 'readonly'
    self.tapal_vehicle['state'] = 'readonly'
    self.tapal_src_dest['state'] = 'readonly'
    self.tapal_bal['state'] = 'readonly'
    self.tapal_t_b_amnt['state'] = 'readonly'

def tapal_payment_methods(self):
    self.tapal_data = get_data_from_db(self, 'TAPAL')
    self.t_bills = len(self.tapal_data)
    self.t_bills_var.set(self.t_bills)
    self.t_bills_entry['state'] = 'readonly'
    self.image = PhotoImage(file=r"traonsport_images/tapal_label.png")
    self.label = Label(self.root, image=self.image)
    self.label.place(x=765, y=210, anchor="center")
    frameDesign(self)
    for i, dat in enumerate(self.tapal_data):
        tapal_data_entries(self, i, dat)
        tapal_state_readonly(self)

def tapal_total_entries(self,i,event):
    try:
        if self.tapal_payment_amount[i].get():
            data = self.tapal_data[i][-1] - self.tapal_payment_amount[i].get()
            self.tapal_total_balance[i].set(data)
    except:
        self.tapal_total_balance[i].set(self.tapal_data[i][-1])

def tapal_entries_set(self):
    if self.p_bills_entry.get().isdigit() and self.amount_entry.get().isdigit() and self.p_bills_var.get() and not self.p_bills_var.get() > self.t_bills:
        data = round(self.amount_var.get() / self.p_bills_var.get(), 2)
        for i in range(self.p_bills_var.get()):
            self.tapal_payment_amount[i].set(data)
            new_bal = self.tapal_data[i][-1] - data
            self.tapal_total_balance[i].set(new_bal)

def tapal_save_call(self):
    check_payment_entries(self.tapal_payment_amount)
    data = [dat for dat in self.tapal_payment_amount if dat.get()]
    if data:
        response = messagebox.askyesno("Question", "Do you want to Save TAPAL Payment!")
        if response:
            sum =0
            tapal_querys =[]
            total_amount =0
            for i in range(len(self.tapal_payment_amount)):
                if self.tapal_payment_amount[i].get() and self.tapal_payment_amount[i].get()!='':
                    bill_no =self.tapal_data[i][0]
                    amount = self.tapal_payment_amount[i].get()
                    data = get_balance_db(bill_no)
                    total = amount - data[-1]
                    update_query = f"UPDATE `royal_transport`.`booking_entry` SET `tapal` = '{amount}', `total_balance` = '{total}' WHERE (`bill_no` = '{bill_no}');"
                    tapal_querys.append(update_query)

            if tapal_querys:
                for query in tapal_querys:
                    execute_query(query)
                messagebox.showinfo('SUCCESS',"Payment Saved successfully ")
    else:
        messagebox.showerror("ERROR", "Payment Entry Not Given!")

#************ GENRAL ******************************

def check_payment_entries(var):
    c = 0
    try:
        for i in range(len(var)):
            c = i
            var[i].get()
    except:
        var[c].set(0)

def get_balance_db(bill_no):
    query = f"SELECT balance,balance_paid,tapal,total_balance FROM royal_transport.booking_entry where bill_no='{bill_no}';"
    data = fetch_colum_data(query=query)[0]
    return data

def verify_amount_and_entries_values(self):
    flag=True
    if self.type_var.get() =='ADVANCE':
       if self.amount_entry.get().isdigit() and self.amount_var.get():
           data =[dat.get() for dat in self.adv_payment_amount if dat.get()]
           if not self.amount_var.get() == sum(data):
               messagebox.showerror("ERROR", f"Amount value '{self.amount_var.get()}' And Total Advance `{sum(data)}` Does Not Match!")
               flag=False

    elif self.type_var.get() =='BALANCE':

        if self.amount_entry.get().isdigit() and self.amount_var.get():
            data = [dat.get() for dat in self.bal_payment_amount if dat.get()]
            if not self.amount_var.get() == sum(data):
                messagebox.showerror("ERROR", f"Amount value '{self.amount_var.get()}' And Total Balance `{sum(data)}` Does Not Match!")
                flag=False

    elif self.type_var.get() =='TAPAL':
        if self.amount_entry.get().isdigit() and self.amount_var.get():
            data = [dat.get() for dat in self.tapal_payment_amount if dat.get()]
            if not self.amount_var.get() == sum(data):
                messagebox.showerror("ERROR", f"Amount value '{self.amount_var.get()}' And Total Tapal `{sum(data)}` Does Not Match!")
                flag=False

    return flag

def check_negative_value(self):
    flag =True
    if self.type_var.get() == 'ADVANCE':
        for i, dat in enumerate(self.adv_total_payment):
            if dat.get() < 0:
                messagebox.showerror('ERROR',f"Advance Amount '{self.adv_payment_amount[i].get()}' "
                                             f"Is More Than Total Advance '{self.adv_data[i][-1]}' \t\t\t"
                                             f"  In Bill No '{self.adv_data[i][0]}'")
                self.adv_payment_amount[i].set(0)
                self.adv_total_payment[i].set(self.adv_data[i][-1])
                flag=False

    elif self.type_var.get() == 'BALANCE':
        for i, dat in enumerate(self.bal_total_payment):
            if dat.get() < 0:
                messagebox.showerror('ERROR',f"Balance Amount '{self.bal_payment_amount[i].get()}' "
                                             f"Is More Than Total Balance '{self.bal_data[i][-1]}' \t\t\t"
                                             f" In Bill No '{self.bal_data[i][0]}'")
                self.bal_payment_amount[i].set(0)
                self.bal_total_payment[i].set(self.bal_data[i][-1])
                flag=False

    elif self.type_var.get() == 'TAPAL':
        for i, dat in enumerate(self.adv_total_payment):
            if dat.get() < 0:
                self.tapal_payment_amount[i].set(0)
                self.tapal_total_balance[i].set(self.tapal_data[i][-1])
                messagebox.showerror('ERROR',f"Tapal Amount '{self.tapal_payment_amount[i].get()}' "
                                             f"Is More Than Total Tapal '{self.tapal_data[i][-1]}' \t\t\t"
                                             f" In Bill No '{self.tapal_data[i][0]}'")

                flag=False
    return flag

