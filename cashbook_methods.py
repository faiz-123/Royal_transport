from genral_methods import *


def Set_Label_Image(self,image_path):
    self.l_image = PhotoImage(file=image_path)
    self.label_image = Label(self.root, image=self.l_image,bg='white')
    self.label_image.place(x=25,y=215,width=1480,height=500)

def treeview_design(self):
    self.tree = ttk.Treeview(self.root, columns='', show='headings', selectmode='browse')
    set_style()
    self.tree.place(x=30, y=218, width=1470, height=435)

def return_str_dat(self,key):
    str_data = ''
    if key == 'cal':
        start_d = (datetime.strptime(self.start_d.get(), '%d/%m/%Y')).strftime('%Y/%m/%d')
        end_d = (datetime.strptime(self.end_d.get(), '%d/%m/%Y')).strftime('%Y/%m/%d')
        str_data += f" date BETWEEN '{start_d}'  AND '{end_d}'"
    elif key == 'month':
        month = (datetime.strptime(self.month_var.get(), "%B")).month
        year = datetime.now().year
        str_data += f"MONTH(date) = {month} AND YEAR(date) = {year}"

    return str_data

def convert_data_to_digit(self,data):
    output_data = []
    for dat in data:
        t = []
        for i in range(len(dat)):
            if str(dat[i]).isdigit() and not i == 0:
                t.append(format_currency(dat[i]))
            else:
                t.append(dat[i])
        output_data.append(tuple(t))

    return output_data

def booking_tree_column_set(self):
    colums = ('bill_no', 'date', 'v_no', 's_d', 'freight', 'holding', 'majuri', 'bhadu', 'advance', 'p_bal', 'tapal', 'balance')
    self.tree['columns'] = colums

    self.tree.column("bill_no", anchor=CENTER, width=10, minwidth=10)
    self.tree.column("date", anchor=CENTER, width=60, minwidth=10)
    self.tree.column("v_no", anchor=CENTER, width=60, minwidth=10)
    self.tree.column("s_d", anchor=CENTER, width=200, minwidth=200)
    self.tree.column("freight", anchor=CENTER, width=60, minwidth=10)
    self.tree.column("holding", anchor=CENTER, width=60, minwidth=10)
    self.tree.column("majuri", anchor=CENTER, width=60, minwidth=10)
    self.tree.column("bhadu", anchor=CENTER, width=60, minwidth=10)
    self.tree.column("advance", anchor=CENTER, width=60, minwidth=10)
    self.tree.column("p_bal", anchor=CENTER, width=60, minwidth=10)
    self.tree.column("tapal", anchor=CENTER, width=60, minwidth=10)
    self.tree.column("balance", anchor=CENTER, width=60, minwidth=10)

    self.tree.tag_configure('T', font=("times new roman", 13, 'bold'), foreground='black')
    self.tree.tag_configure('C', font=("times new roman", 13, 'bold'), foreground='red')

    self.tree.heading("bill_no", text="BILL NO")
    self.tree.heading("date", text="DATE")
    self.tree.heading("v_no", text="VEHICLE NO")
    self.tree.heading("s_d", text="SRC - DEST")
    self.tree.heading("freight", text="FREIGHT")
    self.tree.heading("holding", text="HOLDING")
    self.tree.heading("majuri", text="MAJURI")
    self.tree.heading("bhadu", text="BHADU")
    self.tree.heading("advance", text="ADVANCE")
    self.tree.heading("p_bal", text="PAID BALANCE")
    self.tree.heading("tapal", text="TAPAL")
    self.tree.heading("balance", text="BALANCE")

def payment_tree_column_set(self):
    colums = ('id', 'date', 'v_no', 'amount', 'p_mode', 'p_type')
    self.tree['columns'] = colums

    self.tree.column("id", anchor=CENTER, width=10, minwidth=10)
    self.tree.column("date", anchor=CENTER, width=60, minwidth=10)
    self.tree.column("v_no", anchor=CENTER, width=60, minwidth=10)
    self.tree.column("amount", anchor=CENTER, width=200, minwidth=200)
    self.tree.column("p_mode", anchor=CENTER, width=60, minwidth=10)
    self.tree.column("p_type", anchor=CENTER, width=60, minwidth=10)

    self.tree.tag_configure('T', font=("times new roman", 15, 'bold'), foreground='black')
    self.tree.tag_configure('AC', font=("times new roman", 13, 'bold'), foreground='green')

    self.tree.heading("id", text="ID")
    self.tree.heading("date", text="DATE")
    self.tree.heading("v_no", text="VEHICLE NO")
    self.tree.heading("amount", text="AMOUNT")
    self.tree.heading("p_mode", text="PAYMENT MODE")
    self.tree.heading("p_type", text="TYPE")

