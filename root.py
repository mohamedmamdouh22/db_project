from tkinter import *
import mysql.connector as msc
# import sqlite3
root = Tk()
root.geometry("1300x900")
root.minsize(1300, 900)
root.resizable(width=True, height=True)
root.title('Students Database')
root.iconbitmap(default=r'./images/icon.ico')

# connect to database
con = msc.connect(
    user='ahmedaliv',
    password='0120246061Mm',
    host='db4free.net',
    port=3306,
    database='studentsdb99'
)
# con=sqlite3.connect(database='db2.db')
cur=con.cursor()