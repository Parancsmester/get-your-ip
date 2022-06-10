from urllib.request import urlopen
from tkinter import Tk, Frame, Label, Button, CENTER

r = urlopen('https://api.ipify.org')

w = Tk()
w.geometry('1920x1080')
w.attributes('-fullscreen', True)

f = Frame(w, width=1920, height=1080, bg='black')
f.grid(row=0, column=0, sticky="NW")

l = Label(w, text=r.read().decode('utf-8'), font='Arial 200 bold', bg='black', fg='white')
l.place(relx=0.5, rely=0.5, anchor=CENTER)

b = Button(w, text='Kilépés', font='Arial 50 bold', bg='black', fg='red', command=lambda: exit())
b.place(relx=0.5, rely=0.85, anchor=CENTER)

w.mainloop()
