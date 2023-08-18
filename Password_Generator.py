from tkinter import*
from random import randint
win=Tk()
win.title("Random Password Generator")
win.geometry("500x300")

passwrd=chr(randint(33,126))

def new():
    pw_ent.delete(0,END)
    pw_length=int(ent.get())
    passwrd=''
    for i in range (pw_length):
        passwrd+=chr(randint(33, 126))
    pw_ent.insert(0,passwrd)


def clipper():
    win.clipboard_clear()
    win.clipboard_append((pw_ent.get()))

lf=LabelFrame(win,text="how many Characters?")
lf.pack(pady=20)

ent=Entry(lf,font=("Helvetica",24))
ent.pack(pady=20,padx=20)
pw_ent=Entry(win,text='',font=("Helvetica",24),bg="systembuttonface")
pw_ent.pack(pady=20)

f=Frame(win)
f.pack(pady=20)

my_button=Button(f,text="Generate Password",command=new)
my_button.grid(row=0,column=0,padx=10)

clip_b=Button(f,text="Copy to clipboard",command=clipper)
clip_b.grid(row=0,column=1,padx=10)


win.mainloop()
