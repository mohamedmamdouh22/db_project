from tkinter import *
from root import *
from images import *
from tkinter import messagebox
from add import *
from delete import *

def handleDelete(frame,table,cur):
    Delete(frame,table,cur)
    


class Login:
    framelogin = Frame(root, bg="white",width=500,height=800,highlightbackground='#888',highlightthickness=1)
    def __init__(self,Start_frame,cur):
        Start_frame.place_forget()
        self.cur=cur
        self.currentTable='students'
        self.framelogin = Frame(root, bg="white",width=500,height=900,highlightbackground='#888',highlightthickness=1)
        self.framelogin.place(x=500,y=0)
        ########
        # self.photo=global_image_list[0]
        self.photo=PhotoImage(file='images/login.png')
        self.photo_i=self.photo.subsample(3,3)
        self.ph=Label(self.framelogin,image=self.photo_i)
        self.ph.place(x=25,y=25)
        ##############
        self.lab1in = Label(self.framelogin, text="User Name", font=('Comic Sans MS', 20),bg='white')
        self.lab1in.place(x=180, y=280)
        self.ent1in = Entry(self.framelogin, font=('Comic Sans MS', 20))
        self.ent1in.place(x=80, y=320)
        self.ent1in.focus()
        self.lab2in = Label(self.framelogin, text="Password", font=('Comic Sans MS', 20),bg='white')
        self.lab2in.place(x=180, y=390)
        self.ent2in = Entry(self.framelogin, font=('Comic Sans MS', 20), show="*")
        self.ent2in.place(x=80, y=430)

        self.butin = Button(self.framelogin,bg='limegreen', text="Login", font=('Comic Sans MS', 20),command=lambda:self.check(self.framelogin))
        self.butin.place(x=180, y=550)
        self.resetin = Button(self.framelogin, text="Exit",activebackground='red', font=('Comic Sans MS', 20),command=quit)
        self.resetin.place(x=190, y=680)
    def choose_table(self,to_forget):
        to_forget.place_forget()
        self.tab_frame = Frame(root, bg="white",width=900,height=900,highlightbackground='#888',highlightthickness=1)
        self.tab_frame.place(x=300,y=-30)
        #add button
        self.add_i=PhotoImage(file='images/std.png')
        self.add_img=self.add_i.subsample(3,3)
        self.add=Button(self.tab_frame,text='Student',image=self.add_img,bg='white',height=350,fg='green',width=400,compound=TOP,cursor = 'cross', bd = 3 , relief = RAISED, overrelief = SUNKEN,borderwidth=3,font=('Comic Sans MS',20),command=lambda:self.start_screen(self.tab_frame,'students'))
        self.add.place(x=20,y=100)
        #print the title
        self.var=StringVar()
        self.lab=Label(self.tab_frame,textvariable=self.var,font='times 20 bold',background='white')
        self.var.set('Choose Table')
        self.lab.place(x=350,y=50)
        #search button
        self.search_i=PhotoImage(file='images/course.png')
        self.search_img=self.search_i.subsample(3,3)
        self.search=Button(self.tab_frame,text='Courses',bg='white',height=350,width=400,compound=TOP,image=self.search_img,cursor = 'cross', relief = RAISED, overrelief = SUNKEN,fg='sky blue',borderwidth=3,font=('Comic Sans MS',20),command=lambda:self.start_screen(self.tab_frame,'courses'))
        self.search.place(x=450,y=100)
        #edit button
        self.edit_i=PhotoImage(file='images/inst.png')
        self.edit_img=self.edit_i.subsample(2,2)
        self.edit=Button(self.tab_frame,text='Instructors',bg='white',height=350,width=400,compound=TOP,cursor = 'cross', relief = RAISED, overrelief = SUNKEN,image=self.edit_img,fg='grey',borderwidth=3,font=('Comic Sans MS',20),command=lambda:self.start_screen(self.tab_frame,'instructors'))
        self.edit.place(x=200,y=500)
##########################################################################
    def start_screen(self,to_forget,table_name):
        to_forget.place_forget()
        self.currentTable=table_name
        self.doc_frame = Frame(root, bg="white",width=900,height=900,highlightbackground='#888',highlightthickness=1)
        self.doc_frame.place(x=300,y=0)
        #print the title and back button
        self.back_lab=Button(root,text='Back',font=('Comic Sans MS', 20 ,'bold'),background='white',command=lambda:self.choose_table(self.doc_frame))
        self.back_lab.place(x=30,y=10)
        self.var=StringVar()
        self.lab=Label(self.doc_frame,textvariable=self.var,font=('Comic Sans MS', 20 ,'bold'),background='white')
        self.var.set(table_name.upper())
        self.lab.place(x=350,y=10)
        #add button
        self.add_i=PhotoImage(file='images/add.png')
        self.add_img=self.add_i.subsample(3,3)

        self.add=Button(self.doc_frame,text='ADD',image=self.add_img,bg='white',height=350,fg='green',width=400,compound=TOP,cursor = 'cross', bd = 3 , relief = RAISED, overrelief = SUNKEN,borderwidth=3,font=('Comic Sans MS',20),command=lambda:Add(self.doc_frame,self.cur))
        self.add.place(x=20,y=120)

        #search button
        self.search_i=PhotoImage(file='images/search.png')
        self.search_img=self.search_i.subsample(3,3)
        self.search=Button(self.doc_frame,text='SEARCH',bg='white',height=350,width=400,compound=TOP,image=self.search_img,cursor = 'cross', relief = RAISED, overrelief = SUNKEN,fg='sky blue',borderwidth=3,font=('Comic Sans MS',20))
        self.search.place(x=450,y=120)
        #edit button
        self.edit_i=PhotoImage(file='images/edit.png')
        self.edit_img=self.edit_i.subsample(3,3)
        self.edit=Button(self.doc_frame,text='EDIT',bg='white',height=350,width=400,compound=TOP,cursor = 'cross', relief = RAISED, overrelief = SUNKEN,image=self.edit_img,fg='grey',borderwidth=3,font=('Comic Sans MS',20))
        self.edit.place(x=20,y=520)
        #delete button
        self.delete_i = PhotoImage(file='images/delete.png')
        self.delete_img = self.delete_i.subsample(3, 3)
        self.delete = Button(self.doc_frame, text='DELETE', bg='white', fg='red', height=350,
                        width=400, relief=RAISED, overrelief=SUNKEN, compound=TOP,cursor = 'cross', image=self.delete_img,
                        borderwidth=3, font=('Comic Sans MS', 20),command=lambda: handleDelete(self.doc_frame,self.currentTable,self.cur))
        self.delete.place(x=450, y=520)

    def check(self,to_forget):
        self.cur.execute(f"select email from login_emails where email = '{self.ent1in.get()}' ")
        result_username = self.cur.fetchone()
        if result_username == None:
            messagebox.showerror("Student Enrollment","WRONG Email")


        elif result_username != None :

            self.cur.execute(f"select pass from login_emails where pass = {self.ent2in.get()}")
            result_pass = self.cur.fetchone()
            if result_pass == None:
                messagebox.showerror("Student Enrollment","WRONG PASSWORD")

            else :
                messagebox.showinfo("Student Enrollment","WELCOME "+ self.ent1in.get().split('@')[0])
                self.choose_table(to_forget)
                


