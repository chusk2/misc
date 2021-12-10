from tkinter import *
import tkinter as tk
from tkinter import ttk

root = Tk()
root.config(width = 500, height = 100 )

lbl_message = tk.Label (master = root )
lbl_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
lbl_message.config( text = lbl_text , foreground = 'blue' , background = 'yellow' )
lbl_message.config (wraplength = 350)
lbl_message.config( font = ('Verdana', 18, 'italic') )
lbl_message.config( justify = LEFT )
lbl_message.grid(row=1,columnspan=2)

ent_name = tk.Entry( master = root )
ent_name.insert(0, 'Enter your name here...')
ent_name.grid(column=0,row = 2)

img1 = PhotoImage( file ='C:\\Users\\danie\\Documents\\PYTHON CODE\\python_logo.gif' )
text2 = 'Powered by Python 3.9'

lbl_image = tk.Label ( root, image = img1 , text = text2)
lbl_image.config(compound = 'center')
lbl_image.config( font = ('Courier', 14 , 'bold italic') )
lbl_image.config( foreground = 'blue' )

lbl_image.grid(column=0, row=0)





root.mainloop()