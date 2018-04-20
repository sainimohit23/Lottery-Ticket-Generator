import random
from tkinter import *
import _mysql



db=_mysql.connect(host="localhost",user="root",
                  passwd="sainimohit23",db="dbms")
db.query("""DELETE FROM dbms_project""")
db.query("""alter table dbms_project AUTO_INCREMENT = 1""")


def lotto_no():
    x = random.randint(1, 49)
    q = random.randint(1, 49)
    w = random.randint(1, 49)
    e = random.randint(1, 49)
    r = random.randint(1, 49)
    t = random.randint(1, 49)
    num1.set(x)
    num2.set(q)
    num3.set(w)
    num4.set(e)
    num5.set(r)
    num6.set(t)
    
    my_str = "INSERT INTO dbms_project(a, b, c, d, e, f) VALUES (" + str(x) +','+ str(q) + ',' + str(w) + ',' + str(e) + ',' + str(r) + ',' + str(t)+ ")"
    db.query(my_str)
    
    return

Lottery = Tk()
Lottery.geometry('800x360')
frame = Frame(Lottery)
frame.pack()

Lottery.title('Lottery number Generator')

num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
num4 = StringVar()
num5 = StringVar()
num6 = StringVar()

var = StringVar()
var.set("Lottery Number Generator")
frame1 = Frame(Lottery)
frame1.pack(side=TOP)

label = Label(frame1, textvariable=var, font=("Arial", 48), width=24, fg="cyan")
label.pack(side=TOP)

label1 = Label(frame1, textvariable="", width=24)
label1.pack(side=TOP)
label1 = Label(frame1, textvariable="", width=24)
label1.pack(side=TOP)

frame2 = Frame(Lottery)
frame2.pack(side=TOP)

txtDisplay = Entry(frame1, textvariable=num1, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtDisplay.pack(side=LEFT)
txtDisplay.config(state='readonly')
txtDisplay = Entry(frame1, textvariable=num2, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtDisplay.pack(side=LEFT)
txtDisplay.config(state='readonly')
txtDisplay = Entry(frame1, textvariable=num3, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtDisplay.pack(side=LEFT)
txtDisplay.config(state='readonly')
txtDisplay = Entry(frame1, textvariable=num4, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtDisplay.pack(side=LEFT)
txtDisplay.config(state='readonly')
txtDisplay = Entry(frame1, textvariable=num5, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtDisplay.pack(side=LEFT)
txtDisplay.config(state='readonly')
txtDisplay = Entry(frame1, textvariable=num6, bd=20, insertwidth=1, font=("Arial", 30), justify='center', width=4)
txtDisplay.pack(side=LEFT)
txtDisplay.config(state='readonly')

frame3 = Frame(Lottery)
frame3.pack(side=TOP)
button1 = Button(frame3, state=DISABLED, text="")
button1.pack(side=TOP)
button1 = Button(frame3, padx=8, width=18, pady=8, bd=8, font=("Arial", 26), text="Generate Number", bg="black",fg="white", command=lotto_no)
button1.pack(side=TOP)

Lottery.mainloop()
