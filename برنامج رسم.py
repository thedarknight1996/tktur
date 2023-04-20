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
    if d1.get()=="triangle":
        dd2=int(d2.get()) #قياس
        dd3=int(d3.get()) #انحراف
        dd4=int(d4.get()) #تكرار
        dd5=str(d5.get()) #اللون
        fd=turtle.Screen()
        fd.setup(500,500,dd2-250,dd2-250)
        fd.bgcolor("black")
        ff=turtle.Turtle()
        ff.speed(5)
        ff.color(dd5)
        for m in range(dd4):
            for i in range(3):
                ff.forward(dd2)
                ff.left(120)
            ff.right(dd3)
        fd.mainloop()

    elif d1.get()=="Square":
        dd2=int(d2.get()) #قياس
        dd3=int(d3.get()) #انحراف
        dd4=int(d4.get()) #تكرار
        dd5=str(d5.get()) #اللون
        fd=turtle.Screen()
        fd.setup(500,500,dd2-250,dd2-250)
        fd.bgcolor("black")
        ff=turtle.Turtle()
        ff.speed(5)
        ff.color(dd5)
        for m in range(dd4):
            for i in range(4):
                ff.forward(dd2)
                ff.left(90)
            ff.right(dd3)
        fd.mainloop()       

    elif d1.get()=="circle":
        dd2=int(d2.get()) #قياس
        dd3=int(d3.get()) #انحراف
        dd4=int(d4.get()) #تكرار
        dd5=str(d5.get()) #اللون
        fd=turtle.Screen()
        fd.setup(500,500,dd2-250,dd2-250)
        fd.bgcolor("black")
        ff=turtle.Turtle()
        ff.speed(5)
        ff.color(dd5)
        for m in range(dd4):
            ff.circle(dd2)
            ff.right(dd3)
        fd.mainloop()       


s1=Label(wi,text="What shape do you want to draw ?",fg="white",font=(15),bg="black",justify="center")
s1.place(y=20,x=20)
d1=ttk.Combobox(wi,value=("triangle","Square","circle"),state="readonly",font=("arial",10),width=15,justify="center")
d1.place(y=22,x=350)

s2=Label(wi,text="What is the size of the drawn figure ?",fg="white",font=(10),bg="black")
s2.place(y=70,x=20)
d2=Entry(wi,font=(10),width=14,justify="center")
d2.place(y=72,x=350)

s3=Label(wi,text="What angle of deviation do you want ?",fg="white",font=(10),bg="black")
s3.place(y=120,x=20)
d3=Entry(wi,font=(10),width=14,justify="center")
d3.place(y=122,x=350)

s4=Label(wi,text="How many repetitions do you want ?",fg="white",font=(10),bg="black")
s4.place(y=170,x=20)
d4=Entry(wi,font=(10),width=14,justify="center")
d4.place(y=172,x=350)

s5=Label(wi,text="What color do you want the painting to be ?",fg="white",font=(15),bg="black",justify="center")
s5.place(y=220,x=20)
d5=ttk.Combobox(wi,value=("white","purple","green","red","blue","yellow","orange","grey"),state="readonly",font=("arial",10),width=15,justify="center")
d5.place(y=222,x=350)

b=Button(wi,text="drow",font=(25),fg="green",command=ass)
b.place(y=350,x=230)

c=Button(wi,text="X\n closs the brogram",font=(20),fg="red",command=wi.quit)
c.place(y=400,x=180)

wi.mainloop()
