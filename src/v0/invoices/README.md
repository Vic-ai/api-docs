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
    "externalId": "21b31bc7-1267-4335-893c-d7fe4706a238",
    "source": "Millum",
    "refNumber": "enim dolore",
    "poNumber": "mollit proident Lorem",
    "description": "sunt cupidatat cillum ut",
    "currency": "USD",
    "language": "en",
    "issueDate": "1943-09-10",
    "glDate": "1952-08-16",
    "dueDate": "2001-10-13",
    "paymentRef": "occaecat quis amet",
    "paymentInfo": {
        "kind": "Ut",
        "accountHolderName": "est cupidatat eiusmod et",
        "accountNumber": "aliqua dolor sit ea",
        "routingNumber": "dolor magna Lorem ex",
        "bic": "ipsum quis"
    },
    "paymentTerm": {
        "count": 81868646,
        "unit": "tempor sunt"
    },
    "creditAccount": {
        "internalId": "12345",
        "externalId": "cost-account-external-id"
    },
    "vendor": {
        "internalId": "45678",
        "externalId": "do culpa",
        "orgNumber": "tempor aliquip ea",
        "countryCode": "NO"
    },
    "lineItems": [
        {
        "amount": "1.00",
        "index": 68830011,
        "comment": "Duis voluptate incididunt aute magna",
        "description": "dolor et",
        "billable": true,
        "vat": {
            "internalId": "occaecat in laboris enim",
            "externalId": "Lorem",
            "code": "consectetur",
            "amount": {
            "value": "<Error: Too many levels of nesting to fake this schema>"
            }
        },
        "costAccount": {
            "internalId": "Duis",
            "externalId": "eiusmod ea d",
            "number": "veniam exercitation aliquip do"
        },
        "dimensions": [
            {
            "internalId": "aliqua in aute",
            "externalId": "enim in labore"
            },
            {
            "internalId": "magna sed Lorem",
            "externalId": "ea magna aliqua eiusmod"
            }
        ]
        },
        {
        "amount": "1.00",
        "index": 63232286,
        "comment": "id l",
        "description": "nulla proident in quis et",
        "billable": false,
        "vat": {
            "internalId": "eu qui",
            "externalId": "pariatur in",
            "code": "laboris nisi",
            "amount": {
            "value": "<Error: Too many levels of nesting to fake this schema>"
            }
        },
        "costAccount": {
            "internalId": "nostrud ut culpa dolor dolore",
            "externalId": "adipisicing amet cupidatat ea",
            "number": "veniam"
        },
        "dimensions": [
            {
            "internalId": "mollit reprehenderit",
            "externalId": "sit sunt"
            },
            {
            "internalId": "est ut adipisicing",
            "externalId": "cupidatat cillum incididunt nisi"
            }
        ]
        }
    ]
    }'
```

```bash
curl --location --request POST 'https://api.us.dev.vic.ai/v0/invoice/21 Duis sint pariatur/document?useSystem=INTERNAL' \
--header 'Content-Type: multipart/form-data' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer <Bearer Token>' \
--form 'document=@"/Users/grantz/Downloads/api-design.pdf"'
```


```bash
curl --location --request POST 'https://api.us.dev.vic.ai/v0/invoice/21/process?useSystem=INTERNAL' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer <Bearer Token>'
```
