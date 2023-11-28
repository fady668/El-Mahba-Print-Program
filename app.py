# import Modules
import time
from tkinter import *
from tkinter import ttk
from customtkinter import *
import sys
import os
import sqlite3
import shutil
from PIL import Image, ImageTk
from datetime import datetime
import json

set_appearance_mode('System')
set_default_color_theme('blue')

# CTkButtons Style (global background)
def on_enter(event):
    event.widget['background'] = '#0089C4'

def on_leave(event):
    event.widget['background'] = '#00A2E8'
    
# CTkButtons Style (red background)
def on_enter_red(event):
    event.widget['background'] = '#D91A21'

def on_leave_red(event):
    event.widget['background'] = 'red'

# Printer_APP Class
class Printer_APP(Tk):
    def __init__(self):
        super().__init__()
        self.title('مطبعة المحبة')
        self.iconbitmap('Project_files/Photos/Mahaba-Print-Logo_2.ico')
        self.geometry(f'{self.winfo_screenwidth()}x{self.winfo_screenheight()-80}+{-8}+0')
        self.after(50, lambda: self.state('zoomed'))
        self.config(background='silver')
        self.Font_Family = 'Calibri'
        self.btn_bg = '#00A2E8'
        self.lbl_bg = '#184175'

        # Variables
        self.client_name = StringVar() # in Add Client Window Funcation
        self.client_phone_num = StringVar() # in Add Client Window Funcation
        self.searchVar = StringVar() # in Create Search Frame
        self.FupdateVar = StringVar() # in Edit Client Information Window Funcation
        self.SupdateVar = StringVar() # in Edit Client Information Window Funcation
        self.delNumberVar = IntVar() # in Delete Fatora Funcation
        self.f_searchVar = StringVar() # in Client Work Window Funcation
        self.enter_money = IntVar() # in Save Client Money Funcation
        self.push_way = StringVar()
        
        # fatora entries Variables
        self.f_nameVar = StringVar()
        self.e1_dateVar = StringVar()
        self.e2_dateVar = StringVar()
        self.e3_dateVar = StringVar()
        self.tarafVar1 = StringVar()
        self.farkh_countVar = StringVar()
        self.typeVar1 = StringVar()
        self.typeVar2 = StringVar()
        self.sizeVar1 = StringVar()
        self.sizeVar2 = StringVar()
        self.salaryVar1 = StringVar()
        self.tarafVar2 = StringVar()
        self.zenk_countVar = StringVar()
        self.salaryVar2 = StringVar()
        self.sahba_countVar = StringVar()
        self.sahba2_countVar = StringVar()
        self.sVar1 = StringVar()
        self.sVar2 = StringVar()
        self.daftar_countVar = StringVar()
        self.groups_countVar = StringVar()
        self.counterVar = StringVar()
        self.num_of_countVar1 = StringVar()
        self.num_of_countVar2 = StringVar()
        
        self.slofan_SAVEVar = StringVar()
        self.slofanCkb_SAVEVar = BooleanVar(value=False)
        self.gha_SAVEVar = StringVar()
        self.slofanFinNum_SAVEVar = StringVar()

        self.UV_SAVEVar = StringVar()
        self.UVCkb_SAVEVar = BooleanVar(value=False)
        self.UVFinNum_SaveVar = StringVar()   
        
        self.taksir_SAVEVar = StringVar()
        self.taksirCkb_SAVEVar = BooleanVar(value=False)
        self.taksirNum_SAVEVar = StringVar()
        self.forma_SAVEVar = StringVar() 
        self.formaCkb_SAVEVar = BooleanVar(value=False) 

        self.spot_SAVEVar = StringVar()
        self.spotCkb_SAVEVar = BooleanVar(value=False)
        self.film_SAVEVar = StringVar()
        self.filmCkb_SAVEVar = BooleanVar(value=False)
        
        self.aklasheh_SAVEVar = StringVar()
        self.aklashehCkb_SAVEVar = BooleanVar(value=False)
        self.aklashehSal_SAVEVar = StringVar()
        self.pasma_SAVEVar = StringVar() 
        self.pasmaCkb_SAVEVar = BooleanVar(value=False)

        self.taglid_SAVEVar = StringVar()
        self.taglidCkb_SAVEVar = BooleanVar(value=False)
        self.taglidNum_SAVEVar = StringVar()
        self.taglidSal_SAVEVar = StringVar()
        
        self.tawdib_SAVEVar = StringVar()
        self.tawdibCkb_SAVEVar = BooleanVar(value=False)
        self.tasmim_SAVEVar = StringVar()
        self.tasmimCkb_SAVEVar = BooleanVar(value=False)
        self.slk_SAVEVar = StringVar()
        self.slkCkb_SAVEVar = BooleanVar(value=False)

        self.nakl_SAVEVar = StringVar()
        self.naklCkb_SAVEVar = BooleanVar(value=False)
        self.khadmat_SAVEVar = StringVar()
        self.khadmatCkb_SAVEVar = BooleanVar(value=False)
        self.kas_SAVEVar = StringVar()
        self.kasCkb_SAVEVar = BooleanVar(value=False)
        
        self.f_totalVar = IntVar()

        # Check CTkButtons Variables
        self.Check_btn_fb_var = BooleanVar()

        self.cb_K_Var1 = BooleanVar(value=False)
        self.cb_Y_Var1 = BooleanVar(value=False)
        self.cb_M_Var1 = BooleanVar(value=False)
        self.cb_C_Var1 = BooleanVar(value=False)
        self.cb_zahabi_Var1 = BooleanVar(value=False)
        self.cb_faddi_Var1 = BooleanVar(value=False)
        self.cb_sapgha_Var1 = BooleanVar(value=False)
        self.cb_warnish_Var1 = BooleanVar(value=False)
        self.cb_kohley_Var1 = BooleanVar(value=False)

        self.cb_K_Var2 = BooleanVar(value=False)
        self.cb_Y_Var2 = BooleanVar(value=False)
        self.cb_M_Var2 = BooleanVar(value=False)
        self.cb_C_Var2 = BooleanVar(value=False)
        self.cb_zahabi_Var2 = BooleanVar(value=False)
        self.cb_faddi_Var2 = BooleanVar(value=False)
        self.cb_sapgha_Var2 = BooleanVar(value=False)
        self.cb_warnish_Var2 = BooleanVar(value=False)
        self.cb_kohley_Var2 = BooleanVar(value=False)

        # Edit Variables
        self.f_nameSHOWVar = StringVar()
        self.e1_dateSHOWVar = StringVar()
        self.e2_dateSHOWVar = StringVar()
        self.e3_dateSHOWVar = StringVar()
        self.tarafSHOWVar1 = StringVar()
        self.farkh_countSHOWVar = StringVar()
        self.typeSHOWVar1 = StringVar()
        self.typeSHOWVar2 = StringVar()
        self.sizeSHOWVar1 = StringVar()
        self.sizeSHOWVar2 = StringVar()
        self.salarySHOWVar1 = StringVar()
        self.tarafSHOWVar2 = StringVar()
        self.zenk_countSHOWVar = StringVar()
        self.salarySHOWVar2 = StringVar()
        self.sahba_countSHOWVar = StringVar()
        self.sahba2_countSHOWVar = StringVar()
        self.sSHOWVar1 = StringVar()
        self.sSHOWVar2 = StringVar()
        self.daftar_countSHOWVar = StringVar()
        self.groups_countSHOWVar = StringVar()
        self.counterSHOWVar = StringVar()
        self.num_of_countSHOWVar1 = StringVar()
        self.num_of_countSHOWVar2 = StringVar()
        
        self.slofan_SHOWVar = StringVar()
        self.slofanCkb_SHOWVar = BooleanVar(value=False)
        self.gha_SHOWVar = StringVar()
        self.slofanFinNum_SHOWVar = StringVar()

        self.UV_SHOWVar = StringVar()
        self.UVCkb_SHOWVar = BooleanVar(value=False)
        self.UVFinNum_SHOWVar = StringVar()   
        
        self.taksir_SHOWVar = StringVar()
        self.taksirCkb_SHOWVar = BooleanVar(value=False)
        self.taksirNum_SHOWVar = StringVar()
        self.forma_SHOWVar = StringVar() 
        self.formaCkb_SHOWVar = BooleanVar(value=False) 

        self.spot_SHOWVar = StringVar()
        self.spotCkb_SHOWVar = BooleanVar(value=False)
        self.film_SHOWVar = StringVar()
        self.filmCkb_SHOWVar = BooleanVar(value=False)
        
        self.aklasheh_SHOWVar = StringVar()
        self.aklashehCkb_SHOWVar = BooleanVar(value=False)
        self.aklashehSal_SHOWVar = StringVar()
        self.pasma_SHOWVar = StringVar() 
        self.pasmaCkb_SHOWVar = BooleanVar(value=False)

        self.taglid_SHOWVar = StringVar()
        self.taglidCkb_SHOWVar = BooleanVar(value=False)
        self.taglidNum_SHOWVar = StringVar()
        self.taglidSal_SHOWVar = StringVar()
        
        self.tawdib_SHOWVar = StringVar()
        self.tawdibCkb_SHOWVar = BooleanVar(value=False)
        self.tasmim_SHOWVar = StringVar()
        self.tasmimCkb_SHOWVar = BooleanVar(value=False)
        self.slk_SHOWVar = StringVar()
        self.slkCkb_SHOWVar = BooleanVar(value=False)

        self.nakl_SHOWVar = StringVar()
        self.naklCkb_SHOWVar = BooleanVar(value=False)
        self.khadmat_SHOWVar = StringVar()
        self.khadmatCkb_SHOWVar = BooleanVar(value=False)
        self.kas_SHOWVar = StringVar()
        self.kasCkb_SHOWVar = BooleanVar(value=False)
        
        self.f_totalSHOWVar = IntVar()
        self.money_done_swtch = IntVar()
        
        self.fatora_SHOWmoney = 0
        
        # Check CTkButtons Variables ( Show )
        self.Check_btn_fb_SHOWVar = BooleanVar()
        
        self.cb_K_SHOWVar1 = BooleanVar(value=False)
        self.cb_Y_SHOWVar1 = BooleanVar(value=False)
        self.cb_M_SHOWVar1 = BooleanVar(value=False)
        self.cb_C_SHOWVar1 = BooleanVar(value=False)
        self.cb_zahabi_SHOWVar1 = BooleanVar(value=False)
        self.cb_faddi_SHOWVar1 = BooleanVar(value=False)
        self.cb_sapgha_SHOWVar1 = BooleanVar(value=False)
        self.cb_warnish_SHOWVar1 = BooleanVar(value=False)
        self.cb_kohley_SHOWVar1 = BooleanVar(value=False)
        
        self.cb_K_SHOWVar2 = BooleanVar(value=False)
        self.cb_Y_SHOWVar2 = BooleanVar(value=False)
        self.cb_M_SHOWVar2 = BooleanVar(value=False)
        self.cb_C_SHOWVar2 = BooleanVar(value=False)
        self.cb_zahabi_SHOWVar2 = BooleanVar(value=False)
        self.cb_faddi_SHOWVar2 = BooleanVar(value=False)
        self.cb_sapgha_SHOWVar2 = BooleanVar(value=False)
        self.cb_warnish_SHOWVar2 = BooleanVar(value=False)
        self.cb_kohley_SHOWVar2 = BooleanVar(value=False)

        # Salaries Initialization Variables
        # 1 - The Colors [ K, Y, M, C, zahabi, faddi, sapgha, warnish, kohley, spechial ]---
        self.K_var = DoubleVar()         #                                                  \                                                     
        self.Y_var = DoubleVar()         #                                                   \                                                   
        self.M_var = DoubleVar()         #                                                    \                                                   
        self.C_var = DoubleVar()         #                                                     \                                                  
        self.zahabi_var = DoubleVar()    #                                                      \                                                     
        self.faddi_var = DoubleVar()     #                                                       \                                                    
        self.sapgha_var = DoubleVar()    #                                                        \                                                   
        self.warnish_var = DoubleVar()   #                                                         \                                                  
        self.kohley_var = DoubleVar()    #                                                          \                                                 
        self.spechial_var = DoubleVar()  #                                                           \                                                    
        # 2 - The taglid [ slofan, UV, spot, tawdib, taksir, dapoos, lask, taglid, forma, pasma ]-----)
        self.slofan_var = DoubleVar()    #                                                           /    
        self.UV_var = DoubleVar()        #                                                          / 
        self.taksir_var = DoubleVar()    #                                                         /
        self.film_var = DoubleVar()      #                                                        /
        self.checkboxsVar = 0            #                                                       /
        self.counter = 0
        # ---------------------------------------------------------------------------------------
        # Salaries Initialization Variables (Show)
        # 1 - The Colors [ K, Y, M, C, zahabi, faddi, sapgha, warnish, kohley, spechial ]------
        self.K_SHOWvar = DoubleVar()         #                                                  \                                                     
        self.Y_SHOWvar = DoubleVar()         #                                                   \                                                   
        self.M_SHOWvar = DoubleVar()         #                                                    \                                                   
        self.C_SHOWvar = DoubleVar()         #                                                     \                                                  
        self.zahabi_SHOWvar = DoubleVar()    #                                                      \                                                     
        self.faddi_SHOWvar = DoubleVar()     #                                                       \                                                    
        self.sapgha_SHOWvar = DoubleVar()    #                                                        \                                                   
        self.warnish_SHOWvar = DoubleVar()   #                                                         \                                                  
        self.kohley_SHOWvar = DoubleVar()    #                                                          \                                                 
        self.spechial_SHOWvar = DoubleVar()  #                                                           \                                                    
        # 2 - The taglid [ slofan, UV, spot, tawdib, taksir, dapoos, lask, taglid, forma, pasma ]---------)
        self.slofan_SHOWvar = DoubleVar()    #                                                           /    
        self.UV_SHOWvar = DoubleVar()        #                                                          / 
        self.taksir_SHOWvar = DoubleVar()    #                                                         /
        self.film_SHOWvar = DoubleVar()      #                                                        /
        # --------------------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------------------
        # Create Header frame
        h_frame = Frame(self, bg='White')
        h_frame.place(x=5, y=5, width=self.winfo_screenwidth()-10, height=100)
        image = ImageTk.PhotoImage(Image.open('Project_files/Photos/Mahaba Print Logo_2.jpg'))
        img_lbl = Label(h_frame, image=image, bg='white')
        img_lbl.place(x=500, y=5)
        Printer_name_lbl = Label(h_frame, text='مطبعة المحبة\nللطباعة والتوريدات', bg='white', fg='black', font=(self.Font_Family, 22))
        Printer_name_lbl.place(x=1300, y=8)
        

        # Create Search Frame
        Search_frame = Frame(self, bg='white')
        Search_frame.place(x=self.winfo_screenwidth()-305, y= 110, width=300, height=340)

        Search_lbl = Label(Search_frame, text='البحث عن عميل', fg='white', bg=self.lbl_bg, font=(self.Font_Family, 20))
        Search_lbl.pack(fill=X)
        entry_lbl = Label(Search_frame, text='أدخل أسم العميل', bg='white', font=(self.Font_Family, 18))
        entry_lbl.pack(pady=(30, 20))
        self.Search_entry = Entry(Search_frame, textvariable=self.searchVar, bd=2, width=20, justify='center', font=(self.Font_Family, 15))
        self.Search_entry.pack()
        Search_btn = CTkButton(Search_frame,
                               text='بــــــــــــحــــــــــــــــــــــث',
                               text_color='white', 
                               cursor='hand2',
                               font=(self.Font_Family, 22),
                               border_width=2,
                               border_color='silver',
                               corner_radius=10,
                               width=220,
                               height=55,
                               command=self.client_search)
        Search_btn.pack(pady=20)
        
        reset_btn = CTkButton(Search_frame,
                            text='أعادة تهيئة الجدول',
                            text_color='white', 
                            cursor='hand2',
                            font=(self.Font_Family, 22),
                            border_width=2,
                            border_color='silver',
                            corner_radius=10,
                            width=220,
                            height=55,
                            command=self.table_reset)
        reset_btn.pack(pady=10)


        # Create CTkButtons Frame
        btn_frame = Frame(self, bg='white')
        btn_frame.place(x=self.winfo_screenwidth()-305, y=455, width=300, height=self.winfo_screenheight()-460)

        btn_lbl = Label(btn_frame, text='لوحة التحكم', bg=self.lbl_bg, fg='white', font=(self.Font_Family, 20))
        btn_lbl.pack(fill=X)

        add_btn = CTkButton(btn_frame,
                    text='أضافة عميل جديد',
                    text_color='white', 
                    cursor='hand2',
                    font=(self.Font_Family, 22),
                    border_width=2,
                    border_color='silver',
                    corner_radius=10,
                    width=220,
                    height=55,
                    command=self.add_client)
        add_btn.pack(pady=(30, 15))

        remove_btn = CTkButton(btn_frame,
                            text='حذف العميل', 
                            text_color='white', 
                            cursor='hand2',
                            font=(self.Font_Family, 22),
                            border_width=2,
                            border_color='silver',
                            corner_radius=10,
                            width=220,
                            height=55,
                            command=self.del_client_mess)
        remove_btn.pack(pady=15)

        edit_btn = CTkButton(btn_frame,
                          text='تعديل بيانات العميل', 
                            text_color='white', 
                            cursor='hand2',
                            font=(self.Font_Family, 22),
                            border_width=2,
                            border_color='silver',
                            corner_radius=10,
                            width=220,
                            height=55,
                          command=self.edit_client)
        edit_btn.pack(pady=15)

        work_btn = CTkButton(btn_frame,
                          text='العمل الجاري', 
                            text_color='white', 
                            cursor='hand2',
                            font=(self.Font_Family, 22),
                            border_width=2,
                            border_color='silver',
                            corner_radius=10,
                            width=220,
                            height=55,
                          command=self.client_work)
        work_btn.pack(pady=15)

        count_btn = CTkButton(btn_frame,
                            text='عدد العملاء', 
                            text_color='white', 
                            cursor='hand2',
                            font=(self.Font_Family, 22),
                            border_width=2,
                            border_color='silver',
                            corner_radius=10,
                            width=220,
                            height=55,
                            command=self.client_counter)
        count_btn.pack(pady=15)

        exit_btn = CTkButton(btn_frame,
                            text='إغلاق البرنامج', 
                            text_color='white', 
                            cursor='hand2',
                            font=(self.Font_Family, 22),
                            border_width=2,
                            border_color='silver',
                            corner_radius=10,
                            width=220,
                            height=55,
                            command=sys.exit)
        exit_btn.pack(pady=15)

        # Display Clintes
        display_frame = Frame(self, bg='white')
        display_frame.place(x=5, y=110, width=self.winfo_screenwidth()-315, height=self.winfo_screenheight()-115)

        scroll_x = Scrollbar(display_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(display_frame, orient=VERTICAL)

        self.clients_table = ttk.Treeview(display_frame, 
                                     xscrollcommand=scroll_x.set, 
                                     yscrollcommand=scroll_y.set, 
                                     columns=('Money_Done', 'All_Money', 'Number_Phones', 'Clients_Names'))
        self.clients_table.place(x=18, y=1, width=self.winfo_screenwidth()-315, height=self.winfo_screenheight()-195)

        scroll_x.pack(fill=X, side=BOTTOM)
        scroll_y.pack(fill=Y, side=LEFT)

        ttk.Style().theme_use('winnative')
        ttk.Style().configure('Treeview1.Treeview.Heading', font=(self.Font_Family, 20, 'bold'), foreground='#0024FF', rowheight=60)
        ttk.Style().configure('Treeview1.Treeview', font=(self.Font_Family, 18), rowheight=50)
        self.clients_table['style'] = 'Treeview1.Treeview'

        self.clients_table['show'] = 'headings'
        for column in self.clients_table["columns"]:
            self.clients_table.column(column, anchor=CENTER)
        self.clients_table.heading('Money_Done', text='تم دفع من الحساب', anchor=CENTER)
        self.clients_table.heading('All_Money', text='أجمالي الحساب', anchor=CENTER)
        self.clients_table.heading('Number_Phones', text='ارقام الهاتف', anchor=CENTER)
        self.clients_table.heading('Clients_Names', text='أسماء العملاء', anchor=CENTER)
        self.clients_table.bind('<ButtonRelease-1>', self.get_cursor)
        self.clients_table.bind('<Double-1>', self.clientsTableDouble)

        
        self.clientNameSort()
        self.Display_info()

        # Run Tkinter Application
        self.mainloop()
        
    def clientsTableDouble(self, event):
        self.client_work()

    # ===================================================================================

    # The client_search Funcation
    def client_search(self):
        db = sqlite3.connect("Project_files/Clients.db")   
        cr = db.cursor()
        
        # Fetch All Data from Database
        cr.execute(f'SELECT * FROM Clients where name = "{self.searchVar.get()}"')
        self.rows = cr.fetchall()
        
        # Clear existing data from the table
        if len(self.rows) != 0:
            self.clients_table.delete(*self.clients_table.get_children())
            
            for row in self.rows:
                # Center the data in the "Icon" column
                self.clients_table.insert('', 'end', values=row)

            db.commit()
            db.close()

    # ===================================================================================

    # Display_info Funcation
    def Display_info(self):
        db = sqlite3.connect("Project_files/Clients.db")   
        cr = db.cursor()
        
        # Fetch All Data from Database
        cr.execute('SELECT * FROM Clients')
        self.rows = cr.fetchall()
        
        # Clear existing data from the table
        if len(self.rows) != 0:
            self.clients_table.delete(*self.clients_table.get_children())
            
            for row in self.rows:
                # Center the data in the "Icon" column
                self.clients_table.insert('', 'end', values=row)

            db.commit()
            db.close()
        else:
            self.clients_table.delete(*self.clients_table.get_children())

    # ===================================================================================

    def clientNameSort(self):
    
        db = sqlite3.connect(f'Project_files/Clients.db')
        cr = db.cursor()

        cr.execute(f'SELECT * from Clients')
        fetched_data = cr.fetchall()

        lst = []

        for x in fetched_data:
            lst.append(list(x))

        sorted_lst = sorted(lst, key=lambda x: x[3])

        cr.execute('delete from Clients')

        for row in sorted_lst:
            cr.execute(f'INSERT INTO Clients VALUES ({row[0]}, {row[1]}, "{row[2]}", "{row[3]}")')

        db.commit()
        db.close()

    # ===================================================================================

    def fatoraDateSort(self):
        db = sqlite3.connect(f'Project_files/Clients Work/{self.searchVar.get()}/Fawatir.db')
        cr = db.cursor()

        cr.execute('CREATE TABLE if not exists newTable (done_or_not text, f_money integer, f_date text, f_name text, f_number intger primary key)')
        cr.execute('SELECT * FROM All_fatora')

        fetched_data = cr.fetchall()

        lst = []

        for x in fetched_data:
            lst.append(list(x))

        sorted_lst = sorted(lst, key=lambda x: x[2])
            
        cr.execute('delete from All_fatora')

        for row in sorted_lst:
            cr.execute(f'INSERT INTO newTable VALUES ("{row[0]}", {row[1]}, "{row[2]}", "{row[3]}", {row[4]})')

        cr.execute('DROP TABLE All_fatora')
        cr.execute(f'ALTER TABLE newTable RENAME TO All_fatora')

        db.commit()
        db.close()

    # ===================================================================================
    
    # The Counter Of the Clients Funcation
    def client_counter(self):
        db = sqlite3.connect("Project_files/Clients.db")   
        cr = db.cursor()
        
        # Fetch All Data from Database
        cr.execute('SELECT * FROM Clients')
        self.rows = cr.fetchall()
        count = len(self.rows)

        frame = Tk()
        frame.title('عدد العملاء')
        frame.config(background='#092642')
        frame.geometry(f'350x100+{(self.winfo_screenwidth()-350)//2}+{(self.winfo_screenheight()-100)//2}')

        lbl = Label(frame, text=f'( {count} ) عدد العملاء ', bg='#092642', fg='white', font=(self.Font_Family, 20, 'bold'))
        lbl.pack(pady=(30, 0))

        db.commit()
        db.close()

    # ===================================================================================

    # Add Client Window Funcation
    def add_client(self):
        self.add_window = Toplevel()
        self.add_window.title('أضافة عميل')
        self.add_window.resizable(False, False)
        self.add_window.config(background='silver')
        self.add_window_width = 315
        self.add_window_height = 375
        self.add_window.geometry(f'{self.add_window_width}x{self.add_window_height}+{(self.winfo_screenwidth()-self.add_window_width)//2}+{(self.winfo_screenheight()-self.add_window_height)//2}')

        frame = Frame(self.add_window, bg='white')
        frame.place(x=2, y=2, width=self.add_window_width-4, height=self.add_window_height-4)

        h_lbl = Label(frame, text='اضافة عميل', bg=self.lbl_bg, fg='white', font=(self.Font_Family, 20))
        h_lbl.pack(fill=X)
        f_lbl = Label(frame, text='أسم العميل', bg='white', fg='black', font=(self.Font_Family, 18))
        f_lbl.pack(pady=(30, 0))
        self.f_entry = Entry(frame, bd=2, width=20, textvariable=self.client_name, justify='center', font=(self.Font_Family, 15))
        self.f_entry.pack(pady=(20))
        s_lbl = Label(frame, text='رقم هاتف العميل', bg='white', fg='black', font=(self.Font_Family, 18))
        s_lbl.pack()
        self.s_entry = Entry(frame, bd=2, width=20, textvariable=self.client_phone_num, justify='center', font=(self.Font_Family, 15))
        self.s_entry.pack(pady=20)
        btn = CTkButton(frame, 
                     text='أضافة',
                        text_color='white', 
                        cursor='hand2',
                        font=(self.Font_Family, 22),
                        border_width=2,
                        border_color='silver',
                        corner_radius=10,
                        width=180,
                        height=40,
                     command=self.new_client)
        btn.pack()

    # ===================================================================================

    # Edit Client Information Window Funcation
    def edit_client(self):
        # window
        self.edit_window = Toplevel()
        self.edit_window.title('تعديل بيانات')
        self.edit_window.resizable(False, False)
        self.edit_window.config(background='silver')
        self.edit_window_width = 315
        self.edit_window_height = 375
        self.edit_window.geometry(f'{self.edit_window_width}x{self.edit_window_height}+{(self.winfo_screenwidth()-self.edit_window_width)//2}+{(self.winfo_screenheight()-self.edit_window_height)//2}')
        
        frame = Frame(self.edit_window, bg='white')
        frame.place(x=2, y=2, width=self.edit_window_width-4, height=self.edit_window_height-4)
        h_lbl = Label(frame, text='تعديل بيانات العميل', bg=self.lbl_bg, fg='white', font=(self.Font_Family, 20))
        h_lbl.pack(fill=X)
        f_lbl = Label(frame, text='أسم العميل', bg='white', fg='black', font=(self.Font_Family, 18))
        f_lbl.pack(pady=(30, 0))
        self.f_Uentry = Entry(frame, textvariable=self.FupdateVar, bd=2, width=20, justify='center', font=(self.Font_Family, 15))
        self.f_Uentry.pack(pady=(20))
        s_lbl = Label(frame, text='رقم هاتف العميل', bg='white', fg='black', font=(self.Font_Family, 18))
        s_lbl.pack()
        self.s_Uentry = Entry(frame, textvariable=self.SupdateVar, bd=2, width=20, justify='center', font=(self.Font_Family, 15))
        self.s_Uentry.pack(pady=20)
        btn = CTkButton(frame, text='تعديل', 
                            text_color='white', 
                            cursor='hand2',
                            font=(self.Font_Family, 22),
                            border_width=2,
                            border_color='silver',
                            corner_radius=10,
                            width=180,
                            height=40,
                     command=self.update_client)
        btn.pack()

    # ===================================================================================

        # New Client Funcation
    def new_client(self):
        # Add client to the orignal database
        db = sqlite3.connect('Project_files/Clients.db')
        cr = db.cursor()

        num_phone = '------------------'
        if self.s_entry.get():
            num_phone = self.s_entry.get()

        cr.execute(f'INSERT INTO Clients VALUES (0, 0, "{num_phone}", "{self.f_entry.get()}")')

        if os.path.exists(f'Project_files/Clients Work/{self.f_entry.get()}'):
            shutil.rmtree(f'Project_files/Clients Work/{self.f_entry.get()}')

        # make Client Folder
        os.makedirs(f'Project_files/Clients Work/{self.f_entry.get()}')

        # Create Fawatir database to client
        db_2 = sqlite3.connect(f'Project_files/Clients Work/{self.f_entry.get()}/Fawatir.db')
        cr_2 = db_2.cursor()

        cr_2.execute('CREATE TABLE All_fatora(done_or_not text, f_money integer, f_date text, f_name text, f_number intger)')

        db_2.commit()
        db_2.close()

        db.commit()
        self.clientNameSort()
        self.Display_info()
        self.client_name.set('')
        self.client_phone_num.set('')
        self.add_window.destroy()
        db.close()

    # ===================================================================================

    # reset Clients table Funcation 
    def table_reset(self):
        self.searchVar.set('')
        self.clientNameSort()
        self.Display_info()

    # ===================================================================================

    # Update Information Funcation
    def update_client(self):
        db = sqlite3.connect('Project_files/Clients.db')
        cr = db.cursor()

        old_dir_name = self.searchVar.get()
        new_dir_name = self.f_Uentry.get()
        new_client_phone = self.s_Uentry.get()

        cr.execute(f'UPDATE Clients set name="{new_dir_name}", number_phone="{new_client_phone}" where name="{old_dir_name}"')

        os.rename(f'Project_files/Clients Work/{old_dir_name}', f'Project_files/Clients Work/{new_dir_name}')

        db.commit()
        self.clientNameSort()
        self.Display_info()
        self.searchVar.set(self.f_Uentry.get())
        db.close()

    # ===================================================================================

    # Get Cursor Funcation
    def get_cursor(self, event):
        cursor_info = self.clients_table.focus()
        rows = self.clients_table.item(cursor_info)['values']
        self.FupdateVar.set(rows[3])
        self.SupdateVar.set(f'0{rows[2]}')
        if rows[2] == '------------------':
            self.SupdateVar.set('')
        self.searchVar.set(rows[3])

    # ===================================================================================

    def del_client_mess(self):

        # get all names of clients 
        db = sqlite3.connect('Project_files/Clients.db')
        cr = db.cursor()

        cr.execute('SELECT name FROM Clients')
        names = cr.fetchall()
        Clients_name_lst = []

        for name in names:
            for f_name in name:
                Clients_name_lst.append(f_name)
                
        db.commit()
        db.close()

        if self.searchVar.get() in Clients_name_lst:

            self.dcm = Toplevel()
            self.dcm.title('رسالة حذف العميل')
            self.dcm_width = 350
            self.dcm_height = 120
            self.dcm.config(background='white')
            self.dcm.geometry(f'{self.dcm_width}x{self.dcm_height}+{(self.winfo_screenwidth() - self.dcm_width)//2}+{(self.winfo_screenheight() - self.dcm_height)//2}')

            self.dcm_lbl = Label(self.dcm, text='هل تريد حذف هذا العميل ؟', bg='white', fg='black', font=(self.Font_Family, 18, 'bold')).pack(pady=(10,0))

            yes_btn = CTkButton(self.dcm, text='نعم',
                                fg_color='red',
                                hover_color='#E30004',
                                text_color='white', 
                                cursor='hand2',
                                font=(self.Font_Family, 22),
                                border_width=2,
                                border_color='grey',
                                corner_radius=10,
                                width=60,
                                height=40,
                                command=self.del_client)
            yes_btn.place(x=185, y=60)

            no_btn = CTkButton(self.dcm, text='لا',
                            text_color='white', 
                            cursor='hand2',
                            font=(self.Font_Family, 22),
                            border_width=2,
                            border_color='silver',
                            corner_radius=10,
                            width=60,
                            height=40,
                               command=self.dcm.destroy)
            no_btn.place(x=105, y=60)

        else:
            None

    # ===================================================================================
    
    # Delete Client Funcation
    def del_client(self):
        db = sqlite3.connect("Project_files/Clients.db")   
        cr = db.cursor()

        try:
            shutil.rmtree(f'Project_files/Clients Work/{self.searchVar.get()}')
        except PermissionError as e:
            time.sleep(2)  # Adjust the duration based on your needs
            shutil.rmtree(f'Project_files/Clients Work/{self.searchVar.get()}')
            
        cr.execute(f'delete FROM Clients where name="{self.searchVar.get()}"')

        db.commit()
        self.table_reset()
        self.searchVar.set('')
        db.close()
        self.dcm.destroy()

    # ===================================================================================

    # Client Work Window Funcation
    def client_work(self):
        self.work_window = Toplevel()
        self.work_window.title('العمل الجاري')
        self.work_window.resizable(False, False)
        self.work_window.config(background='silver')
        self.work_window_width = 1020
        self.work_window_height = 675
        self.work_window.geometry(f'{self.work_window_width}x{self.work_window_height}+{((self.winfo_screenwidth()-self.work_window_width)//2)+133}+{(self.winfo_screenheight()-self.work_window_height)//2}')

        
        # get all names of clients 
        db = sqlite3.connect('Project_files/Clients.db')
        cr = db.cursor()

        cr.execute('SELECT name FROM Clients')
        names = cr.fetchall()
        Clients_name_lst = []

        for name in names:
            for f_name in name:
                Clients_name_lst.append(f_name)

        
        db.commit()
        db.close()
        
        name_frame = Frame(self.work_window, bg=self.lbl_bg)
        name_frame.place(x=(self.work_window_width-238)+6, y=2, width=230, height=71)
        name_lbl = Label(name_frame, text=f'أسم العميل\n({self.searchVar.get()})', bg=self.lbl_bg, fg='white', font=(self.Font_Family, 18, 'bold'))
        name_lbl.pack(pady=(2, 0))

        Search_frame = Frame(self.work_window, bg='white')
        Search_frame.place(x=2, y=2, width=(self.work_window_width-238), height=67)

        # entry_lbl = Label(self.work_window, text='أدخل أسم الفاتورة', bg='white', font=(self.Font_Family, 16))
        # entry_lbl.pack(pady=(15, 15))
        Search_entry = Entry(self.work_window, textvariable=self.f_searchVar, bd=2, width=33, justify='right', font=(self.Font_Family, 16, 'bold'))
        Search_entry.place(x=355, y=19)
        Search_btn = CTkButton(self.work_window, text='بــــــــــحــــــــــث', 
                                bg_color='white',
                                text_color='white', 
                                cursor='hand2',
                                font=(self.Font_Family, 22),
                                border_width=2,
                                border_color='silver',
                                corner_radius=10,
                                width=110,
                                height=40,
                               command=self.f_search)
        Search_btn.place(x=220, y=18)
        reset_btn = CTkButton(Search_frame, 
                              text='تهيئة الجدول',
                                text_color='white', 
                                cursor='hand2',
                                font=(self.Font_Family, 22),
                                border_width=2,
                                border_color='silver',
                                corner_radius=10,
                                width=110,
                                height=40,
                              command=self.table_reset_2)
        reset_btn.place(x=95-20, y=16)

        btn_frame = Frame(self.work_window, bg='white')
        btn_frame.place(x=self.work_window_width-232, y=77, width=230, height=700)
        frame_lbl = Label(btn_frame, text='لوحة التحكم', bg=self.lbl_bg, fg='white', font=(self.Font_Family, 18))
        frame_lbl.pack(fill=X)
        add_fatora_btn = CTkButton(btn_frame, text='فاتورة جديدة', 
                                    text_color='white', 
                                    cursor='hand2',
                                    font=(self.Font_Family, 22),
                                    border_width=2,
                                    border_color='silver',
                                    corner_radius=10,
                                    width=60,
                                    height=50,
                                   command=self.Add_fatora)
        add_fatora_btn.place(x=95, y=50)
        del_fatora_btn = CTkButton(btn_frame, 
                                   text='حذف', 
                                    text_color='white', 
                                    fg_color='red', 
                                    hover_color='#E30004',
                                    bg_color='white',
                                    cursor='hand2',
                                    font=(self.Font_Family, 22),
                                    border_width=2,
                                    border_color='grey',
                                    corner_radius=10,
                                    width=60,
                                    height=50,
                                   command=self.del_fatora_mess)
        del_fatora_btn.place(x=23, y=50)
        edit_fatora_btn = CTkButton(btn_frame, text='تحرير الفاتورة',
                                    text_color='white', 
                                    cursor='hand2',
                                    font=(self.Font_Family, 22),
                                    border_width=2,
                                    border_color='silver',
                                    corner_radius=10,
                                    width=190,
                                    height=50,
                                    command=self.Show_Fatora)
        edit_fatora_btn.place(x=23, y=110)
        salary_btn = CTkButton(btn_frame, text='وضع الاسعار',
                                    text_color='white', 
                                    cursor='hand2',
                                    font=(self.Font_Family, 22),
                                    border_width=2,
                                    border_color='silver',
                                    corner_radius=10,
                                    width=190,
                                    height=50,
                                    command=self.put_salary_frame)
        salary_btn.place(x=23, y=170)
        estlam_btn = CTkButton(btn_frame, text='استلام نقدية',
                                    text_color='white', 
                                    cursor='hand2',
                                    font=(self.Font_Family, 22),
                                    border_width=2,
                                    border_color='silver',
                                    corner_radius=10,
                                    width=190,
                                    height=50,
                                    command=self.take_money)
        estlam_btn.place(x=23, y=230)
        kashfHesab_btn = CTkButton(btn_frame, text='كشف حساب',
                                    text_color='white', 
                                    cursor='hand2',
                                    font=(self.Font_Family, 22),
                                    border_width=2,
                                    border_color='silver',
                                    corner_radius=10,
                                    width=190,
                                    height=50)
        kashfHesab_btn.place(x=23, y=290)
        
        pakyElhesap_frame = CTkFrame(btn_frame, fg_color='white', corner_radius=20, border_width=3, border_color='black', width=220)
        pakyElhesap_frame.pack(pady=(350, 0))
        pakyElhesap_lbl = Label(pakyElhesap_frame, text=f'اجــــــمــــــالــــــي الــــــحـــــــســــــاب', bg='white', fg='red', font=(self.Font_Family, 18, 'bold'), width=14)
        pakyElhesap_lbl.pack()
        self.pakyElhesap_lbl_2 = Label(pakyElhesap_frame, text=f'', bg='white', fg='black', font=(self.Font_Family, 18, 'bold'))
        self.pakyElhesap_lbl_2.pack(pady=5)

        display_ditails = Frame(self.work_window, bg='white')
        display_ditails.place(x=2, y=71, width=self.work_window_width-238, height=self.work_window_height-4)

        scroll_x = Scrollbar(display_ditails, orient=HORIZONTAL)
        scroll_y = Scrollbar(display_ditails, orient=VERTICAL)

        self.tree = ttk.Treeview(display_ditails, xscrollcommand=scroll_x, yscrollcommand=scroll_y, 
                            columns=('DoneOrNot', 'MoneyOfWork', 'dateOfWork', 'NameOfWork', 'NumOfWork'))
        self.tree.place(x=18, y=2, width=self.work_window_width-250, height=self.work_window_height-50)

        scroll_x.pack(fill=X, side=BOTTOM)
        scroll_y.pack(fill=Y, side=LEFT)

        ttk.Style().configure('Treeview2.Treeview.Heading', font=(self.Font_Family, 18, 'bold'), foreground='#0024FF', rowheight=50, width=2)
        ttk.Style().configure('Treeview2.Treeview', font=(self.Font_Family, 16), rowheight=40)
        self.tree['style'] = 'Treeview2.Treeview'

        self.tree['show'] = 'headings'
        for column in self.tree["columns"]:
            self.tree.column(column, anchor=CENTER)
        self.tree.heading(column='NumOfWork', text='رقم الفاتورة', anchor=CENTER)
        self.tree.column('NumOfWork', minwidth=117, width=117, stretch=NO)
        self.tree.heading(column='NameOfWork', text='اسم الفاتورة', anchor=CENTER)
        self.tree.column('NameOfWork', minwidth=220, width=220, stretch=NO)
        self.tree.heading(column='dateOfWork', text='التاريخ', anchor=CENTER)
        self.tree.column('dateOfWork', minwidth=200, width=200, stretch=NO)
        self.tree.heading(column='MoneyOfWork', text='الحساب', anchor=CENTER)
        self.tree.column('MoneyOfWork', minwidth=100, width=100, stretch=NO)
        self.tree.heading(column='DoneOrNot', text='الدفع', anchor=CENTER)
        self.tree.column('DoneOrNot', minwidth=125, width=125, stretch=NO)
        self.tree.bind('<ButtonRelease-1>', self.get_cursor_2)
        self.tree.bind('<Double-1>', self.on_double_Click)

        self.work_window.protocol("WM_DELETE_WINDOW", self.work_window_distroy)

        if not self.searchVar.get():
            self.work_window.destroy()
            None
            
        if self.searchVar.get() not in Clients_name_lst:
            self.work_window.destroy()
            None
        

        self.f_searchVar.set('')
        self.fatoraDateSort()
        self.fatoraNumberSort()
        self.Display_info_2()
        
    def on_double_Click(self, event):
        self.Show_Fatora()
# ======================================================================================================

    def fatoraNumberSort(self):
        
        db = sqlite3.connect(f'Project_files/Clients Work/{self.searchVar.get()}/Fawatir.db')
        cr = db.cursor()

        cr.execute(f'SELECT * from All_fatora')
        fetched_data = cr.fetchall()

        lst = []

        for x in fetched_data:
            lst.append(list(x))

        for x in range(len(lst)):
            lst[x][-1] = x+1
            
        cr.execute('delete from All_fatora')

        for row in lst:
            cr.execute(f'INSERT INTO All_fatora VALUES ("{row[0]}", {row[1]}, "{row[2]}", "{row[3]}", {row[4]})')

        db.commit()
        db.close()

        # db = sqlite3.connect(f'Project_files/Clients Work/{self.searchVar.get()}/Fawatir.db')
        # cr = db.cursor()

        # cr.execute('CREATE TABLE if not exists newTable (done_or_not text, f_money integer, f_date text, f_name text, f_number intger primary key)')
        # cr.execute('SELECT * FROM All_fatora')

        # fetched_data = cr.fetchall()

        # lst = []

        # for x in fetched_data:
        #     lst.append(list(x))

        # for x in range(len(lst)):
        #     lst[x][-1] = x+1
            
        # cr.execute('delete from All_fatora')

        # for row in lst:
        #     cr.execute(f'INSERT INTO newTable VALUES ("لم يتم الدفع", {row[0]}, "{row[1]}", "{row[2]}", {row[3]})')

        # cr.execute('DROP TABLE All_fatora')
        # cr.execute(f'ALTER TABLE newTable RENAME TO All_fatora')

        # db.commit()
        # db.close()

    # ======================================================================================================
    # Add Client Work Funcation
    def Add_fatora(self):
        self.n_window = Toplevel()
        self.n_window.title('أضافة فاتورة')
        self.n_window.config(background='silver')
        self.n_window_width = 550
        self.n_window_hieght = self.work_window_height + 90
        self.n_window.geometry(f'{self.n_window_width}x{self.winfo_screenheight()-100}+20+10')
        # Check CTkButtons Style
        ttk.Style().configure('Custom.TCheckbutton', background = 'white')
        # ComboBox Sytle
        ttk.Style().configure('TCombobox', background = 'white') 

        work_info_frame = Frame(self.n_window, bg='white')
        work_info_frame.place(x=0, y=0, width=self.n_window_width, height=100)
        client_name = Label(work_info_frame, text=('----------> ' + str(self.searchVar.get()) + ' <----------'), bg='white', fg='black', font=(self.Font_Family, 17, 'bold')).pack(pady=5)
        name_of_work_lbl = Label(work_info_frame, text=' : اسم العملية', bg='white', font=(self.Font_Family, 15))
        name_of_work_lbl.place(x=self.n_window_width-110, y=55)
        self.name_of_work_entry = Entry(work_info_frame, textvariable=self.f_nameVar, bd=2, bg='white', justify='right', font=(self.Font_Family, 13))
        self.name_of_work_entry.place(x=self.n_window_width-310, y=60, width=200, height=25)
        date_of_work_lbl = Label(work_info_frame, text=' : التاريخ', bg='white', font=(self.Font_Family, 15))
        date_of_work_lbl.place(x=self.n_window_width-390, y=55)
        self.day_of_work_entry1 = Entry(work_info_frame, textvariable=self.e1_dateVar, bg='white', justify='center', font=(self.Font_Family, 12))
        self.month_of_work_entry2 = Entry(work_info_frame, textvariable=self.e2_dateVar, bg='white', justify='center', font=(self.Font_Family, 12))
        self.year_of_work_entry3 = Entry(work_info_frame, textvariable=self.e3_dateVar, bg='white', justify='center', font=(self.Font_Family, 12))
        slash_1 = Label(work_info_frame, text=' / ', bg='white', font=(self.Font_Family, 15))
        slash_2 = Label(work_info_frame, text=' / ', bg='white', font=(self.Font_Family, 15))
        self.day_of_work_entry1.place(x=self.n_window_width-415, y=60, width=25, height=20)
        slash_1.place(x=self.n_window_width-435, y=55)
        self.month_of_work_entry2.place(x=self.n_window_width-460, y=60, width=25, height=20)
        slash_2.place(x=self.n_window_width-480, y=55)
        self.year_of_work_entry3.place(x=self.n_window_width-530, y=60, width=50, height=20)
        
        # fill the Date Automaticlly 
        f_date = (str(datetime.now())[:str(datetime.now()).find(' ')].strip()).replace('-', '/', 1)
        
        year = f_date[:f_date.find('/')]
        month = f_date[f_date.find('/'):f_date.find('-')].strip('/')
        day = f_date[f_date.find('-'):].strip('-')
        self.e1_dateVar.set(day)
        self.e2_dateVar.set(month)
        self.e3_dateVar.set(year)

        warak_frame = Frame(self.n_window, bg='white')
        warak_frame.place(x=0, y=105, width=self.n_window_width, height=120)
        warak_lbl = Label(warak_frame, text='الورق', bg=self.lbl_bg, fg='white', font=(self.Font_Family, 18, 'bold'))
        warak_lbl.pack(fill=X)
        taraf_lbl = Label(warak_frame, text=' : طرف', bg='white', font=(self.Font_Family, 15))
        taraf_lbl.place(x=self.n_window_width-65, y=45)
        taraf_combo = ttk.Combobox(warak_frame, textvariable=self.tarafVar1, values=('المطبعة', 'العميل'), justify='center', state='readonly', font=(self.Font_Family, 13))
        taraf_combo.place(x=self.n_window_width-165, y=45, width=100, height=25)
        farkh_count_lbl = Label(warak_frame, text=' : عدد الأفرخ', bg='white', font=(self.Font_Family, 15))
        farkh_count_lbl.place(x=self.n_window_width-270, y=45)
        farkh_count_entry = Entry(warak_frame, textvariable=self.farkh_countVar, bd=2, bg='white', justify='right', font=(self.Font_Family, 13))
        farkh_count_entry.place(x=self.n_window_width-350, y=45, width=70, height=25)
        salary1_lbl = Label(warak_frame, text=' : السعر', bg='white', font=(self.Font_Family, 15))
        salary1_lbl.place(x=self.n_window_width-470, y=45)
        salary1_entry = Entry(warak_frame, textvariable=self.salaryVar1, bd=2, bg='white', justify='right', font=(self.Font_Family, 13))
        salary1_entry.place(x=self.n_window_width-540, y=47, width=70, height=25)
        type_lbl = Label(warak_frame, text=' : نوع', bg='white', font=(self.Font_Family, 15))
        type_lbl.place(x=self.n_window_width-65, y=80)
        self.type_combo1 = ttk.Combobox(warak_frame, textvariable=self.typeVar1, values=['كوشيه', 'طبع', 'استيكر', 'دوبلكس', 'برستول كوشيه'], state='readonly', justify='center', font=(self.Font_Family, 12, 'bold'))
        self.type_combo1.place(x=self.n_window_width-175, y=87, width=110, height=25)
        self.type_combo1.bind("<<ComboboxSelected>>", self.combo_selected)
        self.type_combo2 = ttk.Combobox(warak_frame, textvariable=self.typeVar2, state='normal', justify='center', font=(self.Font_Family, 12, 'bold'))
        self.type_combo2.place(x=self.n_window_width-305, y=87, width=110, height=25)
        size_lbl = Label(warak_frame, text=' : مقاس القص', bg='white', font=(self.Font_Family, 15))
        size_lbl.place(x=self.n_window_width-420, y=80)
        size_entry_1 = Entry(warak_frame, textvariable=self.sizeVar1, bd=2, bg='white', justify='center', font=(self.Font_Family, 13))
        size_entry_1.place(x=self.n_window_width-465, y=87, width=40, height=20)
        size_x_lbl = Label(warak_frame, text='X', bg='white', font=(self.Font_Family, 15))
        size_x_lbl.place(x=self.n_window_width-480, y=82)
        size_entry_2 = Entry(warak_frame, textvariable=self.sizeVar2, bd=2, bg='white', justify='center', font=(self.Font_Family, 13))
        size_entry_2.place(x=self.n_window_width-520, y=87, width=40, height=20)

        zenk_frame = Frame(self.n_window, bg='white')
        zenk_frame.place(x=0, y=230, width=self.n_window_width, height=90)
        zenk_lbl = Label(zenk_frame, text='الزنك', bg=self.lbl_bg, fg='white', font=(self.Font_Family, 18, 'bold'))
        zenk_lbl.pack(fill=X)
        taraf_lbl = Label(zenk_frame, text=' : طرف', bg='white', font=(self.Font_Family, 15))
        taraf_lbl.place(x=self.n_window_width-65, y=50)
        self.taraf_combo = ttk.Combobox(zenk_frame, textvariable=self.tarafVar2, style='MyCustomStyleName.TCombobox', values=('المطبعة', 'العميل'), justify='center', state='readonly', font=(self.Font_Family))
        self.taraf_combo.place(x=self.n_window_width-165, y=50, width=100)
        self.taraf_combo.bind("<<ComboboxSelected>>", self.taraf_combo_selected)
        zenk_count_lbl = Label(zenk_frame, text=' : عدد الزنك', bg='white', font=(self.Font_Family, 15))
        zenk_count_lbl.place(x=self.n_window_width-280, y=50)
        zenk_count_entry = Entry(zenk_frame, textvariable=self.zenk_countVar, bd=2, bg='white', justify='right', font=(self.Font_Family, 13))
        zenk_count_entry.place(x=self.n_window_width-350, y=50, width=70, height=25)
        salary2_lbl = Label(zenk_frame, text=' : السعر', bg='white', font=(self.Font_Family, 15))
        salary2_lbl.place(x=self.n_window_width-470, y=50)
        salary2_entry = Entry(zenk_frame, textvariable=self.salaryVar2, bd=2, bg='white', justify='right', font=(self.Font_Family, 13))
        salary2_entry.place(x=self.n_window_width-540, y=55, width=70, height=25)
        self.salaryVar2.set(42.5)

        self.print_frame = Frame(self.n_window, bg='white')
        self.print_frame.place(x=0, y=325, width=self.n_window_width, height=160)
        print_lbl = Label(self.print_frame, text='الطباعة', bg=self.lbl_bg, fg='white', font=(self.Font_Family, 18, 'bold'))
        print_lbl.pack(fill=X)
        sahba_count_lbl = Label(self.print_frame, text=' : عدد السحبات', bg='white', font=(self.Font_Family, 15))
        sahba_count_lbl.place(x=self.n_window_width-140, y=45)
        sahba_count_entry = Entry(self.print_frame, textvariable=self.sahba_countVar, bd=2, bg='white', justify='right', font=(self.Font_Family, 13))
        sahba_count_entry.place(x=self.n_window_width-210, y=45, width=70, height=25)
        sahba_count_entry_2 = Entry(self.print_frame, textvariable=self.sahba2_countVar, bd=2, bg='white', justify='right', font=(self.Font_Family, 13))
        sahba_count_entry_2.place(x=self.n_window_width-300, y=45, width=70, height=25)
        tt_lbl = Label(self.print_frame, text='تطبع و تقلب', bg='white', font=(self.Font_Family, 15))
        tt_lbl.place(x=self.n_window_width-470, y=45)
        ckb_1 = ttk.Checkbutton(self.print_frame, variable=self.Check_btn_fb_var, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.big_size).place(x=self.n_window_width-500, y=47)
        colors_lbl = Label(self.print_frame, text=' : الالوان', bg='white', font=(self.Font_Family, 15)).place(x=self.n_window_width-80, y=80)
        colors_frame_width = (self.n_window_width-80)-(self.n_window_width-500)+50
        colors_frame = Frame(self.print_frame, bg='silver', highlightbackground='black', highlightcolor='black', highlightthickness=1)
        colors_frame.place(x=5, y=85, width=colors_frame_width, height=30)
        color_k = Label(colors_frame, text='K', bg='silver', font=(self.Font_Family, 15, 'bold'))
        color_k.place(x=colors_frame_width-25, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-35, width=1, height=30)
        color_Y = Label(colors_frame, text='Y', bg='silver', font=(self.Font_Family, 15, 'bold'))
        color_Y.place(x=colors_frame_width-60, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-70, width=1, height=30)
        color_M = Label(colors_frame, text='M', bg='silver', font=(self.Font_Family, 15, 'bold'))
        color_M.place(x=colors_frame_width-98, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-105, width=1, height=30)
        color_C = Label(colors_frame, text='C', bg='silver', font=(self.Font_Family, 15, 'bold'))
        color_C.place(x=colors_frame_width-130, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-135, width=1, height=30)
        color_z = Label(colors_frame, text='ذهبي', bg='silver', font=(self.Font_Family, 13, 'bold'))
        color_z.place(x=colors_frame_width-177, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-182, width=1, height=30)
        color_f = Label(colors_frame, text='فضي', bg='silver', font=(self.Font_Family, 13, 'bold'))
        color_f.place(x=colors_frame_width-220, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-222, width=1, height=30)
        color_s = Label(colors_frame, text='صبغة', bg='silver', font=(self.Font_Family, 13, 'bold'))
        color_s.place(x=colors_frame_width-270, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-272, width=1, height=30)
        color_w = Label(colors_frame, text='ورنيش', bg='silver', font=(self.Font_Family, 13, 'bold'))
        color_w.place(x=colors_frame_width-325, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-330, width=1, height=30)
        color_k = Label(colors_frame, text='كحلي', bg='silver', font=(self.Font_Family, 13, 'bold'))
        color_k.place(x=colors_frame_width-375, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-380, width=1, height=30)
        color_SP = Label(colors_frame, text='اسبيشيال', bg='silver', font=(self.Font_Family, 13, 'bold'))
        color_SP.place(x=10, y=2, height=20)
        fase_lbl = Label(self.print_frame, text=' : وجه', bg='white', font=(self.Font_Family, 15))
        fase_lbl.place(x=self.n_window_width-80, y=120)
        fase_frame = Frame(self.print_frame, bg='white')
        fase_frame.place(x=95, y=125, width=colors_frame_width-90, height=20)
        cb_k1 = ttk.Checkbutton(fase_frame, variable=self.cb_K_Var1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.K).place(x=(colors_frame_width-90)-25, y=0)
        cb_y1 = ttk.Checkbutton(fase_frame, variable=self.cb_Y_Var1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.Y).place(x=(colors_frame_width-90)-60, y=0)
        cb_m1 = ttk.Checkbutton(fase_frame, variable=self.cb_M_Var1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.M).place(x=(colors_frame_width-90)-98, y=0)
        cb_c1 = ttk.Checkbutton(fase_frame, variable=self.cb_C_Var1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.C).place(x=(colors_frame_width-90)-130, y=0)
        cb_zahabi1 = ttk.Checkbutton(fase_frame, variable=self.cb_zahabi_Var1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.Zahabi).place(x=(colors_frame_width-90)-170, y=0)
        cb_faddi1 = ttk.Checkbutton(fase_frame, variable=self.cb_faddi_Var1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.faddi).place(x=(colors_frame_width-90)-215, y=0)
        cb_sapgha1 = ttk.Checkbutton(fase_frame, variable=self.cb_sapgha_Var1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.sapgha).place(x=(colors_frame_width-90)-260, y=0)
        cb_warnish1 = ttk.Checkbutton(fase_frame, variable=self.cb_warnish_Var1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.warnish).place(x=(colors_frame_width-90)-310, y=0)
        cb_kohley1 = ttk.Checkbutton(fase_frame, variable=self.cb_kohley_Var1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.kohley).place(x=(colors_frame_width-90)-360, y=0)
        s1_entry = Entry(self.print_frame, textvariable=self.sVar1, bd=2, justify='center', font=(self.Font_Family, 12, 'bold'))
        s1_entry.place(x=5, y=127, width=80, height=20)

        back_lbl = Label(self.print_frame, text=' : ظهر', bg='white', font=(self.Font_Family, 15))
        back_lbl.place(x=self.n_window_width-80, y=160)
        back_frame = Frame(self.print_frame, bg='white')
        back_frame.place(x=95, y=165, width=colors_frame_width-90, height=20)
        ckb_k2 = ttk.Checkbutton(back_frame, variable=self.cb_K_Var2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.K).place(x=(colors_frame_width-90)-25, y=0)
        ckb_y2 = ttk.Checkbutton(back_frame, variable=self.cb_Y_Var2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.Y).place(x=(colors_frame_width-90)-60, y=0)
        ckb_m2 = ttk.Checkbutton(back_frame, variable=self.cb_M_Var2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.M).place(x=(colors_frame_width-90)-98, y=0)
        ckb_c2 = ttk.Checkbutton(back_frame, variable=self.cb_C_Var2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.C).place(x=(colors_frame_width-90)-130, y=0)
        ckb_zahabi2 = ttk.Checkbutton(back_frame, variable=self.cb_zahabi_Var2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.Zahabi).place(x=(colors_frame_width-90)-170, y=0)
        ckb_faddi2 = ttk.Checkbutton(back_frame, variable=self.cb_faddi_Var2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.faddi).place(x=(colors_frame_width-90)-215, y=0)
        ckb_sapgha2 = ttk.Checkbutton(back_frame, variable=self.cb_sapgha_Var2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.sapgha).place(x=(colors_frame_width-90)-260, y=0)
        ckb_warnish2 = ttk.Checkbutton(back_frame, variable=self.cb_warnish_Var2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.warnish).place(x=(colors_frame_width-90)-310, y=0)
        ckb_kohley2 = ttk.Checkbutton(back_frame, variable=self.cb_kohley_Var2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.kohley).place(x=(colors_frame_width-90)-360, y=0)
        s2_entry = Entry(self.print_frame, textvariable=self.sVar2, bd=2, bg='white', justify='center', font=(self.Font_Family, 12, 'bold'))
        s2_entry.place(x=5, y=167, width=80, height=20)

        self.fin_frame = Frame(self.n_window, bg='white')
        self.fin_frame.place(x=0, y=490, width=self.n_window_width, height=535)
        fin_lbl = Label(self.fin_frame, text='التجليد و التشطيب', bg=self.lbl_bg, fg='white', font=(self.Font_Family, 18, 'bold'))
        fin_lbl.pack(fill=X)
        daftar_count_lbl = Label(self.fin_frame, text='عدد الدفاتر', bg='white', font=(self.Font_Family, 15))
        daftar_count_lbl.place(x=self.n_window_width-100, y=43)
        groups_count_lbl = Label(self.fin_frame, text='المجموعات', bg='white', font=(self.Font_Family, 15))
        groups_count_lbl.place(x=self.n_window_width-222, y=43)
        counter_lbl = Label(self.fin_frame, text='الترتيب', bg='white', font=(self.Font_Family, 15))
        counter_lbl.place(x=self.n_window_width-350, y=43)
        num_of_count_lbl = Label(self.fin_frame, text='الترقيم', bg='white', font=(self.Font_Family, 15))
        num_of_count_lbl.place(x=self.n_window_width-475, y=43)
        entries_frame = Frame(self.fin_frame, bg='silver', highlightthickness=1, highlightbackground='black', highlightcolor='black')
        entries_frame.place(x=5, y=75, width=self.n_window_width-10, height=30)
        entry_1 = Entry(entries_frame, textvariable=self.daftar_countVar, bd=2, bg='white', justify='center', font=(self.Font_Family, 13))
        entry_1.place(x=self.n_window_width-100, y=5, width=70, height=20)
        sep_1 = Frame(entries_frame, bg='black')
        sep_1.place(x=self.n_window_width-125, width=1, height=30)
        combo_2 = ttk.Combobox(entries_frame, textvariable=self.groups_countVar, values=['25', '33', '50', '100' ,'150' ,'200'], state='readonly', justify='center', font=(self.Font_Family, 11, 'bold'))
        combo_2.place(x=self.n_window_width-220, y=5, width=70, height=20)
        sep_2 = Frame(entries_frame, bg='black')
        sep_2.place(x=self.n_window_width-250, width=1, height=30)
        counter_combo = ttk.Combobox(entries_frame, textvariable=self.counterVar, values=('اول', 'اول + اخير', 'اول + وسط + اخير', 'اول + 2وسط + اخير', 'اول + 3وسط + اخير'), justify='center', state='readonly', font=(self.Font_Family, 10, 'bold'))
        counter_combo.place(x=self.n_window_width-377, y=5, width=120, height=20)
        sep_3 = Frame(entries_frame, bg='black')
        sep_3.place(x=self.n_window_width-385, width=1, height=30)
        num_of_count_lbl_1 = Label(entries_frame, text=' : من', bg='silver', fg='black', font=(self.Font_Family, 13))
        num_of_count_lbl_1.place(x=self.n_window_width-430, y=0)
        num_of_count_entry_1 = Entry(entries_frame, textvariable=self.num_of_countVar1, bd=2, bg='white', justify='center', font=(self.Font_Family, 13))
        num_of_count_entry_1.place(x=self.n_window_width-520, y=5, width=90, height=20)

        label_slofan = Label(self.fin_frame, text=' سلوفان', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-65, y=110)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.slofanCkb_SAVEVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.n_window_width-90, y=117)
        combo_box = ttk.Combobox(self.fin_frame, textvariable=self.slofan_SAVEVar, values=['مط', 'لامع'], state='readonly', justify='center',font=(self.Font_Family, 13, 'bold')).place(x=self.n_window_width-195, y=115, width=100, height=25)
        label = Label(self.fin_frame, text=' : الجهه', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-260, y=110)
        combo_box = ttk.Combobox(self.fin_frame, textvariable=self.gha_SAVEVar, values=['وجه واحد', 'وجهين'], state='readonly', justify='center',font=(self.Font_Family, 13, 'bold')).place(x=self.n_window_width-360, y=115, width=100, height=25)
        label = Label(self.fin_frame, text=' : العدد النهائي', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-470, y=110)
        entry = Entry(self.fin_frame, textvariable=self.slofanFinNum_SAVEVar, bd=2, justify='center',font=(self.Font_Family, 15)).place(x=self.n_window_width-540, y=115, width=70, height=25)

        label_UV = Label(self.fin_frame, text=' U.V', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-65, y=145)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.UVCkb_SAVEVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.n_window_width-90, y=152)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.UV_SAVEVar, justify='center',font=(self.Font_Family, 15)).place(x=self.n_window_width-195, y=150, width=100, height=25)
        label = Label(self.fin_frame, text=' : العدد النهائي', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-470, y=145)
        entry = Entry(self.fin_frame, textvariable=self.UVFinNum_SaveVar, bd=2, justify='center',font=(self.Font_Family, 15)).place(x=self.n_window_width-540, y=150, width=70, height=25)
        
        label_taksir = Label(self.fin_frame, text=' تكسير', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-65, y=110+70)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.taksirCkb_SAVEVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.n_window_width-90, y=115+70)
        self.combo_box = ttk.Combobox(self.fin_frame, textvariable=self.taksir_SAVEVar, values=['كامل', 'نصف تكسيره', 'ريجه'], state='readonly', justify='center',font=(self.Font_Family, 13, 'bold'))
        self.combo_box.place(x=self.n_window_width-195, y=115+70, width=100, height=25)
        self.combo_box.bind("<<ComboboxSelected>>", self.taksir_combo_selected)
        label = Label(self.fin_frame, text=' : العدد', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-260, y=110+70)
        entry = Entry(self.fin_frame, textvariable=self.taksirNum_SAVEVar, bd=2, justify='center',font=(self.Font_Family, 15)).place(x=self.n_window_width-360, y=115+70, width=100, height=25)
        label_forma = Label(self.fin_frame, text=' فورمة', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-445, y=110+70)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.formaCkb_SAVEVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.n_window_width-465, y=117+70)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.forma_SAVEVar, justify='center',font=(self.Font_Family, 15)).place(x=self.n_window_width-540, y=115+70, width=70, height=25)

        label_spot = Label(self.fin_frame, text=' اسبوت', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-65, y=180+30)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.spotCkb_SAVEVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.n_window_width-90, y=180+40)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.spot_SAVEVar, justify='center', font=(self.Font_Family, 15)).place(x=self.n_window_width-195, y=180+40, width=100, height=25)
        label_film_spot = Label(self.fin_frame, text=' فيلم ', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-445, y=180+30)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.filmCkb_SAVEVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.n_window_width-465, y=180+40)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.film_SAVEVar, justify='center',font=(self.Font_Family, 15)).place(x=self.n_window_width-540, y=180+40, width=70, height=25)
        
        label_forma = Label(self.fin_frame, text=' اكلاشيه', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-65, y=140+70+40)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.aklashehCkb_SAVEVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.n_window_width-90, y=140+70+45)
        combo_box = ttk.Combobox(self.fin_frame, textvariable=self.aklasheh_SAVEVar, values=['بصمة' , 'كوفراج', 'بصمه وكوفراج'], state='readonly', justify='center',font=(self.Font_Family, 13, 'bold')).place(x=self.n_window_width-195, y=140+70+46, width=100, height=25)
        label = Label(self.fin_frame, text=' : السعر', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-260, y=140+70+40)
        entry = Entry(self.fin_frame, textvariable=self.aklashehSal_SAVEVar, bd=2, justify='center', font=(self.Font_Family, 15)).place(x=self.n_window_width-360, y=140+70+45, width=100, height=25)
        label_film_spot = Label(self.fin_frame, text=' بصمه ', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-445, y=140+70+40)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.pasmaCkb_SAVEVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.n_window_width-465, y=140+70+45)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.pasma_SAVEVar, justify='center',font=(self.Font_Family, 15)).place(x=self.n_window_width-540, y=145+70+40, width=70, height=25)
        
        label_taglid = Label(self.fin_frame, text=' تجليد', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-65, y=140+70+75)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.taglidCkb_SAVEVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.n_window_width-90, y=140+70+80)
        combo_box = ttk.Combobox(self.fin_frame, textvariable=self.taglid_SAVEVar, values=['كرتون', 'لف', 'لطش', 'دبوس', 'لصق بونطه', 'غراء'], state='readonly', justify='center',font=(self.Font_Family, 13, 'bold')).place(x=self.n_window_width-195, y=140+70+80, width=100, height=25)
        label = Label(self.fin_frame, text=' : العدد', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-260, y=140+70+75)
        entry = Entry(self.fin_frame, textvariable=self.taglidNum_SAVEVar, bd=2, justify='center', font=(self.Font_Family, 15)).place(x=self.n_window_width-360, y=140+70+80, width=100, height=25)
        label = Label(self.fin_frame, text=' : السعر', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-465, y=140+70+75)
        entry = Entry(self.fin_frame, textvariable=self.taglidSal_SAVEVar, bd=2, justify='center',font=(self.Font_Family, 15)).place(x=self.n_window_width-540, y=140+70+80, width=70, height=25)

        label_tawdib = Label(self.fin_frame, text=' توضيب', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-65, y=235+85)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.tawdibCkb_SAVEVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.n_window_width-90, y=240+85)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.tawdib_SAVEVar, justify='center',font=(self.Font_Family, 15)).place(x=self.n_window_width-195, y=240+85, width=100, height=25)
        label_tasmim = Label(self.fin_frame, text=' تصميم', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-260, y=235+85)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.tasmimCkb_SAVEVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.n_window_width-285, y=240+85)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.tasmim_SAVEVar, justify='center',font=(self.Font_Family, 15)).place(x=self.n_window_width-360, y=240+85, width=70, height=25)
        label_slk = Label(self.fin_frame, text=' سلك', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-445, y=235+85)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.slkCkb_SAVEVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.n_window_width-465, y=240+85)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.slk_SAVEVar, justify='center',font=(self.Font_Family, 15)).place(x=self.n_window_width-540, y=240+85, width=70, height=25)

        label_nakl = Label(self.fin_frame, text=' نقل', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-65, y=235+70+50)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.naklCkb_SAVEVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.n_window_width-90, y=240+70+50)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.nakl_SAVEVar, justify='center',font=(self.Font_Family, 15)).place(x=self.n_window_width-195, y=240+70+50, width=100, height=25)
        label_khadmat = Label(self.fin_frame, text=' خدمات', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-260, y=235+70+50)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.khadmatCkb_SAVEVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.n_window_width-285, y=240+70+50)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.khadmat_SAVEVar, justify='center',font=(self.Font_Family, 15)).place(x=self.n_window_width-360, y=240+70+50, width=70, height=25)
        label_kas = Label(self.fin_frame, text=' قص', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.n_window_width-445, y=235+70+50)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.kasCkb_SAVEVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.n_window_width-465, y=240+70+50)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.kas_SAVEVar, justify='center',font=(self.Font_Family, 15)).place(x=self.n_window_width-540, y=240+70+50, width=70, height=25)
        
        sep = Frame(self.fin_frame, bg=self.lbl_bg, width=160, height=6).pack(fill=X, pady=(355, 0))
        
        control_btns_frame = Frame(self.n_window, bg='white')
        control_btns_frame.place(x=0, y=715+200, width=self.n_window_width, height=100)
        show_total_entry = Entry(control_btns_frame, textvariable=self.f_totalVar, state='readonly', bd=2, fg='black', justify='center',font=(self.Font_Family, 17, 'bold'))
        show_total_entry.place(x=self.n_window_width-150, y=10, width=100, height=40)
        add_btn = CTkButton(self.n_window, text='حفظ الفاتورة', 
                            bg_color='white',
                            text_color='white', 
                            cursor='hand2',
                            font=(self.Font_Family, 22),
                            border_width=2,
                            border_color='silver',
                            corner_radius=10,
                            width=70,
                            height=40,
                            command=self.new_fatora)
        add_btn.place(x=self.n_window_width-335, y=10)
        f_reset_btn = CTkButton(control_btns_frame, text='إفراغ',
                                text_color='white', 
                                bg_color='white',
                                cursor='hand2',
                                font=(self.Font_Family, 22),
                                border_width=2,
                                border_color='silver',
                                corner_radius=10,
                                width=70,
                                height=40,
                                command=self.FfromNewOne)
        f_reset_btn.place(x=self.n_window_width-415, y=10)
        cancel_btn = CTkButton(control_btns_frame, text='إلغاء',
                               bg_color='white',
                               fg_color='red',
                               hover_color='#E30004', 
                               text_color='white', 
                                cursor='hand2',
                                font=(self.Font_Family, 22),
                                border_width=2,
                                border_color='grey',
                                corner_radius=10,
                                width=70,
                                height=40,
                            command=self.destroy_func1)
        cancel_btn.place(x=self.n_window_width-495, y=10)
        self.show_salaries()

    # ===================================================================================
    # Show Client Work Funcation
    def Show_Fatora(self):
        self.s_window = Toplevel()
        self.s_window.title('تحرير فاتورة')
        self.s_window.config(background='silver')
        self.s_window_width = 550
        self.s_window_hieght = self.work_window_height + 90
        self.s_window.geometry(f'{self.s_window_width}x{self.winfo_screenheight()-100}+33+10')
        # Check CTkButtons Style
        ttk.Style().configure('Custom.TCheckbutton', background = 'white')

        # Fetch The Name Of the fatora of the client in the list
        self.client_name = self.searchVar.get()

        db = sqlite3.connect(f'Project_files/Clients Work/{self.client_name}/Fawatir.db')
        cr = db.cursor()

        cr.execute('Select f_name from All_fatora')
        names = cr.fetchall()
        Client_fatora_names = []

        for name in names:
            for f_name in name:
                Client_fatora_names.append(f_name)

        db.commit()
        db.close()

        work_info_frame = Frame(self.s_window, bg='white')
        work_info_frame.place(x=0, y=0, width=self.s_window_width, height=100)
        name_of_work_lbl = Label(work_info_frame, text=' : اسم العملية', bg='white', font=(self.Font_Family, 15))
        name_of_work_lbl.place(x=self.s_window_width-110, y=55)
        client_name = Label(work_info_frame, text='----------> ' + str(self.searchVar.get()) + ' <----------', bg='white', fg='black', font=(self.Font_Family, 17, 'bold')).pack(pady=5)
        self.name_of_work_entry = Entry(work_info_frame, textvariable=self.f_nameSHOWVar, bd=2, bg='white', justify='right', font=(self.Font_Family, 13))
        self.name_of_work_entry.place(x=self.s_window_width-310, y=60, width=200, height=25)
        date_of_work_lbl = Label(work_info_frame, text=' : التاريخ', bg='white', font=(self.Font_Family, 15))
        date_of_work_lbl.place(x=self.s_window_width-400, y=55)
        self.day_of_work_entry1 = Entry(work_info_frame, textvariable=self.e1_dateSHOWVar, bg='white', justify='center', font=(self.Font_Family, 12))
        self.month_of_work_entry2 = Entry(work_info_frame, textvariable=self.e2_dateSHOWVar, bg='white', justify='center', font=(self.Font_Family, 12))
        self.year_of_work_entry3 = Entry(work_info_frame, textvariable=self.e3_dateSHOWVar, bg='white', justify='center', font=(self.Font_Family, 12))
        slash_1 = Label(work_info_frame, text='/', bg='white', font=(self.Font_Family, 15))
        slash_2 = Label(work_info_frame, text='/', bg='white', font=(self.Font_Family, 15))
        self.day_of_work_entry1.place(x=self.s_window_width-425, y=60, width=25, height=20)
        slash_1.place(x=self.s_window_width-435, y=55)
        self.month_of_work_entry2.place(x=self.s_window_width-460, y=60, width=25, height=20)
        slash_2.place(x=self.s_window_width-470, y=55)
        self.year_of_work_entry3.place(x=self.s_window_width-520, y=60, width=50, height=20)

        warak_frame = Frame(self.s_window, bg='white')
        warak_frame.place(x=0, y=105, width=self.s_window_width, height=120)
        warak_lbl = Label(warak_frame, text='الورق', bg=self.lbl_bg, fg='white', font=(self.Font_Family, 18, 'bold'))
        warak_lbl.pack(fill=X)
        taraf_lbl = Label(warak_frame, text=' : طرف', bg='white', font=(self.Font_Family, 15))
        taraf_lbl.place(x=self.s_window_width-65, y=45)
        taraf_combo = ttk.Combobox(warak_frame, textvariable=self.tarafSHOWVar1, values=('المطبعة', 'العميل'), justify='center', state='readonly', font=(self.Font_Family))
        taraf_combo.place(x=self.s_window_width-165, y=45, width=100)
        farkh_count_lbl = Label(warak_frame, text=' : عدد الأفرخ', bg='white', font=(self.Font_Family, 15))
        farkh_count_lbl.place(x=self.s_window_width-270, y=45)
        farkh_count_entry = Entry(warak_frame, textvariable=self.farkh_countSHOWVar, bd=2, bg='white', justify='right', font=(self.Font_Family, 13))
        farkh_count_entry.place(x=self.s_window_width-350, y=45, width=70, height=25)
        salary1_lbl = Label(warak_frame, text=' : السعر', bg='white', font=(self.Font_Family, 15))
        salary1_lbl.place(x=self.s_window_width-450, y=45)
        salary1_entry = Entry(warak_frame, textvariable=self.salarySHOWVar1, bd=2, bg='white', justify='right', font=(self.Font_Family, 13))
        salary1_entry.place(x=self.s_window_width-520, y=47, width=70, height=25)
        type_lbl = Label(warak_frame, text=' : نوع', bg='white', font=(self.Font_Family, 15))
        type_lbl.place(x=self.s_window_width-65, y=80)
        self.type_combo1 = ttk.Combobox(warak_frame, textvariable=self.typeSHOWVar1, values=['كوشيه', 'طبع', 'استيكر', 'دوبلكس', 'برستول كوشيه'], state='readonly', justify='center', font=(self.Font_Family, 12, 'bold'))
        self.type_combo1.place(x=self.s_window_width-175, y=87, width=110, height=25)
        self.type_combo1.bind("<<ComboboxSelected>>", self.combo_selected2)
        self.type_combo2 = ttk.Combobox(warak_frame, textvariable=self.typeSHOWVar2, state='normal', justify='center', font=(self.Font_Family, 12, 'bold'))
        self.type_combo2.place(x=self.s_window_width-305, y=87, width=110, height=25)
        size_lbl = Label(warak_frame, text=' : مقاس القص', bg='white', font=(self.Font_Family, 15))
        size_lbl.place(x=self.s_window_width-420, y=80)
        size_entry_1 = Entry(warak_frame, textvariable=self.sizeSHOWVar1, bd=2, bg='white', justify='center', font=(self.Font_Family, 13))
        size_entry_1.place(x=self.s_window_width-465, y=87, width=40, height=20)
        size_x_lbl = Label(warak_frame, text='X', bg='white', font=(self.Font_Family, 15))
        size_x_lbl.place(x=self.s_window_width-480, y=82)
        size_entry_2 = Entry(warak_frame, textvariable=self.sizeSHOWVar2, bd=2, bg='white', justify='center', font=(self.Font_Family, 13))
        size_entry_2.place(x=self.s_window_width-520, y=87, width=40, height=20)

        zenk_frame = Frame(self.s_window, bg='white')
        zenk_frame.place(x=0, y=230, width=self.s_window_width, height=90)
        zenk_lbl = Label(zenk_frame, text='الزنك', bg=self.lbl_bg, fg='white', font=(self.Font_Family, 18, 'bold'))
        zenk_lbl.pack(fill=X)
        taraf_lbl = Label(zenk_frame, text=' : طرف', bg='white', font=(self.Font_Family, 15))
        taraf_lbl.place(x=self.s_window_width-65, y=50)
        self.taraf_combo = ttk.Combobox(zenk_frame, textvariable=self.tarafSHOWVar2, values=('المطبعة', 'العميل'), justify='center', state='readonly', font=(self.Font_Family))
        self.taraf_combo.place(x=self.s_window_width-165, y=50, width=100)
        self.taraf_combo.bind("<<ComboboxSelected>>", self.taraf_combo_selected)
        zenk_count_lbl = Label(zenk_frame, text=' : عدد الزنك', bg='white', font=(self.Font_Family, 15))
        zenk_count_lbl.place(x=self.s_window_width-280, y=50)
        zenk_count_entry = Entry(zenk_frame, textvariable=self.zenk_countSHOWVar, bd=2, bg='white', justify='right', font=(self.Font_Family, 13))
        zenk_count_entry.place(x=self.s_window_width-350, y=50, width=70, height=25)
        salary2_lbl = Label(zenk_frame, text=' : السعر', bg='white', font=(self.Font_Family, 15))
        salary2_lbl.place(x=self.s_window_width-450, y=50)
        salary2_entry = Entry(zenk_frame, textvariable=self.salarySHOWVar2, bd=2, bg='white', justify='right', font=(self.Font_Family, 13))
        salary2_entry.place(x=self.s_window_width-520, y=50, width=70, height=25)
        self.salaryVar2.set(42.5)

        self.print_frame = Frame(self.s_window, bg='white')
        self.print_frame.place(x=0, y=325, width=self.s_window_width, height=160)
        print_lbl = Label(self.print_frame, text='الطباعة', bg=self.lbl_bg, fg='white', font=(self.Font_Family, 18, 'bold'))
        print_lbl.pack(fill=X)
        sahba_count_lbl = Label(self.print_frame, text=' : عدد السحبات', bg='white', font=(self.Font_Family, 15))
        sahba_count_lbl.place(x=self.s_window_width-140, y=45)
        sahba_count_entry = Entry(self.print_frame, textvariable=self.sahba_countSHOWVar, bd=2, bg='white', justify='right', font=(self.Font_Family, 13))
        sahba_count_entry.place(x=self.s_window_width-210, y=45, width=70, height=25)
        sahba_count_entry_2 = Entry(self.print_frame, textvariable=self.sahba2_countSHOWVar, bd=2, bg='white', justify='right', font=(self.Font_Family, 13))
        sahba_count_entry_2.place(x=self.s_window_width-300, y=45, width=70, height=25)
        tt_lbl = Label(self.print_frame, text='تطبع و تقلب', bg='white', font=(self.Font_Family, 15))
        tt_lbl.place(x=self.s_window_width-470, y=45)
        ckb_1 = ttk.Checkbutton(self.print_frame, variable=self.Check_btn_fb_SHOWVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.big_size_2).place(x=self.s_window_width-500, y=47)
        colors_lbl = Label(self.print_frame, text=' : الالوان', bg='white', font=(self.Font_Family, 15)).place(x=self.s_window_width-80, y=80)
        colors_frame_width = (self.s_window_width-80)-(self.s_window_width-500)+50
        colors_frame = Frame(self.print_frame, bg='silver', highlightbackground='black', highlightcolor='black', highlightthickness=1)
        colors_frame.place(x=5, y=85, width=colors_frame_width, height=30)
        color_k = Label(colors_frame, text='K', bg='silver', font=(self.Font_Family, 15, 'bold'))
        color_k.place(x=colors_frame_width-25, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-35, width=1, height=30)
        color_Y = Label(colors_frame, text='Y', bg='silver', font=(self.Font_Family, 15, 'bold'))
        color_Y.place(x=colors_frame_width-60, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-70, width=1, height=30)
        color_M = Label(colors_frame, text='M', bg='silver', font=(self.Font_Family, 15, 'bold'))
        color_M.place(x=colors_frame_width-98, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-105, width=1, height=30)
        color_C = Label(colors_frame, text='C', bg='silver', font=(self.Font_Family, 15, 'bold'))
        color_C.place(x=colors_frame_width-130, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-135, width=1, height=30)
        color_z = Label(colors_frame, text='ذهبي', bg='silver', font=(self.Font_Family, 13, 'bold'))
        color_z.place(x=colors_frame_width-177, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-182, width=1, height=30)
        color_f = Label(colors_frame, text='فضي', bg='silver', font=(self.Font_Family, 13, 'bold'))
        color_f.place(x=colors_frame_width-220, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-222, width=1, height=30)
        color_s = Label(colors_frame, text='صبغة', bg='silver', font=(self.Font_Family, 13, 'bold'))
        color_s.place(x=colors_frame_width-270, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-272, width=1, height=30)
        color_w = Label(colors_frame, text='ورنيش', bg='silver', font=(self.Font_Family, 13, 'bold'))
        color_w.place(x=colors_frame_width-325, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-330, width=1, height=30)
        color_k = Label(colors_frame, text='كحلي', bg='silver', font=(self.Font_Family, 13, 'bold'))
        color_k.place(x=colors_frame_width-375, y=2, height=20)
        sep = Frame(colors_frame, bg='black')
        sep.place(x=colors_frame_width-380, width=1, height=30)
        color_SP = Label(colors_frame, text='اسبيشيال', bg='silver', font=(self.Font_Family, 13, 'bold'))
        color_SP.place(x=10, y=2, height=20)
        fase_lbl = Label(self.print_frame, text=' : وجه', bg='white', font=(self.Font_Family, 15))
        fase_lbl.place(x=self.s_window_width-80, y=120)
        fase_frame = Frame(self.print_frame, bg='white')
        fase_frame.place(x=95, y=125, width=colors_frame_width-90, height=20)
        cb_k1 = ttk.Checkbutton(fase_frame, variable=self.cb_K_SHOWVar1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.K).place(x=(colors_frame_width-90)-25, y=0)
        cb_y1 = ttk.Checkbutton(fase_frame, variable=self.cb_Y_SHOWVar1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.Y).place(x=(colors_frame_width-90)-60, y=0)
        cb_m1 = ttk.Checkbutton(fase_frame, variable=self.cb_M_SHOWVar1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.M).place(x=(colors_frame_width-90)-98, y=0)
        cb_c1 = ttk.Checkbutton(fase_frame, variable=self.cb_C_SHOWVar1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.C).place(x=(colors_frame_width-90)-130, y=0)
        cb_zahabi1 = ttk.Checkbutton(fase_frame, variable=self.cb_zahabi_SHOWVar1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.Zahabi).place(x=(colors_frame_width-90)-170, y=0)
        cb_faddi1 = ttk.Checkbutton(fase_frame, variable=self.cb_faddi_SHOWVar1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.faddi).place(x=(colors_frame_width-90)-215, y=0)
        cb_sapgha1 = ttk.Checkbutton(fase_frame, variable=self.cb_sapgha_SHOWVar1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.sapgha).place(x=(colors_frame_width-90)-260, y=0)
        cb_warnish1 = ttk.Checkbutton(fase_frame, variable=self.cb_warnish_SHOWVar1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.warnish).place(x=(colors_frame_width-90)-310, y=0)
        cb_kohley1 = ttk.Checkbutton(fase_frame, variable=self.cb_kohley_SHOWVar1, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.kohley).place(x=(colors_frame_width-90)-360, y=0)
        s1_entry = Entry(self.print_frame, textvariable=self.sSHOWVar1, bd=2, justify='center', font=(self.Font_Family, 12, 'bold'))
        s1_entry.place(x=5, y=127, width=80, height=20)

        back_lbl = Label(self.print_frame, text=' : ظهر', bg='white', font=(self.Font_Family, 15))
        back_lbl.place(x=self.s_window_width-80, y=160)
        back_frame = Frame(self.print_frame, bg='white')
        back_frame.place(x=95, y=165, width=colors_frame_width-90, height=20)
        ckb_k2 = ttk.Checkbutton(back_frame, variable=self.cb_K_SHOWVar2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.K).place(x=(colors_frame_width-90)-25, y=0)
        ckb_y2 = ttk.Checkbutton(back_frame, variable=self.cb_Y_SHOWVar2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.Y).place(x=(colors_frame_width-90)-60, y=0)
        ckb_m2 = ttk.Checkbutton(back_frame, variable=self.cb_M_SHOWVar2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.M).place(x=(colors_frame_width-90)-98, y=0)
        ckb_c2 = ttk.Checkbutton(back_frame, variable=self.cb_C_SHOWVar2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.C).place(x=(colors_frame_width-90)-130, y=0)
        ckb_zahabi2 = ttk.Checkbutton(back_frame, variable=self.cb_zahabi_SHOWVar2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.Zahabi).place(x=(colors_frame_width-90)-170, y=0)
        ckb_faddi2 = ttk.Checkbutton(back_frame, variable=self.cb_faddi_SHOWVar2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.faddi).place(x=(colors_frame_width-90)-215, y=0)
        ckb_sapgha2 = ttk.Checkbutton(back_frame, variable=self.cb_sapgha_SHOWVar2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.sapgha).place(x=(colors_frame_width-90)-260, y=0)
        ckb_warnish2 = ttk.Checkbutton(back_frame, variable=self.cb_warnish_SHOWVar2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.warnish).place(x=(colors_frame_width-90)-310, y=0)
        ckb_kohley2 = ttk.Checkbutton(back_frame, variable=self.cb_kohley_SHOWVar2, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0), command=self.kohley).place(x=(colors_frame_width-90)-360, y=0)
        s2_entry = Entry(self.print_frame, textvariable=self.sSHOWVar2, bd=2, bg='white', justify='center', font=(self.Font_Family, 12, 'bold'))
        s2_entry.place(x=5, y=167, width=80, height=20)

        self.fin_frame = Frame(self.s_window, bg='white')
        self.fin_frame.place(x=0, y=490, width=self.s_window_width, height=535)
        fin_lbl = Label(self.fin_frame, text='التجليد و التشطيب', bg=self.lbl_bg, fg='white', font=(self.Font_Family, 18, 'bold'))
        fin_lbl.pack(fill=X)
        daftar_count_lbl = Label(self.fin_frame, text='عدد الدفاتر', bg='white', font=(self.Font_Family, 15))
        daftar_count_lbl.place(x=self.s_window_width-100, y=43)
        groups_count_lbl = Label(self.fin_frame, text='المجموعات', bg='white', font=(self.Font_Family, 15))
        groups_count_lbl.place(x=self.s_window_width-222, y=43)
        counter_lbl = Label(self.fin_frame, text='الترتيب', bg='white', font=(self.Font_Family, 15))
        counter_lbl.place(x=self.s_window_width-350, y=43)
        num_of_count_lbl = Label(self.fin_frame, text='الترقيم', bg='white', font=(self.Font_Family, 15))
        num_of_count_lbl.place(x=self.s_window_width-475, y=43)
        entries_frame = Frame(self.fin_frame, bg='silver', highlightthickness=1, highlightbackground='black', highlightcolor='black')
        entries_frame.place(x=5, y=75, width=self.s_window_width-10, height=30)
        entry_1 = Entry(entries_frame, textvariable=self.daftar_countSHOWVar, bd=2, bg='white', justify='center', font=(self.Font_Family, 13))
        entry_1.place(x=self.s_window_width-100, y=5, width=70, height=20)
        sep_1 = Frame(entries_frame, bg='black')
        sep_1.place(x=self.s_window_width-125, width=1, height=30)
        combo_2 = ttk.Combobox(entries_frame, textvariable=self.groups_countSHOWVar, values=['25', '33', '50', '100' ,'150' ,'200'], state='readonly', justify='center', font=(self.Font_Family, 11, 'bold'))
        combo_2.place(x=self.s_window_width-220, y=5, width=70, height=20)
        sep_2 = Frame(entries_frame, bg='black')
        sep_2.place(x=self.s_window_width-250, width=1, height=30)
        counter_combo = ttk.Combobox(entries_frame, textvariable=self.counterSHOWVar, values=('اول', 'اول + اخير', 'اول + وسط + اخير', 'اول + 2وسط + اخير', 'اول + 3وسط + اخير'), justify='center', state='readonly', font=(self.Font_Family, 10, 'bold'))
        counter_combo.place(x=self.s_window_width-377, y=5, width=120, height=20)
        sep_3 = Frame(entries_frame, bg='black')
        sep_3.place(x=self.s_window_width-385, width=1, height=30)
        num_of_count_lbl_1 = Label(entries_frame, text=' : من', bg='silver', fg='black', font=(self.Font_Family, 13))
        num_of_count_lbl_1.place(x=self.s_window_width-430, y=0)
        num_of_count_entry_1 = Entry(entries_frame, textvariable=self.num_of_countSHOWVar1, bd=2, bg='white', justify='center', font=(self.Font_Family, 13))
        num_of_count_entry_1.place(x=self.s_window_width-520, y=5, width=90, height=20)

        label_slofan = Label(self.fin_frame, text=' سلوفان', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-65, y=110)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.slofanCkb_SHOWVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.s_window_width-90, y=117)
        combo_box = ttk.Combobox(self.fin_frame, textvariable=self.slofan_SHOWVar, values=['مط', 'لامع'], state='readonly', justify='center',font=(self.Font_Family, 13, 'bold')).place(x=self.s_window_width-195, y=115, width=100, height=25)
        label = Label(self.fin_frame, text=' : الجهه', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-260, y=110)
        combo_box = ttk.Combobox(self.fin_frame, textvariable=self.gha_SHOWVar, values=['وجه واحد', 'وجهين'], state='readonly', justify='center',font=(self.Font_Family, 13, 'bold')).place(x=self.s_window_width-360, y=115, width=100, height=25)
        label = Label(self.fin_frame, text=' : العدد النهائي', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-470, y=110)
        entry = Entry(self.fin_frame, textvariable=self.slofanFinNum_SHOWVar, bd=2, justify='center',font=(self.Font_Family, 15)).place(x=self.s_window_width-540, y=115, width=70, height=25)

        label_UV = Label(self.fin_frame, text=' U.V', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-65, y=145)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.UVCkb_SHOWVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.s_window_width-90, y=152)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.UV_SHOWVar, justify='center',font=(self.Font_Family, 15)).place(x=self.s_window_width-195, y=150, width=100, height=25)
        label = Label(self.fin_frame, text=' : العدد النهائي', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-470, y=145)
        entry = Entry(self.fin_frame, textvariable=self.UVFinNum_SHOWVar, bd=2, justify='center',font=(self.Font_Family, 15)).place(x=self.s_window_width-540, y=150, width=70, height=25)
        
        label_taksir = Label(self.fin_frame, text=' تكسير', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-65, y=110+70)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.taksirCkb_SHOWVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.s_window_width-90, y=115+70)
        self.combo_box = ttk.Combobox(self.fin_frame, textvariable=self.taksir_SHOWVar, values=['كامل', 'نصف تكسيره', 'ريجه'], state='readonly', justify='center',font=(self.Font_Family, 13, 'bold'))
        self.combo_box.place(x=self.s_window_width-195, y=115+70, width=100, height=25)
        self.combo_box.bind("<<ComboboxSelected>>", self.taksir_combo_selected2)
        label = Label(self.fin_frame, text=' : العدد', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-260, y=110+70)
        entry = Entry(self.fin_frame, textvariable=self.taksirNum_SHOWVar, bd=2, justify='center',font=(self.Font_Family, 15)).place(x=self.s_window_width-360, y=115+70, width=100, height=25)
        label_forma = Label(self.fin_frame, text=' فورمة', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-445, y=110+70)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.formaCkb_SHOWVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.s_window_width-465, y=117+70)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.forma_SHOWVar, justify='center',font=(self.Font_Family, 15)).place(x=self.s_window_width-540, y=115+70, width=70, height=25)

        label_spot = Label(self.fin_frame, text=' اسبوت', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-65, y=180+30)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.spotCkb_SHOWVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.s_window_width-90, y=180+40)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.spot_SHOWVar, justify='center', font=(self.Font_Family, 15)).place(x=self.s_window_width-195, y=180+40, width=100, height=25)
        label_film_spot = Label(self.fin_frame, text=' فيلم ', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-445, y=180+30)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.filmCkb_SHOWVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.s_window_width-465, y=180+40)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.film_SHOWVar, justify='center',font=(self.Font_Family, 15)).place(x=self.s_window_width-540, y=180+40, width=70, height=25)
        
        label_forma = Label(self.fin_frame, text=' اكلاشيه', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-65, y=140+70+40)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.aklashehCkb_SHOWVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.s_window_width-90, y=140+70+45)
        combo_box = ttk.Combobox(self.fin_frame, textvariable=self.aklasheh_SHOWVar, values=['بصمة' , 'كوفراج', 'بصمه وكوفراج'], state='readonly', justify='center',font=(self.Font_Family, 13, 'bold')).place(x=self.s_window_width-195, y=140+70+46, width=100, height=25)
        label = Label(self.fin_frame, text=' : السعر', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-260, y=140+70+40)
        entry = Entry(self.fin_frame, textvariable=self.aklashehSal_SHOWVar, bd=2, justify='center', font=(self.Font_Family, 15)).place(x=self.s_window_width-360, y=140+70+45, width=100, height=25)
        label_film_spot = Label(self.fin_frame, text=' بصمه ', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-445, y=140+70+40)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.pasmaCkb_SHOWVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.s_window_width-465, y=140+70+45)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.pasma_SHOWVar, justify='center',font=(self.Font_Family, 15)).place(x=self.s_window_width-540, y=145+70+40, width=70, height=25)
        
        label_taglid = Label(self.fin_frame, text=' تجليد', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-65, y=140+70+75)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.taglidCkb_SHOWVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.s_window_width-90, y=140+70+80)
        combo_box = ttk.Combobox(self.fin_frame, textvariable=self.taglid_SHOWVar, values=['كرتون', 'لف', 'لطش', 'دبوس', 'لصق بونطه', 'غراء'], state='readonly', justify='center',font=(self.Font_Family, 13, 'bold')).place(x=self.s_window_width-195, y=140+70+80, width=100, height=25)
        label = Label(self.fin_frame, text=' : العدد', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-260, y=140+70+75)
        entry = Entry(self.fin_frame, textvariable=self.taglidNum_SHOWVar, bd=2, justify='center', font=(self.Font_Family, 15)).place(x=self.s_window_width-360, y=140+70+80, width=100, height=25)
        label = Label(self.fin_frame, text=' : السعر', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-465, y=140+70+75)
        entry = Entry(self.fin_frame, textvariable=self.taglidSal_SHOWVar, bd=2, justify='center',font=(self.Font_Family, 15)).place(x=self.s_window_width-540, y=140+70+80, width=70, height=25)

        label_tawdib = Label(self.fin_frame, text=' توضيب', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-65, y=235+85)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.tawdibCkb_SHOWVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.s_window_width-90, y=240+85)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.tawdib_SHOWVar, justify='center',font=(self.Font_Family, 15)).place(x=self.s_window_width-195, y=240+85, width=100, height=25)
        label_tasmim = Label(self.fin_frame, text=' تصميم', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-260, y=235+85)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.tasmimCkb_SHOWVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.s_window_width-285, y=240+85)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.tasmim_SHOWVar, justify='center',font=(self.Font_Family, 15)).place(x=self.s_window_width-360, y=240+85, width=70, height=25)
        label_slk = Label(self.fin_frame, text=' سلك', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-445, y=235+85)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.slkCkb_SHOWVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.s_window_width-465, y=240+85)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.slk_SHOWVar, justify='center',font=(self.Font_Family, 15)).place(x=self.s_window_width-540, y=240+85, width=70, height=25)

        label_nakl = Label(self.fin_frame, text=' نقل', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-65, y=235+70+50)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.naklCkb_SHOWVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.s_window_width-90, y=240+70+50)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.nakl_SHOWVar, justify='center',font=(self.Font_Family, 15)).place(x=self.s_window_width-195, y=240+70+50, width=100, height=25)
        label_khadmat = Label(self.fin_frame, text=' خدمات', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-260, y=235+70+50)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.khadmatCkb_SHOWVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.s_window_width-285, y=240+70+50)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.khadmat_SHOWVar, justify='center',font=(self.Font_Family, 15)).place(x=self.s_window_width-360, y=240+70+50, width=70, height=25)
        label_kas = Label(self.fin_frame, text=' قص', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=self.s_window_width-445, y=235+70+50)
        ckb = ttk.Checkbutton(self.fin_frame, variable=self.kasCkb_SHOWVar, style='Custom.TCheckbutton', takefocus=False, padding=(5, 0)).place(x=self.s_window_width-465, y=240+70+50)
        entry = Entry(self.fin_frame, bd=2, bg='white', textvariable=self.kas_SHOWVar, justify='center',font=(self.Font_Family, 15)).place(x=self.s_window_width-540, y=240+70+50, width=70, height=25)
        
        sep = Frame(self.fin_frame, bg=self.lbl_bg, width=160, height=6).pack(fill=X, pady=(355, 0))
            
        control_btns_frame = Frame(self.s_window, bg='white')
        control_btns_frame.place(x=0, y=715+200, width=self.s_window_width, height=100)
        takeMoney_btn = CTkButton(control_btns_frame, text='تم الدفع', 
                                  fg_color='#8DDB45', 
                                  hover_color='#83CC40',
                                  text_color='white', 
                                    bg_color='white',
                                    cursor='hand2',
                                    font=(self.Font_Family, 22),
                                    border_width=2,
                                    border_color='grey',
                                    corner_radius=10,
                                    width=30,
                                    height=40,
                                  command=self.f_moneyDone)
        takeMoney_btn.place(x=self.s_window_width-90, y=10)
        show_total_entry = Entry(control_btns_frame, textvariable=self.f_totalSHOWVar, state='readonly', bd=2, fg='black', justify='center',font=(self.Font_Family, 17, 'bold'))
        show_total_entry.place(x=self.s_window_width-200, y=10, width=100, height=40)
        add_btn = CTkButton(control_btns_frame, text='تعديل الفاتوره', 
                            text_color='white', 
                                bg_color='white',
                                cursor='hand2',
                                font=(self.Font_Family, 22),
                                border_width=2,
                                border_color='silver',
                                corner_radius=10,
                                width=70,
                                height=40,
                            command=self.fatora_update)
        add_btn.place(x=self.s_window_width-370, y=10)
        sal_btn = CTkButton(control_btns_frame, text='الاسعار', 
                            text_color='white', 
                                bg_color='white',
                                cursor='hand2',
                                font=(self.Font_Family, 22),
                                border_width=2,
                                border_color='silver',
                                corner_radius=10,
                                width=70,
                                height=40,
                            command=self.show_sla_window)
        sal_btn.place(x=self.s_window_width-450, y=10)
        cancel_btn = CTkButton(control_btns_frame, text='إلغاء',
                               fg_color='red',
                               hover_color='#E30004', 
                               text_color='white', 
                                bg_color='white',
                                cursor='hand2',
                                font=(self.Font_Family, 22),
                                border_width=2,
                                border_color='grey',
                                corner_radius=10,
                                width=70,
                                height=40,
                               command=self.destroy_func2)
        cancel_btn.place(x=self.s_window_width-530, y=10)

        self.big_size_2()

        # self.s_window.protocol("WM_DELETE_WINDOW", self.destroy_func2)
        
        if self.f_searchVar.get() not in Client_fatora_names:
            self.s_window.destroy()
            None

    # ================================= CHECKBOXS =======================================

    # make Salaries Dictionaries (Checkboxs)
        # The Colors [ K, Y, M, C, zahabi, faddi, sapgha, warnish, kohley, spechial ]
        # the taglid [ slofan, UV, spot, tawdib, taksir, dapoos, lask, taglid, forma, pasma 

    def K(self):
        with open('Project_files/Salaries.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['K']

    def Y(self):
        with open('Project_files/Salaries.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['Y']

    def M(self):
        with open('Project_files/Salaries.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['M']

    def C(self):
        with open('Project_files/Salaries.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['C']

    def Zahabi(self):
        with open('Project_files/Salaries.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['zahabi']

    def faddi(self):
        with open('Project_files/Salaries.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['faddi']

    def sapgha(self):
        with open('Project_files/Salaries.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['sapgha']

    def warnish(self):
        with open('Project_files/Salaries.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['warnish']

    def kohley(self):
        with open('Project_files/Salaries.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['kohley']

    def spechial(self):
        with open('Project_files/Salaries.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['spechial']

    # ----------------------------------------------------------

    def K_SHOW(self):
        with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.name_of_work_entry.get()}/fatoraInformation.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['K']
        print(salaries)

    def Y_SHOW(self):
        with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.name_of_work_entry.get()}/fatoraInformation.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['Y']

    def M_SHOW(self):
        with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.name_of_work_entry.get()}/fatoraInformation.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['M']

    def C_SHOW(self):
        with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.name_of_work_entry.get()}/fatoraInformation.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['C']

    def Zahabi_SHOW(self):
        with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.name_of_work_entry.get()}/fatoraInformation.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['zahabi']

    def faddi_SHOW(self):
        with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.name_of_work_entry.get()}/fatoraInformation.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['faddi']

    def sapgha_SHOW(self):
        with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.name_of_work_entry.get()}/fatoraInformation.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['sapgha']

    def warnish_SHOW(self):
        with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.name_of_work_entry.get()}/fatoraInformation.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['warnish']

    def kohley_SHOW(self):
        with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.name_of_work_entry.get()}/fatoraInformation.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['kohley']

    def spechial_SHOW(self):
        with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.name_of_work_entry.get()}/fatoraInformation.json', 'r') as file:
            salaries = json.load(file)
        self.checkboxsVar += salaries['spechial']

    # ===================================================================================

    def combo_selected(self, event):
        if self.typeVar1.get() == 'كوشيه':
            self.type_combo2['values'] = ['90gm 70%', '115gm 70%', '130gm 70%', '150gm 70%', '170gm 70%', '200gm 70%', '250gm 70%', '300gm 70%', '350gm 70%', '90gm جاير', '115gm جاير', '130gm جاير', '150gm جاير', '170gm جاير', '200gm جاير', '250gm جاير', '300gm جاير', '350gm جاير']
        if self.typeVar1.get() == 'طبع':
            self.type_combo2['values'] = ['70gm 70%', '80gm 70%', '100gm 70%', '120gm 70%', '70gm جاير', '80gm جاير', '100gm جاير', '120gm جاير', 'ورق كريمي', 'مكربن']
        if self.typeVar1.get() == 'استيكر':
            self.type_combo2['values'] = ['بلاستيك ابيض', 'بلاستيك شفاف', 'فضي', 'ذهبي', 'ورق']
        if self.typeVar1.get() == 'دوبلكس':
            self.type_combo2['values'] = ['220gm', '250gm', '300gm', '350gm']
        if self.typeVar1.get() == 'برستول كوشيه':
            self.type_combo2['values'] = ['230gm 70%', '250gm 70%', '300gm 70%', '250gm جاير', '300gm جاير', '350gm 70%']

    def combo_selected2(self, event):
        if self.typeSHOWVar1.get() == 'كوشيه':
            self.type_combo2['values'] = ['90gm 70%', '115gm 70%', '130gm 70%', '150gm 70%', '170gm 70%', '200gm 70%', '250gm 70%', '300gm 70%', '350gm 70%', '90gm جاير', '115gm جاير', '130gm جاير', '150gm جاير', '170gm جاير', '200gm جاير', '250gm جاير', '300gm جاير', '350gm جاير']
        if self.typeSHOWVar1.get() == 'طبع':
            self.type_combo2['values'] = ['70gm 70%', '80gm 70%', '100gm 70%', '120gm 70%', '70gm جاير', '80gm جاير', '100gm جاير', '120gm جاير', 'ورق كريمي', 'مكربن']
        if self.typeSHOWVar1.get() == 'استيكر':
            self.type_combo2['values'] = ['بلاستيك ابيض', 'بلاستيك شفاف', 'فضي', 'ذهبي', 'ورق']
        if self.typeSHOWVar1.get() == 'دوبلكس':
            self.type_combo2['values'] = ['220gm', '250gm', '300gm', '350gm']
        if self.typeSHOWVar1.get() == 'برستول كوشيه':
            self.type_combo2['values'] = ['230gm 70%', '250gm 70%', '300gm 70%', '250gm جاير', '300gm جاير', '350gm 70%']

    def taraf_combo_selected(self, event):
        if self.tarafVar2.get() == 'العميل':
            self.salaryVar2.set(0)
        elif self.tarafVar2.get() == 'المطبعة':
            self.salaryVar2.set(42.5)
        if self.tarafSHOWVar2.get() == 'العميل':
            self.salarySHOWVar2.set(0)
        elif self.tarafSHOWVar2.get() == 'المطبعة':
            self.salarySHOWVar2.set(42.5)
            
    def taksir_combo_selected(self, event):
        with open('Project_files/Salaries.json', 'r') as file:
            self.salaries = json.load(file)
        file.close()
            
        if self.taksir_SAVEVar.get() == 'كامل' or self.taksir_SAVEVar.get() == 'ريجه':
            self.salaries['taksir'] = 75
        elif self.taksir_SAVEVar.get() == 'نصف تكسيره':
            self.salaries['taksir'] = 100
            
        with open('Project_files/Salaries.json', 'w') as file:
            json.dump(self.salaries, file)
        file.close()
        
        self.show_salaries()
            
    def taksir_combo_selected2(self, event):
        with open('Project_files/Salaries.json', 'r') as file:
            self.salaries = json.load(file)
        file.close()
            
        if self.taksir_SHOWVar.get() == 'كامل' or self.taksir_SHOWVar.get() == 'ريجه':
            self.salaries['taksir'] = 75
        elif self.taksir_SHOWVar.get() == 'نصف تكسيره':
            self.salaries['taksir'] = 100
            
        with open('Project_files/Salaries.json', 'w') as file:
            json.dump(self.salaries, file)
        file.close()
        
        self.show_salaries()
    
    # def taksir_combo_selected2(self, event):
    #     if self.taksir_SHOWVar.get() == 'كامل' or self.taksir_SHOWVar.get() == 'ريجه':
    #         self.taksir_var.set(75)
    #     elif self.taksir_SHOWVar.get() == 'نصف تكسيره':
    #         self.taksir_var.set(100)

    # ===================================================================================

    # Make Work Windonw in Big Size Funcation
    def big_size(self):
        if self.Check_btn_fb_var.get():
            self.print_frame.place(x=0, y=325, width=self.n_window_width, height=190)
            self.fin_frame.place(x=0, y=520, width=self.n_window_width, height=270+260)
        elif not self.Check_btn_fb_var.get():
            self.print_frame.place(x=0, y=325, width=self.n_window_width, height=160)
            self.fin_frame.place(x=0, y=490, width=self.n_window_width, height=270+260)

    def big_size_2(self):
        if self.Check_btn_fb_SHOWVar.get():
            self.print_frame.place(x=0, y=325, width=self.s_window_width, height=190)
            self.fin_frame.place(x=0, y=520, width=self.s_window_width, height=270+260)
        elif not self.Check_btn_fb_SHOWVar.get():
            self.print_frame.place(x=0, y=325, width=self.s_window_width, height=160)
            self.fin_frame.place(x=0, y=490, width=self.s_window_width, height=270+260)

    # ===================================================================================
    
    # Save Client Money Funcation
    def take_money(self):
        self.tk_money = Toplevel()
        self.tk_money.title('إستلام النقدية')
        self.tk_money_width = 400
        self.tk_money_hieght = 600
        self.tk_money.config(background='white')
        self.tk_money.geometry(f'{self.tk_money_width}x{self.tk_money_hieght}+{(self.winfo_screenwidth()-self.tk_money_width)//2}+{(self.winfo_screenheight()-self.tk_money_hieght)//2}')

        enter_money_lbl = Label(self.tk_money, text='أدخل المبلغ المُستَلم وطريقة الدفع', bg='white', fg='black', font=(self.Font_Family, 17))
        enter_money_lbl.pack(pady=10)
        enter_money_entry = Entry(self.tk_money, textvariable=self.enter_money, bd=2, bg='white', justify='center', width=10, font=(self.Font_Family, 15))
        enter_money_entry.place(x=205, y=70)
        self.push_way_combo = ttk.Combobox(self.tk_money, textvariable=self.push_way, justify='center', state='readonly', values=['كاش', 'محفظه الكترونيه'], width=11, font=(self.Font_Family, 13))
        self.push_way_combo.set('... طريقة الدفع')
        self.push_way_combo.place(x=75, y=70)
        enter_money_btn = CTkButton(self.tk_money, text='إستلام',
                                    text_color='white', 
                                    bg_color='white',
                                    cursor='hand2',
                                    font=(self.Font_Family, 22),
                                    border_width=2,
                                    border_color='silver',
                                    corner_radius=10,
                                    width=120,
                                    height=40,
                                    command=self.calculate_money)
        enter_money_btn.pack(pady=(80,0))

        self.done_lbl = Label(self.tk_money, text='', font=(self.Font_Family, 20), bg='white', fg='black')
        self.done_lbl.place(x=35, y=132)
        
        scrollBar_y = Scrollbar(self.tk_money, orient=VERTICAL)
        
        self.money_table = ttk.Treeview(self.tk_money, yscrollcommand=scrollBar_y.set, 
                                     columns=('push_way', 'date', 'money'), show='headings')
        self.money_table.place(x=18, y=200, width=378, height=398)
        
        scrollBar_y.place(x=1, y=200, width=16, height=398)
        
        self.money_table['style'] = 'Treeview3.Treeview'
        ttk.Style().configure('Treeview3.Treeview.Heading',font=(self.Font_Family, 16, 'bold'), foreground='#0024FF', rowheight=50, width=2 )
        ttk.Style().configure('Treeview3.Treeview',font=(self.Font_Family, 14), rowheight=40, width=2 )
        
        self.money_table['show'] = 'headings'
        self.money_table.heading('push_way', text='طريقة الدفع', anchor=CENTER)
        self.money_table.column('push_way', minwidth=378//3, width=378//3, stretch=NO, anchor=CENTER) 
        self.money_table.heading('date', text='التاريخ', anchor=CENTER)
        self.money_table.column('date', minwidth=378//3, width=378//3, stretch=NO, anchor=CENTER)
        self.money_table.heading('money', text='المبلغ', anchor=CENTER)
        self.money_table.column('money', minwidth=378//3, width=(378//3)-3, stretch=NO, anchor=CENTER)

        self.display_take_money_table()
        
    # ===================================================================================
    
    def calculate_money(self):
        db = sqlite3.connect(f'Project_files/Clients Work/{self.searchVar.get()}/money_table.db')
        cr = db.cursor()
        
        cr.execute('CREATE TABLE IF NOT EXISTS money(pushWay text, date text, money intger)')
        db.commit()
        if self.enter_money.get():
            if self.enter_money.get() != 0 and self.push_way.get() != '... طريقة الدفع':
                # fill the Date Automaticlly 
                f_date = (str(datetime.now())[:str(datetime.now()).find(' ')].strip()).replace('-', '/')

                enter_money = self.enter_money.get()

                cr.execute(f'INSERT INTO money VALUES ("{self.push_way.get()}", "{f_date}", {self.enter_money.get()})')

                db.commit()
                db.close()

                db = sqlite3.connect(f'Project_files/Clients.db')
                cr = db.cursor()

                cr.execute(f'select done_of_money, all_of_money from Clients where name = "{self.searchVar.get()}"')
                info = cr.fetchall()

                done_m = info[0][0] + enter_money
                all_m = info[0][1] - enter_money

                cr.execute(f'update Clients set done_of_money = {done_m}, all_of_money = {all_m} where name = "{self.searchVar.get()}"')

                db.commit()
                self.display_take_money_table()
                self.Display_info()
                self.enter_money.set(0)
                self.push_way_combo.set('... طريقة الدفع')
                self.tk_money.destroy()
                db.close()
            else:
                self.showPushError()
        else:
            self.showPushError()
    # ===================================================================================

    def display_take_money_table(self):
        db = sqlite3.connect(f'Project_files/Clients Work/{self.searchVar.get()}/money_table.db')
        cr = db.cursor()
        
        # Fetch All Data from Database
        cr.execute('SELECT * FROM money')
        self.rows = cr.fetchall()

        db_2 = sqlite3.connect('Project_files/Clients.db')
        cr_2 = db_2.cursor()
        
        cr_2.execute(f'SELECT all_of_money FROM Clients WHERE name = "{self.searchVar.get()}"')
        fetched_data = cr_2.fetchall()
        
        for x in fetched_data:
            for y in x:
                self.done_lbl.config(text='خالص') if y == 0 else self.done_lbl.config(text='')
        
        db_2.commit()
        db_2.close()
                
        # Clear existing data from the table
        if len(self.rows) != 0:
            self.money_table.delete(*self.money_table.get_children())
            
            for row in self.rows:
                self.money_table.insert('', 'end', values=row)

            db.commit()
            self.Display_info_2()
            db.close()
        else:
            self.money_table.delete(*self.money_table.get_children())

    # ===================================================================================
    def nameCount(self):
        db = sqlite3.connect(f'Project_files/Clients Work/{self.searchVar.get()}/Fawatir.db')
        cr = db.cursor()

        f_date = ''
        
        cr.execute(f'SELECT f_name FROM All_fatora')
        feched_data = cr.fetchall()

        currentName = self.f_nameVar.get()
        name_lst = []
        newName = ''

        for x in feched_data:
            for y in x:
                name_lst.append(y)

        if currentName in name_lst:
            for n in name_lst:
                    if '(' in n:
                        n_p1 = n[:n.find('(')]
                        n_p2 = n[n.find('('):]
                        name_num = int(str(n_p2[1:]).strip(')'))

                        if n_p1.strip() == currentName :
                            newName = currentName + f' ({name_num + 1})'
                    else:    
                        newName = currentName + ' (1)'
        else:
            newName = currentName

        self.f_nameVar.set(newName)
    # ===================================================================================

    def f_moneyDone(self):
        self.S_E = Tk()
        self.S_E.title('تم الدفع')
        self.S_E_width = 350
        self.S_E_height = 150
        self.S_E.config(background='white')
        self.S_E.geometry(f'{self.S_E_width}x{self.S_E_height}+{(self.winfo_screenwidth() - self.S_E_width)//2}+{(self.winfo_screenheight() - self.S_E_height)//2}')
        
        db = sqlite3.connect(f'Project_files/Clients Work/{self.searchVar.get()}/Fawatir.db')
        cr = db.cursor()
        
        cr.execute(f'UPDATE All_fatora SET done_or_not = "تم الدفع" where f_name = "{self.f_searchVar.get()}"')
        
        db.commit()
        self.Display_info_2()
        db.close()

        S_E_lbl = Label(self.S_E, text='تم دفع حساب هذه الفاتورة', bg='white', fg='black', font=(self.Font_Family, 18, 'bold')).pack(pady=(10,0))

        ok_btn = CTkButton(self.S_E, text='ok', 
                           text_color='white', 
                                bg_color='white',
                                cursor='hand2',
                                font=(self.Font_Family, 22),
                                border_width=2,
                                border_color='silver',
                                corner_radius=10,
                                width=70,
                                height=40,
                           command=self.S_E.destroy)
        ok_btn.pack(pady=(15, 0))
        
    # ===================================================================================
    
    # Add New Fatora Funcation
    def new_fatora(self):
        self.show_salaries()
        # Add fatora to Fawatir database
        db = sqlite3.connect(f'Project_files/Clients Work/{self.searchVar.get()}/Fawatir.db')
        cr = db.cursor()
        
        # Fill The data Automatic if not exiests
        f_date = ''

        if self.e3_dateVar.get() and self.e2_dateVar.get() and self.e1_dateVar.get():
            f_date = f'{self.e3_dateVar.get()} / {self.e2_dateVar.get()} / {(self.e1_dateVar.get()).zfill(2)}'
        else:
            f_date = str(datetime.now())[:str(datetime.now()).find(' ')].strip().replace('-', ' / ')
        
        if not self.f_nameVar.get():
            self.showNameFatoraError()
        else:
            self.nameCount()    
            cr.execute('SELECT * FROM All_fatora')
            Fawatir = cr.fetchall()
            f_count = len(Fawatir)

            cr.execute(f'INSERT INTO All_fatora VALUES ("لم يتم الدفع", 0, "{f_date}", "{self.f_nameVar.get()}", {f_count + 1})')

            db.commit()
            self.Display_info_2()

            if os.path.exists(f'Project_files/Clients Work/{self.searchVar.get()}/{self.f_nameVar.get()}'):
                shutil.rmtree(f'Project_files/Clients Work/{self.searchVar.get()}/{self.f_nameVar.get()}')
                
            os.makedirs(f'Project_files/Clients Work/{self.searchVar.get()}/{self.f_nameVar.get()}')

            info_dict = {
                'اسم العملية':self.f_nameVar.get() ,'التاريخ':[self.e1_dateVar.get(), self.e2_dateVar.get(), self.e3_dateVar.get()], 
                '1طرف':self.tarafVar1.get(), 'عدد الافرخ':self.farkh_countVar.get(), 
                'نوع':[self.type_combo1.get(), self.type_combo2.get()], 'مقاس القص':[self.sizeVar1.get(), self.sizeVar2.get()], '1السعر':self.salaryVar1.get(), 
                '2طرف':self.tarafVar2.get(), 'عدد الزنك':self.zenk_countVar.get(), '2السعر':self.salaryVar2.get(), 
                'عدد السحبات':self.sahba_countVar.get(), 'الرقم الفعلي':self.sahba2_countVar.get(), 'تطبع وتقلب':self.Check_btn_fb_var.get(), 
                'K1':self.cb_K_Var1.get(), 'Y1':self.cb_Y_Var1.get(), 'M1':self.cb_M_Var1.get(), 'C1':self.cb_C_Var1.get(), '1ذهبي':self.cb_zahabi_Var1.get(), '1فضي':self.cb_faddi_Var1.get(), '1صبغة':self.cb_sapgha_Var1.get(), '1ورنيش':self.cb_warnish_Var1.get(), '1كحلي':self.cb_kohley_Var1.get(), '1اسبيشيال':self.sVar1.get(), 
                'K2':self.cb_K_Var2.get(), 'Y2':self.cb_Y_Var2.get(), 'M2':self.cb_M_Var2.get(), 'C2':self.cb_C_Var2.get(), '2ذهبي':self.cb_zahabi_Var2.get(), '2فضي':self.cb_faddi_Var2.get(), '2صبغة':self.cb_sapgha_Var2.get(), '2ورنيش':self.cb_warnish_Var2.get(), '2كحلي':self.cb_kohley_Var2.get(), '2اسبيشيال':self.sVar2.get(), 
                'عدد الدفاتر':self.daftar_countVar.get(), 'عدد المجموعات':self.groups_countVar.get(), 'الترتيب':self.counterVar.get(), 'الترقيم':{'من':self.num_of_countVar1.get(), 'الي':self.num_of_countVar2.get()}, 
                'التجليد':[[self.slofanCkb_SAVEVar.get(), self.slofan_SAVEVar.get(), self.slofanFinNum_SAVEVar.get(), self.gha_SAVEVar.get()], 
                            [self.UVCkb_SAVEVar.get(), self.UV_SAVEVar.get(), self.UVFinNum_SaveVar.get()], 
                            [self.taksirCkb_SAVEVar.get(), self.taksir_SAVEVar.get(), self.taksirNum_SAVEVar.get(), self.formaCkb_SAVEVar.get(), self.forma_SAVEVar.get()],
                            [self.spotCkb_SAVEVar.get(), self.spot_SAVEVar.get(), self.filmCkb_SAVEVar.get(), self.film_SAVEVar.get()],
                            [self.aklashehCkb_SAVEVar.get(), self.aklasheh_SAVEVar.get(), self.pasmaCkb_SAVEVar.get(), self.pasma_SAVEVar.get()],
                            [self.taglidCkb_SAVEVar.get(), self.taglid_SAVEVar.get(), self.taglidNum_SAVEVar.get(), self.taglidSal_SAVEVar.get()],
                            [self.tawdibCkb_SAVEVar.get(), self.tawdib_SAVEVar.get(), self.tasmimCkb_SAVEVar.get(), self.tasmim_SAVEVar.get(), self.slkCkb_SAVEVar.get(), self.slk_SAVEVar.get()],
                            [self.naklCkb_SAVEVar.get(), self.nakl_SAVEVar.get(), self.khadmatCkb_SAVEVar.get(), self.khadmat_SAVEVar.get(), self.kasCkb_SAVEVar.get(), self.kas_SAVEVar.get()]]
            }

            with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.f_nameVar.get()}/fatoraInformation.json', 'X') as file_1:
                json.dump(info_dict, file_1)
                
            file_1.close()

            fatora_salaries = {
                'K':self.K_var.get(),
                'Y':self.Y_var.get(),
                'M':self.M_var.get(),
                'C':self.C_var.get(),
                'zahabi':self.zahabi_var.get(),
                'faddi':self.faddi_var.get(),
                'sapgha':self.sapgha_var.get(),
                'warnish':self.warnish_var.get(),
                'kohley':self.kohley_var.get(),
                'spechial':self.spechial_var.get(),
                'slofan':self.slofan_var.get(),
                'UV':self.UV_var.get(),
                'taksir':self.taksir_var.get(), 
                'film' : self.film_var.get()
            }
            
            with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.f_nameVar.get()}/fatoraSalaries.json', 'x') as sal_json_file:
                json.dump(fatora_salaries, sal_json_file)

            sal_json_file.close()

            with open('Project_files/Salaries.json', 'r') as file_4:
                salaries = json.load(file_4)
                
            file_4.close()

            fatora_Money = 0

            multiple_var1 = 0
            multiple_var2 = 0

            if self.tarafVar1.get() == 'المطبعة':
                if self.farkh_countVar.get() and self.salaryVar1.get():
                    multiple_var1 = (int(self.farkh_countVar.get()) * float(self.salaryVar1.get()))
            elif self.tarafVar1.get() == 'العميل':
                multiple_var1 = 0
                
            if self.tarafVar2.get() == 'المطبعة':
                if self.zenk_countVar.get() and self.salaryVar2.get():
                    multiple_var2 = (int(self.zenk_countVar.get()) * float(self.salaryVar2.get()))
            elif self.tarafVar2.get() == 'العميل' or not self.zenk_countVar.get() or not self.salaryVar2.get():
                multiple_var2 = 0

            fatora_Money += multiple_var1 + multiple_var2

            self.checkboxsVar = 0
            
            # Colors Money

            if self.cb_K_Var1.get():
                self.K()
            if self.cb_Y_Var1.get():
                self.Y()
            if self.cb_M_Var1.get():
                self.M()
            if self.cb_C_Var1.get():
                self.C()
            if self.cb_zahabi_Var1.get():
                self.Zahabi()
            if self.cb_faddi_Var1.get():
                self.faddi()
            if self.cb_sapgha_Var1.get():
                self.sapgha()
            if self.cb_warnish_Var1.get():
                self.warnish()
            if self.cb_kohley_Var1.get():
                self.kohley()
            if self.sVar1.get():
                self.spechial()

            if self.cb_K_Var2.get():
                self.K()
            if self.cb_Y_Var2.get():
                self.Y()
            if self.cb_M_Var2.get():
                self.M()
            if self.cb_C_Var2.get():
                self.C()
            if self.cb_zahabi_Var2.get():
                self.Zahabi()
            if self.cb_faddi_Var2.get():
                self.faddi()
            if self.cb_sapgha_Var2.get():
                self.sapgha()
            if self.cb_warnish_Var2.get():
                self.warnish()
            if self.cb_kohley_Var2.get():
                self.kohley()
            if self.sVar2.get():
                self.spechial()

            # if self.sahba_countVar.get():
            #     sahbaCountVar_int = int(f'{self.sahba_countVar.get()}')
            #     sahba_part_2 = int(str(sahbaCountVar_int)[1:])
                
            #     if sahbaCountVar_int > 1000:
            #         if len(str(sahbaCountVar_int)) == 4:
            #             self.counter = int(str(self.sahba_countVar.get())[0])
            #         if len(str(sahbaCountVar_int)) == 5:
            #             self.counter = int(str(self.sahba_countVar.get())[:2])
            #         if len(str(sahbaCountVar_int)) == 6:
            #             self.counter = int(str(self.sahba_countVar.get())[:3])
            #         if sahba_part_2 > 100:
            #             self.counter += 1
            #     else:
            #         self.counter = 1
                    
            # fatora_Money += (self.counter * self.checkboxsVar) 

            if self.sahba2_countVar.get():

                fatora_Money += (float(self.sahba2_countVar.get()) * self.checkboxsVar)
            
            # Taglid Money
            if self.slofanCkb_SAVEVar.get():
                fatora_Money += (int(self.slofanFinNum_SAVEVar.get()) * salaries['slofan'])
            if self.UVCkb_SAVEVar.get():
                fatora_Money += (int(self.UVFinNum_SaveVar.get()) * salaries['UV'])
            if self.taksirCkb_SAVEVar.get():
                
                    # old way
                # if self.taksirNum_SAVEVar.get():
                    # taksir1 = int(f'{self.taksirNum_SAVEVar.get()}')
                    # taksir2 = int(str(taksir1)[1:])

                    # self.counter2 = 0
                    # if taksir1 >= 1000:
                    #     if len(str(taksir1)) == 4:
                    #         self.counter2 = int(str(self.taksirNum_SAVEVar.get())[0])
                    #     if len(str(taksir1)) == 5:
                    #         self.counter2 = int(str(self.taksirNum_SAVEVar.get())[:2])
                    #     if len(str(taksir1)) == 6:
                    #         self.counter2 = int(str(self.taksirNum_SAVEVar.get())[:3])
                    #     if taksir2 > 100:
                    #         self.counter2 += 1
                    # else:
                    #     self.counter2 = 1
                    
                fatora_Money += (float(self.taksirNum_SAVEVar.get()) * salaries['taksir'])
                    
            if self.formaCkb_SAVEVar.get():
                fatora_Money += float(self.forma_SAVEVar.get())
            if self.spotCkb_SAVEVar.get():
                fatora_Money += float(self.spot_SAVEVar.get())
            if self.filmCkb_SAVEVar.get():
                fatora_Money += salaries['film']
            if self.aklashehCkb_SAVEVar.get():
                fatora_Money += float(self.aklashehSal_SAVEVar.get())
            if self.pasmaCkb_SAVEVar.get():
                fatora_Money += float(self.pasma_SAVEVar.get())
            if self.taglidCkb_SAVEVar.get():
                fatora_Money += (float(self.taglidNum_SAVEVar.get()) * float(self.taglidSal_SAVEVar.get()))
            if self.tawdibCkb_SAVEVar.get():
                fatora_Money += float(self.tawdib_SAVEVar.get())
            if self.tasmimCkb_SAVEVar.get():
                fatora_Money += float(self.tasmim_SAVEVar.get())
            if self.slkCkb_SAVEVar.get():
                fatora_Money += float(self.slk_SAVEVar.get())
            if self.kasCkb_SAVEVar.get():
                fatora_Money += float(self.kas_SAVEVar.get())
            if self.khadmatCkb_SAVEVar.get():
                fatora_Money += float(self.khadmat_SAVEVar.get())
            if self.naklCkb_SAVEVar.get():
                fatora_Money += float(self.nakl_SAVEVar.get())


            with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.f_nameVar.get()}/All Money.json', 'x') as file_2:
                json.dump(fatora_Money, file_2)
                
            file_2.close()
                
            self.f_totalVar.set(fatora_Money)

            self.display_money()
            self.fatora_reset()
            self.fatoraDateSort()
            self.fatoraNumberSort()
            self.Display_info_2()
            self.n_window.destroy()

        db.close()
    # ===================================================================================

    def showNameFatoraError(self):
        self.S_E = Toplevel()
        self.S_E.title('!خطأ في الفاتورة')
        self.S_E_width = 350
        self.S_E_height = 120
        self.S_E.config(background='white')
        self.S_E.geometry(f'{self.S_E_width}x{self.S_E_height}+{(self.winfo_screenwidth() - self.S_E_width)//2}+{(self.winfo_screenheight() - self.S_E_height)//2}')

        self.S_E_lbl = Label(self.S_E, text='لم يتم كتابة اسم الفاتورة', bg='white', fg='black', font=(self.Font_Family, 18, 'bold')).pack(pady=(10,0))

        ok_btn = CTkButton(self.S_E, text='ok',
                           text_color='white', 
                                    bg_color='white',
                                    cursor='hand2',
                                    font=(self.Font_Family, 22),
                                    border_width=2,
                                    border_color='silver',
                                    corner_radius=10,
                                    width=70,
                                    height=40, 
                           command=self.S_E.destroy)
        ok_btn.pack(pady=(15, 0))
    # ===================================================================================
        
    def showPushError(self):
        # Note to user
        self.S_E = Toplevel()
        self.S_E.title('!خطأ في الدفعة')
        self.S_E_width = 350
        self.S_E_height = 120
        self.S_E.config(background='white')
        self.S_E.geometry(f'{self.S_E_width}x{self.S_E_height}+{(self.winfo_screenwidth() - self.S_E_width)//2}+{(self.winfo_screenheight() - self.S_E_height)//2}')

        self.S_E_lbl = Label(self.S_E, text='اكمل الخانات لتتم الدفعة', bg='white', fg='black', font=(self.Font_Family, 18, 'bold')).pack(pady=(10,0))

        ok_btn = CTkButton(self.S_E, text='ok',
                        text_color='white', 
                                    bg_color='white',
                                    cursor='hand2',
                                    font=(self.Font_Family, 22),
                                    border_width=2,
                                    border_color='silver',
                                    corner_radius=10,
                                    width=70,
                                    height=40, 
                        command=self.S_E.destroy)
        ok_btn.pack(pady=(15, 0))
    # ===================================================================================

    def fatora_reset(self):
        self.f_nameVar.set('')
        self.e1_dateVar.set('')
        self.e2_dateVar.set('')
        self.e3_dateVar.set('')
        self.tarafVar1.set('')
        self.farkh_countVar.set('')
        self.typeVar1.set('')
        self.typeVar2.set('')
        self.sizeVar1.set('')
        self.sizeVar2.set('')
        self.salaryVar1.set('')
        self.tarafVar2.set('')
        self.zenk_countVar.set('')
        self.salaryVar2.set(42.5)
        self.sahba_countVar.set('')
        self.sahba2_countVar.set('')
        self.sVar1.set('')
        self.sVar2.set('')
        
        self.Check_btn_fb_var.set(0)

        self.cb_K_Var1.set(False)
        self.cb_Y_Var1.set(False)
        self.cb_M_Var1.set(False)
        self.cb_C_Var1.set(False)
        self.cb_zahabi_Var1.set(False)
        self.cb_faddi_Var1.set(False)
        self.cb_sapgha_Var1.set(False)
        self.cb_warnish_Var1.set(False)
        self.cb_kohley_Var1.set(False)

        self.cb_K_Var2.set(False)
        self.cb_Y_Var2.set(False)
        self.cb_M_Var2.set(False)
        self.cb_C_Var2.set(False)
        self.cb_zahabi_Var2.set(False)
        self.cb_faddi_Var2.set(False)
        self.cb_sapgha_Var2.set(False)
        self.cb_warnish_Var2.set(False)
        self.cb_kohley_Var2.set(False)
        
        self.daftar_countVar.set('')
        self.groups_countVar.set('')
        self.counterVar.set('')
        self.num_of_countVar1.set('')
        self.num_of_countVar2.set('')
        
        self.slofan_SAVEVar.set('')
        self.slofanCkb_SAVEVar.set(False)
        self.gha_SAVEVar.set('')
        self.slofanFinNum_SAVEVar.set('')

        self.UV_SAVEVar.set('')
        self.UVCkb_SAVEVar.set(False)
        self.UVFinNum_SaveVar.set('')   
        
        self.taksir_SAVEVar.set('')
        self.taksirCkb_SAVEVar.set(False)
        self.taksirNum_SAVEVar.set('')
        self.forma_SAVEVar.set('') 
        self.formaCkb_SAVEVar.set(False) 

        self.spot_SAVEVar.set('')
        self.spotCkb_SAVEVar.set(False)
        self.film_SAVEVar.set('')
        self.filmCkb_SAVEVar.set(False)
        
        self.aklasheh_SAVEVar.set('')
        self.aklashehCkb_SAVEVar.set(False)
        self.aklashehSal_SAVEVar.set('')
        self.pasma_SAVEVar.set('') 
        self.pasmaCkb_SAVEVar.set(False)

        self.taglid_SAVEVar.set('')
        self.taglidCkb_SAVEVar.set(False)
        self.taglidNum_SAVEVar.set('')
        self.taglidSal_SAVEVar.set('')
        
        self.tawdib_SAVEVar.set('')
        self.tawdibCkb_SAVEVar.set(False)
        self.slk_SAVEVar.set('')
        self.slkCkb_SAVEVar.set(False)

        self.nakl_SAVEVar.set('')
        self.naklCkb_SAVEVar.set(False)
        self.kas_SAVEVar.set('')
        self.kasCkb_SAVEVar.set(False)

        self.khadmatCkb_SAVEVar.set(False)
        self.khadmat_SAVEVar.set('')
        
        self.f_totalVar.set(0)

    # ===================================================================================
        
    def fatora_reset_2(self):
        self.f_nameSHOWVar.set('')
        self.e1_dateSHOWVar.set('')
        self.e2_dateSHOWVar.set('')
        self.e3_dateSHOWVar.set('')
        self.tarafSHOWVar1.set('')
        self.farkh_countSHOWVar.set('')
        self.typeSHOWVar1.set('')
        self.typeSHOWVar2.set('')
        self.sizeSHOWVar1.set('')
        self.sizeSHOWVar2.set('')
        self.salarySHOWVar1.set('')
        self.tarafSHOWVar2.set('')
        self.zenk_countSHOWVar.set('')
        self.salarySHOWVar2.set('')
        self.sahba_countSHOWVar.set('')
        self.sahba2_countSHOWVar.set('')
        self.sSHOWVar1.set('')
        self.sSHOWVar2.set('')

        self.Check_btn_fb_SHOWVar.set(0)

        self.cb_K_SHOWVar1.set(False)
        self.cb_Y_SHOWVar1.set(False)
        self.cb_M_SHOWVar1.set(False)
        self.cb_C_SHOWVar1.set(False)
        self.cb_zahabi_SHOWVar1.set(False)
        self.cb_faddi_SHOWVar1.set(False)
        self.cb_sapgha_SHOWVar1.set(False)
        self.cb_warnish_SHOWVar1.set(False)
        self.cb_kohley_SHOWVar1.set(False)

        self.cb_K_SHOWVar2.set(False)
        self.cb_Y_SHOWVar2.set(False)
        self.cb_M_SHOWVar2.set(False)
        self.cb_C_SHOWVar2.set(False)
        self.cb_zahabi_SHOWVar2.set(False)
        self.cb_faddi_SHOWVar2.set(False)
        self.cb_sapgha_SHOWVar2.set(False)
        self.cb_warnish_SHOWVar2.set(False)
        self.cb_kohley_SHOWVar2.set(False)
        
        self.daftar_countSHOWVar.set('')
        self.groups_countSHOWVar.set('')
        self.counterSHOWVar.set('')
        self.num_of_countSHOWVar1.set('')
        self.num_of_countSHOWVar2.set('')
        
        self.slofan_SHOWVar.set('')
        self.slofanCkb_SHOWVar.set(False)
        self.gha_SHOWVar.set('')
        self.slofanFinNum_SHOWVar.set('')

        self.UV_SHOWVar.set('')
        self.UVCkb_SHOWVar.set(False)
        self.UVFinNum_SHOWVar.set('')   
        
        self.taksir_SHOWVar.set('')
        self.taksirCkb_SHOWVar.set(False)
        self.taksirNum_SHOWVar.set('')
        self.forma_SHOWVar.set('') 
        self.formaCkb_SHOWVar.set(False) 

        self.spot_SHOWVar.set('')
        self.spotCkb_SHOWVar.set(False)
        self.film_SHOWVar.set('')
        self.filmCkb_SHOWVar.set(False)
        
        self.aklasheh_SHOWVar.set('')
        self.aklashehCkb_SHOWVar.set(False)
        self.aklashehSal_SHOWVar.set('')
        self.pasma_SHOWVar.set('') 
        self.pasmaCkb_SHOWVar.set(False)

        self.taglid_SHOWVar.set('')
        self.taglidCkb_SHOWVar.set(False)
        self.taglidNum_SHOWVar.set('')
        self.taglidSal_SHOWVar.set('')
        
        self.tawdib_SHOWVar.set('')
        self.tawdibCkb_SHOWVar.set(False)
        self.slk_SHOWVar.set('')
        self.slkCkb_SHOWVar.set(False)

        self.nakl_SHOWVar.set('')
        self.naklCkb_SHOWVar.set(False)
        self.kas_SHOWVar.set('')
        self.kasCkb_SHOWVar.set(False)

        self.khadmatCkb_SHOWVar.set(False)
        self.khadmat_SHOWVar.set('')
        
        self.f_totalSHOWVar.set(0)
    # ===================================================================================

    def FfromNewOne(self):
        self.destroy_func1()
        self.Add_fatora()
    # ===================================================================================
    
    def fatora_update(self):
        db = sqlite3.connect(f'Project_files/Clients Work/{self.searchVar.get()}/Fawatir.db')
        cr = db.cursor()

        old_name = self.f_searchVar.get()
        new_name = self.f_nameSHOWVar.get()
        f_date = f'{self.e3_dateSHOWVar.get()} / {self.e2_dateSHOWVar.get()} / {(self.e1_dateSHOWVar.get()).zfill(2)}'

        cr.execute(f'update All_fatora set f_date = "{f_date}", f_name = "{new_name}" where f_number = {self.delNumberVar.get()}')
        if new_name:
            os.rename(f'Project_files/Clients Work/{self.searchVar.get()}/{old_name}', f'Project_files/Clients Work/{self.searchVar.get()}/{new_name}')
        else:
            os.makedirs(f'Project_files/Clients Work/{self.searchVar.get()}/{self.name_of_work_entry.get()}')
        
        info_dict = {
            'اسم العملية': self.f_nameSHOWVar.get(), 'التاريخ':[self.e1_dateSHOWVar.get(), self.e2_dateSHOWVar.get(), self.e3_dateSHOWVar.get()], 
            '1طرف':self.tarafSHOWVar1.get(), 'عدد الافرخ':self.farkh_countSHOWVar.get(), 
            'نوع':[self.typeSHOWVar1.get(), self.typeSHOWVar2.get()], 'مقاس القص':[self.sizeSHOWVar1.get(), self.sizeSHOWVar2.get()], '1السعر':self.salarySHOWVar1.get(), 
            '2طرف':self.tarafSHOWVar2.get(), 'عدد الزنك':self.zenk_countSHOWVar.get(), '2السعر':self.salarySHOWVar2.get(), 
            'عدد السحبات':self.sahba_countSHOWVar.get(), 'الرقم الفعلي':self.sahba2_countSHOWVar.get(), 'تطبع وتقلب':self.Check_btn_fb_SHOWVar.get(), 
            'K1':self.cb_K_SHOWVar1.get(), 'Y1':self.cb_Y_SHOWVar1.get(), 'M1':self.cb_M_SHOWVar1.get(), 'C1':self.cb_C_SHOWVar1.get(), '1ذهبي':self.cb_zahabi_SHOWVar1.get(), '1فضي':self.cb_faddi_SHOWVar1.get(), '1صبغة':self.cb_sapgha_SHOWVar1.get(), '1ورنيش':self.cb_warnish_SHOWVar1.get(), '1كحلي':self.cb_kohley_SHOWVar1.get(), '1اسبيشيال':self.sSHOWVar1.get(), 
            'K2':self.cb_K_SHOWVar2.get(), 'Y2':self.cb_Y_SHOWVar2.get(), 'M2':self.cb_M_SHOWVar2.get(), 'C2':self.cb_C_SHOWVar2.get(), '2ذهبي':self.cb_zahabi_SHOWVar2.get(), '2فضي':self.cb_faddi_SHOWVar2.get(), '2صبغة':self.cb_sapgha_SHOWVar2.get(), '2ورنيش':self.cb_warnish_SHOWVar2.get(), '2كحلي':self.cb_kohley_SHOWVar2.get(), '2اسبيشيال':self.sSHOWVar2.get(), 
            'عدد الدفاتر':self.daftar_countSHOWVar.get(), 'عدد المجموعات':self.groups_countSHOWVar.get(), 'الترتيب':self.counterSHOWVar.get(), 'الترقيم':{'من':self.num_of_countSHOWVar1.get(), 'الي':self.num_of_countSHOWVar2.get()}, 
            'التجليد':[[self.slofanCkb_SHOWVar.get(), self.slofan_SHOWVar.get(), self.slofanFinNum_SHOWVar.get(), self.gha_SHOWVar.get()], 
                        [self.UVCkb_SHOWVar.get(), self.UV_SHOWVar.get(), self.UVFinNum_SHOWVar.get()], 
                        [self.taksirCkb_SHOWVar.get(), self.taksir_SHOWVar.get(), self.taksirNum_SHOWVar.get(), self.formaCkb_SHOWVar.get(), self.forma_SHOWVar.get()],
                        [self.spotCkb_SHOWVar.get(), self.spot_SHOWVar.get(), self.filmCkb_SHOWVar.get(), self.film_SHOWVar.get()],
                        [self.aklashehCkb_SHOWVar.get(), self.aklasheh_SHOWVar.get(), self.pasmaCkb_SHOWVar.get(), self.pasma_SHOWVar.get()],
                        [self.taglidCkb_SHOWVar.get(), self.taglid_SHOWVar.get(), self.taglidNum_SHOWVar.get(), self.taglidSal_SHOWVar.get()],
                        [self.tawdibCkb_SHOWVar.get(), self.tawdib_SHOWVar.get(), self.tasmimCkb_SHOWVar.get(), self.tasmim_SHOWVar.get(), self.slkCkb_SHOWVar.get(), self.slk_SHOWVar.get()],
                        [self.naklCkb_SHOWVar.get(), self.nakl_SHOWVar.get(), self.khadmatCkb_SHOWVar.get(), self.khadmat_SHOWVar.get(), self.kasCkb_SHOWVar.get(), self.kas_SHOWVar.get()]]
        }

        with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.name_of_work_entry.get()}/fatoraInformation.json', 'w') as file:
            json.dump(info_dict, file)

        fatora_salaries = {
            'K':self.K_SHOWvar.get(),
            'Y':self.Y_SHOWvar.get(),
            'M':self.M_SHOWvar.get(),
            'C':self.C_SHOWvar.get(),
            'zahabi':self.zahabi_SHOWvar.get(),
            'faddi':self.faddi_SHOWvar.get(),
            'sapgha':self.sapgha_SHOWvar.get(),
            'warnish':self.warnish_SHOWvar.get(),
            'kohley':self.kohley_SHOWvar.get(),
            'spechial':self.spechial_SHOWvar.get(),
            'slofan':self.slofan_SHOWvar.get(),
            'UV':self.UV_SHOWvar.get(),
            'taksir':self.taksir_SHOWvar.get(), 
            'film' : self.film_SHOWvar.get()
            }

        with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.name_of_work_entry.get()}/fatoraSalaries.json', 'w') as sal_json_file:
            json.dump(fatora_salaries, sal_json_file)

        sal_json_file.close()
            
        with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.name_of_work_entry.get()}/fatoraSalaries.json', 'r') as file_4:
            fatora_salaries = json.load(file_4)

        fatora_Money_SHOW = 0

        multiple_var1 = 0
        multiple_var2 = 0

        if self.tarafSHOWVar1.get() == 'المطبعة':
            if self.farkh_countSHOWVar.get() and self.salarySHOWVar1.get():
                multiple_var1 = (int(self.farkh_countSHOWVar.get()) * float(self.salarySHOWVar1.get()))
        elif self.tarafSHOWVar1.get() == 'العميل':
            multiple_var1 = 0
            
        if self.tarafSHOWVar2.get() == 'المطبعة':
            if self.zenk_countSHOWVar.get() and self.salarySHOWVar2.get():
                multiple_var2 = (int(self.zenk_countSHOWVar.get()) * float(self.salarySHOWVar2.get()))
        elif self.tarafSHOWVar2.get() == 'العميل':
            multiple_var2 = 0

        fatora_Money_SHOW += multiple_var1 + multiple_var2

        self.checkboxsVar = 0
        
        # Colors Money

        if self.cb_K_SHOWVar1.get():
            self.checkboxsVar += fatora_salaries['K']
        if self.cb_Y_SHOWVar1.get():
            self.checkboxsVar += fatora_salaries['Y']
        if self.cb_M_SHOWVar1.get():
            self.checkboxsVar += fatora_salaries['M']
        if self.cb_C_SHOWVar1.get():
            self.checkboxsVar += fatora_salaries['C']
        if self.cb_zahabi_SHOWVar1.get():
            self.checkboxsVar += fatora_salaries['zahabi']
        if self.cb_faddi_SHOWVar1.get():
            self.checkboxsVar += fatora_salaries['faddi']
        if self.cb_sapgha_SHOWVar1.get():
            self.checkboxsVar += fatora_salaries['sapgha']
        if self.cb_warnish_SHOWVar1.get():
            self.checkboxsVar += fatora_salaries['warnish']
        if self.cb_kohley_SHOWVar1.get():
            self.checkboxsVar += fatora_salaries['kohley']
        if self.sSHOWVar1.get():
            self.checkboxsVar += fatora_salaries['spechial']

        if self.cb_K_SHOWVar2.get():
            self.checkboxsVar += fatora_salaries['K']
        if self.cb_Y_SHOWVar2.get():
            self.checkboxsVar += fatora_salaries['Y']
        if self.cb_M_SHOWVar2.get():
            self.checkboxsVar += fatora_salaries['M']
        if self.cb_C_SHOWVar2.get():
            self.checkboxsVar += fatora_salaries['C']
        if self.cb_zahabi_SHOWVar2.get():
            self.checkboxsVar += fatora_salaries['zahabi']
        if self.cb_faddi_SHOWVar2.get():
            self.checkboxsVar += fatora_salaries['faddi']
        if self.cb_sapgha_SHOWVar2.get():
            self.checkboxsVar += fatora_salaries['sapgha']
        if self.cb_warnish_SHOWVar2.get():
            self.checkboxsVar += fatora_salaries['warnish']
        if self.cb_kohley_SHOWVar2.get():
            self.checkboxsVar += fatora_salaries['kohley']
        if self.sSHOWVar2.get():
            self.checkboxsVar += fatora_salaries['spechial']

        # if self.sahba_countSHOWVar.get():
        #     sahbaCountVar_int = int(f'{self.sahba_countSHOWVar.get()}')
        #     sahba_part_2 = int(str(sahbaCountVar_int)[1:])
            
        #     if sahbaCountVar_int > 1000:
        #         if len(str(sahbaCountVar_int)) == 4:
        #             self.counter = int(str(self.sahba_countSHOWVar.get())[0])
        #         if len(str(sahbaCountVar_int)) == 5:
        #             self.counter = int(str(self.sahba_countSHOWVar.get())[0:2])
        #         if len(str(sahbaCountVar_int)) == 6:
        #             self.counter = int(str(self.sahba_countSHOWVar.get())[0:3])
        #         if sahba_part_2 > 100:
        #             self.counter += 1
        #     else:
        #         self.counter = 1
                
        # fatora_Money_SHOW += (self.counter * self.checkboxsVar) 

        if self.sahba2_countSHOWVar.get():
            fatora_Money_SHOW += (float(self.sahba2_countSHOWVar.get()) * self.checkboxsVar)
        
        # Taglid Money
        if self.slofanCkb_SHOWVar.get():
            fatora_Money_SHOW += (int(self.slofanFinNum_SHOWVar.get()) * fatora_salaries['slofan'])
        if self.UVCkb_SHOWVar.get():
            fatora_Money_SHOW += (int(self.UVFinNum_SHOWVar.get()) * fatora_salaries['UV'])
        if self.taksirCkb_SHOWVar.get():
            
            # old way
            # if self.taksirNum_SHOWVar.get():
            #     taksir1 = int(f'{self.taksirNum_SHOWVar.get()}')
            #     taksir2 = int(str(taksir1)[1:])

            #     self.counter2SHOW = 0
            #     if taksir1 >= 1000:
            #         if len(str(taksir1)) == 4:
            #             self.counter2SHOW = int(str(self.taksirNum_SHOWVar.get())[0])
            #         if len(str(taksir1)) == 5:
            #             self.counter2SHOW = int(str(self.taksirNum_SHOWVar.get())[:2])
            #         if len(str(taksir1)) == 6:
            #             self.counter2SHOW = int(str(self.taksirNum_SHOWVar.get())[:3])
            #         if taksir2 > 100:
            #             self.counter2SHOW += 1
            #     else:
            #         self.counter2SHOW = 1
                
            fatora_Money_SHOW += (int(self.taksirNum_SHOWVar.get()) * fatora_salaries['taksir'])
                
        if self.formaCkb_SHOWVar.get():
            fatora_Money_SHOW += float(self.forma_SHOWVar.get())
        if self.spotCkb_SHOWVar.get():
            fatora_Money_SHOW += float(self.spot_SHOWVar.get())
        if self.filmCkb_SHOWVar.get():
            fatora_Money_SHOW += fatora_salaries['film']
        if self.aklashehCkb_SHOWVar.get():
            fatora_Money_SHOW += float(self.aklashehSal_SHOWVar.get())
        if self.pasmaCkb_SHOWVar.get():
            fatora_Money_SHOW += float(self.pasma_SHOWVar.get())
        if self.taglidCkb_SHOWVar.get():
            fatora_Money_SHOW += (float(self.taglidNum_SHOWVar.get()) * float(self.taglidSal_SHOWVar.get()))
        if self.tawdibCkb_SHOWVar.get():
            fatora_Money_SHOW += float(self.tawdib_SHOWVar.get())
        if self.tasmimCkb_SHOWVar.get():
            fatora_Money_SHOW += float(self.tasmim_SHOWVar.get())
        if self.slkCkb_SHOWVar.get():
            fatora_Money_SHOW += float(self.slk_SHOWVar.get())
        if self.kasCkb_SHOWVar.get():
            fatora_Money_SHOW += float(self.kas_SHOWVar.get())
        if self.khadmatCkb_SHOWVar.get():
            fatora_Money_SHOW += float(self.khadmat_SHOWVar.get())
        if self.naklCkb_SHOWVar.get():
            fatora_Money_SHOW += float(self.nakl_SHOWVar.get())
            
        with open(f'Project_files/Clients Work/{self.searchVar.get()}/{new_name}/All Money.json', 'w') as file_2:
            json.dump(fatora_Money_SHOW, file_2)
            
        self.f_totalSHOWVar.set(fatora_Money_SHOW)

        db.commit()
        file_2.close()
        file.close()
        self.fatoraDateSort()
        self.fatoraNumberSort()
        self.display_money()
        self.Display_info_2()
        db.close()

    # ===================================================================================
    # Display Information of the Client Work
    def Display_info_2(self):
        db = sqlite3.connect(F"Project_files/Clients Work/{self.searchVar.get()}/Fawatir.db")
        cr = db.cursor()
        
        # Fetch All Data from Database
        cr.execute('SELECT * FROM All_fatora')
        self.rows = cr.fetchall()
        
        db_2 = sqlite3.connect('Project_files/Clients.db')
        cr_2 = db_2.cursor()
        
        cr_2.execute(f'SELECT all_of_money FROM Clients WHERE name = "{self.searchVar.get()}"')
        fetched_data = cr_2.fetchall()
        
        for x in fetched_data:
            for y in x:
                self.pakyElhesap_lbl_2.config(text=f'{y}')
        
        db_2.commit()
        db_2.close()
        
        # Clear existing data from the table
        if len(self.rows) != 0:
            self.tree.delete(*self.tree.get_children())
            
            for x in range(len(self.rows)):
                # Center the data in the "Icon" column
                self.tree.insert('', 'end', values=self.rows[x])
            
            # lst = []
            # for line in self.tree.get_children():
            #     lst = self.tree.item(line)['values']
     
            db.commit()
                
            db.close()
        else:
            self.tree.delete(*self.tree.get_children())

    # ===================================================================================

    def destroy_func1(self):
        
        self.fatora_reset()
        self.n_window.destroy()

    # ===================================================================================

    def destroy_func2(self):
        self.s_window.destroy()
        self.f_searchVar.set('')
        self.fatora_reset_2()
        self.Display_info_2()

    def work_window_distroy(self):
        self.work_window.destroy()
        self.searchVar.set('')
        self.Display_info()

    # ===================================================================================
    # Fatora Search Funcation
    def f_search(self):
        searched_fatora = self.f_searchVar.get()

        db = sqlite3.connect(F"Project_files/Clients Work/{self.searchVar.get()}/Fawatir.db")   
        cr = db.cursor()

        # Fetch All Data from Database
        cr.execute(f'SELECT * FROM All_fatora where f_name = "{searched_fatora}"')
        self.rows = cr.fetchall()
        
        # Clear existing data from the table
        if len(self.rows) != 0:
            self.tree.delete(*self.tree.get_children())
            
            for row in self.rows:
                # Center the data in the "Icon" column
                self.tree.insert('', 'end', values=row)

            db.commit()
            db.close()

        # ===================================================================================

    # Reset Work Table Funcation
    def table_reset_2(self):
        self.Display_info_2()
        self.f_searchVar.set('')

    # ===================================================================================
    
    # Salaries Initialization
    def put_salary_frame(self):
        self.psf = Toplevel()
        self.psf.title('وضع الاسعار')
        self.psf.config(background='white')
        self.psf_width = self.work_window_width // 3
        self.psf_height = self.work_window_height
        self.psf.geometry(f'{self.psf_width}x{self.psf_height}+130+{(self.winfo_screenheight()-self.psf_height)//2}')

        l_1 = Label(self.psf, text='وضع اسعار الألوان', bg='white', fg='black', font=(self.Font_Family, 18, 'bold')).pack(fill=X, pady=(10, 0)) 
        sep = Frame(self.psf, bg='black', width=160, height=1).pack(pady=5)
        # The Colors [ K, Y, M, C, zahabi, faddi, sapgha, warnish, kohley, spechial ]
        label_K = Label(self.psf, text=' : K', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=270, y=60)
        entry = Entry(self.psf, bd=2, bg='white', textvariable=self.K_var, justify='center',font=(self.Font_Family, 15)).place(x=220,y=65, width=50, height=20)
        label_Y = Label(self.psf, text=' : Y', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=270, y=90+10)
        entry = Entry(self.psf, bd=2, bg='white', textvariable=self.Y_var, justify='center',font=(self.Font_Family, 15)).place(x=220,y=95+10, width=50, height=20)
        label_M = Label(self.psf, text=' : M', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=270, y=125+10)
        entry = Entry(self.psf, bd=2, bg='white', textvariable=self.M_var, justify='center',font=(self.Font_Family, 15)).place(x=220,y=130+10, width=50, height=20)
        label_C = Label(self.psf, text=' : C', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=270, y=155+10)
        entry = Entry(self.psf, bd=2, bg='white', textvariable=self.C_var, justify='center',font=(self.Font_Family, 15)).place(x=220,y=160+10, width=50, height=20)
        label_zahabi = Label(self.psf, text=' : ذهبي', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=120, y=60)
        entry = Entry(self.psf, bd=2, bg='white', textvariable=self.zahabi_var, justify='center',font=(self.Font_Family, 15)).place(x=70,y=65, width=50, height=20)
        label_faddi = Label(self.psf, text=' : فضي', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=120, y=90+10)
        entry = Entry(self.psf, bd=2, bg='white', textvariable=self.faddi_var, justify='center',font=(self.Font_Family, 15)).place(x=70,y=95+10, width=50, height=20)
        label_sapgha = Label(self.psf, text=' : صبغة', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=120, y=125+10)
        entry = Entry(self.psf, bd=2, bg='white', textvariable=self.sapgha_var, justify='center',font=(self.Font_Family, 15)).place(x=70,y=130+10, width=50, height=20)
        label_warnish = Label(self.psf, text=' : ورنيش', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=120, y=155+10)
        entry = Entry(self.psf, bd=2, bg='white', textvariable=self.warnish_var, justify='center',font=(self.Font_Family, 15)).place(x=70,y=160+10, width=50, height=20)
        label_kohley = Label(self.psf, text=' : كحلي', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=120, y=185+10)
        entry = Entry(self.psf, bd=2, bg='white', textvariable=self.kohley_var, justify='center',font=(self.Font_Family, 15)).place(x=70,y=190+10, width=50, height=20)
        label_spechial = Label(self.psf, text=' : الألوان الاسبيشيال', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=120, y=215+10)
        entry = Entry(self.psf, bd=2, bg='white', textvariable=self.spechial_var, justify='center',font=(self.Font_Family, 15)).place(x=70,y=220+10, width=50, height=20)
        sep = Frame(self.psf, bg='black', width=160, height=1).pack(fill=X, pady=(237-20, 0))

        l_2 = Label(self.psf, text='وضع اسعار التجليد', bg='white', fg='black', font=(self.Font_Family, 18, 'bold')).pack(fill=X, pady=((10, 0))) 
        sep = Frame(self.psf, bg='black', width=160, height=1).pack(pady=5)

        # the taglid [ slofan, UV, spot, tawdib, taksir, dapoos, lask, taglid, forma, pasma ]
        label_slofan = Label(self.psf, text=' : سلوفان', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=255, y=330)
        entry = Entry(self.psf, bd=2, bg='white', textvariable=self.slofan_var, justify='center',font=(self.Font_Family, 15)).place(x=205,y=65+270, width=50, height=20)
        label_UV = Label(self.psf, text=' : U.V', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=255, y=90+275)
        entry = Entry(self.psf, bd=2, bg='white', textvariable=self.UV_var, justify='center',font=(self.Font_Family, 15)).place(x=205,y=95+275, width=50, height=20)
        # label_spot = Label(self.psf, text=' : اسبوت', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=255, y=122+275)
        # entry = Entry(self.psf, bd=2, bg='white', textvariable=self.spot_var, justify='center',font=(self.Font_Family, 15)).place(x=205,y=128+275, width=50, height=20)
        # label_tawdib = Label(self.psf, text=' : توضيب', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=255, y=155+275)
        # entry = Entry(self.psf, bd=2, bg='white', textvariable=self.tawdib_var, justify='center',font=(self.Font_Family, 15)).place(x=205,y=160+275, width=50, height=20)
        # label_pasma = Label(self.psf, text=' : بصمة', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=255, y=185+275)
        # entry = Entry(self.psf, bd=2, bg='white', textvariable=self.taksir_var, justify='center',font=(self.Font_Family, 15)).place(x=205,y=190+275, width=50, height=20)
        label_taksir = Label(self.psf, text=' : تكسير', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=115, y=330)
        entry = Entry(self.psf, bd=2, bg='white', textvariable=self.taksir_var, justify='center',font=(self.Font_Family, 15)).place(x=65,y=65+270, width=50, height=20)
        # label_dapoos = Label(self.psf, text=' : دبوس', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=115, y=90+275)
        # entry = Entry(self.psf, bd=2, bg='white', textvariable=self.lask_var, justify='center',font=(self.Font_Family, 15)).place(x=65,y=95+275, width=50, height=20)
        # label_lask = Label(self.psf, text=' : لصق', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=115, y=122+275)
        # entry = Entry(self.psf, bd=2, bg='white', textvariable=self.taglid_var, justify='center',font=(self.Font_Family, 15)).place(x=65,y=128+275, width=50, height=20)
        # label_taglid = Label(self.psf, text=' : تجليد', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=115, y=155+275)
        # entry = Entry(self.psf, bd=2, bg='white', textvariable=self.forma_var, justify='center',font=(self.Font_Family, 15)).place(x=65,y=160+275, width=50, height=20)
        # label_forma = Label(self.psf, text=' : فورمة', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=115, y=185+275)
        # entry = Entry(self.psf, bd=2, bg='white', textvariable=self.pasma_var, justify='center',font=(self.Font_Family, 15)).place(x=65,y=190+275, width=50, height=20)
        label_film = Label(self.psf, text=' : فيلم', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=115, y=90+275)
        entry = Entry(self.psf, bd=2, bg='white', textvariable=self.film_var, justify='center',font=(self.Font_Family, 15)).place(x=65,y=95+275, width=50, height=20)
        # label_forma = Label(self.psf, text=' : اكلاشيه', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=115, y=245+275)
        # entry = Entry(self.psf, bd=2, bg='white', textvariable=self.pasma_var, justify='center',font=(self.Font_Family, 15)).place(x=65,y=250+275, width=50, height=20)

        # CTkButtons
        btn_1 = CTkButton(self.psf, text='تسجيل الأسعار', 
                          text_color='white', 
                            bg_color='white',
                            cursor='hand2',
                            font=(self.Font_Family, 22),
                            border_width=2,
                            border_color='silver',
                            corner_radius=10,
                            width=200,
                            height=60,
                          command=self.save_salaries)
        btn_1.pack(pady=(170+20, 0))
        # btn_2 = CTkButton(self.psf, text='وضع الأسعار من جديد', bg=self.btn_bg, fg='white', width=25, height=1, font=(self.Font_Family, 16, 'bold'), command=self.Reset_salaries_mess)
        # btn_2.pack(pady=(5, 0))

        btn_3 = CTkButton(self.psf, text='إغلاق النافذة', 
                          text_color='white', 
                          fg_color='red',
                          hover_color='#E30004',
                            bg_color='white',
                            cursor='hand2',
                            font=(self.Font_Family, 22),
                            border_width=2,
                            border_color='silver',
                            corner_radius=10,
                            width=200,
                            height=60,
                          command=self.psf.destroy)
        btn_3.pack(pady=(10, 0))

        self.show_salaries()

    def save_salaries(self):
        # make Salaries Dictionary
            # The Colors [ K, Y, M, C, zahabi, faddi, sapgha, warnish, kohley, spechial ]
            # the taglid [ slofan, UV, spot, tawdib, taksir, dapoos, lask, taglid, forma, pasma ]
        self.Salaries = {
            'K':self.K_var.get(),
            'Y':self.Y_var.get(),
            'M':self.M_var.get(),
            'C':self.C_var.get(),
            'zahabi':self.zahabi_var.get(),
            'faddi':self.faddi_var.get(),
            'sapgha':self.sapgha_var.get(),
            'warnish':self.warnish_var.get(),
            'kohley':self.kohley_var.get(),
            'spechial':self.spechial_var.get(),
            'slofan':self.slofan_var.get(),
            'UV':self.UV_var.get(),
            'taksir':self.taksir_var.get(), 
            'film' : self.film_var.get()
        }
        # Add Salaries Dictionary To json File
        with open('Project_files/Salaries.json', 'w') as file:
            json.dump(self.Salaries, file)
        file.close()
        
        self.show_salaries()

    def show_sla_window(self):
        self.ssf = Toplevel()
        self.ssf.title('وضع الاسعار')
        self.ssf.config(background='white')
        self.ssf_width = self.work_window_width // 3
        self.ssf_height = self.work_window_height
        self.ssf.geometry(f'{self.ssf_width}x{self.ssf_height}+130+{(self.winfo_screenheight()-self.ssf_height)//2}')

        l_1 = Label(self.ssf, text='وضع اسعار الألوان', bg='white', fg='black', font=(self.Font_Family, 18, 'bold')).pack(fill=X, pady=(10, 0)) 
        sep = Frame(self.ssf, bg='black', width=160, height=1).pack(pady=5)
        # The Colors [ K, Y, M, C, zahabi, faddi, sapgha, warnish, kohley, spechial ]
        label_K = Label(self.ssf, text=' : K', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=270, y=60)
        entry = Entry(self.ssf, bd=2, bg='white', textvariable=self.K_SHOWvar, justify='center',font=(self.Font_Family, 15)).place(x=220,y=65, width=50, height=20)
        label_Y = Label(self.ssf, text=' : Y', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=270, y=90+10)
        entry = Entry(self.ssf, bd=2, bg='white', textvariable=self.Y_SHOWvar, justify='center',font=(self.Font_Family, 15)).place(x=220,y=95+10, width=50, height=20)
        label_M = Label(self.ssf, text=' : M', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=270, y=125+10)
        entry = Entry(self.ssf, bd=2, bg='white', textvariable=self.M_SHOWvar, justify='center',font=(self.Font_Family, 15)).place(x=220,y=130+10, width=50, height=20)
        label_C = Label(self.ssf, text=' : C', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=270, y=155+10)
        entry = Entry(self.ssf, bd=2, bg='white', textvariable=self.C_SHOWvar, justify='center',font=(self.Font_Family, 15)).place(x=220,y=160+10, width=50, height=20)
        label_zahabi = Label(self.ssf, text=' : ذهبي', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=120, y=60)
        entry = Entry(self.ssf, bd=2, bg='white', textvariable=self.zahabi_SHOWvar, justify='center',font=(self.Font_Family, 15)).place(x=70,y=65, width=50, height=20)
        label_faddi = Label(self.ssf, text=' : فضي', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=120, y=90+10)
        entry = Entry(self.ssf, bd=2, bg='white', textvariable=self.faddi_SHOWvar, justify='center',font=(self.Font_Family, 15)).place(x=70,y=95+10, width=50, height=20)
        label_sapgha = Label(self.ssf, text=' : صبغة', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=120, y=125+10)
        entry = Entry(self.ssf, bd=2, bg='white', textvariable=self.sapgha_SHOWvar, justify='center',font=(self.Font_Family, 15)).place(x=70,y=130+10, width=50, height=20)
        label_warnish = Label(self.ssf, text=' : ورنيش', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=120, y=155+10)
        entry = Entry(self.ssf, bd=2, bg='white', textvariable=self.warnish_SHOWvar, justify='center',font=(self.Font_Family, 15)).place(x=70,y=160+10, width=50, height=20)
        label_kohley = Label(self.ssf, text=' : كحلي', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=120, y=185+10)
        entry = Entry(self.ssf, bd=2, bg='white', textvariable=self.kohley_SHOWvar, justify='center',font=(self.Font_Family, 15)).place(x=70,y=190+10, width=50, height=20)
        label_spechial = Label(self.ssf, text=' : الألوان الاسبيشيال', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=120, y=215+10)
        entry = Entry(self.ssf, bd=2, bg='white', textvariable=self.spechial_SHOWvar, justify='center',font=(self.Font_Family, 15)).place(x=70,y=220+10, width=50, height=20)
        sep = Frame(self.ssf, bg='black', width=160, height=1).pack(fill=X, pady=(237-20, 0))

        l_2 = Label(self.ssf, text='وضع اسعار التجليد', bg='white', fg='black', font=(self.Font_Family, 18, 'bold')).pack(fill=X, pady=((10, 0))) 
        sep = Frame(self.ssf, bg='black', width=160, height=1).pack(pady=5)

        # the taglid [ slofan, UV, spot, tawdib, taksir, dapoos, lask, taglid, forma, pasma ]
        label_slofan = Label(self.ssf, text=' : سلوفان', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=255, y=330)
        entry = Entry(self.ssf, bd=2, bg='white', textvariable=self.slofan_SHOWvar, justify='center',font=(self.Font_Family, 15)).place(x=205,y=65+270, width=50, height=20)
        label_UV = Label(self.ssf, text=' : U.V', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=255, y=90+275)
        entry = Entry(self.ssf, bd=2, bg='white', textvariable=self.UV_SHOWvar, justify='center',font=(self.Font_Family, 15)).place(x=205,y=95+275, width=50, height=20)
        label_taksir = Label(self.ssf, text=' : تكسير', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=115, y=330)
        entry = Entry(self.ssf, bd=2, bg='white', textvariable=self.taksir_SHOWvar, justify='center',font=(self.Font_Family, 15)).place(x=65,y=65+270, width=50, height=20)
        label_film = Label(self.ssf, text=' : فيلم', bg='white', fg='black', font=(self.Font_Family, 15)).place(x=115, y=90+275)
        entry = Entry(self.ssf, bd=2, bg='white', textvariable=self.film_SHOWvar, justify='center',font=(self.Font_Family, 15)).place(x=65,y=95+275, width=50, height=20)

        # CTkButtons
        btn_3 = CTkButton(self.ssf, text='إغلاق النافذة',
                          text_color='white', 
                          fg_color='red',
                          hover_color='#E30004',
                                bg_color='white',
                                cursor='hand2',
                                font=(self.Font_Family, 22),
                                border_width=2,
                                border_color='silver',
                                corner_radius=10,
                                width=70,
                                height=40,
                          command=self.ssf.destroy)
        btn_3.pack(pady=(170+50, 0))

        if os.path.exists(f'Project_files/Clients Work/{self.searchVar.get()}/{self.f_searchVar.get()}/fatoraSalaries.json'):
            with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.f_searchVar.get()}/fatoraSalaries.json', 'r') as sal_file:
                sal_dict = json.load(sal_file)

            self.K_SHOWvar.set(sal_dict['K'])
            self.Y_SHOWvar.set(sal_dict['Y'])
            self.M_SHOWvar.set(sal_dict['M'])
            self.C_SHOWvar.set(sal_dict['C'])
            self.zahabi_SHOWvar.set(sal_dict['zahabi'])
            self.faddi_SHOWvar.set(sal_dict['faddi'])
            self.sapgha_SHOWvar.set(sal_dict['sapgha'])
            self.warnish_SHOWvar.set(sal_dict['warnish'])
            self.kohley_SHOWvar.set(sal_dict['kohley'])
            self.spechial_SHOWvar.set(sal_dict['spechial'])
            self.slofan_SHOWvar.set(sal_dict['slofan'])
            self.UV_SHOWvar.set(sal_dict['UV'])
            self.taksir_SHOWvar.set(sal_dict['taksir'])
            self.film_SHOWvar.set(sal_dict['film'])

            sal_file.close()

    def save_SHOW_salaries(self):
        pass

    def show_salaries(self):
        with open('Project_files/Salaries.json', 'r') as file:
            try:
                Salaries = json.load(file)
            except EOFError:
                print('The File is\'t Have Data to show')
        self.K_var.set(Salaries['K'])
        self.Y_var.set(Salaries['Y'])
        self.M_var.set(Salaries['M'])
        self.C_var.set(Salaries['C'])
        self.zahabi_var.set(Salaries['zahabi'])
        self.faddi_var.set(Salaries['faddi'])
        self.sapgha_var.set(Salaries['sapgha'])
        self.warnish_var.set(Salaries['warnish'])
        self.kohley_var.set(Salaries['kohley'])
        self.spechial_var.set(Salaries['spechial'])
        self.slofan_var.set(Salaries['slofan'])
        self.UV_var.set(Salaries['UV'])
        self.taksir_var.set(Salaries['taksir'])
        self.film_var.set(Salaries['film'])
        
    # ===================================================================================
    
    def del_fatora_mess(self):

        db = sqlite3.connect(f'Project_files/Clients Work/{self.searchVar.get()}/Fawatir.db')
        cr = db.cursor()

        cr.execute('Select f_name from All_fatora')
        names = cr.fetchall()
        Client_fatora_names = []

        for name in names:
            for f_name in name:
                Client_fatora_names.append(f_name)

        db.commit()
        db.close()

        if self.f_searchVar.get() in Client_fatora_names:

            self.dfm = Toplevel()
            self.dfm.title('رسالة حذف الفاتوره')
            self.dfm_width = 350
            self.dfm_height = 120
            self.dfm.config(background='white')
            self.dfm.geometry(f'{self.dfm_width}x{self.dfm_height}+{(self.winfo_screenwidth() - self.dfm_width)//2}+{(self.winfo_screenheight() - self.dfm_height)//2}')

            self.dfm_lbl = Label(self.dfm, text='هل تريد حذف هذه الفاتورة ؟', bg='white', fg='black', font=(self.Font_Family, 18, 'bold')).pack(pady=(10,0))

            yes_btn = CTkButton(self.dfm, text='نعم', 
                                text_color='white', 
                                fg_color='red', 
                                hover_color='#E30004',
                                    bg_color='white',
                                    cursor='hand2',
                                    font=(self.Font_Family, 22),
                                    border_width=2,
                                    border_color='grey',
                                    corner_radius=10,
                                    width=70,
                                    height=40,
                                command=self.del_fatora).place(x=185, y=60)

            yes_btn = CTkButton(self.dfm, text='لا',
                                text_color='white', 
                                    bg_color='white',
                                    cursor='hand2',
                                    font=(self.Font_Family, 22),
                                    border_width=2,
                                    border_color='silver',
                                    corner_radius=10,
                                    width=70,
                                    height=40,
                                command=self.dfm.destroy).place(x=105, y=60)
        
        else:
            None

    # ===================================================================================

    # Delete Fatora Fucation
    def del_fatora(self):
        Clients_db = sqlite3.connect("Project_files/Clients.db")
        Clients_cr = Clients_db.cursor()

        db = sqlite3.connect(f"Project_files/Clients Work/{self.searchVar.get()}/Fawatir.db")   
        cr = db.cursor()

        # Delete Fatora Money from the Client all_of_money
        cr.execute(f'select (f_money) from All_fatora where f_number = {self.delNumberVar.get()}')
        fatora_money = cr.fetchall()

        fm = 0
        for f in fatora_money:
            for m in f:
                fm += m
            
        Clients_cr.execute(f'select (all_of_money) from Clients where name = "{self.searchVar.get()}"')
        client_all_money = Clients_cr.fetchall()

        cam = 0
        for am in client_all_money:
            for m in am:
                cam += m
        
        if cam > 0:
            fi_money = cam - fm
            Clients_cr.execute(f'update Clients set all_of_money = {fi_money} where name = "{self.searchVar.get()}"')

        # Fetch All Data from Database
        # old way 
        cr.execute(f'delete FROM All_fatora where f_number = {self.delNumberVar.get()}')
        # new way
        # cr.execute(f'update All_fatora set f_money = "لاغي" where f_number = {self.delNumberVar.get()}')

        # Delete Fatora File
        try:
            if self.f_searchVar.get():
                if os.path.exists(f"Project_files/Clients Work/{self.searchVar.get()}/{self.f_searchVar.get()}"):
                    shutil.rmtree(f"Project_files/Clients Work/{self.searchVar.get()}/{self.f_searchVar.get()}")
                    
        except Exception:
            if self.f_searchVar.get():
                if os.path.exists(f"Project_files/Clients Work/{self.searchVar.get()}/{self.f_searchVar.get()}"):
                    os.rmdir(f"Project_files/Clients Work/{self.searchVar.get()}/{self.f_searchVar.get()}")
    
        db.commit() 
        db.close()

        Clients_db.commit()
        Clients_db.close() 

        self.dfm.destroy()
        self.Display_info()
        self.fatoraNumberSort()
        self.f_searchVar.set('')
        self.Display_info_2()


    # ===================================================================================
    
    def get_cursor_2(self, event):
        cursor_info = self.tree.focus()
        rows = self.tree.item(cursor_info)['values']
        self.f_searchVar.set(rows[3])
        self.delNumberVar.set(rows[4])
        cr_date = rows[2].replace(' / ', '-', 1).replace(' / ', '/')
        year = cr_date[:cr_date.find('-')]
        month = cr_date[cr_date.find('-'):cr_date.find('/')].strip('-')
        day = cr_date[cr_date.find('/'):].strip('/')

        # Fetch The info_dict From json File and Show in the Window 
        if os.path.exists(f'Project_files/Clients Work/{self.searchVar.get()}/{self.f_searchVar.get()}/fatoraInformation.json'):
            with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.f_searchVar.get()}/fatoraInformation.json', 'r') as file:
                info_dict = json.load(file)
            file.close()

            # The Final
            self.f_nameSHOWVar.set(info_dict['اسم العملية'])
            self.e1_dateSHOWVar.set(day)
            self.e2_dateSHOWVar.set(month)
            self.e3_dateSHOWVar.set(year)
            self.tarafSHOWVar1.set(info_dict['1طرف'])
            self.farkh_countSHOWVar.set(info_dict['عدد الافرخ'])
            self.typeSHOWVar1.set(info_dict['نوع'][0])
            self.typeSHOWVar2.set(info_dict['نوع'][1])
            self.sizeSHOWVar1.set(info_dict['مقاس القص'][0])
            self.sizeSHOWVar2.set(info_dict['مقاس القص'][1])
            self.salarySHOWVar1.set(info_dict['1السعر'])
            self.tarafSHOWVar2.set(info_dict['2طرف'])
            self.zenk_countSHOWVar.set(info_dict['عدد الزنك'])
            self.salarySHOWVar2.set(info_dict['2السعر'])
            self.sahba_countSHOWVar.set(info_dict['عدد السحبات'])
            self.sahba2_countSHOWVar.set(info_dict['الرقم الفعلي'])
            self.Check_btn_fb_SHOWVar.set(info_dict['تطبع وتقلب'])
            self.cb_K_SHOWVar1.set(info_dict['K1'])
            self.cb_Y_SHOWVar1.set(info_dict['Y1'])
            self.cb_M_SHOWVar1.set(info_dict['M1'])
            self.cb_C_SHOWVar1.set(info_dict['C1'])
            self.cb_zahabi_SHOWVar1.set(info_dict['1ذهبي'])
            self.cb_faddi_SHOWVar1.set(info_dict['1فضي'])
            self.cb_sapgha_SHOWVar1.set(info_dict['1صبغة'])
            self.cb_warnish_SHOWVar1.set(info_dict['1ورنيش'])
            self.cb_kohley_SHOWVar1.set(info_dict['1كحلي'])
            self.sSHOWVar1.set(info_dict['1اسبيشيال'])
            self.cb_K_SHOWVar2.set(info_dict['K2'])
            self.cb_Y_SHOWVar2.set(info_dict['Y2'])
            self.cb_M_SHOWVar2.set(info_dict['M2'])
            self.cb_C_SHOWVar2.set(info_dict['C2'])
            self.cb_zahabi_SHOWVar2.set(info_dict['2ذهبي'])
            self.cb_faddi_SHOWVar2.set(info_dict['2فضي'])


            self.cb_sapgha_SHOWVar2.set(info_dict['2صبغة'])
            self.cb_warnish_SHOWVar2.set(info_dict['2ورنيش'])
            self.cb_kohley_SHOWVar2.set(info_dict['2كحلي'])
            self.sSHOWVar2.set(info_dict['2اسبيشيال'])
            self.daftar_countSHOWVar.set(info_dict['عدد الدفاتر'])
            self.groups_countSHOWVar.set(info_dict['عدد المجموعات'])
            self.counterSHOWVar.set(info_dict['الترتيب'])
            self.num_of_countSHOWVar1.set(info_dict['الترقيم']['من'])
            self.num_of_countSHOWVar2.set(info_dict['الترقيم']['الي'])
            self.slofanCkb_SHOWVar.set(info_dict['التجليد'][0][0])
            self.slofan_SHOWVar.set(info_dict['التجليد'][0][1])
            self.slofanFinNum_SHOWVar.set(info_dict['التجليد'][0][2])
            self.gha_SHOWVar.set(info_dict['التجليد'][0][3])
            self.UVCkb_SHOWVar.set(info_dict['التجليد'][1][0])
            self.UV_SHOWVar.set(info_dict['التجليد'][1][1])
            self.UVFinNum_SHOWVar.set(info_dict['التجليد'][1][2])
            self.taksirCkb_SHOWVar.set(info_dict['التجليد'][2][0])
            self.taksir_SHOWVar.set(info_dict['التجليد'][2][1])
            self.taksirNum_SHOWVar.set(info_dict['التجليد'][2][2])
            self.formaCkb_SHOWVar.set(info_dict['التجليد'][2][3])
            self.forma_SHOWVar.set(info_dict['التجليد'][2][4])
            self.spotCkb_SHOWVar.set(info_dict['التجليد'][3][0])
            self.spot_SHOWVar.set(info_dict['التجليد'][3][1])
            self.filmCkb_SHOWVar.set(info_dict['التجليد'][3][2])
            self.film_SHOWVar.set(info_dict['التجليد'][3][3])
            self.aklashehCkb_SHOWVar.set(info_dict['التجليد'][4][0])
            self.aklasheh_SHOWVar.set(info_dict['التجليد'][4][1])
            self.pasmaCkb_SHOWVar.set(info_dict['التجليد'][4][2])
            self.pasma_SHOWVar.set(info_dict['التجليد'][4][3])
            self.taglidCkb_SHOWVar.set(info_dict['التجليد'][5][0])
            self.taglid_SHOWVar.set(info_dict['التجليد'][5][1])
            self.taglidNum_SHOWVar.set(info_dict['التجليد'][5][2])
            self.taglidSal_SHOWVar.set(info_dict['التجليد'][5][3])
            self.tawdibCkb_SHOWVar.set(info_dict['التجليد'][6][0])
            self.tawdib_SHOWVar.set(info_dict['التجليد'][6][1])
            self.tasmimCkb_SHOWVar.set(info_dict['التجليد'][6][2])
            self.tasmim_SHOWVar.set(info_dict['التجليد'][6][3])
            self.slkCkb_SHOWVar.set(info_dict['التجليد'][6][4])
            self.slk_SHOWVar.set(info_dict['التجليد'][6][5])
            self.naklCkb_SHOWVar.set(info_dict['التجليد'][7][0])
            self.nakl_SHOWVar.set(info_dict['التجليد'][7][1])
            self.khadmatCkb_SHOWVar.set(info_dict['التجليد'][7][2])
            self.khadmat_SHOWVar.set(info_dict['التجليد'][7][3])
            self.kasCkb_SHOWVar.set(info_dict['التجليد'][7][4])
            self.kas_SHOWVar.set(info_dict['التجليد'][7][5])
        
        if os.path.exists(f'Project_files/Clients Work/{self.searchVar.get()}/{self.f_searchVar.get()}/fatoraSalaries.json'):
            with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.f_searchVar.get()}/fatoraSalaries.json', 'r') as file:
                fatora_salaries = json.load(file)
                
            self.K_SHOWvar.set(fatora_salaries['K'])
            self.Y_SHOWvar.set(fatora_salaries['Y'])
            self.M_SHOWvar.set(fatora_salaries['M'])
            self.C_SHOWvar.set(fatora_salaries['C'])
            self.zahabi_SHOWvar.set(fatora_salaries['zahabi'])
            self.faddi_SHOWvar.set(fatora_salaries['faddi'])
            self.sapgha_SHOWvar.set(fatora_salaries['sapgha'])
            self.warnish_SHOWvar.set(fatora_salaries['warnish'])
            self.kohley_SHOWvar.set(fatora_salaries['kohley'])
            self.spechial_SHOWvar.set(fatora_salaries['spechial'])
            self.slofan_SHOWvar.set(fatora_salaries['slofan'])
            self.UV_SHOWvar.set(fatora_salaries['UV'])
            self.taksir_SHOWvar.set(fatora_salaries['taksir'])
            self.film_SHOWvar.set(fatora_salaries['film'])

        if os.path.exists(f'Project_files/Clients Work/{self.searchVar.get()}/{self.f_searchVar.get()}/All Money.json'):
            with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.f_searchVar.get()}/All Money.json', 'r') as file:
                fatora_money = json.load(file)
            
            self.f_totalSHOWVar.set(fatora_money)
            


    # Display Money in Work Table 
    def display_money(self):
        with open(f'Project_files/Clients Work/{self.searchVar.get()}/{self.name_of_work_entry.get()}/All Money.json', 'r') as file:
            fatora_money = json.load(file)

        db = sqlite3.connect(f'Project_files/Clients Work/{self.searchVar.get()}/Fawatir.db')
        cr = db.cursor()

        cr.execute(f'update All_fatora set f_money = {fatora_money} where f_name = "{self.name_of_work_entry.get()}"')

        client_money = 0
        all_money = []

        cr.execute(f'select f_money from All_fatora')
        fetched_data = cr.fetchall()
        
        for f in fetched_data:
            for m in f:
                all_money.append(m)

        for m in all_money:
            client_money += m
    
        db.commit()
        self.Display_info_2()
        db.close()

        client_db = sqlite3.connect('Project_files/Clients.db')
        c_cr = client_db.cursor()

        c_cr.execute(f'select done_of_money from Clients where name = "{self.searchVar.get()}"')

        done_money = c_cr.fetchall()

        c_cr.execute(f'update Clients set all_of_money = {client_money-done_money[0][0]} where name = "{self.searchVar.get()}"')

        client_db.commit()
        self.Display_info()
        client_db.close()

# Take instance from Printer_APP Class
App = Printer_APP()