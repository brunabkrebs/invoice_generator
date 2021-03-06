# Program to generate Invoices automatically

# Import packages
import tkinter
from tkinter import *
from tkcalendar import Calendar
from docxtpl import DocxTemplate
import comtypes.client
import os
from tkinter import messagebox
import datetime
from datetime import date

# Set up GUI
gui = tkinter.Tk()
gui.title('Invoice Generator')
gui.geometry("550x450")

for rows in range(0,9):
    gui.grid_rowconfigure(rows,minsize=20)

gui.grid_columnconfigure(0,minsize=30)
gui.grid_columnconfigure(2,minsize=10)



# Get user's input for info to be added on invoice
loclabel = Label(gui, text='Event location:', font="Arial 16" ).grid(row=1,column=1, sticky=tkinter.W)
places = {'Bloomington', 'Indy BR'}
locselector = StringVar(gui)
locdropdown = OptionMenu(gui, locselector, *places)
locdropdown.grid(row=1,column=3, sticky=tkinter.W)
locdropdown.config(width=15, font="Arial 12")

invoicenumberlabel = Label(gui, text='Invoice Number:', font="Arial 16").grid(row=3, column=1)
nbr = tkinter.StringVar()
invoicenbrinput = Entry(gui, textvariable=nbr, width=19, font="Arial 12").grid(row=3, column=3, sticky=tkinter.W)

eventdatelabel = Label(gui, text='Event Date:',font="Arial 16").grid(row=5,column=1,sticky=tkinter.W)
eventdatecal = Calendar(font="Arial 11", selectmode='day',firstweekday="sunday", theme="clam")
eventdatecal.grid(row=6,column=3)

def generatebuttonclicked():
    location = locselector.get()
    invoicenumber = nbr.get()
    eventdate = eventdatecal.selection_get()
    eventdate = str(eventdate)
    year, month, day = map(int, eventdate.split('-'))
    eventdate = datetime.date(year, month, day).strftime('%B %d, %Y')

    invoicedate = date.today().strftime("%m/%d/%Y")
    acctnbr = ""
    if location == "Bloomington":
        acctnbr = 2
    elif location == "Indy BR":
        acctnbr = 1


    # Define template
    doc = DocxTemplate("template.docx")

    # Add user's input to template
    context = {'invoicenumber': invoicenumber, 'invoicedate': invoicedate, 'eventdate': eventdate, 'location': location, 'acctnbr' : acctnbr}
    doc.render(context)

    #Save to specific folder according to event location
    if location == "Bloomington":
        doc.save("G:\\Pro Beer Sports\\Invoices\\Bloomington\\Pro Beer Sports %s Invoice #%s.docx" % (location, invoicenumber))
    elif location == "Indy BR":
        doc.save("G:\\Pro Beer Sports\\Invoices\\Indy BR\\Pro Beer Sports %s Invoice #%s.docx" % (location, invoicenumber))


    # Convert generated invoice from .docx to .pdf
    filename = ("Pro Beer Sports %s Invoice #%s.docx" % (location, invoicenumber))
    filename2 = ("Pro Beer Sports %s Invoice #%s" % (location, invoicenumber))
    wdFormatPDF = 17

    if location == "Bloomington":
        in_file = os.path.abspath("G:\\Pro Beer Sports\\Invoices\\Bloomington\\" + filename)
        out_file = os.path.abspath("G:\\Pro Beer Sports\\Invoices\\Bloomington\\" + filename2 + ".pdf")
        print(out_file)
    elif location == "Indy BR":
        in_file = os.path.abspath("G:\\Pro Beer Sports\\Invoices\\Indy BR\\" + filename)
        out_file = os.path.abspath("G:\\Pro Beer Sports\\Invoices\\Indy BR\\" + filename2 + ".pdf")

    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()

    # Remove the original .docx file
    os.remove(in_file)

    # Create a message box confirming the program ran successfully
    messagebox.showinfo('', 'The invoice has been successfully generated!')

finalbutton = tkinter.Button(gui, text = 'Generate Invoice', width=22, font="Arial 16", command=generatebuttonclicked).grid(row=8, column=3)

gui.mainloop()
