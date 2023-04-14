# Purchase Orders

## [`POST /v0/purchaseOrders`](../../vic.api.v0.html#/PurchaseOrders/createPurchaseOrder)

Creates a purchase order in the Vic.ai system.

### Example

```bash
curl --location --request POST 'https://api.us.dev.vic.ai/v0/purchaseOrders' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>' \
    --data-raw '{
        "amount": "1.00",
        "createdOn": "2022-06-01",
        "deliverOn": "2022-07-01",
        "issuedOn": "2022-06-01",
        "currencyId": "USD",
        "poNumber": "abc123",
        "requestor": "Bob From Marketing",
        "description": "A purchase order",
        "externalId": "po-1",
        "vendor": {
            "externalId": "the-vendor-external-id"
        },
        "lineItems": [
            {
                "productNumber": "11111",
                "productDescription": "Some widget",
                "unitOfMeasure": null,
                "quantity": "12.3",
                "quantityReceived": "13.0",
                "unitAmount": "3.50",
                "lineItemTotal": "45.50",
                "lineNumber": 0,
                "dimensions": [
                    {"externalId": "dimenstion-external-id"}
                ]
            },
            {
                "productNumber": "22222",
                "productDescription": "A different widget",
                "unitOfMeasure": null,
                "quantity": "1.0",
                "quantityReceived": "1.0",
                "unitAmount": "3.50",
                "lineItemTotal": "3.50",
                "lineNumber": 1,
                "dimensions": [
                    {"externalId": "dimenstion-external-id"}
                ]
            }
        ]
    }'
```

## [`GET /v0/purchaseOrders/{purchaseOrderId}`](../../vic.api.v0.html#/PurchaseOrders/getPurchaseOrder)

Fetch a purchase order in the Vic.ai system.

Only the `internalId` of the purchase order is supported.

### Example

```bash
curl --location --request GET 'https://api.us.dev.vic.ai/v0/purchaseOrders/ffb64be6-5e80-47d1-90bd-316663c52c8' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>'
```

## [`DELETE /v0/purchaseOrders/{purchaseOrderId}`](../../vic.api.v0.html#/PurchaseOrders/deletePurchaseOrder)

Deletes a purchase order from the Vic.ai system.

Only the `internalId` of the purchase order is supported.

### Example

```bash
curl --location --request DELETE 'https://api.us.dev.vic.ai/v0/purchaseOrders/ffb64be6-5e80-47d1-90bd-316663c52c8' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>'
```


## [`POST /v0/purchaseOrders/{purchaseOrderId}/process`](../../vic.api.v0.html#/PurchaseOrders/processPurchaseOrder)

Start the matching process for the purchase order.

Only the `internalId` of the purchase order is supported.

### Example

```bash
curl --location --request POST 'https://api.us.dev.vic.ai/v0/purchaseOrders/ffb64be6-5e80-47d1-90bd-316663c52c8/process' \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer <Bearer Token>'
```
