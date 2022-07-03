'''
Tkinter - packer
Lucas
30.05.2022
'''

from tkinter import *
tkFenster = Tk()
tkFenster.title("pack example 04")

# var_name = Frame(master=tkFenster, bg ="HINTERGRUNDFARBE", fg ="SCHRIFTFARBE")
# Frame() packt mehrere Elemente zusammen
rahmen1 = Frame(master=tkFenster, bg='magenta')
rahmen1.pack(side='top', padx='5', pady='5')

rahmen2 = Frame(master=tkFenster, bg='cyan')
rahmen2.pack(side='bottom', fill = "x", padx='5',pady='5')

label1 = Label(master=rahmen1, text="eins",bg="red", fg="white")
label2 = Label(master=rahmen1, text="zwei",bg="green", fg="black")
label3 = Label(master=rahmen2, text="drei",bg="blue", fg="white")
label4 = Label(master=rahmen2, text="vier",bg="yellow", fg="black")

label1.pack(fill = "x", ipadx = 5, ipady = 5,padx = 5, pady = 5)
label2.pack(side = "right", ipadx = 20, ipady = 20,padx = 20, pady = 20)
label4.pack(side = "bottom", ipadx = 5, ipady = 5,padx = 5, pady = 5)
label3.pack(fill = "both")

tkFenster.mainloop()