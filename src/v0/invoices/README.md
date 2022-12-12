# Invoices

## [`POST /v0/invoices`](../../vic.api.v0.html#/invoices/createInvoice)
## [`POST /v0/invoices/{id}/document`](../../vic.api.v0.html#/invoices/uploadDocumentInvoice)
## [`POST /v0/invoices/{id}/process`](../../vic.api.v0.html#/invoices/startProcessingInvoice)

Create an invoice in the Vic.ai system.

## Creating Invoice

When creating an invoice, there are three steps to follow:

1. Create the invoice with a POST to `/invoices`
2. Upload the document with a POST to `/invoice/{id}/document`
3. Process the document with a POST to `/invoice/{id}/process`

You can make the id the internal id (from vic.ai) or the external id (from your system).
### Example

```bash
curl --location --request POST 'https://api.us.dev.vic.ai/v0/invoices' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>' \
    --data-raw '{
        "transactionType": "INVOICE",
        "source": "MILLUM",
        "refNumber": "12345",
        "poNumber": "PO99999",
        "description": "Invoice Header Description",
        "currency": "NOK",
        "issueDate": "2022-06-08",
        "glDate": "2022-06-08",
        "dueDate": "2022-06-18",
        "paymentRef": "1010101010",
        "paymentInfo": {
            "kind": "BBAN",
            "accountHolderName": "Test Name",
            "accountNumber": "10805655555",
            "routingNumber": "1345435",
            "bic": "32435"
        },
        "paymentTerm": {
            "count": 10,
            "unit": "DAYS"
        },
        "vendor": {
            "orgNumber": "926858963",
            "countryCode": "NO"
        },
        "lineItems": [
            {
            "amount": "800",
            "index": 0,
            "comment": "Comment index 0",
            "description": "Invoice line 0 Desc",
            "billable": null,
            "vat": {
                "amount":"250"
            },
            "costAccount": {
                "number": "22530"
            },
            "dimensions": [
                {
                    "externalId": "cla_7"
                },
                {
                    "externalId": "prod_470"
                }
            ]
            },
            {
            "amount": "1000",
            "index": 1,
            "comment": "Comment index 1",
            "description": "Invoice line 1 Desc",
            "billable": null,
            "costAccount": {
                "number": "63010"
            },
            "dimensions": [
                {
                    "externalId": "loc_3"
                },
                {
                    "externalId": "dep_9"
                }
            ]
            }
        ]
        }'
```

```bash
curl --location --request POST 'https://api.us.dev.vic.ai/v0/invoice/12345/document?useSystem=INTERNAL' \
--header 'Content-Type: multipart/form-data' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer <Bearer Token>' \
--form 'document=@"/path/to/document.pdf"'
```


```bash
curl --location --request POST 'https://api.us.dev.vic.ai/v0/invoice/21/process?useSystem=INTERNAL' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer <Bearer Token>'
```
