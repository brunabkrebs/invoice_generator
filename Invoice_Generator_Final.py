# Program to generate Invoices automatically

# Import packages
from docxtpl import DocxTemplate
from datetime import date
import comtypes.client
import os

# Define template
doc = DocxTemplate("template.docx")

# Get user's input for info to be added on invoice
invoicedate = date.today().strftime("%m/%d/%Y")
location = input("Where was the event?\n")
invoicenumber = input("What is the invoice number?\n")
eventdate = input("What is the event's date?\n")

# Add user's input to template
context = {'invoicenumber' : invoicenumber, 'invoicedate' : invoicedate, 'eventdate' : eventdate, 'location' : location}
doc.render(context)
doc.save("Pro Beer Sports %s Invoice #%s.docx" % (location, invoicenumber))

# Convert generated invoice from .docx to .pdf
filename = ("Pro Beer Sports %s Invoice #%s.docx" % (location, invoicenumber))
filename2 = ("Pro Beer Sports %s Invoice #%s" % (location, invoicenumber))
wdFormatPDF = 17
in_file = os.path.abspath("C:\\Users\\bruna\\Desktop\\Invoice_Generator\\" + filename)
out_file = os.path.abspath("C:\\Users\\bruna\\Desktop\\Invoice_Generator\\" + filename2 + ".pdf")
print(out_file)
word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()

# Remove the original .docx file
os.remove(in_file)

# Message to confirm the program ran successfully
print("\nThe invoice has been successfully generated.")