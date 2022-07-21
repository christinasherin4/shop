from tkinter import *
root=Tk()
root.geometry("1000x500")
root.title("Coffee Shop Billing System")
Label(text="COFFEE SHOP BILLING MANAGEMENT",bg="black",fg="white",font=("calibri",33),width="300",height="2").pack()

def Reset():
    entry_Mocha.delete(0,END)
    entry_Cappuccino.delete(0,END)
    entry_Esspresso.delete(0,END)
    entry_Latte.delete(0,END)
    print()
def Total():
    try:a1=int(Mocha.get())
    except:a1=0
    try:a2=int(Cappuccino.get())
    except:a2=0
    try:a3=int(Esspresso.get())
    except:a3=0
    try:a4=int(Latte.get())
    except:a4=0
    print()
#define cost
    c1=60*a1
    c2=30*a2
    c3=7*a3
    c4=100*a4
    lbl_total=Label(f2,font=('arial',20,'bold'),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)
    entry_total=Entry(f2,font=("arial",20,"bold"),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)
    totalcost=c1+c2+c3+c4
    string_bill="Rs.",str("%2f"%totalcost)
    Total_bill.set(string_bill)
    
#MENU CARD
f=Frame(root,bg="gold",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=20,y=125)
Label(f,text="Menu",font=("Gabriola",40,"bold"),fg="black",bg="gold").place(x=80,y=0)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Mocha.........Rs.170",fg="black",bg="blue")
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Cappuccino.........Rs.180",fg="black",bg="blue")
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Espresso.........Rs.200",fg="black",bg="blue")
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Latte.........Rs.330",fg="black",bg="blue")

#BILL
f2=Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=680,y=118)
Bill=Label(f2,text="Bill"
,font=("calibiri",20),bg="lightyellow")
Bill.place(x=120,y=10)

#ENTRY WORK
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()
Mocha=StringVar()
Cappuccino=StringVar()
Latte=StringVar()
Esspresso=StringVar()
Total_bill=StringVar()

#Label
lbl_Mocha=Label(f1,font=('arial',20,'bold'),text="Mocha",width=12,fg="grey")

lbl_Cappuccino=Label(f1,font=('arial',20,'bold'),text="Cappuccino",width=12,fg="grey")

lbl_Esspresso=Label(f1,font=('arial',20,'bold'),text="Esspresso",width=12,fg="grey")

lbl_Latte=Label(f1,font=('arial',20,'bold'),text="Latte",width=12,fg="grey")


lbl_Mocha.grid(row=1,column=0)
lbl_Cappuccino.grid(row=2,column=0)
lbl_Esspresso.grid(row=3,column=0)
lbl_Latte.grid(row=4,column=0)
#Entry
entry_Mocha=Entry(f1,font=("arial",20,"bold"),textvariable=Mocha,bd=6,width=8,bg="gold")
entry_Mocha.grid(row=1,column=1)
entry_Cappuccino=Entry(f1,font=("arial",20,"bold"),textvariable=Cappuccino,bd=6,width=8,bg="gold")
entry_Cappuccino.grid(row=2,column=1)
entry_Esspresso=Entry(f1,font=("arial",20,"bold"),textvariable=Esspresso,bd=6,width=8,bg="gold")
entry_Esspresso.grid(row=3,column=1)
entry_Latte=Entry(f1,font=("arial",20,"bold"),textvariable=Latte,bd=6,width=8,bg="gold")
entry_Latte.grid(row=4,column=1)


#buttons
btn_reset=Button(f1,bd=5,fg="black",bg="blue",font=("arial",16,"bold"),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)
btn_total=Button(f1,bd=5,fg="black",bg="blue",font=("arial",16,"bold"),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)
root.mainloop()
