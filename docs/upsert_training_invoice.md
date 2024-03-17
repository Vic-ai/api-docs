Use this request to *upsert* training invoice data for one invoice into
Vic.ai.

When putting a new invoice into the system, an `invoiceDocument` will be
required. If the training invoice already exists, an `invoiceDocument`
will not be required.

All requests that need to have the `invoiceDocument` updated should have
a `multipart/form-data` content type.

If the training invoice just needs to be updated without a document
specified a content type of `application/json` is permitted.

If the invoice is known by Vic.ai, the `externalId` supplied will be
used to resolve the invoice and perform an update of the data,
otherwise, a new invoice will be created.

When updating a training invoice, the `invoiceDocument` is no longer required,
and the `Content-Type` can be `application/json`

If the training invoice needs the underlying document updated, use a
`multipart/form-data` to accomplish this. It will have the same format as the
insert described above.

Some things to note about updating existing invoices.

* The line items passed will be set as the desired state of the invoice.
* Empty list of line items will cause all line items to be deleted.
* Existing line items passed will be matched as best as possible. If they can
  not be matched they will be deleted and replaced with the desired items.
