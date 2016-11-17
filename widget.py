from tkinter import *


master = Tk()

label = Label(master)
label.config(text = 'Cabelo')
label.pack()
w = Scale(master, from_=0, to=5, orient=HORIZONTAL)
w.pack()

label = Label(master)
label.config(text = 'Pele')
label.pack()
w = Scale(master, from_=0, to=5, orient=HORIZONTAL)
w.pack()

label = Label(master)
label.config(text = 'Sobrancelha')
label.pack()
w = Scale(master, from_=0, to=5, orient=HORIZONTAL)
w.pack()

label = Label(master)
label.config(text = 'Olhos')
label.pack()
w = Scale(master, from_=0, to=5, orient=HORIZONTAL)
w.pack()

label = Label(master)
label.config(text = 'Nariz')
label.pack()
w = Scale(master, from_=0, to=5, orient=HORIZONTAL)
w.pack()

label = Label(master)
label.config(text = 'Barba')
label.pack()
w = Scale(master, from_=0, to=5, orient=HORIZONTAL)
w.pack()

label = Label(master)
label.config(text = 'Orelha')
label.pack()
w = Scale(master, from_=0, to=5, orient=HORIZONTAL)
w.pack()

label = Label(master)
label.config(text = 'Boca')
label.pack()
w = Scale(master, from_=0, to=5, orient=HORIZONTAL)
w.pack()

mainloop()
