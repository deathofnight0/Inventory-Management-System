from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter.messagebox import *

global root


class dealer:
    global root

    def __init__(self, conn, root):
        cursor = conn.cursor()

        def quitfunc():
            a = askquestion(
                title="Quit?", message="Do you really want to quit?")
            if a == 'yes':
                self.root.destroy()
                root.deiconify()

        def new(self):
            self.saveb.configure(state=NORMAL)
            self.did_in.configure(state=NORMAL)
            self.dbal_in.configure(state=NORMAL)
            self.text.configure(text="")

            self.dname_in.delete(0, END)
            self.did_in.delete(0, END)
            self.dadd_in.delete(0, END)
            self.dmob_in.delete(0, END)
            self.dbal_in.delete(0, END)
            self.modifyb.configure(state=DISABLED)
            self.deleteb.configure(state=DISABLED)

        def delete(self):

            a = messagebox.askquestion(
                "askquestion", "Are you sure you want to delete dealer data?")
            if a == 'yes':
                s2 = "delete from dealers where dealerid='{}'".format(
                    self.did_in.get())
                cursor.execute(s2)
                conn.commit()
                self.did_in.configure(state=NORMAL)
                self.dbal_in.configure(state=NORMAL)
                self.dname_in.delete(0, END)
                self.did_in.delete(0, END)
                self.dadd_in.delete(0, END)
                self.dmob_in.delete(0, END)
                self.dbal_in.delete(0, END)
                self.text.configure(text="Data has been deleted")
                self.modifyb.configure(state=DISABLED)
                self.deleteb.configure(state=DISABLED)

        def modify(self):
            print("hello")
            if self.dname_in.get().isalpha() == False:
                self.text.configure(text="Enter valid name!")
            else:
                if len(self.dmob_in.get()) != 10:
                    self.text.configure(text="Mobile number is invalid")
                else:
                    s1 = "update dealers set  dealername='{}',address='{}',mobile={} where dealerid='{}' ".format(
                        self.dname_in.get(),
                        self.dadd_in.get(),
                        self.dmob_in.get(),
                        self.did_in.get())
                    cursor.execute(s1)
                    conn.commit()
                    self.text.configure(text="Data is Updated")
                    self.modifyb.configure(state=DISABLED)
                    self.deleteb.configure(state=DISABLED)

        def find(self):
            s4 = "select * from dealers where dealerid='{}' or dealername='{}'".format(
                self.did_in.get(), self.dname_in.get())
            cursor.execute(s4)
            rows = cursor.fetchall()
            if rows == []:
                self.text.configure(text="Data not found")
            else:
                self.saveb.configure(state=DISABLED)
                self.modifyb.configure(state=NORMAL)
                self.deleteb.configure(state=NORMAL)
                self.dbal_in.configure(state=NORMAL)
                self.did_in.delete(0, END)
                self.dname_in.delete(0, END)
                self.dadd_in.delete(0, END)
                self.dmob_in.delete(0, END)
                self.dbal_in.delete(0, END)
                self.did_in.insert(0, rows[0][1])
                self.dname_in.insert(0, rows[0][2])
                self.dadd_in.insert(0, rows[0][3])
                self.dmob_in.insert(0, rows[0][4])
                self.dbal_in.insert(0, rows[0][5])
                self.did_in.configure(state=DISABLED)
                self.dbal_in.configure(state=DISABLED)
                self.text.configure(text="Data found")

        def save(self):
            if len(self.did_in.get()) == 0 or len(self.dname_in.get()) == 0 or len(self.dadd_in.get()) == 0 or len(
                    self.dmob_in.get()) == 0 or len(
                    self.dbal_in.get()) == 0:
                self.text.configure(text="Some fields are empty!")
            else:
                cursor.execute("select dealerid from dealers")
                rows1 = cursor.fetchall()
                for (i,) in rows1:
                    if i == self.did_in.get():
                        self.text.configure(text="Dealer with same id exists")
                        break
                else:
                    if self.dname_in.get().isalpha() == False:
                        self.text.configure(text="Enter valid name!")
                    else:
                        if len(self.dmob_in.get()) != 10:
                            self.text.configure(
                                text="Mobile number is invalid")
                        else:
                            s3 = "insert into dealers(dealerid,dealername,address,mobile,balance) values('{}','{}','{}','{}',{})".format(
                                self.did_in.get(), self.dname_in.get(), self.dadd_in.get(), self.dmob_in.get(),
                                self.dbal_in.get())
                            print(s3)
                            cursor.execute(s3)
                            conn.commit()
                            self.saveb.configure(state=DISABLED)
                            self.text.configure(text="Data has been added")

        self.root = Toplevel(root)
        self.root.title("Dealers")
        self.root.geometry("500x350")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", quitfunc)
        self.frame = Frame(self.root)
        self.frame2 = Frame(self.root)
        # Creating widgets
        self.title = Label(
            self.frame, text="Manage Dealers", font=('arial', 20))
        self.did = Label(self.frame, text="Dealer Id", font=('arial', 16))
        self.did_in = Entry(self.frame, font=('arial', 14))

        self.dname = Label(self.frame, text="Dealer Name", font=('arial', 16))
        self.dname_in = Entry(self.frame, font=('arial', 14))

        self.dadd = Label(self.frame, text="Address", font=('arial', 16))
        self.dadd_in = Entry(self.frame, font=('arial', 14))

        self.dmob = Label(self.frame, text="Mobile no", font=('arial', 16))
        self.dmob_in = Entry(self.frame, font=('arial', 14))

        self.dbal = Label(self.frame, text="Balance", font=('arial', 16))
        self.dbal_in = Entry(self.frame, font=('arial', 14))

        self.newb = Button(self.frame2, text="New", font=(
            'arial'), command=lambda: new(self))
        self.saveb = Button(self.frame2, text="Save", font=(
            'arial'), command=lambda: save(self))
        self.modifyb = Button(self.frame2, text="Modify", font=(
            'arial'), state=DISABLED, command=lambda: modify(self))
        self.deleteb = Button(self.frame2, text="Delete", font=(
            'arial'), state=DISABLED, command=lambda: delete(self))
        self.findb = Button(self.frame2, text="Find", font=(
            'arial'), command=lambda: find(self))
        self.text = Label(self.root, font=('arial', 16))
        # Aligning widgets
        x = 1
        y = 0
        for i in range(1, len(self.frame.winfo_children())):
            self.frame.winfo_children()[i].grid_configure(
                row=x, column=y, sticky='w', pady=3)
            if i % 2 == 0:
                x += 1
            y = (y + 1) % 2
        for i in range(len(self.frame2.winfo_children())):
            self.frame2.winfo_children()[i].grid(
                row=0, column=i, padx=6)
        self.frame.grid(row=0, column=0, padx=(70, 0))
        self.frame2.grid(row=1, column=0, columnspan=3,
                         pady=(20, 0), padx=(60, 0))
        self.title.grid(row=0, column=0, columnspan=2)
        self.text.grid(row=2, column=0, columnspan=3,
                       pady=(20, 0), padx=(40, 0))
        mainloop()