def total_entries(self,data):
    # print(data)
    self.total_bill = Entry(self.root,font=('times new roman',17,'bold'),justify=CENTER,bg='white',fg='red',bd=0)
    self.total_bill.place(x=40,y=670,width=65)

    self.total_freight = Entry(self.root,font=('times new roman',15,'bold'),justify=CENTER,bg='white',fg='black',bd=0)
    self.total_freight.place(x=562,y=670,width=152,height=28)

    self.total_bhadu = Entry(self.root,font=('times new roman',15,'bold'),justify=CENTER,bg='white',fg='blue',bd=0)
    self.total_bhadu.place(x=880,y=670,width=150,height=28)

    self.total_advance = Entry(self.root,font=('times new roman',15,'bold'),justify=CENTER,bg='white',fg='green',bd=0)
    self.total_advance.place(x=1045,y=670,width=145,height=28)

    self.total_p_bal = Entry(self.root,font=('times new roman',15,'bold'),justify=CENTER,bg='white',fg='green',bd=0)
    self.total_p_bal.place(x=1205,y=670,width=150,height=28)

    self.total_balance = Entry(self.root,font=('times new roman',15,'bold'),justify=CENTER,bg='white',fg='red',bd=0)
    self.total_balance.place(x=1368,y=670,width=125,height=28)

    if data:
        insert_booking_total_entries(self,data)

def insert_booking_total_entries(self,data):

    self.total_bill.delete(0, END)
    self.total_freight.delete(0, END)
    self.total_bhadu.delete(0, END)
    self.total_advance.delete(0, END)
    self.total_p_bal.delete(0, END)
    self.total_balance.delete(0, END)

    self.total_bill.insert(0, data[0])
    self.total_freight.insert(0, data[1])
    self.total_bhadu.insert(0, data[2])
    self.total_advance.insert(0, data[3])
    self.total_p_bal.insert(0, data[4])
    self.total_balance.insert(0, data[5])

def clear_total_entries(self):
    self.total_bill.delete(0, END)
    self.total_freight.delete(0, END)
    self.total_bhadu.delete(0, END)
    self.total_advance.delete(0, END)
    self.total_p_bal.delete(0, END)
    self.total_balance.delete(0, END)

def set_booking_values(self,str_data):
    query = f"""SELECT bill_no,DATE_FORMAT(date, '%d/%m/%y'),vehicle_no,src_dest,freight,hld_amount,majuri_amount,
                freight + hld_amount + majuri_amount as bhadu, adv_amount, balance_paid,tapal,total_balance 
                FROM royal_transport.booking_entry WHERE name='{self.name}' and {str_data} ORDER BY date ASC;
            """

    output = fetch_colum_data(query)
    data = convert_data_to_digit(self, output)

    self.tree.delete(*self.tree.get_children())

    for i, dat in enumerate(data):
        if output[i][5]:
            query = f"SELECT hld_date FROM royal_transport.booking_entry where bill_no={dat[0]};"
            h_date = fetch_colum_data(query=query)[0]
            h_date = h_date[0].split(' ')
            parent = self.tree.insert("", END, values=dat, tags='T')
            self.tree.insert(parent, END, values=("", "", "", "", '(' + h_date[0], h_date[1].upper(), h_date[2] + ')'),
                             tags='C')
        else:
            self.tree.insert("", END, values=dat, tags='T')

    # **************************************  Total *****************************************************

    query = f"""SELECT count(bill_no),sum(freight),sum(freight + hld_amount + majuri_amount),
                sum(adv_amount), sum(balance_paid),sum(total_balance)
                FROM royal_transport.booking_entry WHERE name='{self.name}' and {str_data} ORDER BY date ASC;"""

    data = fetch_colum_data(query)
    if data[0][0]:
        data = convert_data_to_digit(self, data)[0]
        insert_booking_total_entries(self, data)
    else:
        clear_total_entries(self)

def payment_total_entriy(self):

    self.payment_total_amount = Entry(self.root,font=('times new roman',18,'bold'),justify=CENTER,bg='white',fg='green',bd=0)
    self.payment_total_amount.place(x=698,y=670,width=350,height=28)

def insert_value_with_child(self,dat):
    data = dat
    parent = self.tree.insert("", END, values=(data[0], data[1], '', data[3], data[4], data[5]), tags='T')
    v_dict = eval(data[2])
    bills = v_dict.keys()
    for bl in bills:
        query = f"SELECT bill_no,DATE_FORMAT(date, '%d/%m/%y'),vehicle_no FROM royal_transport.booking_entry where bill_no={bl};"
        f_data = fetch_colum_data(query)[0]
        amoont=format_currency(v_dict[bl])
        self.tree.insert(parent, END, values=(f_data[0],f_data[1],f_data[2],amoont), tags='AC')

def set_payment_values(self,str_data):
    q = ''

    query = f"""SELECT id,date_format(date,'%d/%m/%y'),vehicle_no,amount,payment_mode,payment_type 
                FROM royal_transport.payment_entry where name='{self.name}' 
                and{q} {str_data} ORDER BY date ASC;
            """

    data = fetch_colum_data(query)
    data = convert_data_to_digit(self, data)

    self.tree.delete(*self.tree.get_children())
    for dat in data:
        if not is_dict_string(dat[2]):
            self.tree.insert("", END, values=dat, tags='T')
        else:
            insert_value_with_child(self, dat)

    query = f"SELECT sum(amount) FROM royal_transport.payment_entry WHERE name='{self.name}' and{q} {str_data} ORDER BY date ASC;"

    data = fetch_colum_data(query)
    if data[0][0]:
        data = format_currency(data[0][0])
        self.payment_total_amount.delete(0, END)
        self.payment_total_amount.insert(0, data)

def payment_radio_destroy(self):
    self.advance_radio.destroy()
    self.balance_radio.destroy()
    self.all_radio.destroy()
    self.p_radio_var.set('')

