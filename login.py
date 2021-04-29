from tkinter import *
from datetime import *
import time
from math import *
import sqlite3
from tkinter import messagebox, ttk
import random
import smtplib

class Login_window:
    def __init__(self, root):
        self.root=root
        self.root.title("Log In")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        ###############     background colours
        left_lbl=Label(self.root, bg="#08A3D2", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl=Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        ####################       frames
        login_frame=Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        title=Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white", fg="#08A3D2").place(x=250, y=50)

        email=Label(login_frame, text="Email Address", font=("times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=150)
        self.txt_email=Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=250, y=180, width=350, height=35)

        pass_=Label(login_frame, text="Password", font=("times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=250)
        self.txt_pass_=Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_pass_.place(x=250, y=280, width=350, height=35)

        btn_reg=Button(login_frame, cursor="hand2", command=self.register_window, text="Register new account?", font=("times new roman", 14), bg="white", bd=0, fg="#B00857").place(x=250, y=320)
        btn_forget=Button(login_frame, cursor="hand2", command=self.forget_password_window, text="Forget Password?", font=("times new roman", 14), bg="white", bd=0, fg="red").place(x=450, y=320)

        btn_login=Button(login_frame, cursor="hand2", text="Login", command=self.login, font=("times new roman", 20, "bold"), fg="white", bg="#B00857").place(x=250, y=380, width=180, height=40)

        
        ###############     clock
        self.lbl=Label(self.root,text="", font=("Book Antiqua", 25, "bold"),fg="white", compound=BOTTOM, bg="#081923", bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)
        #self.clock_image() #081923
        self.working()
        
    def register_window(self):
        
        self.root.destroy()
        import register

    
            
    def reset(self):
        #self.cmb_quest.current(0)
        self.txt_new_pass.delete(0, END)
        self.txt_pass_.delete(0, END)
        self.txt_otp.delete(0, END)
        self.txt_email.delete(0, END)

    def forget_password(self):
        '''
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        '''
        if  self.txt_otp.get()=="" or self.txt_new_pass.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)

        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                
                
                
                '''
                cur.execute("SELECT * FROM employee WHERE email=? AND question=? AND answer=?", (self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Please select correct Security Question and Answer", parent=self.root2)
                '''
                
                if otp_send[0]!=self.txt_otp.get():
                    messagebox.showerror("Error", "Incorrect OTP!!", parent=self.root2)
                    con.close()
                    messagebox.showinfo("Success", "Your password has been updated, Please login with new password", parent=self.root2)
                    self.reset()
                    self.root2.destroy()

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
            


        

    def forget_password_window(self):
        
        if self.txt_email.get()=="":
            messagebox.showerror("Error", "Please enter an email address to reset your password", parent=self.root)

        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("SELECT * FROM employee WHERE email=?", (self.txt_email.get(),))
                if row==None:
                    messagebox.showerror("Error", "Please enter a valid email address to reset your password", parent=self.root)
                    
                else:

                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x300+495+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    #---------------forget password
                    
                    '''
                    question=Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
                    self.cmb_quest=ttk.Combobox(self.root2, font=("times new roamn", 13), state='readonly', justify=CENTER)
                    self.cmb_quest['values']=("Select", "Your First Pet Name", "Your Birth place", "Your Best Friend")
                    self.cmb_quest.place(x=50, y=130, width=250)
                    self.cmb_quest.current(0)
                    '''
                    
                    ######(sender, receiver, msg)
                    server.sendmail('chilly.tower@gmail.com', self.txt_email.get(), msg)
                    server.quit()
                    

                    otp=Label(self.root2, text="OTP", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=80)
                    self.txt_otp=Entry(self.root2, font=("times new roamn", 15), bg="lightgray")
                    self.txt_otp.place(x=50, y=110, width=250)

                    new_password=Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=160)
                    self.txt_new_pass=Entry(self.root2, font=("times new roamn", 15), bg="lightgray")
                    self.txt_new_pass.place(x=50, y=190, width=250)

                    btn_change_password=Button(self.root2,text="Reset Password", command=self.forget_password, cursor="hand2", bg="green", fg="white", font=("times new roman", 15, "bold")).place(x=90, y=240)
                    
                   


            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------

    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error", "Please enter both email and password", parent=self.root)

        else:
            try:
                con=sqlite3.connect(database="rms.db")
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid username and password", parent=self.root)
                    
                else:
                    messagebox.showinfo("Success", f"Welcome: {self.txt_email.get()}", parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                    
                con.close()   


            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        


    def clock_image(self, hr, min_, sec_):
        clock=Image.new("RGB", (400, 400), (8,25, 35))
        draw=ImageDraw.Draw(clock)

        
        ################   for clock img (211, 211, 211)
        bg=Image.open("image/logo.jpg")
        bg=bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))
        
        '''
        origin=200, 200
        ###################    For hour line img
        draw.line((origin, 200+40*sin(radians(hr)), 200-40*cos(radians(hr))), fill="#29A19C", width=4)

        ###################    For minute line img
        draw.line((origin, 200+60*sin(radians(min_)), 200-60*cos(radians(min_))), fill="#E94B3CFF", width=3)

        ###################    For second line img
        draw.line((origin, 200+80*sin(radians(sec_)), 200-80*cos(radians(sec_))), fill="green", width=2)


        draw.ellipse((195, 195, 210, 210),fill="#F9D342")
        '''
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
        




