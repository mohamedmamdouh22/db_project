from tkinter import *
from root import *
from images import *
from tkinter import messagebox

def search(frame,table,cur):
    Search(frame,table,cur)

class Search:
    def __init__(self,start_frame,table,cur):
        start_frame.place_forget()
        self.frameSearch = Frame(root, bg="white",width=500,height=800,highlightbackground='#888',highlightthickness=1)
        self.frameSearch.place(x=500,y=0)
        self.currentTable=table
        self.cur = cur
        ########
        # self.photo=global_image_list[0]
        self.photo=PhotoImage(file='images/search.png')
        self.photo_i=self.photo.subsample(3,3)
        self.ph=Label(self.frameSearch,image=self.photo_i)
        self.ph.place(relx=0.5,rely=0.167,anchor=CENTER)
        ##############
        self.lab1in = Label(self.frameSearch, text="Enter ID", font=('Comic Sans MS', 20),bg='white')
        self.lab1in.place(x=180, y=280)
        self.ent1in = Entry(self.frameSearch, font=('Comic Sans MS', 20))
        self.ent1in.place(x=80, y=320)
        self.ent1in.focus()
        
        self.butin = Button(self.frameSearch,bg='limegreen', text="Search", font=('Comic Sans MS', 20),command=lambda:self.check(self.frameSearch,self.currentTable,cur))
        self.butin.place(x=180, y=550)

