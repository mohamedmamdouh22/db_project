from tkinter import *
from root import *
from images import *
from tkinter import messagebox

class Delete:
    def __init__(self,start_frame,table,cur,con,start_screen):
        start_frame.place_forget()
        self.frameDelete = Frame(root, bg="white",width=600,height=900,highlightbackground='#888',highlightthickness=1)
        self.frameDelete.place(x=400,y=0)
        self.currentTable=table
        self.start_screen= start_screen
        self.cur=cur
        self.con=con
        ########
        # self.photo=global_image_list[0]
        self.photo=PhotoImage(file='images/delete.png')
        self.photo_i=self.photo.subsample(3,3)
        self.ph=Label(self.frameDelete,image=self.photo_i)
        self.ph.place(relx=0.5,rely=0.167,anchor=CENTER)
        ##############
        self.lab1in = Label(self.frameDelete, text="Enter ID", font=('Comic Sans MS', 20),bg='white')
        self.lab1in.place(x=180, y=280)
        self.ent1in = Entry(self.frameDelete, font=('Comic Sans MS', 20))
        self.ent1in.place(x=80, y=320)
        self.ent1in.focus()
        self.butin = Button(self.frameDelete,bg='limegreen', text="Delete", font=('Comic Sans MS', 20),command=lambda:self.check(self.currentTable,cur))
        self.butin.place(x=180, y=550)
        self.resetin = Button(self.frameDelete, text="Exit", activebackground='red', font=('Comic Sans MS', 20), command=self.handleExit)
        self.resetin.place(x=190, y=680)
        
    def check(self,table,cur):
        cur.execute(f"select id from {table}  where id = '{self.ent1in.get()}' ")
        if cur.fetchone() is None:
            messagebox.showerror("Error","No such record exists")
        else:
            cur.execute(f"delete from {table} where id = '{self.ent1in.get()}' ")
            con.commit()
            messagebox.showinfo('Student enrollment program',"Deleted Successfuly...")
    def handleExit(self):
        self.start_screen(self.frameDelete,self.currentTable)

        