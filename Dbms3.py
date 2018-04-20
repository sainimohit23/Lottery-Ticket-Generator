import random
from tkinter import *
import _mysql



db=_mysql.connect(host="localhost",user="root",
                  passwd="sainimohit23",db="dbms")


db.query("""SELECT num_id FROM dbms_project ORDER BY num_id DESC""")
get_max=db.store_result()
get_max = get_max.fetch_row()
max_id = int(get_max[0][0])




def lotto_no(max_id):
    x = random.randint(1, max_id)
    db.query("SELECT * FROM dbms_project WHERE num_id = "+ str(x))
    r=db.store_result()
    r = r.fetch_row()
    
    
    num1.set(int(r[0][1]))
    num2.set(int(r[0][2]))
    num3.set(int(r[0][3]))
    num4.set(int(r[0][4]))
    num5.set(int(r[0][5]))
    num6.set(int(r[0][6]))
    
    return

Lottery = Tk()
Lottery.geometry('800x360')
frame = Frame(Lottery)
frame.pack()

Lottery.title('WINNING LOTTERY NUMBER')

num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
num4 = StringVar()
num5 = StringVar()
num6 = StringVar()

var = StringVar()
var.set("Winning Lottery Number")
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
button1 = Button(frame3, padx=8, width=20, pady=8, bd=8, font=("Arial", 26), text="Generate Winning Number", bg="black",fg="white", command=lotto_no(max_id))
button1.pack(side=TOP)

Lottery.mainloop()

