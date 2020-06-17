#Line 195 Remove bug

from tkinter import*
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import sys,sqlite3,time
from datetime import datetime
import random
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import pycountry
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_number
from phonenumbers.phonenumberutil import region_code_for_country_code




class win2:
    def __init__(self,root):    
        self.root=root
        self.root.title("Student Management System".center(420))
        self.root.geometry("1350x700+0+0")
        self.root.configure(background = "black")
        bg_color="#074463"
        self.bg_icon = ImageTk.PhotoImage(file="PIC/1360-x-768-wallpapers-universe-scenery-hd-1360x768.jpg")
        bg_lbl = Label(self.root, image = self.bg_icon).pack(fill=Y) # we put image into our window

       # self.bg_icon = ImageTk.PhotoImage(file="beautiful-landscape-nature-scenery-1d-1360x768.jpg")
        self.F2 = ImageTk.PhotoImage(file="PIC/download1.jpeg") # here we store image to a variable using PIL module help 
        self.icon1=ImageTk.PhotoImage(file="PIC/download.jpg")
        self.icon2=ImageTk.PhotoImage(file="PIC/download (1).png")
        self.icon3=ImageTk.PhotoImage(file="PIC/download.png")
        self.icon4=ImageTk.PhotoImage(file="PIC/images.jpg")
        self.user_icon=ImageTk.PhotoImage(file="PIC/images.png")
        self.pasw_icon=ImageTk.PhotoImage(file="PIC/images (1).png")


        #self.signup_icon=ImageTk.PhotoImage(file="signup.jpg")
        

        #title=LabelFrame(self.root, bd=10, relief=GROOVE, text="SignUp",font=("times new roman", 40, "bold"),bg=bg_color,fg="gold")
        #title.place(x=0,y=0, relwidth=1,height= 110)

        #------------Variables--------------#
        self.fname=StringVar()
        self.lname=StringVar()
        self.uname=StringVar()
        self.pasw=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.contact=StringVar()
        self.Role="Admin"
        self.DOB=StringVar()
        self.code=IntVar()
        self.gender.set("Choose Gender")
        #self.DOB.set("Chose D.O.B")

        self.label, self.calendar = "", ""
        now = datetime.now()

        self.Time1=now.strftime('%H:%M:%S')

        self.today= now.strftime("%d/%m/%Y")
        #self.today = datetime.date.today()
        
        
        #self.a=self.code.get()+self.contact.get()
        #self.pn = phonenumbers.parse(self.a)
        
        #self.country = pycountry.countries.get(alpha_2=region_code_for_number(self.pn))
        

        Manage_Frame=LabelFrame(self.root,bd=10, relief=RIDGE,bg=bg_color,text="SignUp",font=("times new roman", 40, "bold"),fg="white")
        Manage_Frame.place(x=260,y=70,width=500,height=560)
        
            
        #m_title=Label(Manage_Frame,text="SIGN UP",compound=LEFT,bg=bg_color,fg="white",font=("times new roman",30,"bold"))
        #m_title.grid(row=0, columnspan=2,pady=20)

        #   ----------------------------------------------------------------------------

        lbl_roll=Label(Manage_Frame,text="First Name",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=0, column=0,padx=20,pady=10,sticky="w")

        txt_roll=Entry(Manage_Frame, textvariable=self.fname, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=0, column=1,padx=20,pady=10,sticky="w")

        lbl_roll=Label(Manage_Frame,text="Last Name",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1, column=0,padx=20,pady=10,sticky="w")

        txt_roll=Entry(Manage_Frame, textvariable=self.lname, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1, column=1,padx=20,pady=10,sticky="w")
        #   ---------------------------------------------------------------------------- 

        lbl_roll=Label(Manage_Frame, text="Password",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=2, column=0,padx=20,pady=10,sticky="w")

        txt_roll=Entry(Manage_Frame, textvariable=self.pasw, font=("times new roman",15,"bold"),bd=5,relief=GROOVE,show="*")
        txt_roll.grid(row=2, column=1,padx=20,pady=10,sticky="w")

        #   ----------------------------------------------------------------------------

        lbl_roll=Label(Manage_Frame,text="Email",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=3, column=0,padx=20,pady=10,sticky="w")

        txt_roll=Entry(Manage_Frame, textvariable=self.email, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=3, column=1,padx=20,pady=10,sticky="w")


        
        #lbl_roll=Label(Manage_Frame,text="D.O.B",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
        #lbl_roll.grid(row=6, column=0,padx=20,pady=10,sticky="w")


        
        self.font=("times new roman",20,"bold")

        labels = ['DOB']
        self.label=(Label(Manage_Frame, text="D.O.B",bg=bg_color, fg="white", font=self.font))
        self.label.place(x=20, y=260, anchor="w")

        self.calendar=(DateEntry(Manage_Frame,textvariable=self.DOB, font=("times new roman",15,"bold"), locale='en_GB',state="readonly", width=19))
        self.calendar.place(x=200, y=260, anchor="w")
        #print (self.calendar)

       # txt_roll=Entry(Manage_Frame, textvariable=self.DOB, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        #txt_roll.grid(row=6, column=1,padx=20,pady=10,sticky="w")

        #   ----------------------------------------------------------------------------


        lbl_roll=Label(Manage_Frame,text="Contact",bg=bg_color,fg="white",font=("times new roman",20,"bold"))
        lbl_roll.place(x=20, y=310, anchor="w")
 
        
        self.code.set(0)
        combo_code = OptionMenu(Manage_Frame, self.code,"+93","+355","+213","+1684","+376","+244","+1264","+672","+1268","+54","+374","+297","+61","+880","+32","+226","+359","+387","+1246","+681","+590","+1441","+673","+591","+973","+257","+229","+975","+1876","+267","+685","+599","+55","+1242","+441534","+375","+501","+7","+250","+381","+670","+262","+993","+992","+40","+690","+245","+1671","+502","+30","+240","+590","+81","+592","+441481","+594","+995","+1473","+44","+241","+503","+224","+220","+299","+350","+233","+968","+216","+962","+385","+509","+36","+852""+504","+58","+1787","+1939","+970","+680","+351","+47","+595","+964","+507","+689","+675","+51","+92","+63","+870","+48","+508","+260","+212","+372","+20","+27","+593","+39","+84","+677","+251","+252","+263","+966","+34","+291","+382","+373","+261","+590","+212","+377","+998","+95","+223","+853","+976","+692","+389","+230","+356","+265","+960","+596","+1670","+1664","+222","+441624","+256","+255","+60","+52","+972","+33","+246","+290","+358","+679","+500","+691","+298","+505","+31","+47","+264","+678","+687","+227","+672","+234","+64","+977","+674","+683","+682","+225","+41","+57","+86","+237","+56","+61","+1","+242","+236","+243","+420","+357","+61","+506","+599","+238","+53","+268","+963","+599","+996","+254","+211","+597","+686","+855","+1869","+269","+239","+421","+82","+386","+850","+965","+221","+378","+232","+248","+7","+1345","+65","+46","+249","+1809","1-829","+1767","+253","+45","+1-284","+49","+967","+213","+1","+598","+262","+1","+961","+1758","+856","+688","+886","+1868","+90","+94","+423","+371","+676","+370","+352","+231","+266","+66","+228","+235","+1649","+218","+379","+1784","+971","+376","+1268","+93","+1264","+1340","+354","+98","+374","+355","+244","+1684","+54","+61","+43","+297","+91","+35818","+994","+353","+62","+380","+974","+258" )
        combo_code.place(x=200,y=300)


        #combo_code=ttk.Combobox(Manage_Frame, textvariable=self.code, font=("times new roman",16,"bold"),width=5,height = 15 ,state='readonly')
        #combo_code['values']=("+93","+355","+213","+1684","+376","+244","+1264","+672","+1268","+54","+374","+297","+61")
        #combo_code.place(x=185,y=330)

        txt_roll=Entry(Manage_Frame, width=20,textvariable=self.contact, font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=240,y=300)

        #   ----------------------------------------------------------------------------
        
        lb_gender=Label(Manage_Frame,text="Gender", font=("times new roman",20,"bold"),bg=bg_color,fg="white")
        lb_gender.place(x=20, y=370, anchor="w")
        
        combo_gender=ttk.Combobox(Manage_Frame, textvariable=self.gender, font=("times new roman",13,"bold"),width=21,state='readonly')
        combo_gender['values']=("Male","Female","Others")
        combo_gender.place(x=200, y=370, anchor="w")

       
        
        #-------Button Frame-------------#

        btn_Frame=Frame(Manage_Frame,bd=4, relief=RIDGE,bg=bg_color)
        btn_Frame.place(x=10,y=420)

        SignUpbtn=Button(btn_Frame, command=self.save, text="SignUp", font="bold", width=8).grid(row=0,column=0,padx=15, pady=10)
        Backbtn=Button(btn_Frame, command=self.back,text="Back",font="bold", width=8).grid(row=0,column=4,padx=15, pady=10)
        Clearbtn=Button(btn_Frame,command=self.clear,text="Clear",font="bold", width=8).grid(row=0,column=8,padx=15, pady=10)
        Exitbtn=Button(btn_Frame,command=self.exit,text="Exit", font="bold", width=8).grid(row=0,column=12,padx=15, pady=10)
        

        F2 = LabelFrame(self.root,bd=10,relief=SUNKEN, bg="")
        F2.place(x=760,y=70,width=310,height=560 )
        lbl2 = Label(F2,bg=bg_color, image = self.F2).grid(row=0, column=0,padx=100,pady=20)
        lbl3 = Label(F2, text = "Also Sign Up fot the new Users",bg="white",fg="green", font= ("times new roman",10,"italic")).grid(row=1, column=0,padx=10)
        lbl4 = Label(F2, text = "OASIS",fg="green",bg="white", font= ("times new roman",10,"italic")).grid(row=2, column=0,padx=10)

        lbl5 = Label(F2, text = "Follow Us On",fg="red",bg="white", font= ("times new roman",15)).place(x=150,y=350,anchor="c")

        lbl6 = Label(F2, text = "Developed by Aditya Jha\n and \nGaurav Kr. Gupta",fg="#4863A0",bg="white", font= ("times new roman",15)).place(x=40,y=440)


        btn_login = Button(F2, text="Login",relief=FLAT,width =20,height=1,command=self.login2, font=("times new roman",14,"bold"),bg="#348017",foreground="#FEFCFF").grid(row = 3,column=0,padx=10,pady=25 )
        btn_SignUp = Button(F2, text="SignUp",width =20,height=1,command=self.signup,relief=RAISED, font=("times new roman",14,"bold"),bg="#1569C7",foreground="#FEFCFF").grid(row = 4,column=0 )
        
        btn_link1 = Button(F2, image=self.icon2 ,relief=RAISED, font=("times new roman",14,"bold"),command=self.link1,bg="#1569C7",foreground="#FEFCFF").place(x=20 ,y=400,anchor="w" )
        btn_link2 = Button(F2, image=self.icon3, relief=RAISED, font=("times new roman",14,"bold"),command=self.link2,bg="#1569C7",foreground="#FEFCFF").place(x=90 ,y=400,anchor="w"  )
        btn_link3 = Button(F2, image=self.icon1, relief=RAISED, font=("times new roman",14,"bold"),command=self.link3,bg="#1569C7",foreground="#FEFCFF").place(x=160 ,y=400,anchor="w" )
        btn_link4 = Button(F2, image=self.icon4, relief=RAISED, font=("times new roman",14,"bold"),command=self.link4,bg="#1569C7",foreground="#FEFCFF").place(x=230 ,y=400,anchor="w" )
        

