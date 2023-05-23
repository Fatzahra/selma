# selma
import tkinter
from tkinter import messagebox
import sqlite3 

# Create the main window
window = tkinter.Tk()
window.title("Gestion de stock")
window.geometry('500x500')
window.configure(bg='#333333')

# Establish a database connection and create the "login" table if it doesn't exist
conn = sqlite3.connect('login.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS login(
    username TEXT,
    password TEXT
)""")
conn.close()

# Function to handle the login process
def login():
    # Open the database connection
    conn = sqlite3.connect('login.db')
    cur = conn.cursor()
    
    # Insert a sample login record into the "login" table (for testing purposes)
    cur.execute("INSERT INTO login (username, password) VALUES('emsi', 1234)")
    conn.commit()

    # Retrieve the entered username and password and check if they match any records in the "login" table
    user_query = 'SELECT * FROM login where username =? and password =? '
    cur.execute(user_query, [(username_entry.get()), (password_entry.get())])

    result = cur.fetchall() # Retrieve all the results

    if result:
        messagebox.showinfo("Success", 'Successfully logged in.')
        # Perform actions after successful login (e.g., open the main application form)
    else:
        messagebox.showerror("False", 'Wrong Login, please try again.')

    # Close the database connection
    conn.close()

# Create a frame widget with a white background
frame = tkinter.Frame(bg='white')

# Create the widgets
login_label = tkinter.Label(frame, text="Login", bg='white', fg="#0f4d7d", font=("", 30))
username_label = tkinter.Label(frame, text="Username", bg='white', fg="#0f4d7d", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(frame, text="Password", bg='white', fg="#0f4d7d", font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login", bg="white", fg="#0f4d7d", font=("Arial", 16), command=login)

# Place the widgets in the frame using the grid layout
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

# Pack the frame to display it in the window
frame.pack()

# Start the main event loop
window.mainloop()
from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk, messagebox
import sqlite3

# GUI Designing

class CRUDClass:
    def __init__(self, root):
        self.root=root
        self.root.geometry("830x370+200+130")
        self.root.title("Gestion de stock")
        self.root.config(bg="white")

        # All variables

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_nom=StringVar()
        self.var_prix=StringVar()
        self.var_Quantité=StringVar()
        self.var_Date=StringVar()

        # Label
        lbl_title=Label(self.root, text="stock", font=("Arial", 20, "bold"), fg="#0f4d7d").place(x=15, y=20, width=800,height=40)
        lbl_search=Label(self.root,text="SearchByID", bg="white", font=("Arial",15)).place(x=390, y=80)
        lbl_Nom=Label(self.root, text="Nom produit", font=("Arial", 15), bg="white").place(x=50,y=80)
        lb1_Prix=Label(self.root, text="Prix", font=("Arial", 15), bg="white").place(x=50, y=120)
        lbl_Quantité=Label(self.root, text="Quantité", font=("Arial", 15), bg="white").place(x=50, y=160)
        lbl_Date=Label(self.root, text="Date entrée ", font=("Arial", 15), bg="white").place(x=50, y=200)
        
        # Textbox
        txt_search=Entry(self.root, textvariable=self.var_searchtxt, font=("Arial",15), bg="white").place(x=505, y=80, width=160)
        txt_Nom=Entry(self.root, textvariable=self.var_nom, font=("Arial",15), bg="white").place(x=180, y=80, width=180)
        txt_Prix=Entry(self.root, textvariable=self.var_prix, font=("Arial",15), bg="white").place(x=180,y=120, width=180)
        txt_Quantité=Entry(self.root, textvariable=self.var_Quantité, show="*", font=("Arial",15), bg="white").place(x=180, y=160, width=180)
        txt_Date=Entry(self.root, textvariable=self.var_Date, font=("Arial", 15), bg="white").place(x=180, y=200, width=180)
        
        # Buttons
        btn_search=Button(self.root, text="Search", font=("Times New Roman",15), bg="#4caf50",fg="white",cursor="hand2").place(x=700, y=79,width=100,height=30)  # Button for searching
        btn_add=Button(self.root,text="Save",command=self.Save, font=("Times New Roman", 15), bg="#2196f3",fg="white", cursor="hand2").place(x=180, y=250,width=110,height=30)  # Button for saving data
        btn_update=Button(self.root, text="Update", font=("Times New Roman",15), bg="#4caf50",fg="white", cursor="hand2").place(x=300,y=250,width=110,height=30)  # Button for updating data
        btn_delete=Button(self.root, text="Delete", font=("Times New Roman",15), bg="#f44336",fg="white", cursor="hand2").place(x=180,  # Button for deleting data
  #User_Details
        emp_frame=Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=420, y=120,width=380,height=215)
        #Scrollbar
        scrolly=Scrollbar (emp_frame, orient=VERTICAL)
        scrollx=Scrollbar(emp_frame, orient=HORIZONTAL)
        #CreatingTableView
        self.supplierTable=ttk.Treeview(emp_frame, columns=("Nom", "prix", "Quantité","Date"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.supplierTable.heading("Nom",text="Nom")
        self.supplierTable.heading("prix", text="prix")
        self.supplierTable.heading("Quantité", text="Quantité")
        self.supplierTable.heading("Date",text="Date")
        self.supplierTable["show"]="headings"
        self.supplierTable.column("Nom",width=50)
        self.supplierTable.column("prix",width=100)
        self.supplierTable.column("Quantité",width=100)
        self.supplierTable.column("Date",width=100)

        self.supplierTable.pack(fill=BOTH, expand=1)
        
        self.show()

        #DatabaseConnection

    
    con = sqlite3.connect(database='PRODUIT.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS produit (
        nom VARCHAR(100),
        prix VARCHAR(100), 
        quantité VARCHAR(100), 
        date VARC(100)
        )""")
        


        #Save
    def Save(self):
        connection
        try:
            if self.var_Nom.get()=="":
                messagebox.showerror("Error", "Name must be required",parent=self.root)
            else:
                cur.execute("Select * from Login where Nom=?", (self.var_nom.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "Nom already exits, Try different",parent=self.root)
                else:
                    cur.execute("Insert into login (Nom, prix, quantité, date) values (?, ?, ?, ?)",(
                                        self.var_nom.get(),
                                        self.var_prix.get(),
                                        self.var_Quantité.get(),
                                        self.var_Date.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Sucess", "New product Added Sucessfully", parent=self.root)
                    self.clear()
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent=self.root) # remplacer les valeurs
            

#Showdata
    def show(self):
        connection
        try:
            cur.execute("select * from Login")
            rows=cur.fetchall()
            self.supplierTable.delete(self.supplierTable.get_children()) # supprimer toutes les lignes présentes dans le widget de tableau supplierTable. Cela permet de nettoyer le tableau en vue d'ajouter de nouvelles données ou de mettre à jour les données affichées.
            for row in rows:
                self.supplierTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
#GetData
    def get_data(self):
            f=self.supplierTable.focus()
            content=self.supplierTable.item(f)
            row=content['values']
            # print (row)
            self.var_nom.set(row[0]),
            self.var_prix.set(row[1]),
            self.var_Quantité.set(row [2]),
            self.var_Date.set(row[3])

# Update
    def update(self):
        connection
        try:
            if self.var_loginId.get()=="":
                messagebox.showerror("Error", "Id must be required",parent=self.root)
            else:
                cur.execute("Select * from Login where Nom=?", (self.var_nom.get(), ))
                row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error", "Invalid nom",parent=self.root)
            else:
                cur.execute("Update Login set Nom=?, prix=?, quantité=? where date=?",(
                                    self.var_nom.get(),
                                    self.var_prix.get(),
                                    self.var_Quantité.get(),
                                    self.var_Date.get()
                ))
                con.commit()
                messagebox.showinfo("Sucess", "product Updated Sucessfully" ,parent=self.root)
                self.clear()
                self.show()                                                                                                                                                                                                                                                                                                                       
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)

#Delete
    def delete(self):
        connection
        try:
            if self.var_nom.get()=="":
                messagebox.showerror("Error", "Name must be required",parent=self.root)
            else:
                cur.execute("Select * from Login where Nom=?", (self.var_nom.get(), ))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid ID",parent=self.root)
                else:
                    cosM=messagebox.askyesno ("Confirm", "Do you want to delete",parent=self.root)
                    if cosM==True:
                        cur.execute("delete from Login where Nom=?", (self.var_loginId.get(), ))
                        con.commit()
                        messagebox.showinfo("Delete", "product Delete Successfully",parent=self.root)
                        self.clear()
                        self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)
#ClearForSQLite
    def clear(self):
        self.var_nom.set(""),
        self.var_prix.set(""),
        self.var_Quantité.set(""),
        self.var_Date.set(""),
        self.var_searchtxt.set("")
        self.show()
#Search
    def search(self):
        connection
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Name should be required.",parent=self.root)
            else:
                cur.execute("select * from login where Nom=?", (self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)


#DatabaseConnection
con = sqlite3.connect(database='PRODUIT.db')
cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS produit (
        nom VARCHAR(100),
        prix VARCHAR(100), 
        quantité VARCHAR(100), 
        date VARC(100)
        )""")

def connection ():


    con.commit()
    connection()


    

    #MainMethod

if __name__ =="__main__":
    root=Tk()
    obj=CRUDClass(root)
    root.mainloop()
