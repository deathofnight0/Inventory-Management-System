from tkinter import *
import mysql.connector
from tkinter.messagebox import *


class password:
    global root

    def __init__(self, conn, cuser, root):
        def quitfunc():
            a = askquestion(
                title="Quit?", message="Do you really want to quit?")
            if a == 'yes':
                self.root.destroy()
                root.deiconify()

        def change(self):
            cursor = conn.cursor()
            cursor.execute(
                "select * from users where uid='{}'".format(cuser.lower()))
            row = cursor.fetchall()
            if self.oldpass_in.get() != row[0][4]:
                self.text.configure(text="Incorrect Old password")
            else:
                if self.newpass_in.get() != self.cfrmpass_in.get():
                    self.text.configure(text="New password dont match")
                else:
                    if len(self.newpass_in.get()) < 7:
                        self.text.configure(text="Enter a string password!")
                    else:
                        cursor.execute("update users set password='{}' where uid='{}'".format(
                            self.newpass_in.get(), cuser))
                        conn.commit()
                        self.text.configure(text="Password has been changed!")

        self.root = Toplevel(root)
        self.root.title("Password")
        self.root.geometry("500x350")
        self.root.protocol("WM_DELETE_WINDOW", quitfunc)
        self.frame = Frame(self.root)

        # Creating widgets
        self.title = Label(
            self.frame, text="Change Password", font=('arial', 20))

        self.oldpass = Label(
            self.frame, text="Old Password", font=('arial', 16))
        self.oldpass_in = Entry(self.frame, font=('arial', 14), show='*')

        self.newpass = Label(
            self.frame, text="New Password", font=('arial', 16))
        self.newpass_in = Entry(self.frame, font=('arial', 14), show='*')

        self.cfrmpass = Label(
            self.frame, text="Confirm password", font=('arial', 16))
        self.cfrmpass_in = Entry(self.frame, font=('arial', 14), show='*')

        self.submit = Button(self.root, text="Save changes", font=(
            'arial', 16), command=lambda: change(self))
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
        self.frame.grid(row=0, column=0, padx=(40, 0))
        self.title.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        self.submit.grid_configure(row=1, column=0, columnspan=2,
                                   pady=(20, 0), padx=(50, 0))
        self.text.grid(row=2, column=0, columnspan=2, padx=(70, 0))
        self.newpass.grid_configure(pady=(20, 0))
        self.newpass_in.grid_configure(pady=(20, 0))
        mainloop()
