from tkinter import *
from tkinter import ttk
import turtle
wi=Tk()
wi.title("drow in turtle")
wi.geometry("500x500+800+200")
wi.resizable(False,False)
wi.attributes("-alpha",0.7)
wi.config(background="black")


def ass():
    if d1.get()=="مثلث":
        dd2=int(d2.get()) #قياس
        dd3=int(d3.get()) #انحراف
        dd4=int(d4.get()) #تكرار
        fd=turtle.Screen()
        fd.setup(500,500,250,250)
        fd.bgcolor("black")
        ff=turtle.Turtle()
        ff.speed(5)
        ff.color("blue")
        for m in range(dd4):
            for i in range(3):
                ff.forward(dd2)
                ff.left(120)
            ff.right(dd3)
        fd.mainloop()

    elif d1.get()=="مربع":
        dd2=int(d2.get()) #قياس
        dd3=int(d3.get()) #انحراف
        dd4=int(d4.get()) #تكرار
        fd=turtle.Screen()
        fd.setup(500,500,250,250)
        fd.bgcolor("black")
        ff=turtle.Turtle()
        ff.speed(5)
        ff.color("blue")
        for m in range(dd4):
            for i in range(4):
                ff.forward(dd2)
                ff.left(90)
            ff.right(dd3)
        fd.mainloop()       

    elif d1.get()=="دائرة":
        dd2=int(d2.get()) #قياس
        dd3=int(d3.get()) #انحراف
        dd4=int(d4.get()) #تكرار
        fd=turtle.Screen()
        fd.setup(500,500,250,250)
        fd.bgcolor("black")
        ff=turtle.Turtle()
        ff.speed(5)
        ff.color("blue")
        for m in range(dd4):
            ff.circle(dd2)
            ff.right(dd3)
        fd.mainloop()       


s1=Label(wi,text="ماهو الشكل الذي تريده ان يرسم",fg="white",font=(15),bg="black",justify="center")
s1.place(y=20,x=270)
d1=ttk.Combobox(wi,value=("مثلث","مربع","دائرة"),state="readonly",font=("arial",10),width=22,justify="center")
d1.place(y=22,x=20)

s2=Label(wi,text="ماهو قياس الشكل المرسوم",fg="white",font=(10),bg="black")
s2.place(y=70,x=305)
d2=Entry(wi,font=(10),width=14,justify="center")
d2.place(y=72,x=20)

s3=Label(wi,text="ماهي نسبة الانحراف التي تريدها",fg="white",font=(10),bg="black")
s3.place(y=120,x=265)
d3=Entry(wi,font=(10),width=14,justify="center")
d3.place(y=122,x=20)

s4=Label(wi,text="ما عدد التكرار الذي تريده",fg="white",font=(10),bg="black")
s4.place(y=170,x=310)
d4=Entry(wi,font=(10),width=14,justify="center")
d4.place(y=172,x=20)

b=Button(wi,text="ارسم",font=(20),command=ass)
b.place(y=300,x=230)

wi.mainloop()