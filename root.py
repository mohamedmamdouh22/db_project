from tkinter import *
root = Tk()
import mysql.connector as msc
root.geometry("1300x900")
root.resizable(width=False, height=False)
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
cur=con.cursor()