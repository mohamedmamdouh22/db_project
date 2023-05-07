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

               self.label=Label(self.frameadd,text="student information",font='times 20 bold',bg='white')
               self.label.place(x=180,y=25)


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
               self.noOfCourses=Label(self.frameadd,text="# of courses",font=('Comic Sans MS', 17),bg='white')
               self.noOfCourses.place(x=30,y=570)
               self.entry7=Entry(self.frameadd,font=('Comic Sans MS', 20))
               self.entry7.place(x=180,y=580)

               self.button1=Button(self.frameadd,text="Save",font=('Comic Sans MS', 20),bg="#68ece8", relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf",command=lambda:self.insert('students'))
               self.button1.place(x=100,y=650)
               self.button2=Button(self.frameadd,text="clear",font=('Comic Sans MS', 20),command=self.clear,bg="#68ece8", relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf")
               self.button2.place(x=300,y=650)
         
          elif table=='courses':
               self.ret_frame=doc_frame
               doc_frame.place_forget()
               
               self.cur=cur
               self.frameadd = Frame(root, bg="white",width=600,height=900,highlightbackground='#888',highlightthickness=1)
               self.frameadd.place(x=400,y=0)

               self.label=Label(self.frameadd,text=" course information",font='times 20 bold',bg='white')
               self.label.place(x=180,y=25)

               self.course_name=Label(self.frameadd,text="course name",font=('arial', 20),bg='white')
               self.course_name.place(x=20,y=150)
               self.entry1=Entry(self.frameadd,font=('arial', 20))
               self.entry1.place(x=210,y=160)

               self.course_desc=Label(self.frameadd,text="description",font=('arial', 20),bg='white')
               self.course_desc.place(x=20,y=280)
               self.entry2=Entry(self.frameadd,font=('arial', 20))
               self.entry2.place(x=210,y=290)


               self.num_of_students=Label(self.frameadd,text="Num_students",font=('arial', 20),bg='white')
               self.num_of_students.place(x=20,y=400)
               self.entry3=Entry(self.frameadd,font=('arial', 20))
               self.entry3.place(x=210,y=410)

               self.button1=Button(self.frameadd,text="Save",font=('Comic Sans MS', 20),bg="#68ece8", relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf",command=lambda:self.submit('courses'))
               self.button1.place(x=150,y=550)
               self.button2=Button(self.frameadd,text="clear",font=('Comic Sans MS', 20),command=self.clear,bg="#68ece8", relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf")
               self.button2.place(x=350,y=550)
               
               
          else:
               self.ret_frame=doc_frame
               doc_frame.place_forget()
               
               self.cur=cur
               self.frameadd = Frame(root, bg="white",width=600,height=900,highlightbackground='#888',highlightthickness=1)
               self.frameadd.place(x=400,y=0)

               self.label=Label(self.frameadd,text="instructor information",font='times 20 bold',bg='white')
               self.label.place(x=180,y=25)


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

               self.dateofbirthday=Label(self.frameadd,text="Date ",font=('Comic Sans MS', 20),bg='white')
               self.dateofbirthday.place(x=30,y=500)
               self.entry6=Entry(self.frameadd,font=('Comic Sans MS', 20))
               self.entry6.place(x=180,y=510)
               self.noOfCourses=Label(self.frameadd,text="# of courses",font=('Comic Sans MS', 17),bg='white')
               self.noOfCourses.place(x=30,y=570)
               self.entry7=Entry(self.frameadd,font=('Comic Sans MS', 20))
               self.entry7.place(x=180,y=580)




               self.button1=Button(self.frameadd,text="Save",font=('Comic Sans MS', 20),bg="#68ece8", relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf",command=lambda:self.insert('instructors'))
               self.button1.place(x=100,y=650)
               self.button2=Button(self.frameadd,text="clear",font=('Comic Sans MS', 20),command=self.clear,bg="#68ece8", relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf")
               self.button2.place(x=300,y=650)
         
              
     def insert(self,table):
          self.courses = Frame(root, bg="white",width=600,height=900,highlightbackground='#888',highlightthickness=1)
          firstname=self.entry1.get()
          lasttname=self.entry2.get()
          phone=self.entry3.get()
          email= self.entry4.get()
          address=self.entry5.get()
          gender=self.gender_var.get()
          date=self.entry6.get()
          cur.execute(f'select email from {table}')
          mails=cur.fetchall()
          cur.execute(f'select phone from {table}')
          phons=cur.fetchall()
          saved_mails=[]
          saved_phons=[]
          for mail in mails:
               saved_mails.append(mail[0])
          for phon in phons:
               saved_phons.append(phon[0])
          if firstname.isdigit() or lasttname.isdigit() or phone.isalpha() or email.count('@')==0 :
               messagebox.showerror('Student enrollment program','wrong data types')  
          elif firstname=='' or lasttname == '' or phone=='' or email == '' or date == '' :
               messagebox.showerror('Student enrollment program','please, fill all entries')
          elif email in saved_mails:
               messagebox.showerror('Student enrollment program','email already exists')
          elif phone in saved_phons: 
               messagebox.showerror('Student enrollment program','phone already exists')
          elif int(self.entry7.get())==0:
               messagebox.showerror('Student enrollment program','student should assign at least one course')
          elif int(self.entry7.get())>4:
               messagebox.showerror('Student enrollment program','student should assign maximum 4 courses')
          else:
               self.courses.place(x=400,y=0)
               n=int(self.entry7.get())
               L=[]
               for i in range(n):
                    
                    k=Label(self.courses,text=f"course{i+1} ",font=('Comic Sans MS', 20),bg='white')
                    k.place(x=20,y=100*i+1)
                    L.append(Entry(self.courses,font=('Comic Sans MS', 20)))
                    L[i].place(x=150,y=110*i+1)
               self.button1=Button(self.courses,text="Save",font=('Comic Sans MS', 20),bg="#68ece8", relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf",command=lambda:self.save_std(L,table))
               self.button1.place(x=100,y=650)
               self.button2=Button(self.courses,text="clear",font=('Comic Sans MS', 20),command=self.clear,bg="#68ece8", relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf")
               self.button2.place(x=300,y=650)

     def save_std(self,L,table):
               firstname=self.entry1.get()
               lasttname=self.entry2.get()
               phone=self.entry3.get()
               email= self.entry4.get()
               address=self.entry5.get()
               gender=self.gender_var.get()
               date=self.entry6.get()

               for i in range(len(L)):
                    cur.execute(f'select id from courses where id={L[i].get()}')
                    row = cur.fetchone()
                    if row is not None:
                         cur.execute(f"INSERT INTO {table} (first_name,last_name,phone,email,address,gender,date_of_birth,course_id) VALUES ('{firstname}','{lasttname}','{phone}','{email}','{address}','{gender}','{date}','{L[i].get()}')")
                         con.commit()
                         messagebox.showinfo('Student enrollment program','courses Added Success')
                         self.frameadd.place_forget()
                         self.courses.place_forget()
                         self.ret_frame.place(x=300,y=0)
                    else:
                         messagebox.showerror('Student enrollment program','course id not found')


     def clear(self):
          try:
               self.entry1.delete(0,END)
               self.entry2.delete(0,END)
               self.entry3.delete(0,END)
               self.entry4.delete(0,END)
               self.entry5.delete(0,END)
          except:
               print('no entry found')
     

     def submit(self,table):
          coursename=self.entry1.get()
          desc=self.entry2.get()
          numberofstudent=self.entry3.get()
          if coursename=='' or desc=='' or numberofstudent=='':
               messagebox.showerror('Student enrollment program','please, fill all entries')
          else:
               cur.execute(f"INSERT INTO {table} (name,description,no_of_students) VALUES ('{coursename}','{desc}','{numberofstudent}')")
               con.commit()          
               messagebox.showinfo('Student enrollment program','course Added Success')
               self.frameadd.place_forget()
               self.ret_frame.place(x=300,y=0)
