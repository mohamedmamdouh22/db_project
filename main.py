from tkinter import *
from login import *
from hover import *
from root import *
from images import *
import mysql.connector
from mysql.connector import Error
#Start up frame
# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='Electronics',
#                                          user='pynative',
#                                          password='pynative@#29')
#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)

# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")
frame = Frame(root,width=1400,height=900,highlightbackground='#888',highlightthickness=1)
frame.place(x=0,y=0)
var=StringVar()
Label(frame,textvariable=var,height=5,font='times 20 bold').pack()
var.set('Welcome To Student Enrollment Program')
##########################
photo=PhotoImage(file="student.png",height=800)
Label(frame,image=photo,width=1400).pack()
def login():
    Login(frame)
logbutton = HoverButton(frame,text="LOG IN",bg="#68ece8",font=("Arial",30),fg="black", relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf",cursor="mouse",command=lambda : login())
logbutton.place(x=400,y=700)
# button exit
exit = HoverButton(frame,text="EXIT",bg="#68ece8",font=("Arial",30),fg="black",activeforeground='red', relief = RAISED, overrelief = SUNKEN,activebackground="#4dbedf",cursor="mouse",command=quit)
exit.place(x=850,y=700)


root.mainloop()