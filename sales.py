from tkinter import *
import tkinter.ttk as ttk
import mysql.connector
from ttkthemes import ThemedTk
from tkinter.messagebox import *

global root


class sales1:
    global root

    def __init__(self, cursor, root):
        def display(self):
            style = ttk.Style()
            style.configure("Treeview.Heading", font=(
                'Microsoft YaHei UI', 12))
            style.configure("Treeview", font=('Microsoft YaHei UI', 10))
            if len(self.stdt_in.get()) == 0 or len(self.enddt_in.get()) == 0:
                self.text.configure(text="Some fields are empty")
            else:
                self.new = Toplevel(self.root)
                self.new.title("Report")
                self.treeframe = Frame(self.new)
                self.new.configure(bg='#B3D9FF')
                self.root.protocol("WM_DELETE_WINDOW", quitfunc)
                s1 = "select * from sales where bill_date between '{}' and '{}'".format(
                    self.stdt_in.get(), self.enddt_in.get())
                cursor.execute(s1)
                rows = cursor.fetchall()
                self.ftitle = Label(self.new, text="Sales Report", font=(
                    'Microsoft YaHei UI', 20), bg='#B3D9FF')
                self.tscroll = Scrollbar(self.treeframe)
                self.tscroll.pack(side=RIGHT, fill=Y)
                self.tv = ttk.Treeview(self.treeframe, column=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
                                       show='headings',
                                       yscrollcommand=self.tscroll.set)
                self.tv.pack()
                self.tv.heading("1", text="Sr. no.")
                self.tv.heading("2", text="Bill Number")
                self.tv.heading("3", text="Bill Date")
                self.tv.heading("4", text="Category")
                self.tv.heading("5", text="Model")
                self.tv.heading("6", text="MRP")
                self.tv.heading("7", text="Customer name")
                self.tv.heading("8", text="Address")
                self.tv.heading("9", text="Mobile no.")
                self.tv.heading("10", text="Quantity")
                self.tv.heading("11", text="Amount")
                self.tv.heading("12", text="Paid")
                self.tv.heading("13", text="Balance")
                self.tscroll.config(command=self.tv.yview)

                for i in range(1, 14):
                    self.tv.column(i, width=120, anchor=CENTER)
                for i in range(len(rows)):
                    self.tv.insert('', END, values=rows[i])
                self.ftitle.grid(row=0, column=0)
                self.treeframe.grid(row=1, column=0, padx=20, pady=20)
                self.new.mainloop()

        def quitfunc():
            a = askquestion(
                title="Quit?", message="Do you really want to quit?")
            if a == 'yes':
                self.root.destroy()
                root.deiconify()

        self.root = Toplevel(root)
        self.root.title("Stock Report")
        self.root.geometry("500x300")
        self.frame = Frame(self.root)

        # Creating widgets
        self.title = Label(self.frame, text="Sales Report Generator", font=(
            'Microsoft YaHei UI', 20))

        self.stdt = Label(self.frame, text="Start date",
                          font=('Microsoft YaHei UI', 16))
        self.stdt_in = Entry(self.frame, font=('Microsoft YaHei UI', 14))

        self.enddt = Label(self.frame, text="End date",
                           font=('Microsoft YaHei UI', 16))
        self.enddt_in = Entry(self.frame, font=('Microsoft YaHei UI', 14))

        self.display = Button(self.frame, text="Display", font=('Microsoft YaHei UI', 16),
                              command=lambda: display(self))
        self.text = Label(self.root, text="", font=('Microsoft YaHei UI', 16))

        # Aligning widgets
        x = 1
        y = 0
        for i in range(1, len(self.frame.winfo_children())):
            self.frame.winfo_children()[i].grid_configure(
                row=x, column=y, sticky='w', pady=15)
            if i % 2 == 0:
                x += 1
            y = (y + 1) % 2
        self.frame.grid(row=0, column=0, padx=(80, 0))
        self.display.grid(column=1, padx=(20, 0))

        self.title.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        self.text.grid(column=0, padx=(80, 0))
        mainloop()
