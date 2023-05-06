from tkinter import *
from root import *
from images import *
from tkinter import messagebox

def search(frame,table,cur):
    Search(frame,table,cur)

class Search:
    def __init__(self,start_frame,table,cur):
        start_frame.place_forget()
        self.frameSearch = Frame(root, bg="white",width=600,height=900,highlightbackground='#888',highlightthickness=1)
        self.frameSearch.place(x=400,y=0)
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
        self.result_frame = Frame(root, bg="white",width=600,height=900,highlightbackground='#888',highlightthickness=1)
        self.result_frame.place(x=400,y=0,width=600, relheight=1, anchor="nw")
    
        # Add labels to display the search result fields
        Label(self.result_frame, text="ID:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=0, column=0, padx=50, pady=25, sticky="w")
        Label(self.result_frame, text="First Name:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=1, column=0, padx=50, pady=25, sticky="w")
        Label(self.result_frame, text="Last Name:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=2, column=0, padx=50, pady=25, sticky="w")
        Label(self.result_frame, text="Phone:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=3, column=0, padx=50, pady=25, sticky="w")
        Label(self.result_frame, text="E-mail:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=4, column=0, padx=50, pady=25, sticky="w")
        Label(self.result_frame, text="Address:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=5, column=0, padx=50, pady=25, sticky="w")
        Label(self.result_frame, text="Gender:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=6, column=0, padx=50, pady=25, sticky="w")
        Label(self.result_frame, text="Date of Birth:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=7, column=0, padx=50, pady=25, sticky="w")
        Label(self.result_frame, text="Course ID:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=8, column=0, padx=50, pady=25, sticky="w")

        # Display the search result values
        Label(self.result_frame, text=result[0], font=("Arial", 14), bg="#f0f0f0").grid(row=0, column=3, padx=20, pady=5, sticky="e")
        Label(self.result_frame, text=result[1], font=("Arial", 14), bg="#f0f0f0").grid(row=1, column=3, padx=20, pady=5, sticky="e")
        Label(self.result_frame, text=result[2], font=("Arial", 14), bg="#f0f0f0").grid(row=2, column=3, padx=20, pady=5, sticky="e")
        Label(self.result_frame, text=result[3], font=("Arial", 14), bg="#f0f0f0").grid(row=3, column=3, padx=20, pady=5, sticky="e")
        Label(self.result_frame, text=result[4], font=("Arial", 14), bg="#f0f0f0").grid(row=4, column=3, padx=20, pady=5, sticky="e")
        Label(self.result_frame, text=result[5], font=("Arial", 14), bg="#f0f0f0").grid(row=5, column=3, padx=20, pady=5, sticky="e")
        Label(self.result_frame, text=result[6], font=("Arial", 14), bg="#f0f0f0").grid(row=6, column=3, padx=20, pady=5, sticky="e")
        Label(self.result_frame, text=result[7], font=("Arial", 14), bg="#f0f0f0").grid(row=7, column=3, padx=20, pady=5, sticky="e")
        Label(self.result_frame, text=result[8], font=("Arial", 14), bg="#f0f0f0").grid(row=8, column=3, padx=20, pady=5, sticky="e")
        #search again button
        self.back_s = Button(self.result_frame, bg='limegreen', text="Search Again", activebackground='red', font=('Comic Sans MS', 20), command=lambda: search(self.result_frame, self.currentTable, self.cur))
        self.back_s.grid(row=9, column=0, padx=30, pady=20, sticky="e")
        
    def display_instructor(self, to_forget, result):
        # Create a new frame to display the search results
        to_forget.place_forget()
        self.result_frame = Frame(root, bg="white",width=600,height=900,highlightbackground='#888',highlightthickness=1)
        self.result_frame.place(x=400,y=0,width=600, relheight=1, anchor="nw")
    
       # Add labels to display the search result fields
        Label(self.result_frame, text="ID:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=0, column=0, padx=50, pady=25, sticky="w")
        Label(self.result_frame, text="First Name:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=1, column=0, padx=50, pady=25, sticky="w")
        Label(self.result_frame, text="Last Name:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=2, column=0, padx=50, pady=25, sticky="w")
        Label(self.result_frame, text="Phone:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=3, column=0, padx=50, pady=25, sticky="w")
        Label(self.result_frame, text="E-mail:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=4, column=0, padx=50, pady=25, sticky="w")
        Label(self.result_frame, text="Address:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=5, column=0, padx=50, pady=25, sticky="w")
        Label(self.result_frame, text="Gender:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=6, column=0, padx=50, pady=25, sticky="w")
        Label(self.result_frame, text="Date of Birth:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=7, column=0, padx=50, pady=25, sticky="w")
        Label(self.result_frame, text="Course ID:", font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0").grid(row=8, column=0, padx=50, pady=25, sticky="w")

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
        self.back_s.grid(row=9, column=0, padx=30, pady=20, sticky="e")
    def display_course(self, to_forget, result):
        # Create a new frame to display the search results
        to_forget.place_forget()
        self.result_frame = Frame(root, bg="white", width=600, highlightbackground='#888', highlightthickness=1)
        self.result_frame.place(x=400, y=0, width=600, relheight=1, anchor="nw")
        
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
        self.back_s.grid(row=4, column=0, padx=30, pady=20, sticky="e")
        
        # Set the row containing the result_frame to expand vertically
        root.rowconfigure(0, weight=1)

        
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
            
            
