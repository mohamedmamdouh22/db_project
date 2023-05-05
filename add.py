from tkinter import *
from root import *
from login import *
from images import *
# to be implemented
class Add:
   def __init__(self,doc_frame,cur):
        doc_frame.place_forget()
        self.cur=cur
        self.frameadd = Frame(root, bg="white",width=500,height=900,highlightbackground='#888',highlightthickness=1)
        self.frameadd.place(x=400,y=0)

        self.label=Label(self.frameadd,text="Enter your information",font='times 20 bold',bg='white')
        self.label.place(x=70,y=25)


        self.firstname=Label(self.frameadd,text="first name",font=('Comic Sans MS', 20),bg='white')
        self.firstname.place(x=40,y=120)
        self.entry1=Entry(self.frameadd,font=('Comic Sans MS', 20))
        self.entry1.place(x=180,y=130)

        
        self.lastname=Label(self.frameadd,text="last name",font=('Comic Sans MS', 20),bg='white')
        self.lastname.place(x=40,y=180)
        self.entry2=Entry(self.frameadd,font=('Comic Sans MS', 20))
        self.entry2.place(x=180,y=190)

        self.phone=Label(self.frameadd,text="phone",font=('Comic Sans MS', 20),bg='white')
        self.phone.place(x=40,y=240)
        self.entry3=Entry(self.frameadd,font=('Comic Sans MS', 20))
        self.entry3.place(x=180,y=250)

        
        self.email=Label(self.frameadd,text="Email",font=('Comic Sans MS', 20),bg='white')
        self.email.place(x=40,y=310)
        self.entry4=Entry(self.frameadd,font=('Comic Sans MS', 20))
        self.entry4.place(x=180,y=320)

        
        self.address=Label(self.frameadd,text="Adress",font=('Comic Sans MS', 20),bg='white')
        self.address.place(x=40,y=370)
        self.entry5=Entry(self.frameadd,font=('Comic Sans MS', 20))
        self.entry5.place(x=180,y=380)


        gender=StringVar()
        gender.set("none")
       
        self.gender=Label(self.frameadd,text="Gender",font=('Comic Sans MS', 20),bg='white')
        self.gender.place(x=40,y=440)
        self.male=Radiobutton(self.frameadd,text="Male",font=('Comic Sans MS', 20),bg='white',variable=gender,value="Male")
        self.male.place(x=180,y=430)
        self.female=Radiobutton(self.frameadd,text="Female",font=('Comic Sans MS', 20),bg='white',variable=gender,value="Female")
        self.female.place(x=300,y=430)

        self.dateofbirthday=Label(self.frameadd,text="Data ",font=('Comic Sans MS', 20),bg='white')
        self.dateofbirthday.place(x=40,y=500)
        self.entry6=Entry(self.frameadd,font=('Comic Sans MS', 20))
        self.entry6.place(x=180,y=510)


        self.button1=Button(self.frameadd,text="Save",font=('Comic Sans MS', 20),bg="#68ece8", relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf",command=self.insert)
        self.button1.place(x=100,y=650)
        self.button2=Button(self.frameadd,text="clear",font=('Comic Sans MS', 20),bg="#68ece8", relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf")
        self.button2.place(x=300,y=650)

   def insert(self):
         firstname=self.entry1.get()
         lasttname=self.entry2.get()
         phone=self.entry3.get()
         email= self.entry4.get()
         address=self.entry5.get()
     #     gender=self.gender.get()
         date=self.entry6.get()


         self.cur.execute(f"INSERT INTO students (first_name,last_name,phone,email,address,gender,date_of_birth,course_id) VALUES ('{firstname}',{lasttname},'{phone}', '{email}','{address},'mail','{date}',1)")
         self.cur.connection.commit()

            




  













