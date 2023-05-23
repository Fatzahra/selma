import tkinter
from tkinter import messagebox
import sqlite3 


window = tkinter.Tk()
window.title("Gestion de stock")
window.geometry('500x500')
window.configure(bg='#333333')

#database conn

conn = sqlite3.connect('login.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS login(
    username TEXT,
    password TEXT
)""")
conn.close()


def login():
    
    conn = sqlite3.connect('login.db')
    cur = conn.cursor()
    
    cur.execute("INSERT INTO login (username, password) VALUES('emsi', 1234)")
    conn.commit()
    #conn.close()

    user= 'SELECT * FROM login where username =? and password =? '
    cur.execute(user, [(username_entry.get()), (password_entry.get())])

    result = cur.fetchall()
     #recuperer tout les resultats
    if result:
        messagebox.showinfo("Success", 'Successfully logged in.')
        #window.destroy()
        import Form
        

    else:
        messagebox.showerror("False", 'Wrong Login, please try again.')

frame = tkinter.Frame(bg='white')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Login", bg='white', fg="#0f4d7d", font=("", 30))
username_label = tkinter.Label(
    frame, text="Username", bg='white', fg="#0f4d7d", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Password", bg='white', fg="#0f4d7d", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="white", fg="#0f4d7d", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()



window.mainloop()
