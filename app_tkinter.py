from tkinter import *
from tkinter import ttk

class App :
	def __init__ (self, master) :
		self.engButton = ttk.Button(master, text = 'English', command = self.english)
		self.engButton.grid(column = 1, row =1)
		self.deuButton = ttk.Button(master, text = 'Deutsch', command = self.deutsch)
		self.deuButton.grid(column = 2, row =1)
		self.label = ttk.Label(text = '')
		self.label.grid(row = 2, column = 1, columnspan = 2)
	def english(self) :
		self.label.configure(text = 'English')
	def deutsch(self) :
		self.label.configure(text = 'Deutsch')
	

root = Tk()
app = App(root)
root.mainloop()