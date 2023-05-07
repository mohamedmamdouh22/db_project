from tkinter import *
from root import *
from images import *
from tkinter import messagebox

class Edit:
    def __init__(self,start_frame,table,cur):
        
        #delet last frame 
        start_frame.place_forget()

        #creat new frame for edit 
        self.cur=cur
        self.frameEdit = Frame(root,
                               bg="white",
                               width=600,height=900
                               ,highlightbackground='#888'
                               ,highlightthickness=1)
        self.frameEdit.place(x=400,y=0)

        #git to table's name 
        self.currentTable=table
        
        #put the pic for edit 
        self.photo=PhotoImage(file='images/edit.png')
        self.photo_i=self.photo.subsample(3,3)
        self.ph=Label(self.frameEdit,image=self.photo_i)
        self.ph.place(relx=0.5,rely=0.167,anchor=CENTER)
        
        #creat entry to get the id form the user 
        self.lab1in = Label(self.frameEdit, text="Enter ID", font=('Comic Sans MS', 20),bg='white')
        self.lab1in.place(x=180, y=280)
        self.ent1in = Entry(self.frameEdit, font=('Comic Sans MS', 20))
        self.ent1in.place(x=80, y=320)
        self.ent1in.focus()
        
        #check for avilability
        self.butin = Button(self.frameEdit,bg='limegreen', text="Check", font=('Comic Sans MS', 20),command=lambda:self.check(self.currentTable,self.cur))
        self.butin.place(x=180, y=400)

    #check if the id of the user is exist     
    def check(self,table,cur):
        cur.execute(f"select id from {table}  where id = '{self.ent1in.get()}' ")
        if cur.fetchone() is None:
            messagebox.showerror("Error","No such record exists")
        else:
           self.buttonn = Button(self.frameEdit,
                              bg='limegreen', 
                              text="Enter",
                              font=('Comic Sans MS', 20),
                              command=lambda: self.handleupdate(self.frameEdit,table, cur , self.ent1in.get()))
           self.buttonn.place(x=180, y=500)
    
    def handleupdate (self,frame,table,cur , id ):
        Update(frame , table, cur , id )
    



