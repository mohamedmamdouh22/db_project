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
                               width=500,height=900
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
        #cur.execute(f"select id from {table}  where id = '{self.ent1in.get()}' ")
       # if cur.fetchone() is None:
        #    messagebox.showerror("Error","No such record exists")
        #else:
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


        #first name label
        self.firstname=Label(self.frameupdate,text="first name",font=('Comic Sans MS', 20),bg='white')
        self.firstname.place(x=30,y=120)
        self.entry1=Entry(self.frameupdate,font=('Comic Sans MS', 20))
        self.entry1.place(x=190,y=130)

               
        self.lastname=Label(self.frameupdate,text="last name",font=('Comic Sans MS', 20),bg='white')
        self.lastname.place(x=30,y=180)
        self.entry2=Entry(self.frameupdate,font=('Comic Sans MS', 20))
        self.entry2.place(x=190,y=190)

        self.phone=Label(self.frameupdate,text="phone",font=('Comic Sans MS', 20),bg='white')
        self.phone.place(x=30,y=240)
        self.entry3=Entry(self.frameupdate,font=('Comic Sans MS', 20))
        self.entry3.place(x=190,y=250)

               
        self.email=Label(self.frameupdate,text="Email",font=('Comic Sans MS', 20),bg='white')
        self.email.place(x=30,y=310)
        self.entry4=Entry(self.frameupdate,font=('Comic Sans MS', 20))
        self.entry4.place(x=190,y=320)

               
        self.address=Label(self.frameupdate,text="Adress",font=('Comic Sans MS', 20),bg='white')
        self.address.place(x=30,y=370)
        self.entry5=Entry(self.frameupdate,font=('Comic Sans MS', 20))
        self.entry5.place(x=190,y=380)


        self.gender_var=StringVar()
        self.gender_var.set("none")
               
        self.gender=Label(self.frameupdate,text="Gender",font=('Comic Sans MS', 20),bg='white')
        self.gender.place(x=30,y=440)
        self.male=Radiobutton(self.frameupdate,text="Male",font=('Comic Sans MS', 20),bg='white',variable=self.gender_var,value="Male")
        self.male.place(x=180,y=430)
        self.female=Radiobutton(self.frameupdate,text="Female",font=('Comic Sans MS', 20),bg='white',variable=self.gender_var,value="Female")
        self.female.place(x=300,y=430)

        self.dateofbirthday=Label(self.frameupdate,text="Data ",font=('Comic Sans MS', 20),bg='white')
        self.dateofbirthday.place(x=30,y=500)
        self.entry6=Entry(self.frameupdate,font=('Comic Sans MS', 20))
        self.entry6.place(x=180,y=510)
        

        self.button1=Button(self.frameupdate,
                            text="Update",
                            font=('Comic Sans MS', 20),
                            bg="#68ece8", relief = RAISED, 
                            overrelief = SUNKEN,activebackground="#4dbedf",
                            command = lambda : self.update(self.currentTable , self.cur , self.id))
        self.button1.place(x=100,y=650)


        cur.execute(f"select * from {table}  where id = {id} ")
        record = cur.fetchall()
        self.entry1.insert(0 ,record[0])
        self.entry2.insert(0 ,record[1])
        self.entry3.insert(0 ,record[2])
        self.entry4.insert(0 ,record[3])
        self.entry5.insert(0 ,record[4])
        self.entry6.insert(0 ,record[5])
    
    def update (self , table , cur , id):
        
        cur.execute(f""" UPDATE {table} SET  
              self.entry1 = :first_name
              self.entry2 = :last_name,
              self.entry3 = :phone,
              self.entry4 = :email,
              self.entry5 = :adress,
              self.entry6 = :dateofbirthday,

              Where id  = :{id}""",
                     {
                        'first_name' : self.entry1.get(),
                        'last_name' : self.entry2.get(),
                        'phone' : self.entry3.get(),
                        'email' : self.entry4.get(),
                        'adress' : self.entry5.get(),
                        'dateofbirthday' : self.entry6.get(),
                     })
        con.commit()
        messagebox.showinfo('Student enrollment program','Student Added Success')

        

        
