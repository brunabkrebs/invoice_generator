# Program to generate Invoices automatically

# Import packages
from docxtpl import DocxTemplate
import datetime
from datetime import date
import comtypes.client
import os

# Define template
doc = DocxTemplate("template.docx")

# Get user's input for info to be added on invoice
invoicedate = date.today().strftime("%m/%d/%Y")

while True:
    location = input("Where was the event?\n")
    if location == "b":
        location = "Bloomington"
        break
    elif location == "i":
        location = "Indy BR"
        break
    else:
        print("Please add a valid location.")

invoicenumber = input("What is the invoice number?\n")


eventdate_input = input("What is the event's date? mm-dd-yyyy\n")
month, day, year = map(int, eventdate_input.split('-'))
eventdate = datetime.date(year, month, day).strftime('%B %d, %Y')


acctnbr = ""
if location == "Bloomington":
    acctnbr = 2
elif location == "Indy BR":
    acctnbr = 1

# Add user's input to template
context = {'invoicenumber' : invoicenumber, 'invoicedate' : invoicedate, 'eventdate' : eventdate, 'location' : location, 'acctnbr' : acctnbr}
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

# Message to confirm the program ran successfully
print("\nThe invoice has been successfully generated.")