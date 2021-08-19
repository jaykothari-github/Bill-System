from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk
from random import randrange
import sqlite3 as sl

rw = Tk()
rw.title('Billing System')
rw.geometry("1400x700+0+0")

amt = IntVar()
amt.set(0.0)
top1 = IntVar()
top2 = IntVar()
top3 = IntVar()
top4 = IntVar()
top5 = IntVar()

pzpc1 = IntVar()
pzpc2 = IntVar()
pzpc3 = IntVar()
pzpc4 = IntVar()

pzn1 = StringVar()
pzn2 = StringVar()
pzn3 = StringVar()
pzn4 = StringVar()

top1n = StringVar()
top2n = StringVar()
top3n = StringVar()
top4n = StringVar()
top5n = StringVar()

top1.set(0)
top2.set(0)
top3.set(0)
top4.set(0)
top5.set(0)
pzpc1.set(0)
pzpc2.set(0)
pzpc3.set(0)
pzpc4.set(0)

paym = StringVar()

# Functions

def ing(fm,x,y):
    l1 = Label(fm,text='--Ingrediants--',bg='#0a0a73' ,fg='white' ,font=('courier',8,'bold'))
    l1.place(x=x,y=y)

def ingd(fm,des,x,y):
    l1 = Label(fm,text=des,bg='#0a0a73' ,fg='white' ,font=('courier',10,'bold'),justify="center")
    l1.place(x=x,y=y)
    
def price(fm,rs,x,y):

    l1 = Label(fm,text=rs,bg='#0a0a73' ,fg='white' ,font=('courier',14,'bold'),justify="center")
    l1.place(x=x,y=y)

def tpg1(t): # Top1
    top1.set(50)
    top1n.set(t)
    t1.config(bg='red')
    amt.set(top1.get() + top2.get() + top3.get() + top4.get() + top5.get() + pzpc1.get() + pzpc2.get() + pzpc3.get() + pzpc4.get())

def tpg2(t): # top2
    top2.set(50)
    top2n.set(t)
    t2.config(bg='red')
    amt.set(top1.get() + top2.get() + top3.get() + top4.get() + top5.get() + pzpc1.get() + pzpc2.get() + pzpc3.get() + pzpc4.get())

def tpg3(t):  # Top3
    top3.set(50)
    top3n.set(t)
    t3.config(bg='red')
    amt.set(top1.get() + top2.get() + top3.get() + top4.get() + top5.get() + pzpc1.get() + pzpc2.get() + pzpc3.get() + pzpc4.get())

def tpg4(t): # Top4
    top4.set(50)
    top4n.set(t)
    t4.config(bg='red')
    amt.set(top1.get() + top2.get() + top3.get() + top4.get() + top5.get() + pzpc1.get() + pzpc2.get() + pzpc3.get() + pzpc4.get())

def tpg5(t):   # Top5
    top5.set(50)
    top5n.set(t)
    t5.config(bg='red')
    amt.set(top1.get() + top2.get() + top3.get() + top4.get() + top5.get() + pzpc1.get() + pzpc2.get() + pzpc3.get() + pzpc4.get())

def pz1(t):  # Pizza 1
    pzpc1.set(210)
    pzn1.set(t)
    p1.config(bg='red')
    amt.set(top1.get() + top2.get() + top3.get() + top4.get() + top5.get() + pzpc1.get() + pzpc2.get() + pzpc3.get() + pzpc4.get())

def pz2(t):   
    pzpc2.set(240)
    pzn2.set(t)
    p2.config(bg='red')
    amt.set(top1.get() + top2.get() + top3.get() + top4.get() + top5.get() + pzpc1.get() + pzpc2.get() + pzpc3.get() + pzpc4.get())

def pz3(t):
    pzpc3.set(210)
    pzn3.set(t)
    p3.config(bg='red')
    amt.set(top1.get() + top2.get() + top3.get() + top4.get() + top5.get() + pzpc1.get() + pzpc2.get() + pzpc3.get() + pzpc4.get())

