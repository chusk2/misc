import os
import shutil
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

# sudo xrdb -load /dev/null
# tkinter imports
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
###

def process_range():
    rg = page_range.get()
    rg_list = rg.split(',')
    for index, item in enumerate(rg_list):
        if len(item) == 1:
            rg_list[index] = int(item)
        elif '-' in item:
            item = item.split('-')
            item2 = [int(i) for i in item]
            item = tuple(item2)
            rg_list[index] = item
    return rg_list


def add_pages(file, page_range):
    input_pdf = PdfFileReader(str(file))
    output_pdf = PdfFileWriter()
    for rg in page_range:
        if len(str(rg)) == 1:
            page = input_pdf.getPage(rg)
            output_pdf.addPage(page)
        else:
            start, end = rg
            for index in range(start-1, end):
                page = input_pdf.getPage(index)
                output_pdf.addPage(page)
    return output_pdf


def open_file():
    input_file = filedialog.askopenfilename(initialdir=".",
                                            title="Select a File",
                                            filetypes=(("PDF files", "*.pdf"),
                                            ("all files", "*.*")))
    pdf_file = Path(input_file)
    filenameVar.set(pdf_file)


def extract():
    range = process_range()
    file = Path(filenameVar.get())
    filename = Path(f'{output_filename.get()}.pdf')
    output_pdf = add_pages(file, range)
    with filename.open(mode='wb') as f:
        output_pdf.write(f)

# Create the root window
window = tk.Tk()
window.title('PDF Files Manipulation')
# window.geometry('220x250')
window.configure(background="Blue")
window.resizable(True, False)

# Create a File Explorer label
input_frame = ttk.LabelFrame(text='Input PDF Files')

input_frame.grid(column=1, row=1, pady=3, padx=3, sticky=tk.W)

input_file_label = ttk.Label(input_frame, text="Input filename: ")
input_file_label.grid(column=1, row=1)
filenameVar = tk.StringVar()
filename_label = ttk.Label(input_frame, textvariable=filenameVar)
filename_label.grid(column=2, row=1)

pages_range_label = ttk.Label(input_frame, text="Pages range")
pages_range_label.grid(column=1, row=2, sticky=tk.W)
page_range = tk.StringVar()
range_entry = ttk.Entry(input_frame, textvariable=page_range)
range_entry.grid(column=2, row=2, sticky=tk.W)

output_file_label = ttk.Label(input_frame, text="Output filename: ")
output_file_label.grid(column=1, row=3, sticky=tk.W)
output_filename = tk.StringVar()
output_file_entry = ttk.Entry(input_frame, textvariable=output_filename)
output_file_entry.grid(column=2, row=3, sticky=tk.W)





# loop for buttons creation
# Labels of buttons
# Three buttons will be created

open_pdf_button = ttk.Button(window, text='Open input file')
open_pdf_button.grid(column=1, row=3, padx=3, pady=3, sticky=tk.W)
open_pdf_button.configure(command=open_file)

process_pdf_button = ttk.Button(window, text='Extract pages')
process_pdf_button.grid(column=1, row=4, padx=3, pady=3, sticky=tk.W)
process_pdf_button.configure(command=extract)

# END OF FILE PROPERTIES FRAME

# Let the window wait for any events
window.mainloop()
##########################
#  END OF APP INTERFACE  #
##########################







