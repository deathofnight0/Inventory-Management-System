from tkinter import *
import tkinter.ttk as ttk
import mysql.connector
from ttkthemes import ThemedTk
from tkinter.messagebox import *


# global root


#
#
# # def open():
# #     root.withdraw()
# #     a1 = dealer()


class dealer1:
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
        s1 = "select * from dealers"
        cursor.execute(s1)
        rows = cursor.fetchall()
        self.title = Label(self.root, text='Dealer Records', font=(
            'Microsoft YaHei UI', 20), bg='#B3D9FF')
        self.tscroll = Scrollbar(self.treeframe)
        self.tscroll.pack(side=RIGHT, fill=Y)

        self.tv = ttk.Treeview(self.treeframe, column=(1, 2, 3, 4, 5, 6),
                               show='headings', yscrollcommand=self.tscroll.set)
        self.tv.pack()
        self.tv.heading("1", text="Sr. no.")
        self.tv.heading("2", text="Dealer id")
        self.tv.heading("3", text="Dealer name")
        self.tv.heading("4", text="Address")
        self.tv.heading("5", text="Mobile")
        self.tv.heading("6", text="Balance")
        self.tscroll.config(command=self.tv.yview)

        for i in range(1, 6):
            self.tv.column(i, width=120, anchor=CENTER)
        for i in range(len(rows)):
            self.tv.insert('', END, values=rows[i])
        self.title.grid(row=0, column=0)
        self.treeframe.grid(row=1, column=0, padx=20, pady=20)
        mainloop()

# root = ThemedTk(theme='adapta')
# root.geometry("400x400")
# b1 = Button(root, text="Dealer records", font=('arial', 18), command=open)
# b1.grid(row=3, column=0, columnspan=3)
# mainloop()