def pz4(t):
    pzpc4.set(245)
    pzn4.set(t)
    p4.config(bg='red')
    amt.set(top1.get() + top2.get() + top3.get() + top4.get() + top5.get() + pzpc1.get() + pzpc2.get() + pzpc3.get() + pzpc4.get())

def pbill():
    sec = Toplevel()
    sec.title('Bill Window')
    sec.geometry('400x600+300+50')
    sec.resizable(width=False,height=False)

    l1 = Label(sec,text="Domino's Pizza",font=('courier',20,'bold')).place(x=85,y=0)
    l1 = Label(sec,text="---------------------------------------------------------",font=('courier',8)).place(x=0,y=30)
    l1 = Label(sec,text="Customer Name : ",font=('courier',12,'bold')).place(x=0,y=50)
    l1 = Label(sec,text=cus_name.get(),font=('courier',12,'bold')).place(x=160,y=50)
    l1 = Label(sec,text="Customer Contact : ",font=('courier',12,'bold')).place(x=0,y=80)
    l1 = Label(sec,text=cus_con.get() ,font=('courier',12,'bold')).place(x=190,y=80)
    id = Label(sec,text=f'Order Id : {str(randrange(100000000,999999999))}',font=('courier',12,'bold')).place(x=0,y=110)
    l1 = Label(sec,text="---------------------------------------------------------",font=('courier',8)).place(x=0,y=130)
    l1 = Label(sec,text="No.",font=('courier',10)).place(x=5,y=145)
    l1 = Label(sec,text="Name",font=('courier',10)).place(x=120,y=145)
    l1 = Label(sec,text="Qty.",font=('courier',10)).place(x=250,y=145)
    l1 = Label(sec,text="Price",font=('courier',10)).place(x=330,y=145)
    l1 = Label(sec,text="---------------------------------------------------------",font=('courier',8)).place(x=0,y=165)

    n = [pzn1.get(),pzn2.get(),pzn3.get(),pzn4.get(),top1n.get(),top2n.get(),top3n.get(),top4n.get(),top5n.get()]
    p = [pzpc1.get(),pzpc2.get(),pzpc3.get(),pzpc4.get(),top1.get(),top2.get(),top3.get(),top4.get(),top5.get()]
    nn = n.count('')
    pp = p.count(0)
    for i in range(nn):
        n.remove('')
    
    for i in range(pp):
        p.remove(0)
    
    n = tuple(n)
    p = tuple(p)

    d = dict(zip(n,p))

    c= 0
    y = 185
    for i,j in d.items():
        l1 = Label(sec,text=str(c+1),font=('courier',10)).place(x=5,y=y)
        l2 = Label(sec,text=i,font=('courier',10)).place(x=70,y=y)
        l3 = Label(sec,text='1',font=('courier',10)).place(x=255,y=y)
        l4 = Label(sec,text=str(j),font=('courier',10)).place(x=335,y=y)
        c+=1
        y = y + 25
    l1 = Label(sec,text="---------------------------------------------------------",font=('courier',8)).place(x=0,y=y)
    y +=20
    l1 = Label(sec,text='Total : ',font=('courier',14,'bold')).place(x=70,y=y)
    l2 = Label(sec,text=str(amt.get()),font=('courier',14,'bold')).place(x=320,y=y)
    y += 20
    l1 = Label(sec,text="---------------------------------------------------------",font=('courier',8)).place(x=0,y=y)
    y +=20
    l1 = Label(sec,text=f'Payment Method : {pay.get()}',font=('courier',10)).place(x=10,y=y)
    y += 20
    l1 = Label(sec,text="---------------------------------------------------------",font=('courier',8)).place(x=0,y=y)
    y +=20
    l1 = Label(sec,text='Thank You!! Visit Again!!',font=('courier',14,'bold')).place(x=70,y=y)


# Background color : #0a0a73

mainfm = Frame(rw,bg='#0a0a73',height=750, width=1500)
mainfm.pack()

