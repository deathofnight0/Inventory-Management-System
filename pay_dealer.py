from tkinter import *
import mysql.connector
from datetime import datetime
import tkinter.ttk as ttk
from tkinter.messagebox import *

global root


class pay:
    global root

    def __init__(self, conn, root):
        cursor = conn.cursor()
        d = datetime(1, 1, 1).now()

        def quitfunc():
            a = askquestion(
                title="Quit?", message="Do you really want to quit?")
            if a == 'yes':
                self.root.destroy()
                root.deiconify()

        def callback1(event):
            self.billdt_in.configure(state=NORMAL)
            self.cat_in.configure(state=NORMAL)
            self.model_in.configure(state=NORMAL)
            self.amt_in.configure(state=NORMAL)
            self.billdt_in.delete(0, END)
            self.cat_in.delete(0, END)
            self.model_in.delete(0, END)
            self.amt_in.delete(0, END)
            self.billno_in.set("")
            cursor.execute(
                "select * from purchases where dealer='{}' and cleared='no'".format(self.dealer_in.get()))
            self.rows2 = cursor.fetchall()
            self.blist = []
            for i in range(len(self.rows2)):
                self.blist.append(self.rows2[i][1])
            self.billno_in.configure(values=self.blist)
            self.billdt_in.configure(state=DISABLED)
            self.cat_in.configure(state=DISABLED)
            self.model_in.configure(state=DISABLED)
            self.amt_in.configure(state=DISABLED)

        def callback2(event):
            self.billdt_in.configure(state=NORMAL)
            self.cat_in.configure(state=NORMAL)
            self.model_in.configure(state=NORMAL)
            self.amt_in.configure(state=NORMAL)
            self.pending_in.configure(state=NORMAL)
            self.billdt_in.delete(0, END)
            self.cat_in.delete(0, END)
            self.model_in.delete(0, END)
            self.amt_in.delete(0, END)
            self.pending_in.delete(0,END)
            cursor.execute(
                "select * from purchases where bill_no={}".format(int(self.billno_in.get())))
            self.rows3 = cursor.fetchall()
            self.billdt_in.insert(0, self.rows3[0][2])
            self.cat_in.insert(0, self.rows3[0][4])
            self.model_in.insert(0, self.rows3[0][5])
            self.amt_in.insert(0, self.rows3[0][9])
            self.pending_in.insert(0,self.rows3[0][10])
            print(self.rows3[0][10])
            self.billdt_in.configure(state=DISABLED)
            self.cat_in.configure(state=DISABLED)
            self.model_in.configure(state=DISABLED)
            self.amt_in.configure(state=DISABLED)
            self.pending_in.configure(state=DISABLED)

        def new(self):
            self.paydt_in.configure(state=NORMAL)
            self.billdt_in.configure(state=NORMAL)
            self.cat_in.configure(state=NORMAL)
            self.model_in.configure(state=NORMAL)
            self.amt_in.configure(state=NORMAL)
            self.bal_in.configure(state=NORMAL)
            self.pending_in.configure(state=NORMAL)
            self.dealer_in.set("")
            self.billno_in.set("")
            self.paydt_in.delete(0, END)
            self.billdt_in.delete(0, END)
            self.cat_in.delete(0, END)
            self.model_in.delete(0, END)
            self.amt_in.delete(0, END)
            self.paid_in.delete(0, END)
            self.bal_in.delete(0, END)
            self.pending_in.delete(0,END)
            s = d.strftime('%x')
            l = s.split("/")
            l[2] = '20' + l[2]
            date = '{}-{}-{}'.format(l[2], l[0], l[1])
            self.paydt_in.insert(0, date)
            self.paydt_in.configure(state=DISABLED)
            self.billdt_in.configure(state=DISABLED)
            self.cat_in.configure(state=DISABLED)
            self.model_in.configure(state=DISABLED)
            self.amt_in.configure(state=DISABLED)
            self.bal_in.configure(state=DISABLED)
            self.pending_in.configure(state=DISABLED)
            self.text.configure(text="")

        def save(self):
            if len(self.amt_in.get()) == 0 or len(self.paid_in.get()) == 0:
                self.text.configure("Some fields are empty")
            else:
                if int(self.paid_in.get()) > int(self.pending_in.get()):
                    self.text.configure(text="Amount paid is invalid")
                else:
                    self.bal_in.configure(state=NORMAL)
                    self.bal_in.delete(0, END)
                    self.bal_in.insert(0, int(self.pending_in.get()) - int(self.paid_in.get()))
                    self.bal_in.configure(state=DISABLED)
                    cursor.execute(
                        "update dealers set balance=balance-{} where dealername='{}'".format(int(self.paid_in.get()),
                                                                                             self.dealer_in.get()))
                    conn.commit()
                    cursor.execute("update purchases set pending={} where bill_no={}".format(int(self.bal_in.get()),self.billno_in.get()))
                    if int(self.bal_in.get()) == 0:
                        cursor.execute("update purchases set cleared='yes' where bill_no={}".format(int(self.billno_in.get())))
                        conn.commit()
                        cursor.execute("update pu")
                    s1 = "insert into payments(pay_date,bill_date,bill_no,dealer,amount,paid,balance) values('{}','{}',{},'{}',{},{},{})".format(
                        self.paydt_in.get(), self.billdt_in.get(), int(
                            self.billno_in.get()), self.dealer_in.get(), int(self.amt_in.get()),
                        int(self.paid_in.get()), int(self.bal_in.get()))
                    cursor.execute(s1)
                    conn.commit()
                    self.text.configure(text="Record Saved")

        cursor.execute("select * from dealers")
        self.rows = cursor.fetchall()
        self.dlist = []
        for i in range(len(self.rows)):
            self.dlist.append(self.rows[i][2])
        self.root = Tk()
        self.root.title("Login")
        self.root.geometry("500x600")
        self.root.protocol("WM_DELETE_WINDOW", quitfunc)
        self.frame = Frame(self.root)

        # Creating widgets
        self.title = Label(self.frame, text="Dealer Payment", font=('arial', 20))

        self.paydt = Label(self.frame, text="Payment date", font=('arial', 16))
        self.paydt_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.dealer = Label(self.frame, text="Select Dealer", font=('arial', 16))
        self.dealer_in = ttk.Combobox(self.frame, state='readonly', values=self.dlist,
                                 font=('arial', 12), width=22)
        self.dealer_in.bind("<<ComboboxSelected>>", callback1)

        self.billno = Label(self.frame, text="Select Bill no.", font=('arial', 16))
        self.billno_in = ttk.Combobox(self.frame, state='readonly',
                                 font=('arial', 12), width=22)
        self.billno_in.bind("<<ComboboxSelected>>", callback2)

        self.billdt = Label(self.frame, text="Bill date", font=('arial', 16))
        self.billdt_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.cat = Label(self.frame, text="Category", font=('arial', 16))
        self.cat_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.model = Label(self.frame, text="Model", font=('arial', 16))
        self.model_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.amt = Label(self.frame, text="Bill Amount", font=('arial', 16))
        self.amt_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.pending = Label(self.frame, text="Pending Amount", font=('arial', 16))
        self.pending_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.paid = Label(self.frame, text="Amount Paid", font=('arial', 16))
        self.paid_in = Entry(self.frame, font=('arial', 14))

        self.bal = Label(self.frame, text="Balance", font=('arial', 16))
        self.bal_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.newb = Button(self.frame, text="New", font=('arial', 16), command=lambda:new(self))
        self.submit = Button(self.frame, text="Save", font=('arial', 16), command=lambda:save(self))
        self.text = Label(self.root,text="", font=('arial', 16))

        # Aligning widgets
        x = 1
        y = 0
        for i in range(1, len(self.frame.winfo_children())):
            self.frame.winfo_children()[i].grid_configure(
                row=x, column=y, sticky='w', pady=5)
            if i % 2 == 0:
                x += 1
            y = (y + 1) % 2
        self.frame.grid(row=0, column=0, padx=(65, 0))
        self.title.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        self.newb.grid_configure(padx=(80, 0), pady=(20, 0))
        self.submit.grid_configure(padx=(70, 0), pady=(20, 0))
        self.text.grid_configure(row=1, column=0, pady=(20, 0))
        new(self)
        mainloop()
