import pyautogui as pg
import time
import tkinter as tk
from tkinter import filedialog

w = tk.Tk()
w.geometry("480x430")
w.resizable(False,False)
w.title("SPAMMER")
w.configure(background='#5a8c64')

emsg = tk.Label(w, text="SPAM BOT" ,fg="white",bg="blue" ,width=37 ,height=1,font=('times', 17, ' bold '))
emsg.place(x=-82, y=20)

en = tk.Label(w, text="Enter Number Times : ",width=20  ,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold ') )
en.place(x=30, y=100)

s_n = tk.Entry(w,width=32 ,fg="black",font=('times', 15, ' bold '))
s_n.place(x=30, y=150)

emsg = tk.Label(w, text="Enter Message : ",width=20  ,height=1  ,fg="black"  ,bg="#00aeff" ,font=('times', 17, ' bold ') )
emsg.place(x=30, y=200)

s_msg = tk.Entry(w, width=32 ,fg="black",font=('times', 15, ' bold '))
s_msg.place(x=30, y=250)

def n_spam():
    msg = s_msg.get()
    n = s_n.get()

    print(msg, "  a  ", n)

    if len(n)==0 or len(msg)==0:
        return None
    else:
        time.sleep(5)
        for i in range(0, int(n), +1):
            pg.write(f"{msg}")
            pg.press("enter")


def a_spam():
    msg = s_msg.get()
    filepath = filedialog.askopenfilename(title="Open File", filetypes=(("txt files","*.txt"),("all files","*.*")))
    txt = open(filepath, 'r')
    time.sleep(5)
    for i in txt:
        pg.write(f"{msg} {i}")
        pg.press("enter")



p = tk.Button(w, text="START", command=n_spam  ,fg="white"  ,bg="blue"  ,width=7  ,height=1, activebackground = "white" ,font=('times', 15, ' bold '))
p.place(x=75, y=310)

o = tk.Button(w, text="ATTACH &\nSTART", command=a_spam  ,fg="white"  ,bg="blue"  ,width=10  ,height=2, activebackground = "white" ,font=('times', 15, ' bold '))
o.place(x=250, y=300)

w.mainloop()
