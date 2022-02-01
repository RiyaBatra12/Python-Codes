from tkinter import *

def add():
    n1=eval(t1.get())
    n2=eval(t2.get())
    res=n1+n2
    l3.configure(text="Sum is "+str(res))
def subtract():
    n1=eval(t1.get())
    n2=eval(t2.get())
    res=n1-n2
    l3.configure(text="Difference is "+str(res))
def multiply():
    n1=eval(t1.get())
    n2=eval(t2.get())
    res=n1*n2
    l3.configure(text="Product is "+str(res))
def divide():
    n1=eval(t1.get())
    n2=eval(t2.get())
    res=n1/n2
    l3.configure(text="Quotient is "+str(res))
    

t=Tk()
t.geometry("400x300")

l1=Label(t,text="Number 1")
l2=Label(t,text="Number 2")
l1.place(x=50,y=50)
l2.place(x=50,y=80)
t1= Entry(t,width=10)
t2= Entry(t,width=10)
t1.place(x=100,y=50)
t2.place(x=100,y=80)
b1=Button(t,text="+",command=add)
b2=Button(t,text="-",command=subtract)
b3=Button(t,text="*",command=multiply)
b4=Button(t,text="/",command=divide)
b1.place(x=100,y=110)
b2.place(x=190,y=110)
b3.place(x=100,y=160)
b4.place(x=190,y=160)
l3=Label(t,text="Result")
l3.place(x=50,y=190)
t.mainloop()



