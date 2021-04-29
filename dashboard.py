from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
from student import StudentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox

from datetime import *
import time
from math import *
import sqlite3
from tkinter import messagebox
import os
#import login

class RMS:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        ############# icons
        self.logo_dash=ImageTk.PhotoImage(file="Image/student_icon.png")
        

        ####################     title  ########################
        title=Label(self.root, text="Student Result Management System", padx=10 ,compound=LEFT, image=self.logo_dash, font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)

        ###############  Menus
        M_Frame=LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=80)

        btn_course=Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course).place(x=20, y=5, width=200, height=40)
        btn_student=Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_student).place(x=240, y=5, width=200, height=40)
        btn_result=Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_result).place(x=460, y=5, width=200, height=40)
        btn_view=Button(M_Frame, text="View Student Results", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_report).place(x=680, y=5, width=200, height=40)
        btn_logout=Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.logout).place(x=900, y=5, width=200, height=40)
        btn_exit=Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.exit_).place(x=1120, y=5, width=200, height=40)

        ####################   Content     ###################
        self.bg_img=Image.open("Image/big.jpg")
        self.bg_img=self.bg_img.resize((920, 350), Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root, image=self.bg_img).place(x=400, y=180, width=920, height=350)


        ##################      update_details     ##############
        self.lbl_course=Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=413, y=530, width=300, height=100)

        self.lbl_student=Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=723, y=530, width=300, height=100)

        self.lbl_result=Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1033, y=530, width=300, height=100)


        ###############     clock
        self.lbl=Label(self.root,text="\nAnalog Clock", font=("Book Antiqua", 25, "bold"),fg="white", compound=BOTTOM, bg="#081923", bd=0)
        self.lbl.place(x=10, y=180, height=450, width=350)
        #self.clock_image()

        
        
        
        ####################     footer  ########################
        footer=Label(self.root, text="SRM Student Result Management System\nContact us for any Technical Issue: 8939xxxx04", font=("goudy old style", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
        self.update_details()

####################################################################

    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM course ")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Course\n[{str(len(cr))}]")

            cur.execute("SELECT * FROM student ")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")

            
            self.lbl_course.after(200, self.update_details)
             

                    

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clock_image(self, hr, min_, sec_):
        clock=Image.new("RGB", (400, 400), (8,25, 35))
        draw=ImageDraw.Draw(clock)

        
        ################   for clock img
        bg=Image.open("image/clock_img.jfif")
        bg=bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))
        
        '''
        origin=200, 200
        ###################    For hour line img
        draw.line((origin, 200+50*sin(radians(hr)), 200-50*cos(radians(hr))), fill="black", width=4)

        ###################    For minute line img
        draw.line((origin, 200+80*sin(radians(min_)), 200-80*cos(radians(min_))), fill="blue", width=3)

        ###################    For second line img
        draw.line((origin, 200+100*sin(radians(sec_)), 200-100*cos(radians(sec_))), fill="green", width=4)


        draw.ellipse((195, 195, 210, 210),fill="black")
        clock.save("clock_new.png")
        '''
        origin=200, 200
        ###################    For hour line img
        draw.line((origin, 200+40*sin(radians(hr)), 200-40*cos(radians(hr))), fill="#29A19C", width=4)

        ###################    For minute line img
        draw.line((origin, 200+60*sin(radians(min_)), 200-60*cos(radians(min_))), fill="#E94B3CFF", width=3)

        ###################    For second line img
        draw.line((origin, 200+80*sin(radians(sec_)), 200-80*cos(radians(sec_))), fill="green", width=2)


        draw.ellipse((195, 195, 210, 210),fill="#F9D342")
        clock.save("clock_new.png")
        
    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360

        #print(h, m, s)
        #print(hr, min_, sec_)
        self.clock_image(hr, min_, sec_)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)
        

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)


    def logout(self):
        op=messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")
            


    def exit_(self):
        op=messagebox.askyesno("Confirm", "Do you really want to exit?", parent=self.root)
        if op==True:
            self.root.destroy()
            
        
        







        
