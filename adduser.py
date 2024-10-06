from tkinter import *
import tkinter.ttk as ttk
import mysql.connector
from tkinter.messagebox import *

count = 0


class createuser:
    global root

    def __init__(self, conn, root):
        def quitfunc():
            a = askquestion(
                title="Quit?", message="Do you really want to quit?")
            if a == 'yes':
                self.root.destroy()
                root.deiconify()

        def createuser(self):
            if len(self.name_in.get()) == 0 or len(self.uid_in.get()) == 0 or len(self.pswd_in.get()) == 0 or len(
                self.cpswd_in.get()) == 0 or self.ac.get() not in [1, 2] or len(
                    self.mob_in.get()) == 0 or len(self.email_in.get()) == 0 or '@' not in self.email_in.get():
                self.text.configure(text="Some fields are empty")
            else:
                if len(self.mob_in.get())!=10:
                    self.text.configure(text="Invalid Mobile number")
                else:
                    if not self.name_in.get().isalpha() or not self.uid_in.get().isalnum():
                        self.text.configure(text="Enter appropriate name/username")
                    else:
                        if self.pswd_in.get() != self.cpswd_in.get():
                            self.text.configure(text="The passwords don't match")
                        else:
                            if len(self.pswd_in.get()) < 7:
                                self.text.configure(text="Enter a strong password")
                            else:
                                type = 'admin' if self.ac.get() == 1 else "user"
                                s1 = "insert into users values({},'{}','{}','{}','{}','{}','{}')".format(
                                    count, self.name_in.get(), self.uid_in.get(), self.email_in.get(), self.pswd_in.get(), self.mob_in.get(), type)
                                cursor = conn.cursor()
                                cursor.execute(s1)
                                conn.commit()
                                self.text.configure(text="Account Created!")

        self.root = Toplevel(root)
        self.root.title("Create Account")
        self.root.geometry("450x400")
        self.root.protocol("WM_DELETE_WINDOW", quitfunc)
        self.frame = Frame(self.root)

        # Creating widgets
        self.title = Label(self.frame, text="Create User", font=('arial', 20))
        self.name = Label(self.frame, text="Name", font=('arial', 16))
        self.name_in = Entry(self.frame, font=('arial', 14), width=18)

        self.uid = Label(self.frame, text="Username", font=('arial', 16))
        self.uid_in = Entry(self.frame, font=('arial', 14), width=18)

        self.email = Label(self.frame, text="Email", font=('arial', 16))
        self.email_in = Entry(self.frame, font=('arial', 12), width=22)

        self.pswd = Label(self.frame, text="Password", font=('arial', 16))
        self.pswd_in = Entry(self.frame, font=(
            'arial', 14), show="*", width=18)

        self.cpswd = Label(self.frame, text="Confirm Pass", font=('arial', 16))
        self.cpswd_in = Entry(self.frame, font=(
            'arial', 14), show="*", width=18)

        self.mob = Label(self.frame, text="Mobile no.", font=('arial', 16))
        self.mob_in = Entry(self.frame, font=('arial', 14), width=18)

        self.gender = Label(
            self.frame, text="Account type", font=('arial', 16))
        self.frame2 = Frame(self.frame)
        self.ac = IntVar()
        self.rb1 = Radiobutton(self.frame2, text="Admin",
                               variable=self.ac, value=1)
        self.rb2 = Radiobutton(self.frame2, text="User",
                               variable=self.ac, value=2)

        self.submit = Button(self.root, text="Submit",
                             font=('arial', 16), command=lambda: createuser(self))
        self.text = Label(self.root, text="", font=('arial', 16))
        # Aligning the widgets
        self.title.grid(row=0, column=0, columnspan=3)
        self.rb1.grid(row=0, column=0, padx=(10, 0))
        self.rb2.grid(row=0, column=1, padx=(50, 0))
        self.frame2.grid(row=0, column=0)
        self.frame.grid(row=1, column=0, columnspan=3, padx=(60, 0))
        x = 1
        y = 0
        for i in range(1, len(self.frame.winfo_children())):
            self.frame.winfo_children()[i].grid_configure(
                row=x, column=y, sticky='w', pady=4)
            if i % 2 == 0:
                x += 1
            y = (y + 1) % 2
        self.submit.grid(row=2, column=0, padx=(160, 0), pady=(10, 0))
        self.text.grid(row=3, column=0, columnspan=3,
                       padx=(60, 0), pady=(10, 0))
        mainloop()
