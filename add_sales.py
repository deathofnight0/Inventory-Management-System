from tkinter import *
import mysql.connector
from tkinter import ttk
from datetime import datetime
from tkinter.messagebox import *


class sale:
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

        def calcamt(event):
            if self.qty_in.get().isnumeric() == False:
                self.text.configure(text="Enter valid quantity")
            else:
                self.tamt_in.configure(state=NORMAL)
                amount = int(self.qty_in.get()) * int(self.mrp_in.get())
                self.tamt_in.delete(0, END)
                self.tamt_in.insert(0, amount)
                self.tamt_in.configure(state=DISABLED)

        def callback1(event):
            self.modellist.set("")
            self.mrp_in.configure(state=NORMAL)
            self.mrp_in.delete(0, END)
            self.mrp_in.configure(state=DISABLED)
            c = self.catlist.current()
            if c == 0:
                m = 'TV'
            elif c == 1:
                m = 'Smartphone'
            elif c == 2:
                m = 'Accessories'
            elif c == 3:
                m = 'Refrigerator'
            elif c == 4:
                m = 'AC'
            elif c == 5:
                m = 'Washing Machine'

            mlist = [self.rows[i][2]
                     for i in range(len(self.rows)) if self.rows[i][1] == m]
            self.modellist.configure(values=mlist)

        def callback2(event):
            model = self.modellist.get()
            for i in range(len(self.rows)):
                if self.rows[i][2] == model:
                    emrp = self.rows[i][3]
            self.mrp_in.configure(state=NORMAL)
            self.mrp_in.delete(0, END)
            self.mrp_in.insert(0, emrp)
            self.mrp_in.configure(state=DISABLED)

        def new(self):
            cursor.execute("select * from sales")
            rows2 = cursor.fetchall()
            self.billdt_in.configure(state=NORMAL)
            self.billnum_in.configure(state=NORMAL)
            self.mrp_in.configure(state=NORMAL)
            self.tamt_in.configure(state=NORMAL)
            self.bal_in.configure(state=NORMAL)
            self.billnum_in.delete(0, END)
            self.billdt_in.delete(0, END)
            self.catlist.set("")
            self.modellist.set("")
            self.mrp_in.delete(0, END)
            self.cname_in.delete(0, END)
            self.cadd_in.delete(0, END)
            self.cmob_in.delete(0, END)
            self.qty_in.delete(0, END)
            self.tamt_in.delete(0, END)
            self.paid_in.delete(0, END)
            self.bal_in.delete(0, END)
            self.text.configure(text="")
            s = d.strftime('%x')
            l = s.split("/")
            l[2] = '20' + l[2]
            date = '{}-{}-{}'.format(l[2], l[0], l[1])
            self.billdt_in.insert(0, date)
            self.billnum_in.insert(0, len(rows2) + 1)
            self.billdt_in.configure(state=DISABLED)
            self.billnum_in.configure(state=DISABLED)
            self.mrp_in.configure(state=DISABLED)
            self.tamt_in.configure(state=DISABLED)
            self.bal_in.configure(state=DISABLED)

        def save(self):
            if len(self.mrp_in.get()) == 0 or len(self.cname_in.get()) == 0 or len(self.cadd_in.get()) == 0 or len(
                    self.cmob_in.get()) == 0 or len(
                    self.qty_in.get()) == 0 or len(self.paid_in.get()) == 0:
                self.text.configure(text="Some fields are empty")
            else:
                if self.cname_in.get().isalpha() == False:
                    self.text.configure(text="Enter valid Customer name!")
                else:
                    if len(self.cmob_in.get()) != 10 or self.cmob_in.get().isalpha():
                        self.text.configure(text="Enter valid mobile number!")
                    else:
                        if self.paid_in.get().isnumeric() == False:
                            self.text.configure(text="Enter valid paid amount")
                        else:
                            self.bal_in.configure(state=NORMAL)
                            balance = int(self.tamt_in.get()) - \
                                int(self.paid_in.get())
                            self.bal_in.insert(0, balance)
                            self.bal_in.configure(state=DISABLED)
                            cursor.execute(
                                "update stock set quantity=quantity-{} where model='{}'".format(int(self.qty_in.get()),
                                                                                                self.modellist.get()))
                            conn.commit()
                            s1 = "insert into sales(bill_no,bill_date,category,model,mrp,customer_name,customer_address,customer_mobile,quantity,amount,paid,balance) values({},'{}','{}','{}',{},'{}','{}','{}',{},{},{},{}) ".format(
                                int(self.billnum_in.get()), self.billdt_in.get(
                                ), self.catlist.get(), self.modellist.get(), self.mrp_in.get(),
                                self.cname_in.get(), self.cadd_in.get(), self.cmob_in.get(), int(self.qty_in.get()),
                                int(self.tamt_in.get()), int(self.paid_in.get()), int(self.bal_in.get()))
                            cursor.execute(s1)
                            conn.commit()
                            self.text.configure(text="Record Saved")

        cursor.execute("select * from stock")
        self.rows = cursor.fetchall()
        self.clist = []
        for i in range(len(self.rows)):
            if self.rows[i][1] not in self.clist:
                self.clist.append(self.rows[i][1])

        self.root = Toplevel(root)
        self.root.title("Login")
        self.root.geometry("500x650")
        self.root.protocol("WM_DELETE_WINDOW", quitfunc)
        self.frame = Frame(self.root)
        self.list = [1, 2, 3, 4, 5, 6, 7, 8]

        ############### ----Creating widgets----######################
        self.title = Label(self.frame, text="Sales", font=('arial', 20))

        self.billnum = Label(self.frame, text="Bill no.", font=('arial', 16))
        self.billnum_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.billdt = Label(self.frame, text="Bill date", font=('arial', 16))
        self.billdt_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.cat = Label(self.frame, text="Category", font=('arial', 16))
        self.catlist = ttk.Combobox(self.frame, state='readonly', values=self.clist,
                                    font=('arial', 12), width=22)
        self.catlist.bind("<<ComboboxSelected>>", callback1)

        self.model = Label(self.frame, text="Model", font=('arial', 16))
        self.modellist = ttk.Combobox(self.frame, state='readonly',
                                      font=('arial', 12), width=22)
        self.modellist.bind("<<ComboboxSelected>>", callback2)

        self.mrp = Label(self.frame, text="MRP", font=('arial', 16))
        self.mrp_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.cname = Label(self.frame, text="Customer name",
                           font=('arial', 16))
        self.cname_in = Entry(self.frame, font=('arial', 14))

        self.cadd = Label(self.frame, text="Address", font=('arial', 16))
        self.cadd_in = Entry(self.frame, font=('arial', 14))

        self.cmob = Label(self.frame, text="Mobile no.", font=('arial', 16))
        self.cmob_in = Entry(self.frame, font=('arial', 14))

        self.qty = Label(self.frame, text="Quantity", font=('arial', 16))
        self.qty_in = Entry(self.frame, font=('arial', 14))
        self.qty_in.bind("<FocusOut>", calcamt)

        self.tamt = Label(self.frame, text="Total amount", font=('arial', 16))
        self.tamt_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.paid = Label(self.frame, text="Amount paid", font=('arial', 16))
        self.paid_in = Entry(self.frame, font=('arial', 14))

        self.bal = Label(self.frame, text="Balance", font=('arial', 16))
        self.bal_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.newb = Button(self.frame, text="New", font=(
            'arial', 16), command=lambda: new(self))
        self.submit = Button(self.frame, text="Save", font=(
            'arial', 16), command=lambda: save(self))
        self.text = Label(self.root, text="", font=('arial', 16))

        ############### ----Aligning widgets----######################
        x = 1
        y = 0
        for i in range(1, len(self.frame.winfo_children())):
            self.frame.winfo_children()[i].grid_configure(
                row=x, column=y, sticky='w', pady=4)
            if i % 2 == 0:
                x += 1
            y = (y + 1) % 2
        self.frame.grid(row=0, column=0, padx=(70, 0))
        self.title.grid(row=0, column=0, columnspan=3)
        self.newb.grid_configure(padx=(60, 0), pady=(20, 0))
        self.submit.grid_configure(pady=(20, 0), padx=(40, 0))
        self.text.grid(column=0, padx=(20, 0), pady=(20, 0))
        new(self)
        mainloop()
