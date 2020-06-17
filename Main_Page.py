from tkinter import*
import cv2
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import sys,sqlite3,time
from datetime import datetime
import webbrowser
import random
import tkinter as tk
from tkcalendar import Calendar, DateEntry
import pycountry
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_number
from phonenumbers.phonenumberutil import region_code_for_country_code
from tkinter import filedialog

#--------

class win1:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System".center(420))  # title for Window 
        self.root.configure(background = "black")  # background color for window 
        self.root.geometry("1360x768+0+0")

        bg_color ="#074463"

        self.bg_icon = ImageTk.PhotoImage(file="Pic/windows10.jpg")
        bg_lbl = Label(self.root, image = self.bg_icon).pack(fill=Y) 
        self.clock_icon=ImageTk.PhotoImage(file="Pic\Clock_Dark.png")
        
        
        now = datetime.now()
        self.Time1=now.strftime('%H:%M:%S')

        self.today= now.strftime("%d-%b-%Y")
        self.label1, self.calendar1 = "", ""
        now = datetime.now()
        
        self.val=IntVar() 
        self.val.set("1")

        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,bg=bg_color)
        F1.place(x=0,relwidth=1,height=100 )
        lbl = Label(F1,text="OASIS", bg=bg_color, font= ("times new roman",25,"bold")).place(x=120, y=15)

        R1 = Radiobutton(F1, text="Light Mode",font=("bold",9), bg=bg_color,value=1,variable=self.val,command=DISABLED)
        R1.place(x=700,y=20)
        R2 = Radiobutton(F1, text="Dark Mode", font=("bold",9),bg=bg_color,variable=self.val,value=2,command=DISABLED)
        R2.place(x=700,y=40)

        self.font=("times new roman",20,"bold")
        self.calendar = []

        self.calendar.append(DateEntry(F1, font=("times new roman",15,"bold"), locale='en_GB',state="readonly", width=10))
        self.calendar[-1].place(x=855, y=20, anchor="w")
        #print (self.calendar)

        self.time_string = time.strftime('(%H:%M:%S:%p)')
        time1 = Label(F1,text=self.time_string,font=("times new roman",15,"bold"),bg=bg_color)
        time1.place(x=850,y=40)
        time2 = Label(F1,image=self.clock_icon,bg=bg_color)
        time2.place(x=820,y=40)

        lbl2 = Label(F1,text="                           AJ_GKG",font=("times new roman",15,"bold"),bg=bg_color)
        lbl2.place(x=1050,y=0)

        btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black",command=DISABLED).place(x=1145,y=50,anchor="w")

      

root = Tk()
obj = win1(root)
root.mainloop()
