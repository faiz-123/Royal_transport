from genral_methods import *
from fpdf import FPDF
from datetime import date
import webbrowser
from tkPDFViewer import tkPDFViewer
import os



table_data = []
name = ''
method =''


class PDF(FPDF):

    def header(self):

        #************ Set Image **********************************

        self.set_font('helvetica', 'BU', 25)
        self.set_text_color(0, 0, 0)
        self.set_xy(5,5)
        self.cell(287,40,'',border=1,ln=1,align='C')
        self.image(r'traonsport_images/ktc_logo2.png', 7, 7, 35)
        self.image(r'traonsport_images/ktc_logo2.png', 252, 7, 35)

        #************ Set Title **********************************
        self.set_xy(42,7)
        self.set_font('helvetica', 'BU', 35)
        self.set_text_color(138, 10, 10)
        self.cell(210,10,'ROYAL CONTAINER SERVICE',border=0,ln=1,align='C')
        self.set_x(42)
        self.set_font('helvetica', 'B', 13)
        self.set_text_color(0, 0, 0)
        self.cell(210,8,'C-5, City Center Complex, Marida Road, Nadiad-387001. (Guj.)',ln=1,border=0,align='C')
        self.set_x(42)
        self.cell(210,8,'(M) 09427855342  (M) 09429441824  (M) 09429654224',ln=1,border=0,align='C')
        self.set_x(42)
        self.cell(210,8,'Email : ichaklasiya@yahoo.in',ln=1,border=0,align='C')

        #************ Set Name And Date **********************************

        y=self.get_y()
        self.set_xy(5,y+5)
        self.set_font('helvetica', 'B', 15)
        self.set_text_color(0, 0, 0)
        self.cell(287, 10,'NAME : ', align='L',border=1)

        self.set_xy(30, y+5)
        self.set_font('helvetica', 'B', 20)
        self.set_text_color(255, 0,0)
        self.cell(150, 10,name, align='L',border=0)

        self.set_xy(230,y+5)
        self.set_font('helvetica', 'B', 15)
        self.set_text_color(0, 0, 0)
        self.cell(62, 10,'DATE : ', align='L',border=0)

        today_date = str(date.today().strftime("%d- %m- %Y"))
        self.set_xy(250, y+5)
        self.set_font('helvetica', 'B', 15)
        self.set_text_color(255, 0,0)
        self.cell(40, 10,today_date, align='C',ln=1,border=0)

        #************ Set Border **********************************

        y=self.get_y()
        self.set_xy(5,y+1)
        self.cell(287,138,'',border=1,ln=1,align='C')

        #************ Set Border **********************************

        self.set_font('helvetica', 'B', 11)
        self.set_text_color(255, 255, 255)
        self.set_fill_color(19, 80, 211)
        self.set_xy(5,57)

        if method=='BOOKING':
            boking_colum_design(self)
        elif method == 'PAYMENT':
            payment_colum_design(self)



def boking_colum_design(self):
    self.cell(15, 8, 'ID',border=1, align='C',fill=1)
    self.cell(24, 8, 'DATE',border=1, align='C',fill=1)
    self.cell(30, 8, 'VEHICLE NO', border=1, align='C',fill=1)
    self.cell(50, 8, 'SRC - DEST', border=1, align='C',fill=1)
    self.cell(24, 8, 'FREIGHT', border=1, align='C', fill=1)
    self.cell(24, 8, 'HOLDING', border=1, align='C', fill=1)
    self.cell(24, 8, 'MAJURI', border=1, align='C',fill=1)
    self.cell(24, 8, 'BHADU', border=1, align='C', fill=1)
    self.cell(24, 8, 'ADVANCE', border=1, align='C',fill=1)
    self.cell(24, 8, 'BALANCE', border=1, align='C',fill=1)
    self.cell(24, 8, 'TOTAL', border=1, align='C',fill=1)
    self.ln()

def booking_insert_value(pdf):
    pdf.set_font('helvetica', 'B', 12)
    pdf.set_y(65)
    for i,dat in enumerate(table_data):
        pdf.set_x(5)
        pdf.set_text_color(0,0,0)
        pdf.set_font('helvetica', 'B', 10)
        pdf.cell(15, 10, str(i+1), border=1, align='C')
        pdf.cell(24, 10, dat[0], border=1, align='C')
        pdf.cell(30, 10, dat[1],border=1, align='C')
        pdf.set_font('helvetica', 'B', 8)
        pdf.cell(50, 10, dat[2], border=1, align='C')
        pdf.set_font('helvetica', 'B', 9)
        pdf.cell(24, 10,dat[3], border=1, align='C')
        pdf.cell(24, 10, dat[4], border=1, align='C')
        pdf.cell(24, 10, dat[5], border=1, align='C')
        pdf.set_text_color(64, 83, 220)
        pdf.cell(24, 10, dat[6], border=1, align='C')
        pdf.set_text_color(39, 180, 16)
        pdf.cell(24, 10, dat[7], border=1, align='C')
        pdf.cell(24, 10, dat[8], border=1, align='C')
        pdf.set_text_color(212, 33, 33)
        pdf.cell(24, 10, dat[9], border=1, align='C')
        pdf.ln()

