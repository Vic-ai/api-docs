When creating an invoice, there are three steps to follow:

1. Create the invoice with a POST to `/invoices`
2. Upload the document with a POST to `/invoice/{id}/document`
3. Process the document with a POST to `/invoice/{id}/process`

You can make the id the internal id (from vic.ai) or the external id (from your system).

> #### Note
> The maximum file size allowed to upload is 64MB.
