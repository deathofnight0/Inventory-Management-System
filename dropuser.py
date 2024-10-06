from tkinter import *
from tkinter.messagebox import *
import mysql.connector

global root

class drop:
    global root

    def __init__(self, conn, root):
        def quitfunc():
            a = askquestion(
                title="Quit?", message="Do you really want to quit?")
            if a == 'yes':
                self.root.destroy()
                root.deiconify()

        def find(self):
            cursor = conn.cursor()
            cursor.execute(
                "select * from users where uid='{}'".format(self.uid_in.get().lower()))
            row = cursor.fetchall()
            if self.uid_in.get() == 'admin':
                self.text.configure(text="Can't delete admin account!")
            else:
                if row == []:
                    self.text.configure(text="No such user exists!")
                else:
                    self.text.configure(text="Found!")
                    self.name_in.configure(state=NORMAL)
                    self.mail_in.configure(state=NORMAL)
                    self.mob_in.configure(state=NORMAL)
                    self.name_in.delete(0, END)
                    self.mail_in.delete(0, END)
                    self.mob_in.delete(0, END)
                    self.name_in.insert(0, row[0][1])
                    self.mail_in.insert(0, row[0][3])
                    self.mob_in.insert(0, row[0][5])
                    self.name_in.configure(state=DISABLED)
                    self.mail_in.configure(state=DISABLED)
                    self.mob_in.configure(state=DISABLED)

        def ask(self):
            a = askquestion(title="Deleting!",
                            message="Are you sure you want to delete this user?")
            if a == 'yes':
                cursor = conn.cursor()
                cursor.execute(
                    "delete from users where uid='{}'".format(self.uid_in.get()))
                conn.commit()
                self.text.configure(text="User account has been deleted")

        self.root = Toplevel(root)
        self.root.title("Drop account")
        self.root.geometry("500x350")
        self.root.protocol("WM_DELETE_WINDOW", quitfunc)
        self.frame = Frame(self.root)

        # Creating widgets
        self.title = Label(self.frame, text="Delete User", font=('arial', 20))

        self.uid = Label(self.frame, text="User Id", font=('arial', 16))
        self.uid_in = Entry(self.frame, font=('arial', 14))

        self.name = Label(self.frame, text="Name", font=('arial', 16))
        self.name_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.mail = Label(self.frame, text="Email Id", font=('arial', 16))
        self.mail_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.mob = Label(self.frame, text="Mobile no.", font=('arial', 16))
        self.mob_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.findb = Button(self.frame, text="Find", font=(
            'arial', 16), command=lambda: find(self))
        self.submit = Button(self.frame, text="Drop", font=(
            'arial', 16), command=lambda: ask(self))
        self.text = Label(self.root, text="", font=('arial', 16))

        # Aligning widgets
        x = 1
        y = 0
        for i in range(1, len(self.frame.winfo_children())):
            self.frame.winfo_children()[i].grid_configure(
                row=x, column=y, sticky='w', pady=5)
            if i % 2 == 0:
                x += 1
            y = (y + 1) % 2
        self.frame.grid(row=0, column=0, padx=(80, 0))
        self.title.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        self.findb.grid_configure(pady=20, padx=(70, 0))
        self.submit.grid_configure(pady=20, padx=(40, 0))
        self.text.grid(row=1, column=0, columnspan=2, padx=(70, 0))
        mainloop()
