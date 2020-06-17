from tkinter import*
import os
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import webbrowser
import sqlite3

class win1:
    def __init__(self,root):
        self.root=root
        self.root.title("OASIS".center(420))
        self.root.configure(background = "black")
        bg_color="#074463" 
        self.root.geometry("1350x700+0+0")

        self.bg_icon=ImageTk.PhotoImage(file="Pic/7.jpg")
        self.user_icon=ImageTk.PhotoImage(file="Pic/1.jpg")
        self.pass_icon=ImageTk.PhotoImage(file="Pic/2.png")
        self.logo_icon=ImageTk.PhotoImage(file="Pic/4.png")
        self.signup_icon=ImageTk.PhotoImage(file="Pic/8.jpg")
        self.icon1=ImageTk.PhotoImage(file="PIC/download.jpg")
        self.icon2=ImageTk.PhotoImage(file="PIC/download (1).png")
        self.icon3=ImageTk.PhotoImage(file="PIC/download.png")
        self.icon4=ImageTk.PhotoImage(file="PIC/images.jpg")

        
        #------------Variable----------------#
        self.uname=StringVar()
        self.pass_=StringVar()

        bg_lbl=Label(self.root,image=self.bg_icon).pack(fill=Y)
        
        title=Label(self.root,text="OASIS",font=("times new roman",40,"bold"),bd=5,relief=GROOVE, fg="white", bg=bg_color,pady=2)
        title.place(x=0, y=0,relwidth=1)

        F1=LabelFrame(self.root, bd=10, relief=GROOVE, text="Welcome to OASIS",font=("times new roman",30,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=76,relwidth=1,height=120)

        lbl=Label(F1,text="CREATORS:---",bg=bg_color, fg="white",font=("times new roman",20, "bold")).grid(row=0,column=0,padx=20,pady=20)

        lbl2=Label(F1,text="Aditya Jha and Gaurav Kumar Gupta",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=0,column=2,padx=20,pady=20)

        Login_Frame=LabelFrame(self.root, bd=10, relief=GROOVE, text="LogIn",font=("times new roman",20,"bold"),fg="gold",bg=bg_color)
        Login_Frame.place(x=400,y=230,width=600)


        logolbl=Label(Login_Frame, image= self.logo_icon ,bd=5).grid(row=0,columnspan=2)
        
        userlbl=Label(Login_Frame, text="Username", compound=LEFT, font= ("times new roman",20,"bold"),image= self.user_icon,bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)
        
        passlbl=Label(Login_Frame, text="Password", compound=LEFT, font= ("times new roman",20,"bold"),image= self.pass_icon,bg="white").grid(row=2,column=0,padx=20,pady=10)
        txtpass=Entry(Login_Frame,bd=5,textvariable=self.pass_,relief=GROOVE,font=("",15),show="*").grid(row=2,column=1,padx=20)

        btn_login=Button(Login_Frame,text="Login",width=8, command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1)
        
        btn_signup=Button(Login_Frame,text="SignUp",width=8,command=self.signup, font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=0)
        
        tn_reset=Button(Login_Frame,text="Reset",width=8, command=self.reset,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=2)

        F=LabelFrame(self.root, bd=10, relief=GROOVE, text="Links",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F.place(x=0,y=600,relwidth=1, height=100)
        lbl = Label(F, text = "Follow Us On",fg="red",bg=bg_color, font= ("times new roman",15,"bold")).place(x=60,y=10,anchor="c")
        
        btn_link1 = Button(F, image=self.icon2 ,relief=RAISED, font=("times new roman",14,"bold"),command=self.link1,bg="#1569C7",foreground="#FEFCFF").place(x=10 ,y=40,anchor="w" )
        btn_link2 = Button(F, image=self.icon3, relief=RAISED, font=("times new roman",14,"bold"),command=self.link2,bg="#1569C7",foreground="#FEFCFF").place(x=80 ,y=40,anchor="w"  )
        btn_link3 = Button(F, image=self.icon1, relief=RAISED, font=("times new roman",14,"bold"),command=self.link3,bg="#1569C7",foreground="#FEFCFF").place(x=150 ,y=40,anchor="w" )
        btn_link4 = Button(F, image=self.icon4, relief=RAISED, font=("times new roman",14,"bold"),command=self.link4,bg="#1569C7",foreground="#FEFCFF").place(x=220 ,y=40,anchor="w" )


    def link1(self):
        webbrowser.open_new("http://www.google.com")
    
    def link2(self):
        webbrowser.open_new("https://www.instagram.com/?hl=en")
    
    def link3(self):
        webbrowser.open_new("http://www.facebook.com")

    def link4(self):
        webbrowser.open_new("http://www.twitter.com")
    

    def signup(self):
        self.root.destroy()
        import signup
    
    def login(self):
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error!","All field should be filled")
        if self.uname.get()=="" or self.pass_.get()=="":
            messagebox.showerror("Error!","Username field is empty!!")
        if self.pass_.get()=="":
            messagebox.showerror("Error!","Password field is empty!!")    
        else:
            self.conn=sqlite3.connect("Oasis.db")
            self.c=self.conn.cursor()
            self.find_user = ("SELECT * FROM admin WHERE (uname = ? OR email = ?)  AND pasw = ?")
            a=self.c.execute(str(self.find_user),(str(self.uname.get()),str(self.uname.get()),str(self.pass_.get())))
            results = a.fetchall()
            if results:
                for i in results:
                    messagebox.showinfo("Info","Successfully Logined")  
                    self.root.destroy()
                    import Main_Page               
            else:
                messagebox.showerror("Error!","Username or Password may be wrong")  
                            
            
    
    
    def reset(self):
        self.root.destroy()
        import Forgot_Password
        
root=Tk()
obj=win1(root)
root.mainloop()