class Update:
    def __init__(self,start_frame,table,cur,id):
        
        #delet last frame 
        start_frame.place_forget()

        #creat new frame for edit 
        self.cur=cur
        self.frameupdate = Frame(root,
                               bg="white",
                               width=600,
                               height=900
                               ,highlightbackground='#888'
                               ,highlightthickness=1)
        self.frameupdate.place(x=400,y=0)
        

        #git to table's name 
        self.currentTable = table
        self.id = id
        
        if table == "students":
            self.label=Label(self.frameupdate,text="update students name",font='times 20 bold',bg='white')
            self.label.place(x=180,y=25)
            #first name label
            self.firstname=Label(self.frameupdate,text="first name",font=('Comic Sans MS', 20),bg='white')
            self.firstname.place(x=30,y=120)
            self.entry1s=Entry(self.frameupdate,font=('Comic Sans MS', 20))
            self.entry1s.place(x=190,y=130)

                
            self.lastname=Label(self.frameupdate,text="last name",font=('Comic Sans MS', 20),bg='white')
            self.lastname.place(x=30,y=180)
            self.entry2s=Entry(self.frameupdate,font=('Comic Sans MS', 20))
            self.entry2s.place(x=190,y=190)

            self.phone=Label(self.frameupdate,text="phone",font=('Comic Sans MS', 20),bg='white')
            self.phone.place(x=30,y=240)
            self.entry3s=Entry(self.frameupdate,font=('Comic Sans MS', 20))
            self.entry3s.place(x=190,y=250)

                
            self.email=Label(self.frameupdate,text="Email",font=('Comic Sans MS', 20),bg='white')
            self.email.place(x=30,y=310)
            self.entry4s=Entry(self.frameupdate,font=('Comic Sans MS', 20))
            self.entry4s.place(x=190,y=320)

                
            self.address=Label(self.frameupdate,text="Adress",font=('Comic Sans MS', 20),bg='white')
            self.address.place(x=30,y=370)
            self.entry5s=Entry(self.frameupdate,font=('Comic Sans MS', 20))
            self.entry5s.place(x=190,y=380)


            self.gender_vars=StringVar()
            self.gender_vars.set("none")
                
            self.gender=Label(self.frameupdate,text="Gender",font=('Comic Sans MS', 20),bg='white')
            self.gender.place(x=30,y=440)
            self.male=Radiobutton(self.frameupdate,text="Male",font=('Comic Sans MS', 20),bg='white',variable=self.gender_vars,value="Male")
            self.male.place(x=180,y=430)
            self.female=Radiobutton(self.frameupdate,text="Female",font=('Comic Sans MS', 20),bg='white',variable=self.gender_vars,value="Female")
            self.female.place(x=300,y=430)

            self.dateofbirthday=Label(self.frameupdate,text="Data ",font=('Comic Sans MS', 20),bg='white')
            self.dateofbirthday.place(x=30,y=500)
            self.entry6s=Entry(self.frameupdate,font=('Comic Sans MS', 20))
            self.entry6s.place(x=180,y=510)
            
            self.course_id=Label(self.frameupdate,text="Course_id",font=('Comic Sans MS', 20),bg='white')
            self.course_id.place(x=30,y=560)
            self.entry7s=Entry(self.frameupdate,font=('Comic Sans MS', 20))
            self.entry7s.place(x=180,y=570)

            cur.execute(f"select * from '{table}'  where id = '{id}' ")
            con.commit()
            record = cur.fetchone()
            self.entry1s.insert(0 ,record[1])
            self.entry2s.insert(0 ,record[2])
            self.entry3s.insert(0 ,record[3])
            self.entry4s.insert(0 ,record[4])
            self.entry5s.insert(0 ,record[5])
            self.entry6s.insert(0 ,record[7])
            self.entry7s.insert(0 ,record[8])

            self.button1=Button(self.frameupdate,
                                text="Update",
                                font=('Comic Sans MS', 20),
                                bg="#68ece8", relief = RAISED, 
                                overrelief = SUNKEN,activebackground="#4dbedf",
                                command = lambda : self.updates(self.currentTable , self.cur , self.id))
            self.button1.place(x=100,y=650)

   

        elif table == "courses":
            self.label=Label(self.frameupdate,text="update courses",font='times 20 bold',bg='white')
            self.label.place(x=180,y=25)

            self.course_name=Label(self.frameupdate,text="course name",font=('arial', 20),bg='white')
            self.course_name.place(x=20,y=150)
            self.entry1=Entry(self.frameupdate,font=('arial', 20))
            self.entry1.place(x=210,y=160)

            self.course_desc=Label(self.frameupdate,text="description",font=('arial', 20),bg='white')
            self.course_desc.place(x=20,y=280)
            self.entry2=Entry(self.frameupdate,font=('arial', 20))
            self.entry2.place(x=210,y=290)


            self.num_of_students=Label(self.frameupdate,text="Num_students",font=('arial', 20),bg='white')
            self.num_of_students.place(x=20,y=400)
            self.entry3=Entry(self.frameupdate,font=('arial', 20))
            self.entry3.place(x=210,y=410)


            cur.execute(f"select * from '{table}'  where id = '{id}' ")
            con.commit()
            record = cur.fetchone()
            self.entry1.insert(0 ,record[1])
            self.entry2.insert(0 ,record[2])
            self.entry3.insert(0 ,record[3])

            self.button1=Button(self.frameupdate,
                                text="Update",
                                font=('Comic Sans MS', 20),
                                bg="#68ece8", relief = RAISED, 
                                overrelief = SUNKEN,activebackground="#4dbedf",
                                command = lambda : self.updatec(self.currentTable , self.cur , self.id))
            self.button1.place(x=100,y=650)
        else:

            self.label=Label(self.frameupdate,text="update instructors information",font='times 20 bold',bg='white')
            self.label.place(x=180,y=25)
            
            self.firstname=Label(self.frameupdate,text="first name",font=('Comic Sans MS', 20),bg='white')
            self.firstname.place(x=30,y=120)
            self.entry1i=Entry(self.frameupdate,font=('Comic Sans MS', 20))
            self.entry1i.place(x=190,y=130)

                
            self.lastname=Label(self.frameupdate,text="last name",font=('Comic Sans MS', 20),bg='white')
            self.lastname.place(x=30,y=180)
            self.entry2i=Entry(self.frameupdate,font=('Comic Sans MS', 20))
            self.entry2i.place(x=190,y=190)

            self.phone=Label(self.frameupdate,text="phone",font=('Comic Sans MS', 20),bg='white')
            self.phone.place(x=30,y=240)
            self.entry3i=Entry(self.frameupdate,font=('Comic Sans MS', 20))
            self.entry3i.place(x=190,y=250)

                
            self.email=Label(self.frameupdate,text="Email",font=('Comic Sans MS', 20),bg='white')
            self.email.place(x=30,y=310)
            self.entry4i=Entry(self.frameupdate,font=('Comic Sans MS', 20))
            self.entry4i.place(x=190,y=320)

                
            self.address=Label(self.frameupdate,text="Adress",font=('Comic Sans MS', 20),bg='white')
            self.address.place(x=30,y=370)
            self.entry5i=Entry(self.frameupdate,font=('Comic Sans MS', 20))
            self.entry5i.place(x=190,y=380)


            self.gender_vari=StringVar()
            self.gender_vari.set("none")
                
            self.gender=Label(self.frameupdate,text="Gender",font=('Comic Sans MS', 20),bg='white')
            self.gender.place(x=30,y=440)
            self.male=Radiobutton(self.frameupdate,text="Male",font=('Comic Sans MS', 20),bg='white',variable=self.gender_vari,value="Male")
            self.male.place(x=180,y=430)
            self.female=Radiobutton(self.frameupdate,text="Female",font=('Comic Sans MS', 20),bg='white',variable=self.gender_vari,value="Female")
            self.female.place(x=300,y=430)

            self.dateofbirthday=Label(self.frameupdate,text="Data ",font=('Comic Sans MS', 20),bg='white')
            self.dateofbirthday.place(x=30,y=500)
            self.entry6i=Entry(self.frameupdate,font=('Comic Sans MS', 20))
            self.entry6i.place(x=180,y=510)
            
            self.course_id=Label(self.frameupdate,text="Course_id",font=('Comic Sans MS', 20),bg='white')
            self.course_id.place(x=30,y=560)
            self.entry7i=Entry(self.frameupdate,font=('Comic Sans MS', 20))
            self.entry7i.place(x=180,y=570)

            cur.execute(f"select * from '{table}'  where id = '{id}' ")
            con.commit()
            record = cur.fetchone()
            self.entry1i.insert(0 ,record[1])
            self.entry2i.insert(0 ,record[2])
            self.entry3i.insert(0 ,record[3])
            self.entry4i.insert(0 ,record[4])
            self.entry5i.insert(0 ,record[5])
            self.entry6i.insert(0 ,record[7])
            self.entry7i.insert(0 ,record[8])

            self.button1=Button(self.frameupdate,
                                text="Update",
                                font=('Comic Sans MS', 20),
                                bg="#68ece8", relief = RAISED, 
                                overrelief = SUNKEN,activebackground="#4dbedf",
                                command = lambda : self.updatei(self.currentTable , self.cur , self.id))
            self.button1.place(x=100,y=650)


    
    
    def updates (self , table , cur , id ):

        cur.execute(f"update '{table}' set first_name = '{self.entry1s.get()}' where id = '{id}' ")
        con.commit()
        cur.execute(f"update '{table}' set last_name = '{self.entry2s.get()}' where id = '{id}' ")
        con.commit()
        cur.execute(f"update '{table}' set phone = '{self.entry3s.get()}' where id = '{id}' ")
        con.commit()
        cur.execute(f"update '{table}' set email = '{self.entry4s.get()}' where id = '{id}' ")
        con.commit()
        cur.execute(f"update '{table}' set address = '{self.entry5s.get()}' where id = '{id}' ")
        con.commit()
        cur.execute(f"update '{table}' set date_of_birth = '{self.entry6s.get()}' where id = '{id}' ")
        con.commit()
        cur.execute(f"update '{table}' set course_id = '{self.entry7s.get()}' where id = '{id}' ")
        con.commit()
        cur.execute(f"update '{table}' set gender = '{self.gender_vars.get()}' where id = '{id}' ")
        con.commit()
        messagebox.showinfo('Student enrollment program','Student update Success')


    def updatei (self , table , cur , id ):

        cur.execute(f"update '{table}' set first_name = '{self.entry1i.get()}' where id = '{id}' ")
        con.commit()
        cur.execute(f"update '{table}' set last_name = '{self.entry2i.get()}' where id = '{id}' ")
        con.commit()
        cur.execute(f"update '{table}' set phone = '{self.entry3i.get()}' where id = '{id}' ")
        con.commit()
        cur.execute(f"update '{table}' set email = '{self.entry4i.get()}' where id = '{id}' ")
        con.commit()
        cur.execute(f"update '{table}' set address = '{self.entry5i.get()}' where id = '{id}' ")
        con.commit()
        cur.execute(f"update '{table}' set date_of_birth = '{self.entry6i.get()}' where id = '{id}' ")
        con.commit()
        cur.execute(f"update '{table}' set course_id = '{self.entry7i.get()}' where id = '{id}' ")
        con.commit()
        cur.execute(f"update '{table}' set gender = '{self.gender_vari.get()}' where id = '{id}' ")
        con.commit()
        messagebox.showinfo('Student enrollment program','update instrotr info Success')
    
    def updatec (self , table , cur , id ):

        cur.execute(f"update '{table}' set name = '{self.entry1.get()}' where id = '{id}' ")
        con.commit()
        cur.execute(f"update '{table}' set description = '{self.entry2.get()}' where id = '{id}' ")
        con.commit()
        cur.execute(f"update '{table}' set no_of_students = '{self.entry3.get()}' where id = '{id}' ")
        con.commit()
        messagebox.showinfo('Student enrollment program','update courses Success')

