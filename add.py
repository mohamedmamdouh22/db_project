from tkinter import *
from root import *
from login import *
from images import *
from tkinter import messagebox
# to be implemented
class Add:
     def __init__(self,doc_frame,table,cur):
          if table=='students':
               self.ret_frame=doc_frame
               doc_frame.place_forget()
               
               self.cur=cur
               self.frameadd = Frame(root, bg="white",width=600,height=900,highlightbackground='#888',highlightthickness=1)
               self.frameadd.place(x=400,y=0)

               self.label=Label(self.frameadd,text="Enter your information",font='times 20 bold',bg='white')
               self.label.place(x=70,y=25)


               self.firstname=Label(self.frameadd,text="first name",font=('Comic Sans MS', 20),bg='white')
               self.firstname.place(x=30,y=120)
               self.entry1=Entry(self.frameadd,font=('Comic Sans MS', 20))
               self.entry1.place(x=190,y=130)

               
               self.lastname=Label(self.frameadd,text="last name",font=('Comic Sans MS', 20),bg='white')
               self.lastname.place(x=30,y=180)
               self.entry2=Entry(self.frameadd,font=('Comic Sans MS', 20))
               self.entry2.place(x=190,y=190)

               self.phone=Label(self.frameadd,text="phone",font=('Comic Sans MS', 20),bg='white')
               self.phone.place(x=30,y=240)
               self.entry3=Entry(self.frameadd,font=('Comic Sans MS', 20))
               self.entry3.place(x=190,y=250)

               
               self.email=Label(self.frameadd,text="Email",font=('Comic Sans MS', 20),bg='white')
               self.email.place(x=30,y=310)
               self.entry4=Entry(self.frameadd,font=('Comic Sans MS', 20))
               self.entry4.place(x=190,y=320)

               
               self.address=Label(self.frameadd,text="Adress",font=('Comic Sans MS', 20),bg='white')
               self.address.place(x=30,y=370)
               self.entry5=Entry(self.frameadd,font=('Comic Sans MS', 20))
               self.entry5.place(x=190,y=380)


               self.gender_var=StringVar()
               self.gender_var.set("none")
               
               self.gender=Label(self.frameadd,text="Gender",font=('Comic Sans MS', 20),bg='white')
               self.gender.place(x=30,y=440)
               self.male=Radiobutton(self.frameadd,text="Male",font=('Comic Sans MS', 20),bg='white',variable=self.gender_var,value="Male")
               self.male.place(x=180,y=430)
               self.female=Radiobutton(self.frameadd,text="Female",font=('Comic Sans MS', 20),bg='white',variable=self.gender_var,value="Female")
               self.female.place(x=300,y=430)

               self.dateofbirthday=Label(self.frameadd,text="Data ",font=('Comic Sans MS', 20),bg='white')
               self.dateofbirthday.place(x=30,y=500)
               self.entry6=Entry(self.frameadd,font=('Comic Sans MS', 20))
               self.entry6.place(x=180,y=510)


               self.button1=Button(self.frameadd,text="Save",font=('Comic Sans MS', 20),bg="#68ece8", relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf",command=lambda:self.insert('students'))
               self.button1.place(x=100,y=650)
               self.button2=Button(self.frameadd,text="clear",font=('Comic Sans MS', 20),command=self.clear,bg="#68ece8", relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf")
               self.button2.place(x=300,y=650)
          elif table=='courses':
               pass
          else:
               pass
     def insert(self,table):
         firstname=self.entry1.get()
         lasttname=self.entry2.get()
         phone=self.entry3.get()
         email= self.entry4.get()
         address=self.entry5.get()
         gender=self.gender_var.get()
         date=self.entry6.get()
         mails=cur.execute('select email from students').fetchall()
         phons=cur.execute('select phone from students').fetchall()
         saved_mails=[]
         saved_phons=[]
         print(firstname)
         for mail in mails:
              saved_mails.append(mail[0])
         for phon in phons:
              saved_phons.append(phon[0])
         if firstname=='' or lasttname == '' or phon=='' or email == '' or date == '' :
              messagebox.showerror('Student enrollment program','please, fill all entries')
         if email in saved_mails:
              messagebox.showerror('Student enrollment program','email already exists')
         elif phone in saved_phons: 
              messagebox.showerror('Student enrollment program','phone already exists')
         else:     
               cur.execute(f"INSERT INTO {table} (first_name,last_name,phone,email,address,gender,date_of_birth,course_id) VALUES ('{firstname}','{lasttname}','{phone}','{email}','{address}','{gender}','{date}','1')")
               con.commit()
               messagebox.showinfo('Student enrollment program','Student Added Success')
               self.frameadd.place_forget()
               self.ret_frame.place(x=300,y=0)
     def clear(self):
        self.entry1.delete(0,END)
        self.entry2.delete(0,END)
        self.entry3.delete(0,END)
        self.entry4.delete(0,END)
        self.entry5.delete(0,END)

            




  













