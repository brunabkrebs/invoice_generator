# invoice_generator
Program to generate invoices in PDF from a Word template.

Jinja2 tags are inserted where I want the variable text to be, using the docxtpl package.

Example:
" The event was located at {{location}} "

For external use:
Substitute the "context" fields for desired fields
Substitute file paths
