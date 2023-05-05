from tkinter import *
from root import *
from login import *
from images import *
# to be implemented
class Add:
     def __init__(self,doc_frame,cur):
        doc_frame.place_forget()
        
        self.frameadd = Frame(root, bg="white",width=500,height=900,highlightbackground='#888',highlightthickness=1)
        self.frameadd.place(x=200,y=0)