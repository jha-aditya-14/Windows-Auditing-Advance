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
        self.contact=StringVar()
        self.pass1=StringVar()
        self.pass2=StringVar()

        bg_lbl=Label(self.root,image=self.bg_icon).pack(fill=Y)
        
        title=Label(self.root,text="OASIS",font=("times new roman",40,"bold"),bd=5,relief=GROOVE, fg="white", bg=bg_color,pady=2)
        title.place(x=0, y=0,relwidth=1)

        F1=LabelFrame(self.root, bd=10, relief=GROOVE, text="Welcome to OASIS",font=("times new roman",30,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=76,relwidth=1,height=120)

        lbl=Label(F1,text="CREATORS:---",bg=bg_color, fg="white",font=("times new roman",20, "bold")).grid(row=0,column=0,padx=20,pady=20)

        lbl2=Label(F1,text="Aditya Jha and Gaurav Kumar Gupta",bg=bg_color, fg="white",font=("times new roman",15, "bold")).grid(row=0,column=2,padx=20,pady=20)

        self.Login_Frame=LabelFrame(self.root, bd=10, relief=GROOVE, text="LogIn",font=("times new roman",20,"bold"),fg="gold",bg=bg_color)
        self.Login_Frame.place(x=400,y=230,width=600)


        logolbl=Label(self.Login_Frame, image= self.logo_icon ,bd=5).grid(row=0,columnspan=2)
        
        userlbl=Label(self.Login_Frame, text=" Contact No.", compound=LEFT, font= ("times new roman",20,"bold"),image= self.user_icon,bg=bg_color).grid(row=1,column=1,padx=20,pady=10)
        txtuser=Entry(self.Login_Frame,bd=5,textvariable=self.contact,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=50)
        
        btn_login=Button(self.Login_Frame,text="Login",width=8, command=self.login,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=4,column=1,padx=20, pady=20)
        
        btn_signup=Button(self.Login_Frame,text="SignUp",width=8,command=self.signup, font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=4,column=0,padx=15,pady=20)
        
        tn_reset=Button(self.Login_Frame,text="Reset",width=8, command=self.reset,font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=4,column=2,padx=15,pady=20)

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
    
    def reset(self):
        self.var=self.contact.get()
        if self.var=="" :
            return messagebox.showerror("Error!","All field should be filled")
        if "@" in self.var:
            return messagebox.showerror("Error!","Wrong Contact ")
        else:
            self.conn=sqlite3.connect("Oasis.db")
            self.c=self.conn.cursor()
            self.find_user=("SELECT * from admin WHERE contact=? or email = ?")
            self.c.execute(str(self.find_user),(str(self.contact.get()),str(self.contact.get())))
            self.data=self.c.fetchall()
            if self.data:
                for i in self.data:
                    self.Login_Frame.destroy()
                    self.Login_Frame1=LabelFrame(self.root, bd=10, relief=GROOVE, text="Forget Password",font=("times new roman",20,"bold"),fg="gold",bg="#074463")
                    self.Login_Frame1.place(x=400,y=230,width=600)

                    userlbl=Label(self.Login_Frame1, text="New Password", compound=LEFT, font= ("times new roman",20,"bold"),bg="#074463").grid(row=1,column=0,padx=20,pady=10)
                    txtuser=Entry(self.Login_Frame1,bd=5,textvariable=self.pass1,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)
                    
                    passlbl=Label(self.Login_Frame1, text="Confirm Password", compound=LEFT, font= ("times new roman",20,"bold"),bg="#074463").grid(row=2,column=0,padx=20,pady=10)
                    txtuser=Entry(self.Login_Frame1,bd=5,textvariable=self.pass2,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)
                    
                    btn=Button(self.Login_Frame1,text="OK",width=8,command=self.ok, font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=1,padx=10,pady=20)
                    btn1=Button(self.Login_Frame1,text="Back",width=8,command=self.back, font=("times new roman",14,"bold"),bg="yellow",fg="red").grid(row=3,column=0,padx=100,pady=20)
            else:
                return messagebox.showerror("Error","Contact not Exist")
    
    def ok(self):
        if self.pass1.get()=='':
            return messagebox.showerror('Error','Enter a New password')
        if self.pass1.get()=='':
            return messagebox.showerror('Error','Confirm password')

        if len(str(self.pass1.get()))<8:
            return messagebox.showwarning("Warning","Password should be Minimum 8 charactrs")

        elif self.pass1.get()==self.pass2.get():
            try:
                b=self.contact.get() 
                y="UPDATE admin SET pasw="+self.pass1.get()
                y=y+" WHERE contact="+self.var or "email ="+self.var
                #print(str(y))              
                self.c.execute(str(y))
                self.conn.commit()
                self.conn.close()
                messagebox.showinfo("Info","Successfully Changed!!")
                self.root.destroy()
                import Login
            except Exception:
                messagebox.showinfo("Info","Something Wrong Go back and Try Again!!")
                self.root.destroy()
                import Forgot_Password

        else:
            messagebox.showinfo("Info","Password Cann't Changed password may not match Try Again!!")
            self.root.destroy()
            import Forgot_Password
    
    def login(self):
        self.root.destroy()
        import Login 
    
    def back(self):
        self.root.destroy()
        import Forgot_Password
root=Tk()
obj=win1(root)
root.mainloop()