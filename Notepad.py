from tkinter import *
from tkinter import filedialog,font
root=Tk()
root.geometry("1500x1500")
def fucy():
    text=textarea.get("1.0","end")
    print(text)
    location=filedialog.asksaveasfilename()
    file=open(location,"w+")
    file.write(text)
    file.close()
def Ar():
    textarea.config(font="Arial,14,bold")
def Al():
    textarea.config(font="Algerian,14,bold")
def Ca():
    textarea.config(font="Cambria,14,bold")
def Co():
    textarea.config(font="Courier,14,bold")
Label(root,text="Text Editor By Abhinav Gangrade",font="arial 20 bold").pack()
textarea=Text(root,height=100)
textarea.pack()
Button(root,text="Save",command=fucy).place(x=1175,y=400)
font=Menubutton(root,text="Font-Changing",bg="blue")
font.place(x=1175,y=500)
font.menu=Menu(font)
font["menu"]=font.menu
font.menu.add_checkbutton(label="Arial",
command=Ar)
font.menu.add_checkbutton(label="Algerian",
command=Al)
font.menu.add_checkbutton(label="Cambria",
command=Ca)
font.menu.add_checkbutton(label="Courier",
command=Co)
root.mainloop()
