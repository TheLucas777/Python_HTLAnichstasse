'''
Tkinter - packer
Lucas
30.05.2022
'''

from tkinter import *

tkFenster = Tk()
tkFenster.title("pack example 01")

# var_name = Lable(master=tkFenster, text="Text", bg ="HINTERGRUNDFARBE", fg ="SCHRIFTFARBE")
label1 = Label(master=tkFenster, text="eins", bg="red", fg="white")
label2 = Label(master=tkFenster, text="zwei", bg="green", fg="black")
label3 = Label(master=tkFenster, text="drei", bg="blue", fg="white")
label4 = Label(master=tkFenster, text="vier", bg="yellow", fg="black")

label1.pack()
label2.pack()
label4.pack()
label3.pack()

tkFenster.mainloop()