def payment_colum_design(self):
    self.set_font('helvetica', 'B', 15)
    self.cell(30, 10, 'ID',border=1, align='C',fill=1)
    self.cell(40, 10, 'DATE',border=1, align='C',fill=1)
    self.cell(50, 10, 'VEHICLE NO', border=1, align='C',fill=1)
    self.cell(70, 10, 'AMOUNT', border=1, align='C',fill=1)
    self.cell(50, 10, 'PAYMENT MODE', border=1, align='C',fill=1)
    self.cell(47, 10, 'TYPE', border=1, align='C',fill=1)
    self.ln()

def payment_insert_value(pdf):
    pdf.set_font('helvetica', 'B', 12)
    pdf.set_y(67)
    for i,dat in enumerate(table_data):
        pdf.set_x(5)
        pdf.set_text_color(0,0,0)
        pdf.set_font('helvetica', 'B', 15)
        pdf.cell(30, 10, str(i+1), border=1, align='C')
        pdf.cell(40, 10, dat[0], border=1, align='C')
        pdf.cell(50, 10, dat[1],border=1, align='C')
        pdf.set_text_color(39, 180, 16)
        pdf.cell(70, 10, dat[2], border=1, align='C')
        pdf.set_text_color(0, 0, 0)
        pdf.cell(50, 10,dat[3], border=1, align='C')
        pdf.cell(47, 10, dat[4], border=1, align='C')
        pdf.ln()

def preview_pdf(self):
    pdf_root = Toplevel()
    pdf_root.geometry("870x650+380+50")
    pdf_root.title("PDF viewer")
    pdf_root.configure(bg='white')

    v1=tkPDFViewer.ShowPdf()
    v1.img_object_li.clear()
    v2=v1.pdf_view(pdf_root,pdf_location=open(self.filename,"rb"),width=105,height=35)
    v2.pack(pady=(0,0))

    pdf_root.pdf_img = Button_Image(pdf_root, w=60, h=60,img="traonsport_images/whatsapp.png")
    pdf_root.whatsapp_button = Button(pdf_root, text="", font=("times new roman", 15, "bold"),
                             image=pdf_root.pdf_img, borderwidth=0, activebackground="#ffffff", background="#ffffff",
                             foreground="white", compound=CENTER)
    pdf_root.whatsapp_button.place(x=300, y=585, height=60)

    pdf_root.cr_img = Button_Image(pdf_root, w=50, h=50,img="traonsport_images/crome.png")
    pdf_root.crome_button = Button(pdf_root, text="", font=("times new roman", 15, "bold"),
                             image=pdf_root.cr_img, borderwidth=0, activebackground="#ffffff", background="#ffffff",
                             foreground="white", compound=CENTER,command=partial(open_pdf,self))
    pdf_root.crome_button.place(x=400, y=590, height=50)

    pdf_root.gmail_img = Button_Image(pdf_root, w=50, h=35,img="traonsport_images/gmail.png")
    pdf_root.gmail_button = Button(pdf_root, text="", font=("times new roman", 15, "bold"),
                             image=pdf_root.gmail_img, borderwidth=0, activebackground="#ffffff", background="#ffffff",
                             foreground="white", compound=CENTER)
    pdf_root.gmail_button.place(x=500, y=595, height=35)



    # pywhatkit.sendwhats_image('7405552500',"D:/transport_working/cashbook_pdf/booking_03_47_41.pdf")

def open_pdf(self):
    curdir = os.path.abspath(os.getcwd())
    curdir =curdir.replace(r"\\","/")
    filename = "file:///"+curdir+"/"+self.filename
    webbrowser.open(filename, new=1)

def create_pdf_with_tree_data(self):
    global name,method,table_data

    name = self.name
    method = self.radio_var.get()
    table_data = self.data

    pdf = PDF('L', 'mm', 'A4')

    pdf.set_auto_page_break(auto=True,margin=15)

    pdf.add_page()

    if method =='BOOKING':
        booking_insert_value(pdf)
    elif method =='PAYMENT':
        payment_insert_value(pdf)

    self.filename = r"cashbook_pdf/booking_"+ datetime.now().time().strftime("%H_%M_%S") +".pdf"
    pdf.output(self.filename)

    preview_pdf(self)
