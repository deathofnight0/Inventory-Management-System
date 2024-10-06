# from tkinter import *
# import mysql.connector
# from tkinter.messagebox import *
# from ttkthemes import ThemedTk
from dealer import *
from stock import *
from payment import *
from sales import *
from adduser import *
from dropuser import *
from changepass import *
from mdealer import *
from purchaseitem import *
from add_sales import *
from pay_dealer import *
from PIL import ImageTk, Image

conn = mysql.connector.connect(
    host='localhost', database='project', user='root', password='')
cursor = conn.cursor()


def dealreport(root):
    root.withdraw()
    r1 = dealer1(cursor, root)


def stockreport(root):
    root.withdraw()
    r2 = stock1(cursor, root)


def payreport(root):
    root.withdraw()
    r3 = payment1(cursor, root)


def salereport(root):
    root.withdraw()
    r4 = sales1(cursor, root)


def cruser(root):
    root.withdraw()
    u1 = createuser(conn, root)


def deluser(root):
    root.withdraw()
    u2 = drop(conn, root)


def changepassword(cuser, root):
    root.withdraw()
    u3 = password(conn, cuser, root)


def managedealer(root):
    root.withdraw()
    a1 = dealer(conn, root)


def purchase_item(root):
    root.withdraw()
    a2 = purchase(conn, root)


def add_sale(root):
    root.withdraw()
    a3 = sale(conn, root)


def payment(root):
    root.withdraw()
    a3 = pay(conn, root)


def exitprog(root):
    a = askquestion(
        title="Quit?", message="Do you really want to quit?")
    if a == 'yes':
        root.destroy()


def user(cuser):
    def xyz():
        print()

    root = ThemedTk(theme='adapta')
    root.title("Login")
    root.protocol("WM_DELETE_WINDOW", lambda: exitprog(root))
    root.geometry("900x650")
    root.resizable(False, False)
    frame = Frame()
    title = Label(frame, text="User", font=('Microsoft YaHei UI', 38))
    greet = Label(frame, text="Welcome {}".format(
        cuser.title()), font=('Microsoft YaHei UI', 18))
    users = LabelFrame(frame, text="Users", font=('Microsoft YaHei UI', 18))
    activities = LabelFrame(frame, text="Activities",
                            font=('Microsoft YaHei UI', 18))
    reports = LabelFrame(frame, text="Reports",
                         font=('Microsoft YaHei UI', 18))
    # frame.pack(expand='yes', fill='both')

    ################## ----User's Section----#######################
    chngpass = Button(users, text="Change password",
                      font=('Microsoft YaHei UI', 18), command=lambda: changepassword(cuser, root))
    exit = Button(users, text="Exit", font=(
        'Microsoft YaHei UI', 18), command=lambda: exitprog(root))
    chngpass.grid(row=2, column=0, pady=20, padx=10, sticky='w')
    exit.grid(row=3, column=0, pady=20, padx=10, sticky='w')

    ################## ----activity Section----#######################
    addsale = Button(activities, text="Add sale",
                     font=('Microsoft YaHei UI', 18), command=lambda: add_sale(root))
    addsale.grid(row=0, column=1, pady=20, padx=50, sticky='w')

    ################## ----Reports Section----#######################
    dealers1 = Button(reports, text="View Dealers",
                      font=('arial', 18), command=lambda: dealreport(root))
    stock1 = Button(reports, text="Display Stock", font=(
        'Microsoft YaHei UI', 18), command=lambda: stockreport(root))
    payment1 = Button(reports, text="Payment details",
                      font=('Microsoft YaHei UI', 18), command=lambda: payreport(root))
    sales1 = Button(reports, text="Sales Report",
                    font=('Microsoft YaHei UI', 18), command=lambda: salereport(root))
    dealers1.grid(row=0, column=2, pady=20, padx=10, sticky='w')
    stock1.grid(row=1, column=2, pady=20, padx=10, sticky='w')
    payment1.grid(row=2, column=2, pady=20, padx=10, sticky='w')
    sales1.grid(row=3, column=2, pady=20, padx=10, sticky='w')

    ########## ----Main frames alignment----##########

    frame.grid(row=0, column=0, padx=20, pady=20)
    title.grid(row=0, column=0, columnspan=3)
    greet.grid(row=1, column=0, pady=(20, 0), padx=(0, 50))
    users.grid(row=2, column=0, pady=(0, 140), padx=25)
    activities.grid(row=2, column=1, pady=(0, 230), padx=25)
    reports.grid(row=2, column=2, pady=(40, 0), padx=25)


