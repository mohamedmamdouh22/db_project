from tkinter import *
from check import *
from root import *
from images import *
from tkinter import messagebox

class Login:
    framelogin = Frame(root, bg="white",width=500,height=800,highlightbackground='#888',highlightthickness=1)
    def __init__(self,Start_frame,cur):
        Start_frame.place_forget()

        self.framelogin = Frame(root, bg="white",width=500,height=900,highlightbackground='#888',highlightthickness=1)
        self.framelogin.place(x=500,y=0)
        ########
        # self.photo=global_image_list[0]
        self.photo=PhotoImage(file='login.png')
        self.photo_i=self.photo.subsample(3,3)
        self.ph=Label(self.framelogin,image=self.photo_i)
        self.ph.place(x=25,y=25)
        ##############
        self.lab1in = Label(self.framelogin, text="User Name", font=('arial', 20),bg='white')
        self.lab1in.place(x=180, y=280)
        self.ent1in = Entry(self.framelogin, font=('arial', 20))
        self.ent1in.place(x=80, y=320)
        self.ent1in.focus()
        self.lab2in = Label(self.framelogin, text="Password", font=('arial', 20),bg='white')
        self.lab2in.place(x=180, y=390)
        self.ent2in = Entry(self.framelogin, font=('arial', 20), show="*")
        self.ent2in.place(x=80, y=430)
        self.butin = Button(self.framelogin,bg='limegreen', text="LOG IN", font=('arial', 20),command=lambda:self.check(self.framelogin,cur))
        self.butin.place(x=180, y=550)
        self.resetin = Button(self.framelogin, text="EXIT",activebackground='red', font=('arial', 20),command=quit)
        self.resetin.place(x=190, y=680)
    def choose_table(self,to_forget):
        to_forget.place_forget()
        self.tab_frame = Frame(root, bg="white",width=900,height=900,highlightbackground='#888',highlightthickness=1)
        self.tab_frame.place(x=300,y=0)
        #add button
        self.add_i=PhotoImage(file='std.png')
        self.add_img=self.add_i.subsample(3,3)
        self.add=Button(self.tab_frame,text='Student',image=self.add_img,bg='white',height=350,fg='green',width=400,compound=TOP,cursor = 'cross', bd = 3 , relief = RAISED, overrelief = SUNKEN,borderwidth=3,font=('arial',20),command=lambda:self.start_screen(self.tab_frame,'students'))
        self.add.place(x=20,y=120)
        #print the title
        self.var=StringVar()
        self.lab=Label(self.tab_frame,textvariable=self.var,font='times 20 bold',background='white')
        self.var.set('Choose Table')
        self.lab.place(x=350,y=10)
        #search button
        self.search_i=PhotoImage(file='course.png')
        self.search_img=self.search_i.subsample(3,3)
        self.search=Button(self.tab_frame,text='Courses',bg='white',height=350,width=400,compound=TOP,image=self.search_img,cursor = 'cross', relief = RAISED, overrelief = SUNKEN,fg='sky blue',borderwidth=3,font=('arial',20),command=lambda:self.start_screen(self.tab_frame,'courses'))
        self.search.place(x=450,y=120)
        #edit button
        self.edit_i=PhotoImage(file='inst.png')
        self.edit_img=self.edit_i.subsample(2,2)
        self.edit=Button(self.tab_frame,text='Instructors',bg='white',height=350,width=400,compound=TOP,cursor = 'cross', relief = RAISED, overrelief = SUNKEN,image=self.edit_img,fg='grey',borderwidth=3,font=('arial',20),command=lambda:self.start_screen(self.tab_frame,'instructors'))
        self.edit.place(x=200,y=500)
##########################################################################
    def start_screen(self,to_forget,table_name):
        to_forget.place_forget()

        self.doc_frame = Frame(root, bg="white",width=900,height=900,highlightbackground='#888',highlightthickness=1)
        self.doc_frame.place(x=300,y=0)
        #print the title and back button
        self.back_lab=Button(root,text='Back',font='times 20 bold',background='white',command=lambda:self.choose_table(self.doc_frame))
        self.back_lab.place(x=30,y=10)
        self.var=StringVar()
        self.lab=Label(self.doc_frame,textvariable=self.var,font='times 20 bold',background='white')
        self.var.set(table_name.upper())
        self.lab.place(x=350,y=10)
        #add button
        self.add_i=PhotoImage(file='add.png')
        self.add_img=self.add_i.subsample(3,3)
        self.add=Button(self.doc_frame,text='ADD',image=self.add_img,bg='white',height=350,fg='green',width=400,compound=TOP,cursor = 'cross', bd = 3 , relief = RAISED, overrelief = SUNKEN,borderwidth=3,font=('arial',20))
        self.add.place(x=20,y=120)

        #search button
        self.search_i=PhotoImage(file='search.png')
        self.search_img=self.search_i.subsample(3,3)
        self.search=Button(self.doc_frame,text='SEARCH',bg='white',height=350,width=400,compound=TOP,image=self.search_img,cursor = 'cross', relief = RAISED, overrelief = SUNKEN,fg='sky blue',borderwidth=3,font=('arial',20))
        self.search.place(x=450,y=120)
        #edit button
        self.edit_i=PhotoImage(file='edit.png')
        self.edit_img=self.edit_i.subsample(3,3)
        self.edit=Button(self.doc_frame,text='EDIT',bg='white',height=350,width=400,compound=TOP,cursor = 'cross', relief = RAISED, overrelief = SUNKEN,image=self.edit_img,fg='grey',borderwidth=3,font=('arial',20))
        self.edit.place(x=20,y=520)
        #delet button
        self.delete_i = PhotoImage(file='delete.png')
        self.delete_img = self.delete_i.subsample(3, 3)
        self.delete = Button(self.doc_frame, text='DELETE', bg='white', fg='red', height=350,
                        width=400, relief=RAISED, overrelief=SUNKEN, compound=TOP,cursor = 'cross', image=self.delete_img,
                        borderwidth=3, font=('arial', 20))
        self.delete.place(x=450, y=520)
    def check(self,to_forget,cur):
        cur.execute(f"select user from login where user = '{self.ent1in.get()}' ")
        result_username = cur.fetchone()
        if result_username == None:
            messagebox.showerror("Student Enrollment","WRONG USER NAME")


        elif result_username != None :
            cur.execute(f"select pass from login where pass = {self.ent2in.get()}")
            result_pass = cur.fetchone()
            if result_pass == None:
                messagebox.showerror("Student Enrollment","WRONG PASSWORD")

            else :
                messagebox.showinfo("Student Enrollment","WELCOME "+ self.ent1in.get())
                self.choose_table(to_forget)
                


