from tkinter import *
from tkinter import messagebox

def calculate():
    try:
        result=eval(entrytext.get())
        entrytext.set(result)
    except:
        e.delete(0,END)
        messagebox.showerror("Error","enter a valid nymber")
root=Tk()
root.title("Calculator")
root.geometry("200x250")
root.resizable(width=True,height=True)
root.configure(bg="lightblue")

framee=Frame(root)
framee.pack()

entrytext=StringVar()
e=Entry(framee,font=("Arial",10), textvariable=entrytext)
e.grid(row=0,column=0, columnspan=4)

b0=Button(framee, text="0",width=5,height=2, command=lambda:e.insert(END,"0"))
b0.grid(row=4,column=0)
b1=Button(framee, text="1",width=5,height=2,command=lambda:e.insert(END,"1"))
b1.grid(row=3,column=0)
b2=Button(framee, text="2",width=5,height=2, command=lambda:e.insert(END,"2"))
b2.grid(row=3,column=1)
b3=Button(framee, text="3",width=5,height=2, command=lambda:e.insert(END,"3"))
b3.grid(row=3,column=2)
b4=Button(framee, text="4",width=5,height=2, command=lambda:e.insert(END,"4"))
b4.grid(row=2,column=0)
b5=Button(framee, text="5",width=5,height=2, command=lambda:e.insert(END,"5"))
b5.grid(row=2,column=1)
b6=Button(framee, text="6",width=5,height=2, command=lambda:e.insert(END,"6"))
b6.grid(row=2,column=2)
b7=Button(framee, text="7",width=5,height=2, command=lambda:e.insert(END,"7"))
b7.grid(row=1, column=0)
b8=Button(framee, text="8",width=5,height=2, command=lambda:e.insert(END,"8"))
b8.grid(row=1, column=1)
b9=Button(framee, text="9",width=5,height=2, command=lambda:e.insert(END,"9"))
b9.grid(row=1, column=2)

bDiv=Button(framee, text="/",width=5,height=2, command=lambda:e.insert(END,"/"))
bDiv.grid(row=1, column=3)
bMul=Button(framee, text="x",width=5,height=2, command=lambda:e.insert(END,"*"))
bMul.grid(row=2,column=3)
bPlus=Button(framee, text="+",width=5,height=2, command=lambda:e.insert(END,"+"))
bPlus.grid(row=3,column=3)
bSub=Button(framee, text="-",width=5,height=2, command=lambda:e.insert(END,"-"))
bSub.grid(row=4,column=2)
bFl=Button(framee, text=".",width=5,height=2, command=lambda:e.insert(END,"."))
bFl.grid(row=4,column=1)
bClear=Button(framee,text="AC",width=20,height=2, command=lambda:e.delete(0,END))#entrytext.set("")
bClear.grid(row=5,column=0,columnspan=4)

bEqu=Button(framee, text="=",width=5,height=2,command=calculate)
bEqu.grid(row=4,column=3)

root.mainloop()
