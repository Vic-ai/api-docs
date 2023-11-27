# Training Invoices

## [`PUT /v0/trainingInvoices`](../../vic.api.v0.html#/TrainingInvoices/upsertTrainingInvoice)

Upserts a training invoice into the Vic.ai system.

### Inserting Training Invoice

When inserting a new training invoice a `Content-Type` of `multipart/form-data`
is required due to the nature of sending a `pdf`, `png`, `tiff`, or `gif`
document.

Two parameters are required for inserting a new training invoice.

* `invoiceData` - The json data that represents the training invoice.
* `invoiceDocument` - The `pdf`, `png`, `tiff`, or `gif` training invoice document.

#### Example

```bash
curl -X PUT 'https://api.us.stage.vic.ai/v0/trainingInvoice/invoice-123' \
    --location \
    --header 'Content-Type: multipart/form-data' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer MYBEARERTOKEN' \
    --form 'invoiceDocument=@"/path/to/invoice/document.pdf"' \
    --form 'invoiceData="{
        \"externalUpdatedAt\": \"2022-01-20 04:10:00\",
        \"transactionType\": \"INVOICE\",
        \"refNumber\": \"1000000\",
        \"poNumber\": \"PO123\",
        \"description\": \"The invoice description\",
        \"currency\": \"USD\",
        \"language\": \"EN\",
        \"issueDate\": \"2022-01-20\",
        \"glDate\": \"2022-01-20\",
        \"dueDate\": \"2022-01-20\",
        \"paymentInfo\":{
            \"bankAccountNum\":\"1234567890\"
        },
        \"vendorExternalId\": \"vendor-external-id-1\",
        \"lineItems\": [
            {
                \"index\": 0,
                \"amount\": 123.53,
                \"description\": \"Line item description\",
                \"comment\": \"A quick comment about the line item\",
                \"accrual\":{
                    \"start\": \"2022-01-20\",
                    \"count\": 3,
                    \"unit\": \"MONTHS\"
                },
                \"billable\": false,
                \"dimensionsExternalIds\": [\"dimension-external-id-1\"],
                \"costAccountExternalId\": \"cost-account-external-id-1\",
                \"lineType\": \"item\"
            }
        ]
    }";type=application/json'
```

### Updating Training Invoice

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

#### Example

```bash
curl -X PUT 'https://api.us.stage.vic.ai/v0/trainingInvoice/invoice-123' \
    --location \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer MYBEARERTOKEN' \
    --data '{
        "externalUpdatedAt": "2022-01-20 04:10:00",
        "transactionType": "INVOICE",
        "refNumber": "1000000",
        "poNumber": "PO123",
        "description": "The invoice description",
        "currency": "USD",
        "language": "EN",
        "issueDate": "2022-01-20",
        "glDate": "2022-01-20",
        "dueDate": "2022-01-20",
        "paymentInfo":{
            "bankAccountNum":"1234567890"
        },
        "vendorExternalId": "vendor-external-id-1",
        "lineItems": [
            {
                "index": 0,
                "amount": 123.53,
                "description": "Line item description",
                "comment": "A quick comment about the line item",
                "accrual":{
                    "start": "2022-01-20",
                    "count": 3,
                    "unit": "MONTHS"
                },
                "billable": false,
                "dimensionsExternalIds": ["dimension-external-id-1"],
                "costAccountExternalId": "cost-account-external-id-1",
                "lineType": "expense"
            }
        ]
    }"'
```
