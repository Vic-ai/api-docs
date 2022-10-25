# Invoices

To create an invoice in Vic there are three steps:
1. Create the invoice with a POST to /invoices
2. Upload the document with a POST to /invoice/{id}/document
3. Process the document with a POST to  /invoice/{id}/process