from tkinter import *
from login import *
from hover import *
from root import *
from images import *

#Start up frame

frame = Frame(root,width=1400,height=900,highlightbackground='#888',highlightthickness=1)
frame.place(x=0,y=0)
var=StringVar()
Label(frame,textvariable=var,height=5,font='times 20 bold').pack()
var.set('Welcome To Student Enrollment Program')
##########################
photo=PhotoImage(file="images/student.png",height=800)
Label(frame,image=photo,width=1400).pack()
def login(frame,cur,con):
    Login(frame,cur,con)
logbutton = HoverButton(frame,text="Login",bg="#68ece8",font=("Comic Sans MS",30),fg="black", relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf",cursor="mouse",command=lambda : login(frame,cur,con))
logbutton.place(x=400,y=700)
# button exit
exit = HoverButton(frame,text="Exit",bg="#68ece8",font=("Comic Sans MS",30),fg="black",activeforeground='red', relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf",cursor="mouse",command=quit)
exit.place(x=850,y=700)
root.mainloop()
con.close()