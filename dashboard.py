from genral_methods import *
from booking import *
from ledger_entry import *
from vehicle_entry import *
from payment import *
from cashbook import *
from settings import *


class Dashboard:
    def __init__(self,root,login_root):
        self.login_root = login_root
        self.root = root
        self.root.wm_iconbitmap("profit.ico")
        self.root.title("DASHBOARD")
        self.root.state("zoomed")
        self.root.resizable(False,False)

        Set_Bg_Image(self,image_path=r"traonsport_images/dashboard.png")

        img=r"icon/booking.png"
        self.booking_img= Button_Image(self,img=img,w=330,h=245)
        self.booking_button = Button(self.root,image=self.booking_img,
                        borderwidth=0,activebackground="#FFFFFF",background="#FFFFFF",foreground="#FFFFFF",cursor="hand2",compound=CENTER,
                                     command=partial(self.navigate_page,'booking'))
        self.booking_button.place(x=260,y=150)

        img=r"icon/transporter.png"
        self.transporter_img= Button_Image(self,img=img,w=280,h=190)
        self.transporter_button = Button(self.root,image=self.transporter_img,
                        borderwidth=0,activebackground="#FFFFFF",background="#FFFFFF",foreground="#FFFFFF",cursor="hand2",compound=CENTER
                                         ,command=partial(self.navigate_page,'transpoter'))
        self.transporter_button.place(x=605,y=150,width=345,height=250)

        img=r"icon/vehicle.png"
        self.vehicle_img= Button_Image(self,img=img,w=310,h=245)
        self.vehicle_button = Button(self.root,image=self.vehicle_img,
                        borderwidth=0,activebackground="#FFFFFF",background="#FFFFFF",foreground="#FFFFFF",cursor="hand2",compound=CENTER
                                     ,command=partial(self.navigate_page,'vehicle'))
        self.vehicle_button.place(x=965,y=150)

        img=r"icon/payment.png"
        self.payment_img= Button_Image(self,img=img,w=330,h=230)
        self.payment_button = Button(self.root,image=self.payment_img,
                        borderwidth=0,activebackground="#FFFFFF",background="#FFFFFF",foreground="#FFFFFF",cursor="hand2",compound=CENTER
                                     ,command=partial(self.navigate_page,'payment'))
        self.payment_button.place(x=260,y=470)

        img=r"icon/cashbook.png"
        self.cashbook_img= Button_Image(self,img=img,w=345,h=230)
        self.cashbook_button = Button(self.root,image=self.cashbook_img,
                        borderwidth=0,activebackground="#FFFFFF",background="#FFFFFF",foreground="#FFFFFF",cursor="hand2",compound=CENTER
                                      ,command=partial(self.navigate_page,'cashbook'))
        self.cashbook_button.place(x=605,y=470)

        img=r"icon/settings.png"
        self.settings_img= Button_Image(self,img=img,w=300,h=200)
        self.settings_button = Button(self.root,image=self.settings_img,
                        borderwidth=0,activebackground="#FFFFFF",background="#FFFFFF",foreground="#FFFFFF",cursor="hand2",
                                      compound=CENTER,command=partial(self.navigate_page,'setting'))
        self.settings_button.place(x=965,y=470,width=310,height=225)

        self.root.protocol("WM_DELETE_WINDOW", self.dashboard_exit)


    def dashboard_exit(self):
        sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=self.root)
        if sure == True:
            self.root.destroy()
            self.login_root.destroy()


    def navigate_page(self,object):
        if object == 'booking':
            self.root.withdraw()
            booking_root= Toplevel()
            booking_object = Booking(booking_root)
            booking_root.protocol("WM_DELETE_WINDOW", partial(self.exitt,booking_root))
            booking_root.mainloop()

        elif object == 'transpoter':
            self.root.withdraw()
            ledger_root = Toplevel()
            ledger_obj = LedgerEntry(ledger_root)
            ledger_root.protocol("WM_DELETE_WINDOW", partial(self.exitt,ledger_root))
            ledger_root.mainloop()

        elif object == 'vehicle':
            self.root.withdraw()
            trans_root = Toplevel()
            trans_obj = VehicleEntry(trans_root)
            trans_root.protocol("WM_DELETE_WINDOW", partial(self.exitt, trans_root))
            trans_root.mainloop()

        elif object == 'payment':
            self.root.withdraw()
            paym_root = Toplevel()
            paym_obj = Payment(paym_root)
            paym_root.protocol("WM_DELETE_WINDOW", partial(self.exitt, paym_root))
            paym_root.mainloop()
        elif object == 'cashbook':
            self.root.withdraw()
            cashbook_root = Toplevel()
            cahbook_obj = Cashbook(cashbook_root)
            cashbook_root.protocol("WM_DELETE_WINDOW", partial(self.exitt, cashbook_root))
            cashbook_root.mainloop()

        elif object == 'setting':
            self.root.withdraw()
            setting_root = Toplevel()
            setting_obj = Settings(setting_root)
            setting_root.protocol("WM_DELETE_WINDOW", partial(self.exitt, setting_root))
            setting_root.mainloop()

    def exitt(self,d_root):
        sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=d_root)
        if sure == True:
            d_root.destroy()
            self.root.deiconify()
            self.root.state('zoomed')




# root = Tk()
# dashboard_object=Dashboard(root)
# # root.protocol("WM_DELETE_WINDOW", partial(dashboard_object.exitt, root))
# root.mainloop()