l1 = Label(mainfm,text="Welcome to Domino's Pizza!!",bg='#0a0a73' ,fg='white' ,font=('courier',20,'bold')).place(x=500,y=10)

logo1 = ImageTk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Python\Python projects\Billing System\logo.png")
logo = Label(mainfm,image=logo1,bd=0)
logo.place(x=420,y=10)

l1 = Label(mainfm,text="Pizza Vaireties...",bg='#0a0a73' ,fg='white' ,font=('courier',14,'bold')).place(x=20,y=90)

# Pizza Frames

pfm = Frame(mainfm,bg='red',height=400, width=1130).place(x=20,y=125) # Red Frame

# Sub Frame 1
p1fm = Frame(mainfm,bg='#0a0a73',height=350, width=230)
p1fm.place(x=50,y=150)

myimg = ImageTk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Python\Python projects\Billing System\1.jpg")
mylab = Label(p1fm,image=myimg )
mylab.place(x=0,y=0)

l11 = Label(p1fm,text='Veg. Kebab Surprise',bg='#0a0a73' ,fg='white' ,font=('courier',14,'italic','bold'))
l11.place(x=5,y=160)

ing(p1fm,60,185) # Des1
ingd(p1fm,'crunchy onions, \ncrisp capsicum, \njuicy tomatoes ',50,205)

price(p1fm,"Rs. 210/-",65,270)

p1 = Button(p1fm,text='+ Add',width=7,bg='#0a0a73' ,fg='white' ,font=('courier',14,'italic','bold'),command=lambda: pz1('Veg. Kebab Surprise'))
p1.place(x = 70, y=300)

# Sub Frame 2
p2fm = Frame(mainfm,bg='#0a0a73',height=350, width=230)
p2fm.place(x=330,y=150)

myimg1 = ImageTk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Python\Python projects\Billing System\2.jpg")
mylab1 = Label(p2fm,image=myimg1)
mylab1.place(x=0,y=0)

l12 = Label(p2fm,text='Veggie Supreme',bg='#0a0a73' ,fg='white' ,font=('courier',14,'italic','bold'))
l12.place(x=35,y=160)

ing(p2fm,60,185) # Des 2
ingd(p2fm,'golden corn, \nblack olives, \ncrunchy onions',60,205)

price(p2fm,"Rs. 240/-",65,270)

p2 = Button(p2fm,text='+ Add',width=7,bg='#0a0a73' ,fg='white' ,font=('courier',14,'italic','bold'),command=lambda: pz2('Veggie Supreme'))
p2.place(x = 70, y=300)

# Sub Frame 3
p3fm = Frame(mainfm,bg='#0a0a73',height=350, width=230)
p3fm.place(x=610,y=150)

myimg2 = ImageTk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Python\Python projects\Billing System\3.jpg")
mylab2 = Label(p3fm,image=myimg2)
mylab2.place(x=0,y=0)

l13 = Label(p3fm,text='Mexican Delight',bg='#0a0a73' ,fg='white' ,font=('courier',14,'italic','bold'))
l13.place(x=30,y=160)

ing(p3fm,60,185)  # des 3
ingd(p3fm,'Mashrooms, Capsicum, \nJuicy Tometos,\nBlack Olives',40,205)

price(p3fm,"Rs. 210/-",65,270)

p3 = Button(p3fm,text='+ Add',width=7,bg='#0a0a73' ,fg='white' ,font=('courier',14,'italic','bold'),command=lambda: pz3('Mexican Delight'))
p3.place(x = 70, y=300)

# Sub Frame 4
p4fm = Frame(mainfm,bg='#0a0a73',height=350, width=230)
p4fm.place(x=890,y=150)

myimg3 = ImageTk.PhotoImage(file=r"C:\Users\HP\OneDrive\Desktop\Python\Python projects\Billing System\4.jpg")
mylab3 = Label(p4fm,image=myimg3)
mylab3.place(x=0,y=0)

