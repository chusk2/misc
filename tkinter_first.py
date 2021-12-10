#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

def onClick():
	label.configure(text='You have pressed the button!')
	button1.configure(text='I\'ve been clicked', foreground='red')

root = tk.Tk()
root.resizable(False,False)
root.geometry('500x500')
root.title('My first Python GUI')

label = ttk.Label(root,text='My first Tk window', font='Verdana')
label.grid(column=1,row=0)
button1=tk.Button(text='Click me now!', command=onClick)
button1.grid(column=2,row=2)





root.mainloop()