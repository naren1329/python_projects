"""
NAME-D.MUTHU NARENDRAN
PROJECT NAME-QUIZGAME
CREATED DATE-17/8/2023
MODIFIED DATE-
"""
#Modules
import re
from tkinter import ttk
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox  
import mysql.connector

#Create class for Quizgame
class Quizgame:
   #global variable
   inc=0
   score=0
   def __init__ (self):
      self.data=mysql.connector.connect(host="localhost",
                                   user="root",
                                   password="naren@1329",
                                   database="newdatabase")
      self.cursor=self.data.cursor()
      self.cursor.execute("use newdatabase")
      self.cursor.execute("create table if not exists quiztable(name varchar(20),email varchar(20),password varchar(10))")
      self.top=Tk()
      self.top.geometry("1366x768")
      self.top.configure(bg="plum1")

   #3 Button on the home page
   def home(self):
      name=Label(self.top,text="Quiz Game",bg="plum2",font=("Colonna MT",40),width=100).pack()
      log = Button(self.top, text = "Login", fg = "black",bg="plum3",font =("times", 25),command=self.login)
      log.pack(pady = 30)    
      reg = Button(self.top, text = "Register", fg = "black",bg="plum3",font =("times", 25),command=self.registration).pack(pady = 50)   
      ex= Button(self.top, text = "Exit", fg = "black",bg="plum3",font =("times", 25),command=self.top.destroy).pack(pady = 50)

   #Registration function
   def registration(self):
      #calling toplevel function
      a=Toplevel(self.top)
      a.geometry("1366x768")
      a.configure(bg="plum1")
      head=Label(a,text="Welcome to Registration",bg="plum2",font=("Colonna MT",40),width=100).pack()
      name=Label(a,text="Enter name",font=("rock well",20),bg="plum1").place(x=250,y=200)
      name_value=Entry(a,width=50)
      name_value.place(x=500,y=200)
      
      email=Label(a,text="Enter email",font=("rock well",20),bg="plum1").place(x=250,y=300)
      email_value=Entry(a,width=50)
      email_value.place(x=500,y=300)
      
      password=Label(a,text="Enter Password",font=("rock well",20),bg="plum1").place(x=250,y=400)
      password_value=Entry(a,width=50,show="*")
      password_value.place(x=500,y=400)
      
      def get_register():
         try:
            reg_name=name_value.get()
            if len(reg_name) == 0:
               raise Exception("Error:Empty input at name") 
            elif not reg_name.isalpha():
               raise Exception("Error:Name should be in alhabet")
            elif len(reg_name)<3:
               raise Exception("Error:Invalid name")
         except Exception as e:
            messagebox.showinfo("Login Error",e)
            

         try:   
            reg_email=email_value.get()
            check3= re.search(r"^[a-zA-Z][A-Za-z0-9._]+@[a-z]+\.[a-z]{3}$",reg_email)
            if reg_email=="":
               raise Exception("Error:empty input")
            elif reg_email.isspace():
               raise Exception("Error:Empty space occurred")
            elif len(reg_email)<10 or len(reg_email)>35:
               raise Exception("Error:Invalid Email length, email lenght(min-10,max-35)format(ex:muthunaren695@gamil.com)")
            elif not check3:
               raise Exception("Error:Invalid Email,Give correct format(ex:narenchan695@gamil.com)")
         except Exception as e:
            messagebox.showinfo("Login Error",str(e))
            reg_email.delete(0,END)
            return
         try:
            reg_password=password_value.get()
            if len(reg_password)==0:
               raise Exception("ERROR: Empty input")
            elif len(reg_password)<=3 and len(reg_password)>=10:
               raise Exception("ERROR:Invalid password,it should be in 10charecters")
         except Exception as e:
            print(e)
            messagebox.showinfo("Login Error",str(e))
            reg_password.delete(0,END)
            return
         if len(reg_name)!=0 and len(reg_email)!=0 and len(reg_password)!=0:
            view=("insert into quiztable(name,email,password)values(%s,%s,%s)")
            values=(reg_name,reg_email,reg_password)
            self.cursor.execute(view,values)
            self.data.commit()
            a.destroy()
         else:
            #Message box(title,message)
            messagebox.showinfo("Register Error","invalid data")
      ex= Button(a, text = "Submit", fg = "black",font =("times", 20),command=get_register,bg="plum3").place(x=400,y=470)

   #Login function
   def login(self):
      b=Toplevel(self.top)
      b.geometry("1366x768")
      b.configure(bg="plum1")
      head=Label(b,text="Welcome to Registration",bg="plum2",font=("Colonna MT",40),width=100).pack()
      name=Label(b,text="Enter name",font=("rock well",20),bg="plum1").place(x=250,y=200)
      self.name_value=Entry(b,width=50)
      self.name_value.place(x=500,y=200)

      password=Label(b,text="Enter Password",font=("rock well",20),bg="plum1").place(x=250,y=300)
      self.password_value=Entry(b,width=50,show="*")
      self.password_value.place(x=500,y=300)
      
      def get_login():
         #Checking the login name is present or not
         log_name=self.name_value.get()
         log_password=self.password_value.get()
         count = 0
         view=("select * from quiztable")
         self.cursor.execute(view)
         fetch=self.cursor.fetchall()
         if fetch != []:
            for x in range(len(fetch)):
               if log_name==fetch[x][0] and log_password == fetch[x][2]:
                  self.current_user_name = log_name
                  count = 1
                  break
               else:
                  count = 0
            if count >0:
               messagebox.showinfo("Login","Login Successfull")
               b.destroy()
               self.play_score()
            else:
               messagebox.showinfo("Login","Invalid name and password")
         else:
            messagebox.showinfo("Login","Invalid User name")
            
      ex= Button(b, text = "Submit", fg = "black",font =("times", 20),bg="plum3",command=get_login).place(x=400,y=470)

   #Function for quizgame     
   def quiz_game(self):
      
      temp=Quizgame.inc+1
      self.cursor.execute("select * from question")
      fetch=self.cursor.fetchall()
      if Quizgame.inc < len(fetch):
         d=Toplevel(self.top)
         d.geometry("1366x768")
         d.configure(bg="plum1")
         head=Label(d,text="Welcome to quizgame",bg="plum2",font=("Colonna MT",40),width=100).pack()
         head=Label(d,text=f"Question {temp} of {len(fetch)} ",bg="plum2",font=("Colonna MT",40),width=100).pack()
         #Assign each index to the each value
         ques=fetch[Quizgame.inc][0]
         a=fetch[Quizgame.inc][1]
         b=fetch[Quizgame.inc][2]
         c=fetch[Quizgame.inc][3]
         d1=fetch[Quizgame.inc][4]
         answer=fetch[Quizgame.inc][5]
         ques_label=Label(d,text=ques,font=("times",20),bg="plum1").place(x=50,y=150)
         #Declare radio button
         ans=IntVar()
         ans.set(-1)
         R1 = Radiobutton(d, text=a, variable=ans,value=1,bg="plum1")
         R1.place(x=50,y=250 ,anchor = W )
         R2 = Radiobutton(d, text=b, variable=ans,value=2,bg="plum1")
         R2.place(x=50,y=280, anchor = W )
         R3 = Radiobutton(d, text=c, variable=ans,value=3,bg="plum1")
         R3.place(x=50,y=310, anchor = W )
         R4 = Radiobutton(d, text=d1, variable=ans,value=4,bg="plum1")
         R4.place(x=50,y=340, anchor = W)
         #Function for increase score and destroy before screen
         def delete():
            radio_get=ans.get()
            
            if radio_get == answer:
               Quizgame.score+=1
            d.destroy()
            self.quiz_game()
            
         def score_inc():
            n.config(state="normal")
            
         s=Button(d, text = "Submit", fg = "black",bg="plum3",font =("times", 10),command=score_inc)
         s.place(x=200,y=400)
         score_label=Label(d,text=f"Score:0/5",fg = "black",bg="plum3").place(x=400,y=400)
         Quizgame.inc+=1
         n=Button(d, text = "Next", fg = "black",bg="plum3",font =("times", 10),command=delete,state=DISABLED)
         n.place(x=300,y=400)
         
         
      else:
         #Total score view
         d=Toplevel(self.top)
         d.geometry("1366x768")
         d.configure(bg="plum1")
         head=Label(d,text="Welcome to quizgame",bg="plum2",font=("Colonna MT",40),width=80).pack()
         head1=Label(d,text=f"Total score:{Quizgame.score}",bg="plum2",font=("times",40),fg="black",width=45).place(y=100)
         Quizgame.inc=0
         view=("insert into score values(%s,%s)")
         value=(self.current_user_name,Quizgame.score)
         self.cursor.execute(view,value)
         self.data.commit()
         Quizgame.score=0
      
   #Button for play game and view score
   def play_score(self):
      c=Toplevel(self.top)
      c.geometry("620x350")
      c.configure(bg="plum1")
      p= Button(c, text = "Play game", fg = "black",font =("times", 20),bg="plum3",command=self.quiz_game).place(x=200,y=100)
      p1= Button(c, text = "View Score", fg = "black",font =("times", 20),bg="plum3",command=self.score_1).place(x=200,y=200)

   #Function for view a score table
   def score_1(self):
      i=0
      e=Toplevel(self.top)
      e.geometry("1366x768")
      e.configure(bg="plum1")
      head=Label(e,text="Welcome to quizgame",bg="plum2",font=("Colonna MT",40),width=80).pack()
      head=Label(e,text="Overall score board",bg="plum2",font=("Colonna MT",40),width=80).pack()

      self.cursor.execute("select * from score order by mark desc limit 5")
      fetch=self.cursor.fetchall()
      tree = ttk.Treeview(e, column=("Name", "Score"),show='headings', height=10)
      tree.column("#1", anchor=CENTER)
      tree.heading("# 1", text="Name")
      tree.column("# 2", anchor=CENTER)
      tree.heading("# 2", text="Score")
      for i in fetch:
         tree.insert('', 'end', text=tree, values=i)
      tree.place(x=400,y=200)

obj=Quizgame()
obj.home()