l14 = Label(p4fm,text='Spicy Treat',bg='#0a0a73' ,fg='white' ,font=('courier',14,'italic','bold'))
l14.place(x=50,y=160)

ing(p4fm,60,185) # des 4
ingd(p4fm,'Soft Paneer, \ncrisp capsicum, \njuicy tomatoes ',50,200)

price(p4fm,"Rs. 245/-",65,270)

p4 = Button(p4fm,text='+ Add',width=7,bg='#0a0a73' ,fg='white' ,font=('courier',14,'italic','bold'),command=lambda: pz4('Spicy Treat'))
p4.place(x = 70, y=300)

# Toppings

l1 = Label(mainfm,text="Extra Toppings...",bg='#0a0a73' ,fg='white' ,font=('courier',12,'bold'))
l1.place(x=1160,y=180)

t1 = Button(mainfm,text='Cheezzy..',bg='#0a0a73' ,fg='white',width=15 ,font=('courier',12,'bold'),command=lambda : tpg1('Cheezy'))
t1.place(x=1170,y=230)

t2 = Button(mainfm,text='Sauce..',bg='#0a0a73' ,fg='white',width=15 ,font=('courier',12,'bold'),command= lambda : tpg2('Sauce'))
t2.place(x=1170,y=265)

t3 = Button(mainfm,text='Pepperoni..',bg='#0a0a73' ,fg='white',width=15 ,font=('courier',12,'bold'),command=lambda : tpg3('Pepperoni'))
t3.place(x=1170,y=300)

t4 = Button(mainfm,text='Onions..',bg='#0a0a73' ,fg='white',width=15 ,font=('courier',12,'bold'),command=lambda : tpg4('Onions'))
t4.place(x=1170,y=335)

t5 = Button(mainfm,text='Black Olives..',bg='#0a0a73' ,fg='white',width=15 ,font=('courier',12,'bold'),command=lambda : tpg5('Black olives'))
t5.place(x=1170,y=370)

l1 = Label(mainfm,text='*Each cost \n 50 Rs./topping',bg='#0a0a73' ,fg='red' ,font=('courier',10,'bold'),)
l1.place(x=1180,y=410)

# Lower Frame

l1 = Label(mainfm,text="Continue to the bill...",bg='#0a0a73' ,fg='white' ,font=('courier',14,'bold')).place(x=20,y=550)

cfm = Frame(mainfm,bg='red',height=100, width=1130).place(x=20,y=580)

l2 = Label(cfm,text="Customer's name",bg='red',fg='white',font=('courier',14,'bold'))
l2.place(x=60,y=590)

cus_name = Entry(cfm, bg='#f24646',fg='white',font=('courier',14,'bold'), width=10)
cus_name.place(x=80, y = 630)

l3 = Label(cfm,text="Customer's contact",bg='red',fg='white',font=('courier',14,'bold'))
l3.place(x=330,y=590)

cus_con = Entry(cfm, bg='#f24646',fg='white',font=('courier',14,'bold'), width=12)
cus_con.place(x=370, y = 630)

l4 = Label(cfm,text="Bill Amount",bg='red',fg='white',font=('courier',14,'bold'))
l4.place(x=650,y=590)

amt1 = Label(cfm,textvariable=amt,bg='red',fg='white',font=('courier',18,'bold'))
amt1.place(x=700,y=630)

l4 = Label(cfm,text="Payment Method",bg='red',fg='white',font=('courier',14,'bold'))
l4.place(x=920,y=590)

pay = Combobox(cfm, width = 10,background ='#f24646',font=('courier',14,'bold') ,textvariable = paym)
pay['values'] = ("Cash","Card","UPI","Bitcoin")
pay.place(x=940, y = 630)

bill = Button(mainfm,text='Print Bill',bg='red',fg='white',activebackground='#0a0a73', activeforeground='white',
            font=('courier',14,'bold'),bd=1, command=pbill)
bill.place(x=1200,y=590)

rw.mainloop()