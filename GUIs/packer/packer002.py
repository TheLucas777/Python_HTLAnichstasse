'''
Tkinter - packer
Lucas
30.05.2022
'''

from tkinter import *

tkFenster = Tk()
tkFenster.title("pack example 02")

label1 = Label(master=tkFenster, text="eins",
bg="red", fg="white")

label2 = Label(master=tkFenster, text="zwei",
bg="green", fg="black")

label3 = Label(master=tkFenster, text="drei",
bg="blue", fg="white")

label4 = Label(master=tkFenster, text="vier",
bg="yellow", fg="black")



label1.pack(side = "right", ipadx = 5, ipady = 5,
padx = 5, pady = 5)

label2.pack(side = "right", ipadx = 20, ipady = 20,
padx = 20, pady = 20)

label4.pack(side = "bottom", ipadx = 5, ipady = 5,
padx = 5, pady = 5)

label3.pack(side = "bottom", fill="both")

# .pack(side = "WELCHE SEITE SOLL ES ANGEORDNET WERDEN", ipadx = 5, ipady = 5)
# ipadx, ipady ... größe des widgets
# padx, pady ... abstand zwischen den Widgets
# fill = "BOTH" ... widget wird auf ganze breite und ganze höhe angeordnet
tkFenster.mainloop()
