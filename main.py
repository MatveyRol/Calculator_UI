import tkinter
from tkinter import *

window = Tk()
window.geometry('500x700+450+300')

rez = ""

def Enter_Numbers(n):
    global  rez
    rez = str(place_for_numbers.get())
    rez+=str(n)
    place_for_numbers.delete(0, END)
    place_for_numbers.insert(1, rez)

def ravno():
    global rez
    rez = place_for_numbers.get()
    rez = rez.replace("÷", "/").replace("x", "*").replace("^2", "**2")
    rez = str(eval(rez))
    place_for_numbers.delete(0, END)
    place_for_numbers.insert(1, rez)

def AC():
    global rez
    rez = ""
    place_for_numbers.delete(0, END)

def delit():
    global rez
    rez = rez[:-1]
    place_for_numbers.delete(0, END)
    place_for_numbers.insert(1, rez)

def buttons_znaki():
    btn_plus = Button(window, text="+", font=("Copperplate", 20), height=6, width=3, command = lambda n= '+':Enter_Numbers(n))
    btn_plus.place(x=350, y=440)

    btn_umn = Button(window, text="x", font=("Copperplate", 20), height=2, width=3, command = lambda n= 'x':Enter_Numbers(n))
    btn_umn.place(x=350, y=370)

    btn_del = Button(window, text="÷", font=("Copperplate", 20), height=2, width=3, command = lambda n= '÷':Enter_Numbers(n))
    btn_del.place(x=430, y=370)

    btn_minus = Button(window, text="-", font=("Copperplate", 20), height=2, width=3, command = lambda n= '-':Enter_Numbers(n))
    btn_minus.place(x=430, y=440)

    btn_ravno = Button(window, text="=", font=("Copperplate", 20), height=2, width=3, command=ravno)
    btn_ravno.place(x=430, y=510)

    btn_AC = Button(window, text="AC", font=("Copperlate", 20), height=6, width=3, command=AC)
    btn_AC.place(x=40, y=370)

    btn_sk_left = Button(window, text="(", font=("Copperlate", 20), height=2, width=3, command = lambda n= '(':Enter_Numbers(n))
    btn_sk_left.place(x=350, y=300)

    btn_sk_right = Button(window, text=")", font=("Copperlate", 20), height=2, width=3, command = lambda n= ')':Enter_Numbers(n))
    btn_sk_right.place(x=430, y=300)

    btn_st = Button(window, text="x^2", font=("Copperlate", 20), height=2, width=3, command = lambda n= '^2':Enter_Numbers(n))
    btn_st.place(x=430, y=220)

    btn_del = Button(window, text="<=", font=("Copperlate", 20), height=2, width=3, command =delit)
    btn_del.place(x=40, y=300)
def buttons_Numbers():
    btn1 = Button(window, text="1", font=("Copperplate", 20), height=2, width=3, command = lambda n= '1':Enter_Numbers(n))
    btn1.place(x=130, y=300)

    btn2 = Button(window, text="2", font=("Copperplate", 20), height=2, width=3, command = lambda n= '2':Enter_Numbers(n))
    btn2.place(x=200, y=300)

    btn3 = Button(window, text="3", font=("Copperplate", 20), height=2, width=3, command = lambda n= '3':Enter_Numbers(n))
    btn3.place(x=270, y=300)

    btn4 = Button(window, text="4", font=("Copperplate", 20), height=2, width=3, command = lambda n= '4':Enter_Numbers(n))
    btn4.place(x=130, y=370)

    btn5 = Button(window, text="5", font=("Copperplate", 20), height=2, width=3, command = lambda n= '5':Enter_Numbers(n))
    btn5.place(x=200, y=370)

    btn6 = Button(window, text="6", font=("Copperplate", 20), height=2, width=3, command = lambda n= '6':Enter_Numbers(n))
    btn6.place(x=270, y=370)

    btn7 = Button(window, text="7", font=("Copperplate", 20), height=2, width=3, command = lambda n= '7':Enter_Numbers(n))
    btn7.place(x=130, y=440)

    btn8 = Button(window, text="8", font=("Copperplate", 20), height=2, width=3, command = lambda n= '8':Enter_Numbers(n))
    btn8.place(x=200, y=440)

    btn9 = Button(window, text="9", font=("Copperplate", 20), height=2, width=3, command = lambda n= '9':Enter_Numbers(n))
    btn9.place(x=270, y=440)

    btn0 = Button(window, text="0", font=("Copperplate", 20), height=2, width=3, command = lambda n= '0':Enter_Numbers(n))
    btn0.place(x=200, y=510)

buttons_Numbers()
buttons_znaki()
place_for_numbers = Entry(window, width=30)
place_for_numbers.place(x=150, y=150)
window.mainloop()