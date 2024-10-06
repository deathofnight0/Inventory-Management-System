from tkinter import *
import tkinter.ttk as ttk
import mysql.connector
from ttkthemes import ThemedTk
from tkinter.messagebox import *

global root


class payment1:
    global root

    def __init__(self, cursor, root):
        def quitfunc():
            a = askquestion(
                title="Quit?", message="Do you really want to quit?")
            if a == 'yes':
                self.root.destroy()
                root.deiconify()

        self.root = Toplevel(root)
        self.root.title("Dealer records")
        self.root.configure(bg='#B3D9FF')
        self.treeframe = Frame(self.root)
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading",
                             font=('Microsoft YaHei UI', 12))
        self.style.configure("Treeview", font=('Microsoft YaHei UI', 10))
        self.root.protocol("WM_DELETE_WINDOW", quitfunc)
        cursor.execute("select * from payments")
        rows = cursor.fetchall()
        self.title = Label(self.root, text='Payment Records',
                           font=('arial', 20), bg='#B3D9FF')
        self.tscroll = Scrollbar(self.treeframe)
        self.tscroll.pack(side=RIGHT, fill=Y)

        self.tv = ttk.Treeview(self.treeframe, column=(1, 2, 3, 4, 5, 6, 7, 8),
                               show='headings', yscrollcommand=self.tscroll.set)
        self.tv.pack()
        self.tv.heading("1", text="Sr. no.")
        self.tv.heading("2", text="Payment Date")
        self.tv.heading("3", text="Bill Date")
        self.tv.heading("4", text="Bill no.")
        self.tv.heading("5", text="Dealer")
        self.tv.heading("6", text="Amount")
        self.tv.heading("7", text="Paid")
        self.tv.heading("8", text="Balance")
        self.tscroll.config(command=self.tv.yview)

        for i in range(1, 9):
            self.tv.column(i, width=120, anchor=CENTER)
        for i in range(len(rows)):
            self.tv.insert('', END, values=rows[i])
        self.title.grid(row=0, column=0)
        self.treeframe.grid(row=1, column=0, padx=20, pady=20)
        mainloop()