#        link4 = Label(F2, image=self.icon4, fg="blue",anchor="w",cursor="hand2")
#        link4.grid(row = 6,column=3) 
#        link4.bind("<Button-1>", lambda e: webbrowser.open_new("http://www.twitter.com"))





    def link1(self):
        webbrowser.open_new("http://www.google.com")
    
    def link2(self):
        webbrowser.open_new("https://www.instagram.com/?hl=en")
    
    def link3(self):
        webbrowser.open_new("http://www.facebook.com")

    def link4(self):
        webbrowser.open_new("http://www.twitter.com")
    


    def login2(self):
        self.root.destroy()
        import Login
    
    def signup(self):
        self.root.destroy()
        import signup    
    
    def save(self):
        if self.fname.get()=="" and self.pasw.get()=="" and self.email.get()=="" and self.gender.get()=="" and self.contact.get()=="" and self.code.get()=="Code":
            messagebox.showerror("Error!","All Feilds Required")
        if self.fname.get()=='':
            return messagebox.showinfo('Error','Enter a firstname')
            
        if self.pasw.get()=='':
            return messagebox.showinfo('Error','Enter a password')

        if len(str(self.pasw.get()))<8:
            return messagebox.showwarning("Warning","Password should be Minimum 8 charactrs")
        
        if self.contact.get()=='':
            return messagebox.showinfo('Error','Enter a contact')
        
        try:
            tmp=self.contact.get()
            int(tmp)
        except ValueError:
            return messagebox.showinfo('Error','Contact No. Should Be Integer')
        
        if len(self.contact.get()+str(self.code.get()))<10 and len(self.contact.get()+str(self.code.get()))>15:
            return messagebox.showinfo('Error','Enter a valid contact')      
        
        if self.email.get()=='':
            return messagebox.showinfo('Error','Enter an email')
        
            
        if self.gender.get()=='':
            return messagebox.showinfo('Error','Choose Gender')

        if self.code.get()=='':
            return messagebox.showinfo('Error','Choose Country Code')

        if "@" not in self.email.get():
            return messagebox.showwarning("Warrning","Email should have '@' Character")

        if self.today<self.DOB.get():
            return messagebox.showwarning("Error","D.O.B not Possible")
        else:
            self.con2 = str(region_code_for_country_code(self.code.get()))

            self.UID=random.randint(200000,1000000)
            self.uname=self.fname.get()+str(random.randint(1000,40000))

            self.conn=sqlite3.connect("Oasis.db")
            self.c=self.conn.cursor()
            self.c.execute("CREATE TABLE IF NOT EXISTS admin(UID TEXT UNIQUE NOT NULL ,first_name TEXT NOT NULL, last_name TEXT , uname TEXT PRIMARY KEY UNIQUE NOT NULL, pasw TEXT NOT NULL,Role TEXT,email TEXT NOT NULL, gender TEXT NOT NULL, code TEXT NOT NULL, contact TEXT NOT NULL, country TEXT, Joining TEXT, DOB TEXT, Time1 TIME )")
            self.find_user = ("SELECT * FROM admin WHERE email= ?  or contact = ?")
            self.c.execute(str(self.find_user),(self.email.get(),self.contact.get()))
            results = (self.c).fetchall()
            if results:
                messagebox.showerror("Error","Email or Contact  is already Used")
            else:
                try:
                    self.c.execute("INSERT INTO admin (UID ,first_name,last_name,uname, pasw , Role,email, gender , code , contact , country , Joining , DOB , Time1 ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (self.UID,self.fname.get(),self.lname.get(),self.uname,self.pasw.get(),self.Role,self.email.get(),self.gender.get(),self.code.get(),self.contact.get(),self.con2,self.today,self.DOB.get(),self.Time1))
                    self.conn.commit()
                    self.c.close()
                    self.conn.close()
                    messagebox.showinfo("Info",("Your User Name "+str(self.uname)))
                    messagebox.showinfo("Successfull","Successfully Added Data, For Login Click on Back")
                    self.clear()
                except Exception:
                    messagebox.showerror("Error!!","Somthing went wrong not able to add data try again or for Login Click on Back")        
                    self.clear()

    
    def clear(self):
        self.fname.set("")
        self.lname.set("")
        self.pasw.set("")
        self.email.set("")
        self.gender.set("Choose Gender")
        self.contact.set("")        
        self.code.set(0)
        self.DOB.set(self.today)

    def exit(self):
        ask=messagebox.askyesnocancel("Exit","Do you really want to Exit?!!")
        if ask>0:
            self.root.destroy()
        else:
            return
    def back(self):
        self.root.destroy()
        import Login

        

        

root=Tk()
obj=win2(root)
root.mainloop()