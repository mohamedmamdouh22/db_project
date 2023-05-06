from tkinter import *
root = Tk()
import sqlite3
root.geometry("1300x900")
root.resizable(width=False, height=False)
root.title('Students Database')
root.iconbitmap(default=r'./images/icon.ico')
con=sqlite3.connect(database='db2.db')
cur=con.cursor()