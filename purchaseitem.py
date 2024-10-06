from tkinter import *
from tkinter import ttk
import mysql.connector
from datetime import datetime
from tkinter.messagebox import *

global root


class purchase:
    global root

    def __init__(self, conn, root):
        cursor = conn.cursor()

        def quitfunc():
            a = askquestion(
                title="Quit?", message="Do you really want to quit?")
            if a == 'yes':
                self.root.destroy()
                root.deiconify()

        d = datetime(1, 1, 1).now()

        def callback(event):
            self.prebal_in.configure(state=NORMAL)
            cursor.execute("select * from dealers")
            self.rows = cursor.fetchall()
            c = self.dlist.current()
            pb = self.rows[c][5]
            self.prebal_in.insert(0, pb)
            self.prebal_in.configure(state=DISABLED)

        def callback1(event):
            cursor.execute("select * from stock")
            self.rows = cursor.fetchall()
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
            self.mlist = [self.rows[i][2]
                          for i in range(len(self.rows)) if self.rows[i][1] == m]
            self.modellist.configure(values=self.mlist)

        def callback2(event):
            model = self.modellist.get()
            for i in range(len(self.rows)):
                if self.rows[i][2] == model:
                    emrp = self.rows[i][3]
            self.mrp_in.configure(state=NORMAL)
            self.mrp_in.delete(0, END)
            self.mrp_in.insert(0, emrp)
            self.mrp_in.configure(state=DISABLED)

        def calcamt(event):
            amount = int(self.ourprice_in.get()) * int(self.qty_in.get())
            self.amt_in.configure(state=NORMAL)
            self.amt_in.delete(0, END)
            self.amt_in.insert(0, amount)
            self.amt_in.configure(state=DISABLED)

        def new(self):
            cursor.execute("select * from purchases")
            rows2 = cursor.fetchall()
            self.prebal_in.configure(state=NORMAL)
            self.mrp_in.configure(state=NORMAL)
            self.amt_in.configure(state=NORMAL)
            self.billno_in.configure(state=NORMAL)
            self.billdt_in.configure(state=NORMAL)
            self.dlist.set("")
            self.catlist.set("")
            self.modellist.set("")
            self.billno_in.delete(0, END)
            self.billdt_in.delete(0, END)
            self.prebal_in.delete(0, END)
            self.mrp_in.delete(0, END)
            self.ourprice_in.delete(0, END)
            self.qty_in.delete(0, END)
            self.amt_in.delete(0, END)
            s = d.strftime('%x')
            l = s.split("/")
            l[2] = '20' + l[2]
            date = '{}-{}-{}'.format(l[2], l[0], l[1])
            self.billdt_in.insert(0, date)
            self.billno_in.insert(0, len(rows2) + 1)
            self.prebal_in.configure(state=DISABLED)
            self.mrp_in.configure(state=DISABLED)
            self.amt_in.configure(state=DISABLED)
            self.billno_in.configure(state=DISABLED)
            self.billdt_in.configure(state=DISABLED)

        def save(self):
            if len(self.prebal_in.get()) == 0 or len(self.mrp_in.get()) == 0 or len(self.ourprice_in.get()) == 0 or len(
                    self.qty_in.get()) == 0:
                self.text.configure(text="Some fields are empty")
            else:
                if int(self.ourprice_in.get()) > int(self.mrp_in.get()):
                    self.text.configure(text="Our price value is not correct")
                else:
                    cursor.execute(
                        "update stock set quantity=quantity+{} where model='{}'".format(int(self.qty_in.get()),
                                                                                        self.modellist.get()))
                    conn.commit()
                    cursor.execute(
                        "update dealers set balance=balance+{} where dealername='{}'".format(int(self.amt_in.get()),
                                                                                             self.dlist.get()))
                    conn.commit()
                    s1 = "insert into purchases(bill_no,bill_date,dealer,itemcat,model,mrp,price,quantity,amount,cleared) values({},'{}','{}','{}','{}',{},{},{},{},'no')".format(
                        int(self.billno_in.get()), self.billdt_in.get(), self.dlist.get(
                        ), self.catlist.get(), self.modellist.get(), int(self.mrp_in.get()),
                        int(self.ourprice_in.get()),
                        int(self.qty_in.get()), int(self.amt_in.get()))
                    cursor.execute(s1)
                    conn.commit()
                    self.text.configure(text="Record Saved")

        cursor = conn.cursor()
        cursor.execute("select * from dealers")
        self.rows = cursor.fetchall()
        self.list = [self.rows[i][2] for i in range(len(self.rows))]

        cursor.execute("select * from stock")
        self.rows = cursor.fetchall()
        self.clist = []
        for i in range(len(self.rows)):
            if self.rows[i][1] not in self.clist:
                self.clist.append(self.rows[i][1])
        self.root = Toplevel(root)
        self.root.title("Purchase")
        self.root.geometry("500x600")
        self.root.protocol("WM_DELETE_WINDOW", quitfunc)
        self.frame = Frame(self.root)

        # Creating widgets
        self.title = Label(self.frame, text="Purchase", font=('arial', 20))
        self.billno = Label(self.frame, text="Bill No.", font=('arial', 16))
        self.billno_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.billdt = Label(self.frame, text="Bill date", font=('arial', 16))
        self.billdt_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.dlabel = Label(
            self.frame, text="Select Dealer", font=('arial', 16))
        self.dlist = ttk.Combobox(self.frame, state='readonly', values=self.list,
                                  font=('arial', 12), width=22)
        self.dlist.bind("<<ComboboxSelected>>", callback)
        self.prebal = Label(self.frame, text="Pre-Balance", font=('arial', 16))
        self.prebal_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.cat = Label(self.frame, text="Product Category",
                         font=('arial', 16))
        self.catlist = ttk.Combobox(self.frame, state='readonly', values=self.clist,
                                    font=('arial', 12), width=22)
        self.catlist.bind("<<ComboboxSelected>>", callback1)

        self.model = Label(self.frame, text="Model", font=('arial', 16))
        self.modellist = ttk.Combobox(self.frame, state='readonly', values=self.list,
                                      font=('arial', 12), width=22)
        self.modellist.bind("<<ComboboxSelected>>", callback2)

        self.mrp = Label(self.frame, text="MRP", font=('arial', 16))
        self.mrp_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.ourprice = Label(self.frame, text="Our Price", font=('arial', 16))
        self.ourprice_in = Entry(self.frame, font=('arial', 14))

        self.qty = Label(self.frame, text="Quantity", font=('arial', 16))
        self.qty_in = Entry(self.frame, font=('arial', 14))
        self.qty_in.bind("<FocusOut>", calcamt)

        self.amt = Label(self.frame, text="Final amount", font=('arial', 16))
        self.amt_in = Entry(self.frame, font=('arial', 14), state=DISABLED)

        self.newb = Button(self.frame, text="New", font=(
            'arial', 16), command=lambda: new(self))
        self.submit = Button(self.frame, text="Save", font=(
            'arial', 16), command=lambda: save(self))
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
        self.frame.grid(row=0, column=0, padx=(50, 0))
        self.newb.grid_configure(pady=(20, 0), padx=(70, 0))
        self.submit.grid_configure(column=1, pady=(20, 0), padx=(50, 0))
        self.text.grid_configure(row=1, pady=(20, 0), padx=(20, 0))
        self.title.grid(row=0, column=0, columnspan=2)
        new(self)
        mainloop()