def admin():
    def xyz():
        print()

    root = ThemedTk(theme='adapta')
    root.title("Interface")
    root.protocol("WM_DELETE_WINDOW", lambda: exitprog(root))
    root.geometry("900x650")
    root.resizable(False, False)
    frame = Frame()
    title = Label(frame, text="Admin", font=('Microsoft YaHei UI', 38))
    greet = Label(frame, text="Welcome admin", font=('Microsoft YaHei UI', 18))
    users = LabelFrame(frame, text="Users", font=('Microsoft YaHei UI', 18))
    activities = LabelFrame(frame, text="Activities",
                            font=('Microsoft YaHei UI', 18))
    reports = LabelFrame(frame, text="Reports",
                         font=('Microsoft YaHei UI', 18))
    # frame.pack(expand='yes', fill='both')

    ################## ----User's Section----#######################
    newuser = Button(users, text="Create new User",
                     font=('arial', 18), command=lambda: cruser(root))
    drop = Button(users, text="Drop User", font=(
        'Microsoft YaHei UI', 18), command=lambda: deluser(root))
    chngpass = Button(users, text="Change password",
                      font=('Microsoft YaHei UI', 18), command=lambda: changepassword("admin", root))
    exit = Button(users, text="Exit", font=(
        'Microsoft YaHei UI', 18), command=lambda: exitprog(root))
    newuser.grid(row=0, column=0, pady=20, padx=10, sticky='w')
    drop.grid(row=1, column=0, pady=20, padx=10, sticky='w')
    chngpass.grid(row=2, column=0, pady=20, padx=10, sticky='w')
    exit.grid(row=3, column=0, pady=20, padx=10, sticky='w')

    ################## ----activity Section----#######################
    mngdealer = Button(activities, text="Manage Dealers",
                       font=('arial', 18), command=lambda: managedealer(root))
    purchaseb = Button(activities, text="Purchase Items",
                       font=('Microsoft YaHei UI', 18), command=lambda: purchase_item(root))
    addsale = Button(activities, text="Add sale",
                     font=('Microsoft YaHei UI', 18), command=lambda: add_sale(root))
    paydealer = Button(activities, text="Pay to dealer",
                       font=('Microsoft YaHei UI', 18), command=lambda: payment(root))
    mngdealer.grid(row=0, column=1, pady=20, padx=10, sticky='w')
    purchaseb.grid(row=1, column=1, pady=20, padx=10, sticky='w')
    addsale.grid(row=2, column=1, pady=20, padx=10, sticky='w')
    paydealer.grid(row=3, column=1, pady=20, padx=10, sticky='w')

    ################## ----Reports Section----#######################
    dealers1 = Button(reports, text="View Dealers",
                      font=('arial', 18), command=lambda: dealreport(root))
    stock1 = Button(reports, text="Display Stock", font=(
        'Microsoft YaHei UI', 18), command=lambda: stockreport(root))
    payment1 = Button(reports, text="Payment details",
                      font=('Microsoft YaHei UI', 18), command=lambda: payreport(root))
    sales1 = Button(reports, text="Sales Report",
                    font=('Microsoft YaHei UI', 18), command=lambda: salereport(root))
    dealers1.grid(row=0, column=2, pady=20, padx=10, sticky='w')
    stock1.grid(row=1, column=2, pady=20, padx=10, sticky='w')
    payment1.grid(row=2, column=2, pady=20, padx=10, sticky='w')
    sales1.grid(row=3, column=2, pady=20, padx=10, sticky='w')

    ########## ----Main frames alignment----##########

    frame.grid(row=0, column=0, padx=20, pady=20)
    title.grid(row=0, column=0, columnspan=3)
    greet.grid(row=1, column=0, pady=(20, 0), padx=(0, 50))
    users.grid(row=2, column=0, pady=(40, 0), padx=25)
    activities.grid(row=2, column=1, pady=(40, 0), padx=25)
    reports.grid(row=2, column=2, pady=(40, 0), padx=25)


def nxt():
    root.title("Login!")
    root.configure(bg='#F0F0F0')
    label1.destroy()
    welcome.destroy()
    b1.destroy()

    def login():
        if len(uid_in.get()) == 0 or len(pswd_in.get()) == 0:
            text.configure(text="Some fields are empty")
        else:
            s1 = "select * from users where uid='{}'".format(
                uid_in.get().lower())
            cursor.execute(s1)
            row = cursor.fetchall()
            if row == [] or row[0][4] != pswd_in.get():
                text.configure(text="Username/Password invalid!")
            else:
                cuser = uid_in.get()
                if uid_in.get() == "admin":
                    root.destroy()
                    admin()
                else:
                    root.destroy()
                    user(cuser)

    frame = Frame()
    # Creating widgets
    title = Label(frame, text="Login Page", font=('arial', 20))
    uid = Label(frame, text="Username", font=('arial', 16))
    uid_in = Entry(frame, font=('arial', 14))
    pswd = Label(frame, text="Password", font=('arial', 16))
    pswd_in = Entry(frame, font=('arial', 14), show="*")
    submit = Button(frame, text="Login", command=login, font='arial')
    text = Label(frame, text="", font=('arial', 16))

    # Aligning widgets
    x = 1
    y = 0
    for i in range(1, len(frame.winfo_children())):
        frame.winfo_children()[i].grid_configure(
            row=x, column=y, sticky='w', pady=10)
        if i % 2 == 0:
            x += 1
        y = (y + 1) % 2
    frame.grid(row=0, column=2, columnspan=2, padx=(80, 0))
    title.grid(row=0, column=0, columnspan=3, pady=(0, 30))
    submit.grid_configure(row=3, column=1, padx=(40, 0))
    text.grid_configure(row=4, column=0, columnspan=4, padx=(70, 0))


root = Tk()
root.title("Welcome")
root.geometry("500x300")
root.configure(bg='#B3D9FF')
# Creating widgets

image = Image.open("samsung.png")
resize_image = image.resize((200, 200))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img, bg='#B3D9FF')
label1.image = img
welcome = Label(root, text="Welcome!", font=('arial', 20), bg='#B3D9FF')
b1 = Button(root, text="Continue", command=nxt, font=('arial', 16), bg='beige')
# Aligning widgets
label1.place(x=150, y=-30)
welcome.place(x=185, y=140)
b1.place(x=200, y=200)
mainloop()
