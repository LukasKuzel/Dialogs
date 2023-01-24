from tkinter import *


base = Tk()
base.geometry("500x500")
base.title("App")


def submit():
    try:
        float(en1.get())
        float(en2.get())
        lb_answer.config(text="Submited.")
    except ValueError:
        lb_answer.config(text="Seed and parameter must be a number.")


lb1 = Label(base, text="Enter seed:", width=10, font=("arial", 12))
lb1.place(x=20, y=120)
n_var = IntVar()
n_var.set('')
en1 = Entry(base, textvariable=n_var)
en1.place(x=200, y=120)
lb2 = Label(base, text="Enter parameter:", font=("arial", 12))
lb2.place(x=20, y=160)
n_var = IntVar()
n_var.set('')
en2 = Entry(base, textvariable=n_var)
en2.place(x=200, y=160)
lb_answer = Label(base, text="", font=("arial", 12))
lb_answer.place(x=120, y=320)


submit = Button(text="Submit", width=14, command=submit)
submit.place(x=220, y=280)

quit_b = Button(text="Quit", width=10, command=base.destroy)
quit_b.place(x=230, y=450)

base.mainloop()