##########################################################################
    def display_student(self, to_forget, result):
        # Create a new frame to display the search results
        to_forget.place_forget()
        self.result_frame = Frame(root, bg="white",width=500,height=800,highlightbackground='#888',highlightthickness=1)
        self.result_frame.place(x=500,y=0)
    
        # Add labels to display the search result fields
        Label(self.result_frame, text="ID:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=0, column=0, padx=55, pady=27, sticky="w")
        Label(self.result_frame, text="First Name:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=1, column=0, padx=55, pady=27, sticky="w")
        Label(self.result_frame, text="Last Name:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=2, column=0, padx=55, pady=27, sticky="w")
        Label(self.result_frame, text="Phone:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=3, column=0, padx=55, pady=27, sticky="w")
        Label(self.result_frame, text="E-mail:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=4, column=0, padx=55, pady=27, sticky="w")
        Label(self.result_frame, text="Address:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=5, column=0, padx=55, pady=27, sticky="w")
        Label(self.result_frame, text="Gender:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=6, column=0, padx=55, pady=27, sticky="w")
        Label(self.result_frame, text="Date of Birth:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=7, column=0, padx=55, pady=27, sticky="w")
        Label(self.result_frame, text="Course ID:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=8, column=0, padx=55, pady=27, sticky="w")

        # Display the search result values
        Label(self.result_frame, text=result[0], font=("Arial", 14), bg="#f0f0f0").grid(row=0, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[1], font=("Arial", 14), bg="#f0f0f0").grid(row=1, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[2], font=("Arial", 14), bg="#f0f0f0").grid(row=2, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[3], font=("Arial", 14), bg="#f0f0f0").grid(row=3, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[4], font=("Arial", 14), bg="#f0f0f0").grid(row=4, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[5], font=("Arial", 14), bg="#f0f0f0").grid(row=5, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[6], font=("Arial", 14), bg="#f0f0f0").grid(row=6, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[7], font=("Arial", 14), bg="#f0f0f0").grid(row=7, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[8], font=("Arial", 14), bg="#f0f0f0").grid(row=8, column=3, padx=10, pady=5, sticky="e")
        #search again button
        self.back_s = Button(self.result_frame, bg='limegreen', text="Search Again", activebackground='red', font=('Comic Sans MS', 20), command=lambda: search(self.result_frame, self.currentTable, self.cur))
        self.back_s.grid(row=0, column=4, padx=30, pady=20, sticky="e")
        
    def display_instructor(self, to_forget, result):
        # Create a new frame to display the search results
        to_forget.place_forget()
        self.result_frame = Frame(root, bg="white",width=500,height=800,highlightbackground='#888',highlightthickness=1)
        self.result_frame.place(x=500,y=0)
    
       # Add labels to display the search result fields
        Label(self.result_frame, text="ID:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=0, column=0, padx=55, pady=27, sticky="w")
        Label(self.result_frame, text="First Name:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=1, column=0, padx=55, pady=27, sticky="w")
        Label(self.result_frame, text="Last Name:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=2, column=0, padx=55, pady=27, sticky="w")
        Label(self.result_frame, text="Phone:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=3, column=0, padx=55, pady=27, sticky="w")
        Label(self.result_frame, text="E-mail:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=4, column=0, padx=55, pady=27, sticky="w")
        Label(self.result_frame, text="Address:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=5, column=0, padx=55, pady=27, sticky="w")
        Label(self.result_frame, text="Gender:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=6, column=0, padx=55, pady=27, sticky="w")
        Label(self.result_frame, text="Date of Birth:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=7, column=0, padx=55, pady=27, sticky="w")
        Label(self.result_frame, text="Course ID:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=8, column=0, padx=55, pady=27, sticky="w")
    
        # Display the search result values
        Label(self.result_frame, text=result[0], font=("Arial", 14), bg="#f0f0f0").grid(row=0, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[1], font=("Arial", 14), bg="#f0f0f0").grid(row=1, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[2], font=("Arial", 14), bg="#f0f0f0").grid(row=2, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[3], font=("Arial", 14), bg="#f0f0f0").grid(row=3, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[4], font=("Arial", 14), bg="#f0f0f0").grid(row=4, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[5], font=("Arial", 14), bg="#f0f0f0").grid(row=5, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[6], font=("Arial", 14), bg="#f0f0f0").grid(row=6, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[7], font=("Arial", 14), bg="#f0f0f0").grid(row=7, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[8], font=("Arial", 14), bg="#f0f0f0").grid(row=8, column=3, padx=10, pady=5, sticky="e")
        #back button
        self.back_s = Button(self.result_frame, bg='limegreen', text="Search Again", activebackground='red', font=('Comic Sans MS', 20), command=lambda: search(self.result_frame, self.currentTable, self.cur))
        self.back_s.grid(row=0, column=4, padx=30, pady=20, sticky="e")
    def display_course(self, to_forget, result):
        # Create a new frame to display the search results
        to_forget.place_forget()
        self.result_frame = Frame(root, bg="white",width=500,height=800,highlightbackground='#888',highlightthickness=1)
        self.result_frame.place(x=500,y=0)
    
        # Add labels to display the search result fields
        Label(self.result_frame, text="ID:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=0, column=0, padx=55, pady=30, sticky="w")
        Label(self.result_frame, text="Name:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=1, column=0, padx=55, pady=30, sticky="w")
        Label(self.result_frame, text="Description:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=2, column=0, padx=55, pady=30, sticky="w")
        Label(self.result_frame, text="Number of Students:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=3, column=0, padx=55, pady=30, sticky="w")
        
        # Display the search result values
        Label(self.result_frame, text=result[0], font=("Arial", 14), bg="#f0f0f0").grid(row=0, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[1], font=("Arial", 14), bg="#f0f0f0").grid(row=1, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[2], font=("Arial", 14), bg="#f0f0f0").grid(row=2, column=3, padx=10, pady=5, sticky="e")
        Label(self.result_frame, text=result[3], font=("Arial", 14), bg="#f0f0f0").grid(row=3, column=3, padx=10, pady=5, sticky="e")
        #back button
        self.back_s = Button(self.result_frame, bg='limegreen', text="Search Again", activebackground='red', font=('Comic Sans MS', 20), command=lambda: search(self.result_frame, self.currentTable, self.cur))
        self.back_s.grid(row=0, column=4, padx=30, pady=20, sticky="e")
        
    def check(self,to_forget,table_name,cur):
        cur.execute(f"SELECT * FROM {table_name} WHERE id = {self.ent1in.get()}")
        result = cur.fetchone()
        if result == None:
            messagebox.showerror("Error","ID not found in database")
        else:
            if table_name == 'students':
                self.display_student(to_forget, result) 
            elif table_name == 'instructors':
                self.display_instructor(to_forget, result)
            else: #courses
                self.display_course(to_forget, result)
            
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
        self.search=Button(self.doc_frame,text='SEARCH',bg='white',height=350,width=400,compound=TOP,image=self.search_img,cursor = 'cross', relief = RAISED, overrelief = SUNKEN,fg='sky blue',borderwidth=3,font=('Comic Sans MS',20) , command = lambda: search(self.doc_frame,self.currentTable,self.cur))
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
            
    
               
