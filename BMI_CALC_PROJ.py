from tkinter import *
import tkinter as tk
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk

root=Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False,False)
root.configure(bg="#f0f1f5")


def BMI():
        h= float(Height.get())
        w= float(Weight.get())
        m=h/100
        bmi=round(float(w/m**2),1)
        label.config(text=bmi)

        if bmi<18.5:
             label2.config(text="Underweight")
        elif bmi>=18.5 and bmi<25:
             label2.config(text="normal weight")
        elif bmi>=25 and bmi<30:
             label2.config(text="overweight")
        elif bmi>=30 and bmi<=40:
             label2.config(text="Obese Type 1")
        elif bmi>=40.1 and bmi<=50:
             label2.config(text="Obese Type 2")
        elif bmi>50:
             label2.config(text="Obese type 3")
        
    

image_icon = PhotoImage(file=r"C:\Users\Farhaan\Desktop\imggguga\icon.png")
root.iconphoto(False,image_icon)

top=PhotoImage(file=r"C:\Users\Farhaan\Desktop\imggguga\top.png")
top_image=Label(root,image=top,background="#f0f1f5")
top_image.place(x=-10,y=0)


Label(root,width=72,height=16,bg="lightblue").pack(side=BOTTOM)

box=PhotoImage(file=r"C:\Users\Farhaan\Desktop\imggguga\box.png")
Label(root,image=box).place(x=20,y=70)
Label(root,image=box).place(x=240,y=70)

scale=PhotoImage(file=r"C:\Users\Farhaan\Desktop\imggguga\scale.png")
Label(root,image=scale,bg="lightblue").place(x=20,y=300)


# #####   SLIDER1   ........
current_value = tk.DoubleVar()

def get_current_value():
    return "{:.2f}".format(current_value.get())
def slider_change(event):
    Height.set(get_current_value())

    size=int(float(get_current_value()))
    img = (Image.open(r"C:\Users\Farhaan\Desktop\imggguga\man.png"))
    resized_image=img.resize((50,50+size))
    photo2=ImageTk.PhotoImage(resized_image)
    second_image.configure(image=photo2)
    second_image.place(x=70,y=510-size)
    second_image.image=photo2
style=ttk.Style()
style.configure("TScale",background="white")

slider=ttk.Scale(root,from_=0, to=220,orient="horizontal",style="TScale",command=slider_change,variable=current_value)

slider.place(x=80,y=220)

# ########## SLIDER2 ......
current_value2 = tk.DoubleVar()

def get_current_value2():
    return "{:.2f}".format(current_value2.get())
def slider_change2(event):
    Weight.set(get_current_value2())
style2=ttk.Style()
style2.configure("TScale",background="white")

slider2=ttk.Scale(root,from_=0, to=200,orient="horizontal",style="TScale",command=slider_change2,variable=current_value2)

slider2.place(x=300,y=220)






Height=StringVar()
Weight=StringVar()
height=Entry(root,textvariable=Height,width=6,font=("arial 50",38),bg="#fff",fg="#000",bd=0,justify=CENTER)
height.place(x=31,y=124)
Height.set(get_current_value())

weight=Entry(root,textvariable=Weight,width=6,font=("arial 50",38),bg="#fff",fg="#000",bd=0,justify=CENTER)
weight.place(x=251,y=124)
Weight.set(get_current_value2())


second_image=Label(root,bg="lightblue")
second_image.place(x=70,y=530)

Button(root,text="View Report",width=15,height=2,font="arial 10 bold",bg="#1f6e68",fg="white",command=BMI).place(x=280,y=300)

label = Label(root,font="arial 30 bold",bg="lightblue",fg="#fff",bd=2)
label.place(x=150,y=298)

label2 = Label(root,font="arial 20 bold",bg="lightblue",fg="#3b3a3a")
label2.place(x=245,y=430)

ran=tk.StringVar()
llb= tk.Label(root, textvariable=ran,font="arial 10 bold",fg="gray",bg="white")
llb.pack()
ran.set("Height(cm)")
llb.place(x=85,y=80)

ran1=tk.StringVar()
llb= tk.Label(root, textvariable=ran1,font="arial 10 bold",fg="gray",bg="white")
llb.pack()
ran1.set("Weight(kg)")
llb.place(x=305,y=80)

label3 = Label(root,font="arial 10 bold",bg="lightblue")
label3.place(x=200,y=500)

root.mainloop()